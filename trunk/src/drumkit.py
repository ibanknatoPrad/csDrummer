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


    def getVelocity(self):

        tag = self.layer.getElementsByTagName("Velocity")[0]
        assert tag.parentNode == self.layer
        vel = float(tag.firstChild.data)
        return vel


    def getGain(self):

        tag = self.layer.getElementsByTagName("Gain")[0]
        assert tag.parentNode == self.layer
        gain = float(tag.firstChild.data)
        return gain


    def getSample(self):

        tag = self.layer.getElementsByTagName("Sample")[0]
        assert tag.parentNode == self.layer
        sample = str(tag.firstChild.data)
        return sample


class TargetParser:
    """parser for <Target> tag"""

    def __init__(self, target):

        self.target = target


    def getChannel(self):

        tag = self.target.getElementsByTagName("Channel")[0]
        assert tag.parentNode == self.target
        channel = str(tag.firstChild.data)
        return channel


    def getGain(self):

        tag = self.target.getElementsByTagName("Gain")[0]
        assert tag.parentNode == self.target
        gain = float(tag.firstChild.data)
        return gain


    def getADSR(self):

        tag = self.target.getElementsByTagName("Attack")[0]
        assert tag.parentNode.parentNode == self.target
        attack = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Decay")[0]
        assert tag.parentNode.parentNode == self.target
        decay = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Sustain")[0]
        assert tag.parentNode.parentNode == self.target
        sustain = float(tag.firstChild.data)
        tag = self.target.getElementsByTagName("Release")[0]
        assert tag.parentNode.parentNode == self.target
        release = float(tag.firstChild.data)
        return (attack, decay, sustain, release)


    def getLayers(self):

        tags = self.target.getElementsByTagName("Layer")
        layers = []
        for tag in tags:
            assert tag.parentNode == self.target            
            layer = LayerParser(tag)
            layers += [layer]
        return layers


class TechniqueParser:
    """parser for <Technique> tag"""

    def __init__(self, technique):

        self.technique = technique
        
        
    def getName(self):
        
        name = str(self.technique.getAttribute("Name"))
        return name


    def getMIDI(self):

        tags = self.technique.getElementsByTagName("MIDI")
        notes = []
        for tag in tags:
            assert tag.parentNode == self.technique
            note = int(tag.firstChild.data)
            assert (note >= 0) and (note < 128)
            notes += [note]
        return notes


    def getTargets(self):

        tags = self.technique.getElementsByTagName("Target")
        targets = []
        for tag in tags:
            assert tag.parentNode == self.technique
            target = TargetParser(tag)
            targets += [target]
        return targets


class InstrumentParser:
    """parser for <Instrument> tag"""

    def __init__(self, instrument):

        self.instrument = instrument

    
    def getName(self):
        
        name = str(self.technique.getAttribute("Name"))
        return name
        

    def getTechniques(self):

        tags = self.instrument.getElementsByTagName("Technique")
        techniques = []
        for tag in tags:
            assert tag.parentNode == self.instrument
            technique = TechniqueParser(tag)
            techniques += [technique]
        return techniques


class DrumkitParser:
    """parser for entire drum kit"""

    def __init__(self, document):

        self.document = document
        assert self.document.documentElement.tagName == "Drumkit"


    def getChannels(self):

        tags = self.document.getElementsByTagName("Channel")
        channels = []
        for tag in tags:
            assert tag.parentNode.tagName == "Target"
            channel = str(tag.firstChild.data)
            channels += [channel]
        channels = list(set(channels))
        return channels


    def getSamples(self):

        tags = self.document.getElementsByTagName("Sample")
        samples = []
        for tag in tags:
            assert tag.parentNode.tagName == "Layer"
            sample = str(tag.firstChild.data)
            samples += [sample]
        samples = list(set(samples))
        return samples


    def getInstruments(self):

        tags = self.document.getElementsByTagName("Instrument")
        instruments = []
        for tag in tags:
            assert tag.parentNode == self.document.documentElement
            instrument = InstrumentParser(tag)
            instruments += [instrument]
        return instruments


def parseFile(filename):
    
    document = xml.dom.minidom.parse(filename)
    drumkit = DrumkitParser(document)
    return drumkit
    

def parseXML(text):
    
    document = xml.dom.minidom.parseString(text)
    drumkit = DrumkitParser(document)
    return drumkit