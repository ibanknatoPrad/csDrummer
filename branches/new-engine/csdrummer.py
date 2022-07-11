import optparse
import sys
import time

from csound import *



class CommandLineParser:

    def __init__(self):

        # create parser
        self.parser = optparse.OptionParser(
            usage="%prog [options]")
        # add options
        self.parser.add_option(
            "--human-force", metavar="VALUE",
            dest="HumanForce", default=0.25,
            help="hit force altering (0..1), default 0.25")
        self.parser.add_option(
            "--human-time", metavar="VALUE",
            dest="HumanTime", default=0.033,
            help="hit moment altering (sec), default 0.033")
        self.parser.add_option(
            "--human-falloff", metavar="VALUE",
            dest="HumanFalloff", default=0.33,
            help="hit force falling off (sec), default 0.33")
        input_modules = str(InputModuleGenerator.modules.keys())
        self.parser.add_option(
            "--input-module", metavar="MODULE",
            dest="InputModule", default="portmidi",
            help="input modules: " + input_modules)
        output_modules = str(OutputModuleGenerator.modules.keys())
        self.parser.add_option(
            "--output-module", metavar="MODULE",
            dest="OutputModule", default="portaudio",
            help="output modules: " + output_modules)
        self.parser.add_option(
            "--input", metavar="INPUT",
            dest="Input", default="0",
            help="input file or device")
        self.parser.add_option(
            "--output", metavar="OUTPUT",
            dest="Output", default="0",
            help="output file or device")
        self.parser.add_option(
            "--drumkit", metavar="FILENAME",
            dest="DrumKit", default="DrumKit.xml",
            help="drum kit file")
        self.parser.add_option(
            "--multi", action="store_true",
            dest="Multichannel", default=False,
            help="multichannel output")
        self.parser.add_option(
            "--low", action="store_true",
            dest="LowQuality", default=False,
            help="low quality")
        self.parser.add_option(
            "--fftsize", metavar="INT",
            dest="FFTSize", default=1024,
            help="FFT window size")
        self.parser.add_option(
            "--csound", metavar="OPTS",
            dest="Csound", default="",
            help="custom Csound options")
        self.parser.add_option(
            "--debug", action="store_true",
            dest="Debug", default=False,
            help="display debug info")


    def parse(self, arglist):

        # parse args
        options, args = self.parser.parse_args(arglist)
        return options.__dict__



def main():

    # hello
    print "csdrummer, Copyright (C) 2008 Schlagg"
    print "csdrummer comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions. Look at LICENSE.txt for details."
    # init
    opts = CommandLineParser().parse(sys.argv)
    engine = CsoundEngine(opts)
    engine.run()
    while engine.get_status() == 0:
        time.sleep(1)
    engine.halt()
    print "status:", engine.get_status()


if __name__ == "__main__":
    main()

