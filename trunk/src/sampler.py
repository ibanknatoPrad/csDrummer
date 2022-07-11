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

import logging
import math
import random

class Layer:

    def __init__(self):

        self.velocity = float(1)
        self.gain = float(0)
        self.sample = int(0)


class Target:

    def __init__(self):

        self.channel = int(0)
        self.gain = float(0)
        self.adsr = (float(0), float(0), float(0), float(0))
        self.layers = []


class Technique:

    def __init__(self):

        self.midi = []
        self.targets = []


class Instrument:

    def __init__(self):

        self.techniques = []


class Drumkit:

    def __init__(self):

        self.instruments = []


class Sampler:

    def __init__(self):

        self.drumkit = Drumkit()
        # MIDI note to technique mapping
        self.MIDI = {}
        # samples map
        self.samples = {}
        # logging
        self.logger = logging.getLogger("sampler")

    # methods for loader

    def createInstrument(self, dummy):
        
        # relatives
        drumkit = self.drumkit
        # new instrument
        instrument = Instrument()
        drumkit.instruments += [instrument]
        # return index
        return float(len(drumkit.instruments) - 1)


    def createTechnique(self, instrument_n):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        # new technique
        technique = Technique()
        instrument.techniques += [technique]
        # return index
        return float(len(instrument.techniques) - 1)


    def createTarget(self, instrument_n, technique_n):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        # new target
        target = Target()
        technique.targets += [target]
        # return index
        return float(len(technique.targets) - 1)


    def createLayer(self, instrument_n, technique_n, target_n):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # new layer
        layer = Layer()
        target.layers += [layer]
        # return index
        return float(len(target.layers) - 1)


    def setTechniqueMIDI(self, instrument_n, technique_n, midi):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        # set MIDI
        technique.midi += [int(midi)]
        # add to MIDI map
        self.MIDI[int(midi)] = (int(instrument_n), int(technique_n))


    def setTargetChannel(self, instrument_n, technique_n, target_n, channel):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # set channel
        target.channel = int(channel)
        

    def setTargetGain(self, instrument_n, technique_n, target_n, gain):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # set gain
        target.gain = gain


    def setTargetADSR(self, instrument_n, technique_n, target_n, a, d, s, r):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # set adsr
        target.adsr = (a, d, s, r)
        
    
    def sortLayersByVel(self, instrument_n, technique_n, target_n):
        
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        target.layers.sort(cmp=lambda x,y: cmp(x.velocity, y.velocity))        


    def setLayerVelocity(self, instrument_n, technique_n, target_n, layer_n, velocity):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # set velocity
        layer.velocity = velocity


    def setLayerGain(self, instrument_n, technique_n, target_n, layer_n, gain):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # set gain
        layer.gain = gain


    def setLayerSample(self, instrument_n, technique_n, target_n, layer_n, sample):

        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # set sample
        layer.sample = int(sample)

    
    def setSampleData(self, sample, data):

        self.samples[int(sample)] = int(data)
        
    
    def setDebug(self, enabled):
    
        debug = bool(enabled)        
        if debug:
            loggingLevel = logging.DEBUG
        else:
            loggingLevel = logging.INFO
        self.logger.setLevel(loggingLevel)

    
    def printDebug(self, dummy):
        
        self.logger.debug("MIDI map:")
        self.logger.debug(self.MIDI)
        self.logger.debug("samples data:")
        self.logger.debug(self.samples)
        self.logger.debug("drumkit tree:")
        for instrument in self.drumkit.instruments:
            self.logger.debug(instrument.__dict__)
            for technique in instrument.techniques:
                self.logger.debug(technique.__dict__)
                for target in technique.targets:
                    self.logger.debug(target.__dict__)
                    for layer in target.layers:
                        self.logger.debug(layer.__dict__)


    # methods for user

    def isExists(self, midi):

        # look at our map
        if int(midi) in self.MIDI:
            return float(1)
        else:
            return float(0)


    def getInstrument(self, midi):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # return value
        return float(instrument_n)


    def getNumTargets(self, midi):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        # return value
        num = len(technique.targets)
        return float(num)


    def getTargetChannel(self, midi, target_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # return value
        channel = target.channel
        return float(channel)
        

    def getTargetGain(self, midi, target_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # return value
        gain = target.gain
        return float(gain)


    def getTargetADSR(self, midi, target_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # return value
        adsr = target.adsr
        return adsr


    def getNumLayers(self, midi, target_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        # return value
        num = len(target.layers)
        return float(num)


    def getLayerVelocity(self, midi, target_n, layer_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # return value
        velocity = layer.velocity
        return float(velocity)


    def getLayerGain(self, midi, target_n, layer_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # return value
        gain = layer.gain
        return float(gain)


    def getLayerSample(self, midi, target_n, layer_n):

        # restore instrument and technique
        instrument_n, technique_n = self.MIDI[int(midi)]
        # relatives
        drumkit = self.drumkit
        instrument = drumkit.instruments[int(instrument_n)]
        technique = instrument.techniques[int(technique_n)]
        target = technique.targets[int(target_n)]
        layer = target.layers[int(layer_n)]
        # return value
        sample = layer.sample
        return float(sample)
        
    
    def getSampleData(self, sample):

        sample = self.samples[int(sample)]
        return float(sample)
        
    # math
    
    def humanFalloff(self, vel, time, human):
        
        if human > 0:
            alpha = - math.log(1 - 0.997)/human
            falloff = 1 - math.exp(-time)/alpha
        else:
            falloff = 1
        fallVel = vel*falloff
        return float(fallVel)
        
    
    def humanVelocity(self, vel, human):
        
        humanVel = random.gauss(vel, human)
        if humanVel < 0:
            humanVel = 0
        if humanVel > 1:
            humanVel = 1
        return float(humanVel)
        
    
    def humanTime(self, human):
        
        humanTime = random.gauss(human/2, human/2)
        if (humanTime < 0):
            humanTime = 0
        if (humanTime > human):
            humanTime = human
        return float(humanTime)
  
  
    def getMorph(self, midi, target, vel):
        
        # search layers
        numLayers = int(self.getNumLayers(midi, target))
        top = numLayers - 1
        bottom = 0
        for layer in range(numLayers):
            layerVel = self.getLayerVelocity(midi, target, layer)
            topVel = self.getLayerVelocity(midi, target, top)
            bottomVel = self.getLayerVelocity(midi, target, bottom)
            if layerVel <= vel and layerVel > bottomVel:
                bottom = layer
            if layerVel >= vel and layerVel < topVel:
                top = layer
        # calculate morph
        topVel = self.getLayerVelocity(midi, target, top)
        bottomVel = self.getLayerVelocity(midi, target, bottom)
        if (topVel == bottomVel):
            morph = 0
        else:
            morph = (vel - bottomVel)/(topVel - bottomVel)
        return (float(top), float(bottom), float(morph))
