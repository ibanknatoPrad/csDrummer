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

import xml.dom.minidom


class LayerParser:
    """parser for <Layer> tag"""

    def __init__(self, layer):

        self.layer = layer


    def get_velocity(self):

        tag = self.layer.getElementsByTagName("Velocity")[0]
        vel = float(tag.firstChild.data)
        assert (vel >= 0) and (vel <= 1)
        return vel


    def get_gain(self):

        tag = self.layer.getElementsByTagName("Gain")[0]
        gain = float(tag.firstChild.data)
        return gain


    def get_sample(self):

        tag = self.layer.getElementsByTagName("Sample")[0]
        sample = str(tag.firstChild.data)
        return sample


class TargetParser:
    """parser for <Target> tag"""

    def __init__(self, target):

        self.target = target


    def get_channel(self):

        tag = self.target.getElementsByTagName("Channel")[0]
        channel = str(tag.firstChild.data)
        return channel


    def get_adsr(self):

        tag = self.target.getElementsByTagName("Attack")[0]
        attack = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Decay")[0]
        decay = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Sustain")[0]
        sustain = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Release")[0]
        release = float(tag.firstChild.data)
        return (attack, decay, sustain, release)


    def get_layers(self):

        tags = self.target.getElementsByTagName("Layer")
        layers = []
        for tag in tags:
            layer = LayerParser(tag)
            layers += [layer]
        return layers


class TechniqueParser:
    """parser for <Technique> tag"""

    def __init__(self, technique):

        self.technique = technique


    def get_midi(self):

        tags = self.technique.getElementsByTagName("MIDI")
        notes = []
        for tag in tags:
            note = int(tag.firstChild.data)
            assert (note >= 0) and (note < 128)
            notes += [note]
        return notes


    def get_targets(self):

        tags = self.technique.getElementsByTagName("Target")
        targets = []
        for tag in tags:
            target = TargetParser(tag)
            targets += [target]
        return targets


class InstrumentParser:
    """parser for <Instrument> tag"""

    def __init__(self, instrument):

        self.instrument = instrument


    def get_techniques(self):

        tags = self.instrument.getElementsByTagName("Technique")
        techniques = []
        for tag in tags:
            technique = TechniqueParser(tag)
            techniques += [technique]
        return techniques


class DrumKitParser:
    """parser for entire drum kit"""

    def __init__(self, filename):

        self.drumkit = xml.dom.minidom.parse(filename)
        assert self.drumkit.documentElement.tagName == "DrumKit"


    def get_channels(self):

        tags = self.drumkit.getElementsByTagName("Channel")
        channels = []
        for tag in tags:
            channel = str(tag.firstChild.data)
            channels += [channel]
        return channels


    def get_samples(self):

        tags = self.drumkit.getElementsByTagName("Sample")
        samples = []
        for tag in tags:
            sample = str(tag.firstChild.data)
            samples += [sample]
        return samples


    def get_instruments(self):

        tags = self.drumkit.getElementsByTagName("Instrument")
        instruments = []
        for tag in tags:
            instrument = InstrumentParser(tag)
            instruments += [instrument]
        return instruments

