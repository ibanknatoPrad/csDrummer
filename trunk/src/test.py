import unittest
import random

import drumkit
##import csound
import sampler

class TestSampler(unittest.TestCase):
    
    def setUp(self):
        
        self.sampler = sampler.Sampler()
        
        # new instrument
        instr = self.sampler.createInstrument(0)
        # new technique
        tech = self.sampler.createTechnique(instr)
        self.sampler.setTechniqueMIDI(instr, tech, 35)
        self.sampler.setTechniqueMIDI(instr, tech, 36)
        # new target
        target = self.sampler.createTarget(instr, tech)
        # new layer
        layer = self.sampler.createLayer(instr, tech, target)
        layer = self.sampler.createLayer(instr, tech, target)        
        # new target
        target = self.sampler.createTarget(instr, tech)
        # new layer
        layer = self.sampler.createLayer(instr, tech, target)
        layer = self.sampler.createLayer(instr, tech, target)                
        layer = self.sampler.createLayer(instr, tech, target)                
        # sort
        self.sampler.sortLayersByVel(instr, tech, target)
        
        # new instrument
        instr = self.sampler.createInstrument(0)
        # new technique
        tech = self.sampler.createTechnique(instr)
        self.sampler.setTechniqueMIDI(instr, tech, 38)
        self.sampler.setTechniqueMIDI(instr, tech, 40)
        # new target
        target = self.sampler.createTarget(instr, tech)
        # new layer
        layer = self.sampler.createLayer(instr, tech, target)
        self.sampler.setLayerVelocity(instr, tech, target, layer, 0.33)
        layer = self.sampler.createLayer(instr, tech, target)        
        self.sampler.setLayerVelocity(instr, tech, target, layer, 0.75)
        layer = self.sampler.createLayer(instr, tech, target)        
        self.sampler.setLayerVelocity(instr, tech, target, layer, 0.25)        
        layer = self.sampler.createLayer(instr, tech, target)        
        self.sampler.setLayerVelocity(instr, tech, target, layer, 0.66)
        # sort
        self.sampler.sortLayersByVel(instr, tech, target)
        
        self.sampler.setSampleData(0, 100)
        self.sampler.setSampleData(1, 101)


    def testMapping(self):
        
        # check MIDI
       
        assert (int(self.sampler.isExists(35)) == 1)
        assert (int(self.sampler.isExists(36)) == 1)
        assert (int(self.sampler.isExists(38)) == 1)
        assert (int(self.sampler.isExists(40)) == 1)
        
        # check isntruments
        
        instr1 = int(self.sampler.getInstrument(35))
        instr2 = int(self.sampler.getInstrument(36))
        assert (instr1 == instr2)
        instr1 = int(self.sampler.getInstrument(35))
        instr2 = int(self.sampler.getInstrument(40))        
        assert (instr1 != instr2)
       
    
    def testSamplesData(self):
        
        sd = int(self.sampler.getSampleData(0))
        assert(sd == 100)
        sd = int(self.sampler.getSampleData(1))
        assert(sd == 101)
        
    
    def testHuman(self):
        
        # falloff
        
        vel = 0.66
        falloff = self.sampler.humanFalloff(vel, 0.33, 0)
        assert (falloff == vel)
        vel = 0.66
        falloff = self.sampler.humanFalloff(vel, 0.33, 0.5)
        assert (falloff < vel)        
        
        # force
        
        vel = 0.66
        force = self.sampler.humanVelocity(vel, 0.33)
        assert (force >= 0 and force <= 1)
        
        # time 
        
        human = 0.33
        time = self.sampler.humanTime(human)
        assert (time >= 0 and time <= human)
        
    
    def testMorph(self):
        
        midi = 40
        target = 0
        
        # check normal mode

        vel = 0.3
        top, bot, morph = self.sampler.getMorph(midi, target, vel)
        assert (morph >= 0 and morph <= 1)

        vel = 0.6
        top, bot, morph = self.sampler.getMorph(midi, target, vel)
        assert (morph >= 0 and morph <= 1)
        
        # check exceed bounds
        
        vel = 0.1
        top, bot, morph = self.sampler.getMorph(midi, target, vel)
        assert (morph >= 0 and morph <= 1)
        
        vel = 0.9
        top, bot, morph = self.sampler.getMorph(midi, target, vel)
        assert (morph >= 0 and morph <= 1)
        
        
class TestDrumkit(unittest.TestCase):
    
    testXML = """
<Drumkit>
<Version>1</Version>
<Description>test</Description>
<License></License>
<Instrument Name="Instrument1">
<Technique>
<MIDI>35</MIDI>
<MIDI>36</MIDI>
<Target>
<Channel>Mono</Channel>
<Gain>1</Gain>
<ADSR><Attack>0.01</Attack><Decay>0</Decay><Sustain>1</Sustain><Release>0.1</Release></ADSR>
<Layer><Velocity>1</Velocity><Gain>1</Gain><Sample>test.wav</Sample></Layer>
<Layer><Velocity>0</Velocity><Gain>1</Gain><Sample>test2.wav</Sample></Layer>
</Target>
</Technique>
</Instrument>
</Drumkit>
"""

    def testParser(self):
        
        testkit = drumkit.parseXML(self.testXML)
        channels = testkit.getChannels()
        assert (len(channels) == 1)
        assert ("Mono" in channels)
        samples = testkit.getSamples()
        assert (len(samples) == 2)
        assert ("test.wav" in samples)        
        assert ("test2.wav" in samples)                


if __name__ == '__main__':
    unittest.main()
