# csDrummer: Record a drum session in a virtual studio
# Copyright (C) 2008 Schlagg
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import string
import tempfile
import os
import threading


import csnd

import drumkit



class LayerGenerator:

    template = """iLayer pycall1i "add_layer", iMIDI, iTarget
pycalli "set_layer_vel", iMIDI, iTarget, iLayer, %(velocity)s
pycalli "set_layer_gain", iMIDI, iTarget, iLayer, %(gain)s
iSample ftgen 0, 0, 0, -1, "%(sample)s", 0, 0, 1
pycalli "set_layer_sample", iMIDI, iTarget, iLayer, iSample

"""
    velocity = None
    gain = None
    sample = None

    def __init__(self):

        self.velocity = 0
        self.gain = 0
        self.sample = 0


    def get_text(self):

        params = {}
        params["velocity"] =  self.velocity
        params["gain"] =  self.gain
        params["sample"] =  self.sample
        text = self.template % params
        return text


class TargetGenerator:

    template = """iTarget pycall1i "add_target", iMIDI
pycalli "set_target_channel", iMIDI, iTarget, %(channel)s
pycalli "set_target_adsr", iMIDI, iTarget, %(attack)s, %(decay)s, %(sustain)s, %(release)s

"""
    channel = None
    adsr = None
    layers = None

    def __init__(self):

        self.channel = 0
        self.adsr = (0, 0, 0, 0)
        self.layers = []


    def get_text(self):

        # add technique
        params = {}
        params["channel"] =  self.channel
        params["attack"] =  self.adsr[0]
        params["decay"] =  self.adsr[1]
        params["sustain"] =  self.adsr[2]
        params["release"] =  self.adsr[3]
        text = self.template % params
        # add layers
        for layer in self.layers:
            text += layer.get_text()
        return text


class TechniqueGenerator:

    technique_template = """iMIDI = %(midi)s
pycalli "add_technique", iMIDI
pycalli "set_instrument", iMIDI, %(instrument)s

"""
    alias_template = """iAlias = %(alias)s
pycalli "add_alias", iAlias, iMIDI

"""
    midi = None
    instrument = None
    aliases = None
    targets = None

    def __init__(self):

        self.midi = 0
        self.instrument = 0
        self.aliases = []
        self.targets = []


    def get_text(self):

        # add technique
        params = {}
        params["midi"] =  self.midi
        params["instrument"] =  self.instrument
        text = self.technique_template % params
        # add aliases
        for alias in self.aliases:
            alias_params = {}
            alias_params["alias"] =  alias
            text += self.alias_template % alias_params
        # add targets
        for target in self.targets:
            text += target.get_text()
        return text


class DrumKitGenerator:

    def __init__(self, drumkit_parser):

        self.techniques = []
        techniques = self.techniques
        # replace channel names with numbers
        channels_src = drumkit_parser.get_channels()
        channels_src = list(set(channels_src))
        channels = {}
        for n in range(len(channels_src)):
            channels[channels_src[n]] = n + 1
        # scan source tree for instruments and convert it to dest tree
        instruments_src = drumkit_parser.get_instruments()
        for instrument_n in range(len(instruments_src)):
            instrument_src = instruments_src[instrument_n]
            # ... for techniques
            for technique_src in instrument_src.get_techniques():
                technique = TechniqueGenerator()
                techniques += [technique]
                midi = technique_src.get_midi()
                technique.midi = midi[0]
                technique.aliases = midi[1:len(midi)]
                technique.instrument = instrument_n
                # ... for targets
                for target_src in technique_src.get_targets():
                    target = TargetGenerator()
                    technique.targets += [target]
                    target.channel = channels[target_src.get_channel()]
                    target.adsr = target_src.get_adsr()
                    # ... for layers
                    for layer_src in target_src.get_layers():
                        layer = LayerGenerator()
                        target.layers += [layer]
                        layer.velocity = layer_src.get_velocity()
                        layer.gain = layer_src.get_gain()
                        layer.sample = layer_src.get_sample()


    def get_text(self):
        """return text representation of drumkit loader"""

        text = ""
        for technique in self.techniques:
            text += technique.get_text();
        return text


class InputModuleGenerator:

    modules = {
        "portmidi": "-+rtmidi=portmidi --midi-device=%(input)s",
        "alsa": "-+rtmidi=alsa --midi-device=%(input)s",
        "mme": "-+rtmidi=mme --midi-device=%(input)s",
        "file": "-+rtmidi=null --midifile=%(input)s -T"
    }


    def __init__(self, module, input):

        self.module = module
        self.input = input


    def get_text(self):

        text = self.modules[self.module]
        text = text % {"input": self.input}
        return text


class OutputModuleGenerator:

    modules = {
        "portaudio": "-+rtaudio=portaudio --output=dac%(output)s",
        "alsa": "-+rtaudio=alsa --output=dac%(output)s",
        "jack": "-+rtaudio=jack --output=dac%(output)s",
        "mme": "-+rtaudio=mme --output=dac%(output)s",
        "coreaudio": "-+rtaudio=coreaudio --output=dac%(output)s",
        "file": "-+rtaudio=null --output=%(output)s"
    }


    def __init__(self, module, output):

        self.module = module
        self.output = output


    def get_text(self):

        text = self.modules[self.module]
        text = text % {"output": self.output}
        return text


class CsoundGenerator:

    csdfilename = "sampler.csd"
    defcsound = "-d"


    def __init__(self, options):

        self.options = options


    def get_csd(self):

        macros = {}
        # load template csd
        f = open(self.csdfilename)
        csdtemplate = string.Template(f.read())
        f.close()
        # parse drumkit
        drumkit_parser = drumkit.DrumKitParser(self.options["DrumKit"])
        # macro: DrumKitLoader
        drumkit_gen = DrumKitGenerator(drumkit_parser)
        macros["DrumKitLoader"] = drumkit_gen.get_text()
        # macro: NumChannels
        if self.options["Multichannel"]:
            macros["NumChannels"] = len(drumkit_parser.get_channels())
        else:
            macros["NumChannels"] = "1"
        # macro: LowQuality
        if self.options["LowQuality"]:
            macros["LowQuality"] = "1"
        else:
            macros["LowQuality"] = "0"
        # macro: FFTSize
        macros["FFTSize"] = self.options["FFTSize"]
        # macro: HumanForce
        macros["HumanForce"] = self.options["HumanForce"]
        # macro: HumanTime
        macros["HumanTime"] = self.options["HumanTime"]
        # macro: HumanFalloff
        macros["HumanFalloff"] = self.options["HumanFalloff"]
        # macro: CsoundOptions
        csoundopts = " "
        csoundopts += " " + self.defcsound
        if self.options["Debug"]:
            csoundopts += " -v"
        csoundopts += " " + InputModuleGenerator(self.options["InputModule"],
            self.options["Input"]).get_text()
        csoundopts += " " + OutputModuleGenerator(self.options["OutputModule"],
            self.options["Output"]).get_text()
        csoundopts += " " + self.options["Csound"]
        macros["CsoundOptions"] = csoundopts
        # macros: Debug
        if self.options["Debug"]:
            macros["Debug"] = "1"
        else:
            macros["Debug"] = "0"
        # make csd
        csdtext = csdtemplate.safe_substitute(macros)
        return csdtext


class CsoundEngine:


    def __init__(self, options):

        self.options = options
        # generate CSD
        csd = CsoundGenerator(self.options).get_csd()
        if self.options["Debug"]:
            print csd
        # init
        self.csound = csnd.Csound()
        # create temporary CSD
        tempfname = tempfile.mktemp(suffix=".csd")
        f = open(tempfname, "w");
        f.write(csd)
        f.close()
        # compile
        self.csound.Compile(tempfname)
        # remove temporary
        os.remove(f.name)


    def run(self):

        # create thread
        self.perf_thread = csnd.CsoundPerformanceThread(self.csound)
        self.perf_thread.Play()
        self.python_thread = threading.Thread(target=self.perf_thread.Join)
        self.python_thread.start()


    def join(self):

        self.python_thread.join()


    def pause(self):

        self.perf_thread.TogglePause()


    def halt(self):

        self.perf_thread.Stop()
        self.perf_thread.Join()


    def get_status(self):

        return self.perf_thread.GetStatus()


    def get_time(self):

        return self.csound.GetScoreTime()
