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

class Layer:

    velocity = None
    gain = None
    sample = None

    def __init__(self):

        self.velocity = 0
        self.gain = 0
        self.sample = 0


class Target:

    channel = None
    adsr = None
    layers = None

    def __init__(self):

        self.channel = 0
        self.adsr = (0, 0, 0, 0)
        self.layers = []


class Technique:

    instrument = None
    targets = None

    def __init__(self):

        self.instrument = 0
        self.targets = []


class DrumKit:

    def __init__(self):

        self.techniques = {}


    def add_technique(self, midi):

        midi_int = int(midi)
        technique = Technique()
        self.techniques[midi_int] =  technique


    def add_alias(self, alias, midi):

        alias_int = int(alias)
        midi_int = int(midi)
        technique = self.techniques[midi_int]
        self.techniques[alias_int] =  technique


    def is_exists(self, midi):

        midi_int = int(midi)
        if midi_int in self.techniques:
            return float(1)
        else:
            return float(0)


    def set_instrument(self, midi, instrument):

        midi_int = int(midi)
        technique = self.techniques[midi_int]
        technique.instrument = instrument

    def get_instrument(self, midi):

        midi_int = int(midi)
        technique = self.techniques[midi_int]
        instrument = technique.instrument
        return float(instrument)


    def add_target(self, midi):

        midi_int = int(midi)
        technique = self.techniques[midi_int]
        target = Target()
        technique.targets += [target]
        num_targets = len(technique.targets)
        return float(num_targets - 1)


    def get_num_targets(self, midi):

        midi_int = int(midi)
        technique = self.techniques[midi_int]
        num_targets = len(technique.targets)
        return float(num_targets)


    def set_target_channel(self, midi, target, channel):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        target.channel = channel


    def get_target_channel(self, midi, target):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        channel = target.channel
        return channel


    def set_target_adsr(self, midi, target, a, d, s, r):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        target.adsr = (a, d, s, r)


    def get_target_adsr(self, midi, target):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        adsr = target.adsr
        return adsr


    def add_layer(self, midi, target):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = Layer()
        target.layers += [layer]
        num_layers = len(target.layers)
        return float(num_layers - 1)


    def get_num_layers(self, midi, target):

        midi_int = int(midi)
        target_int = int(target)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        num_layers = len(target.layers)
        return float(num_layers)


    def set_layer_vel(self, midi, target, layer, vel):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        layer.velocity = vel


    def get_layer_vel(self, midi, target, layer):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        vel = layer.velocity
        return vel


    def set_layer_gain(self, midi, target, layer, gain):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        layer.gain = gain


    def get_layer_gain(self, midi, target, layer):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        gain = layer.gain
        return gain


    def set_layer_sample(self, midi, target, layer, sample):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        layer.sample = sample


    def get_layer_sample(self, midi, target, layer):

        midi_int = int(midi)
        target_int = int(target)
        layer_int = int(layer)
        technique = self.techniques[midi_int]
        target = technique.targets[target_int]
        layer = target.layers[layer_int]
        sample = layer.sample
        return sample


# create instances

drumkit = DrumKit()


# bindings for Csound

add_technique = drumkit.add_technique
add_alias = drumkit.add_alias
is_exists = drumkit.is_exists
set_instrument = drumkit.set_instrument
get_instrument = drumkit.get_instrument
add_target = drumkit.add_target
get_num_targets = drumkit.get_num_targets
set_target_channel = drumkit.set_target_channel
get_target_channel = drumkit.get_target_channel
set_target_adsr = drumkit.set_target_adsr
get_target_adsr = drumkit.get_target_adsr
add_layer = drumkit.add_layer
get_num_layers = drumkit.get_num_layers
set_layer_vel = drumkit.set_layer_vel
get_layer_vel = drumkit.get_layer_vel
set_layer_gain = drumkit.set_layer_gain
get_layer_gain = drumkit.get_layer_gain
set_layer_sample = drumkit.set_layer_sample
get_layer_sample = drumkit.get_layer_sample
