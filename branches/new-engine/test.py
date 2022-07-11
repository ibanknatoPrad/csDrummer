import unittest

import drumkit
import csound
import sampler

class TestAll(unittest.TestCase):

    xmlfile = "DrumKit.xml"

    def test_drumkit(self):

        print "Parsing", self.xmlfile
        drumkit_parser = drumkit.DrumKitParser(self.xmlfile)
        print "drumkit_parser", drumkit_parser
        print "Channels", drumkit_parser.get_channels()
        print "Samples", drumkit_parser.get_samples()
        for instrument in drumkit_parser.get_instruments():
            print "\tInstrument", instrument
            for technique in instrument.get_techniques():
                print "\t\tTechnique", technique
                print "\t\tMIDI", technique.get_midi()
                for target in technique.get_targets():
                    print "\t\t\tTarget", target
                    print "\t\t\tChannel", target.get_channel()
                    print "\t\t\tADSR", target.get_adsr()
                    for layer in target.get_layers():
                        print "\t\t\t\tLayer", layer
                        print "\t\t\t\tVelocity", layer.get_velocity()
                        print "\t\t\t\tGain", layer.get_gain()
                        print "\t\t\t\tSample", layer.get_sample()


    def test_csdgen(self):

        drumkit_src = drumkit.DrumKitParser(self.xmlfile)
        drumkit_dest = csound.import_drumkit(drumkit_src)
        loader = drumkit_dest.get_text()
        sampler = csound.CsoundGenerator()
        sampler.drumkit_loader = loader
        code = sampler.get_text()
        print code


    def test_sampler(self):

        print "maybe should write test.csd?"


if __name__ == '__main__':
    unittest.main()
