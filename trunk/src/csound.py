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
import logging

import csnd

import drumkit

class DrumkitScript:

    def __init__(self):

        self.text = ""

    def createInstrument(self):

        code = """
iInstrument pycall1i "createInstrument", 0
"""
        self.text += code


    def createTechnique(self):

        code = """
iTechnique pycall1i "createTechnique", iInstrument
"""
        self.text += code


    def createTarget(self):

        code = """
iTarget pycall1i "createTarget", iInstrument, iTechnique
"""
        self.text += code


    def createLayer(self):

        code = """
iLayer pycall1i "createLayer", iInstrument, iTechnique, iTarget
"""
        self.text += code


    def setTechniqueMIDI(self, midi):

        code = """
iMIDI = $MIDI
pycalli "setTechniqueMIDI", iInstrument, iTechnique, iMIDI
"""
        template = string.Template(code)
        subst = {}
        subst["MIDI"] = midi
        self.text += template.substitute(subst)


    def setTargetChannel(self, channel):

        code = """
iChannel = $Channel
pycalli "setTargetChannel", iInstrument, iTechnique, iTarget, iChannel
"""
        template = string.Template(code)
        subst = {}
        subst["Channel"] = channel
        self.text += template.substitute(subst)
        

    def setTargetGain(self, gain):

        code = """
iGain = $Gain
pycalli "setTargetGain", iInstrument, iTechnique, iTarget, iGain
"""
        template = string.Template(code)
        subst = {}
        subst["Gain"] = gain
        self.text += template.substitute(subst)


    def setTargetADSR(self, attack, decay, sustain, release):

        code = """
iAttack = $Attack
iDecay = $Decay
iSustain = $Sustain
iRelease = $Release
pycalli "setTargetADSR", iInstrument, iTechnique, iTarget, iAttack, iDecay, iSustain, iRelease
"""
        template = string.Template(code)
        subst = {}
        subst["Attack"] = attack
        subst["Decay"] = decay
        subst["Sustain"] = sustain
        subst["Release"] = release
        self.text += template.substitute(subst)
        
    
    def sortLayersByVel(self):

        code = """
pycalli "sortLayersByVel", iInstrument, iTechnique, iTarget
"""
        self.text += code        


    def setLayerVelocity(self, velocity):

        code = """
iVelocity = $Velocity
pycalli "setLayerVelocity", iInstrument, iTechnique, iTarget, iLayer, iVelocity
"""
        template = string.Template(code)
        subst = {}
        subst["Velocity"] = velocity
        self.text += template.substitute(subst)


    def setLayerGain(self, gain):

        code = """
iGain = $Gain
pycalli "setLayerGain", iInstrument, iTechnique, iTarget, iLayer, iGain
"""
        template = string.Template(code)
        subst = {}
        subst["Gain"] = gain
        self.text += template.substitute(subst)


    def setLayerSample(self, sample):

        code = """
iSample = $Sample
pycalli "setLayerSample", iInstrument, iTechnique, iTarget, iLayer, iSample
"""
        template = string.Template(code)
        subst = {}
        subst["Sample"] = sample
        self.text += template.substitute(subst)


    def setSampleData(self, sample, data):

        code = """
iSample = $Sample
SFile = "$Data"
iSampleData ftgen 0, 0, 0, -1, SFile, 0, 0, 1
pycalli "setSampleData", iSample, iSampleData
"""
        template = string.Template(code)
        subst = {}
        subst["Sample"] = sample
        subst["Data"] = data
        self.text += template.substitute(subst)
        

class DrumkitScriptProducer:

    def __init__(self, path, drumkit):
        
        self.__path = path
        self.__drumkit = drumkit
        self.script = DrumkitScript()
        self.__preprocessSamples()
        self.__preprocessChannels()
        self.__produceSamples()
        self.__produceDrumkit()
        

    def __produceLayer(self, layer):

        self.script.createLayer()
        self.script.setLayerVelocity(layer.getVelocity())
        self.script.setLayerGain(layer.getGain())
        self.script.setLayerSample(self.__samplesReplace[layer.getSample()])


    def __produceTarget(self, target):

        self.script.createTarget()
        channel = self.__channelsReplace[target.getChannel()]
        self.script.setTargetChannel(channel)
        self.script.setTargetGain(target.getGain())
        a, d, s, r = target.getADSR()
        self.script.setTargetADSR(a, d, s, r)
        for layer in target.getLayers():
            self.__produceLayer(layer)
        self.script.sortLayersByVel()


    def __produceTechnique(self, technique):

        self.script.createTechnique()
        for midi in technique.getMIDI():
            self.script.setTechniqueMIDI(midi)
        for target in technique.getTargets():
            self.__produceTarget(target)


    def __produceInstrument(self, instrument):

        self.script.createInstrument()
        for technique in instrument.getTechniques():
            self.__produceTechnique(technique)
        
    
    def __produceDrumkit(self):

        for instrument in self.__drumkit.getInstruments():
            self.__produceInstrument(instrument)
    

    def __produceSamples(self):
        
        for sample in self.__samplesData.iterkeys():
            sampleData = self.__samplesData[sample]
            sampleData = os.path.join(self.__path, sampleData)
            sampleData = os.path.normpath(sampleData)
            sampleData = os.path.normcase(sampleData)            
            self.script.setSampleData(sample, sampleData)
        
           
    def __preprocessSamples(self):
        
        samplesList = self.__drumkit.getSamples()
        samplesData = {}
        samplesReplace = {}
        sampleN = 0
        for sample in samplesList:
            samplesData[sampleN] = sample
            samplesReplace[sample] = sampleN
            sampleN += 1
        self.__samplesData = samplesData
        self.__samplesReplace = samplesReplace
        
    
    def __preprocessChannels(self):
        
        channelsList = self.__drumkit.getChannels()
        channelsReplace = {}
        channelN = 0
        for channel in channelsList:
            channelsReplace[channel] = channelN
            channelN += 1
        self.__channelsReplace = channelsReplace


def produceDrumkitScript(path, drumkit):
    
    producer = DrumkitScriptProducer(path, drumkit)
    return producer.script.text


inputModules = {
    "default": " ",
    "portmidi": " -+rtmidi=portmidi --midi-device=$Input",
    "alsa": " -+rtmidi=alsa --midi-device=$Input",
    "mme": " -+rtmidi=mme --midi-device=$Input",
    "virtual": " -+rtmidi=virtual --midi-device=0",
    "file": " -+rtmidi=null --midifile=$Input -T"
}


def produceInput(module, input):
    
    template = string.Template(inputModules[module])
    subst = {}
    subst["Input"] = input
    text = template.substitute(subst)
    return text
    

outputModules = {
        "default": " ",
        "portaudio": "-+rtaudio=portaudio --output=dac$Output",
        "alsa": "-+rtaudio=alsa --output=dac$Output",
        "jack": "-+rtaudio=jack --output=dac$Output",
        "mme": "-+rtaudio=mme --output=dac$Output",
        "coreaudio": "-+rtaudio=coreaudio --output=dac$Output",
        "file": "-+rtaudio=null --output=$Output"
    }


def produceOutput(module, output):
    
    template = string.Template(outputModules[module])
    subst = {}
    subst["Output"] = output
    text = template.substitute(subst)
    return text
    

class ScriptOptions:
    
    def __init__(self):
    
        # script parts
        self.SamplerCSD = "sampler.csd"
        self.SamplerPy = "sampler.py"
        # input/output
        self.InputModule = "default"
        self.Input = 0
        self.OutputModule = "default"
        self.Output = ""
        # drumkit
        self.Drumkit = ""
        # modes
        self.Multichannel = False
        self.LowQuality = False
        self.FFTSize = 1024
        # humanizer
        self.HumanFalloff = 1
        self.HumanTime = 0.1
        # Csound
        self.Csound = ""
        self.CsoundDefault = " -d"
        # Debug
        self.Debug = False
     

class ScriptProducer:
    

    def __init__(self, options):

        self.__options = options
        # locate modules dir
        self.__modulesPath = os.path.dirname(__file__)
        # parse drumkit
        self.__parser = drumkit.parseFile(self.__options.Drumkit)
        # configure
        self.__subst = {}
        self.__configModes()
        self.__configDrumkitLoader()
        self.__configHumanize()
        self.__configCommandLine()
        self.__configSampler()
        self.__configDebug()        
        # load template csd
        f = open(os.path.join(self.__modulesPath, self.__options.SamplerCSD), "r")
        template = string.Template(f.read())
        f.close()
        # make csd
        self.text = template.substitute(self.__subst)


    def __configModes(self):

        # Multichannel
        if self.__options.Multichannel:
            self.__subst["NumChannels"] = str(len(self.__parser.getChannels()))
        else:
            self.__subst["NumChannels"] = "1"
        # Quality
        if self.__options.LowQuality:
            self.__subst["LowQuality"] = "1"
        else:
            self.__subst["LowQuality"] = "0"
        # FFT Size
        self.__subst["FFTSize"] = self.__options.FFTSize
        
    
    def __configDrumkitLoader(self):
        
        path = os.path.dirname(self.__options.Drumkit)
        script = produceDrumkitScript(path, self.__parser)        
        self.__subst["DrumkitLoader"] = script
        
    
    def __configHumanize(self):
        
        # macro: HumanTime
        self.__subst["HumanTime"] = self.__options.HumanTime
        # macro: HumanFalloff
        self.__subst["HumanFalloff"] = self.__options.HumanFalloff
        
    
    def __configCommandLine(self):

        csoundOpts = ""
        # default opts
        csoundOpts += " " + self.__options.CsoundDefault
        # debug flag
##        if self.__options.Debug:
##            csoundOpts += " -v"
        # input/output
        csoundOpts += " " + produceInput(self.__options.InputModule, self.__options.Input)
        csoundOpts += " " + produceOutput(self.__options.OutputModule, self.__options.Output)
        # command-line options
        csoundOpts += " " + self.__options.Csound
        self.__subst["CsoundOptions"] = csoundOpts
        
    
    def __configDebug(self):
        
        if self.__options.Debug:
            self.__subst["Debug"] = "1"
        else:
            self.__subst["Debug"] = "0"
            
    
    def __configSampler(self):

        self.__subst["SamplerScript"] = os.path.join(self.__modulesPath, self.__options.SamplerPy)
        
        
def produceScript(options):
    
    producer = ScriptProducer(options)
    return producer.text
        

class CsoundCallback(csnd.CsoundCallbackWrapper):
    
    def __init__(self, csound):
        
        csnd.CsoundCallbackWrapper.__init__(self, csound)
        self.logger = logging.getLogger("Csound")
        self.messageBuffer = ""

    
    def MessageCallback(self, attr, msg):
        
        self.messageBuffer += msg
        lines = self.messageBuffer.splitlines(True)
        self.messageBuffer = ""
        for line in lines:
            if line.endswith("\n"):
                self.logger.debug(line.strip("\n"))
            else:
                self.messageBuffer += line

        

class CsoundEngine:

    def __init__(self, script):

        # init
        self.csound = csnd.Csound()
        self.callback = CsoundCallback(self.csound)
        self.callback.SetMessageCallback()
        self.status = 0
        self.time = 0
        self.__play = False
        self.__stop = False
        # create temporary CSD
        tempFilename = tempfile.mktemp(suffix=".csd")
        f = open(tempFilename, "w");
        f.write(script)
        f.close()
        # compile
        self.csound.Compile(tempFilename)
        # remove temporary
        os.remove(tempFilename)
        # create thread
        self.thread = threading.Thread(target=self.__threadMain)
        self.thread.start()
        

    def __threadMain(self):

        self.status = 0
        while self.status == 0:
            if self.__play:
                self.status = self.csound.PerformBuffer()
                self.time = self.csound.GetScoreTime()
            if self.__stop:
                self.csound.Stop()                
        self.csound.Cleanup()                
   
 
    def join(self):

        self.thread.join()


    def pause(self):

        self.__play = False
        
    
    def play(self):
        
        self.__play = True


    def stop(self):

        self.__stop = True
        self.thread.join()


    def getStatus(self):

        return self.status


    def getTime(self):

        return self.time
