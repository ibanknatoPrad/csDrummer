/* 

csDrummer: Record a drum session in a virtual studio
Copyright (C) 2008 Schlagg

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

*/

giLayer1 ftgen 0, 0, giTableSize, 17, 0, -1
giLayer2 ftgen 0, 0, giTableSize, 17, 0, -1
giAttack ftgen 0, 0, giTableSize, 17, 0, -1
giDecay ftgen 0, 0, giTableSize, 17, 0, -1
giSustain ftgen 0, 0, giTableSize, 17, 0, -1
giRelease ftgen 0, 0, giTableSize, 17, 0, -1
giGain ftgen 0, 0, giTableSize, 17, 0, -1
giChannel ftgen 0, 0, giTableSize, 17, 0, -1
giTrigger ftgen 0, 0, giTableSize, 17, 0, -1

/* Instruments */

giSideStick1 ftgen 0, 0, 0, 1, "DrumKit/16296_ltibbits_sticks_high_pitch.flac", 0, 0, 0
giSideStick2 ftgen 0, 0, 0, 1, "DrumKit/16297_ltibbits_sticks_low_pitch.flac", 0, 0, 0
giSideStickAttack = 0.01
giSideStickDecay = 0
giSideStickSustain = 1
giSideStickRelease = 0.1
giSideStickGain = 0.75
giSideStickChannel = 1
giSideStickTrigger = 1

giBassDrum1 ftgen 0, 0, 0, 1, "DrumKit/16290_ltibbits_kick2_high_vol.flac", 0, 0, 0
giBassDrum2 ftgen 0, 0, 0, 1, "DrumKit/16291_ltibbits_kick2_low_vol.flac", 0, 0, 0
giBassDrumAttack = 0.01
giBassDrumDecay = 0
giBassDrumSustain = 1
giBassDrumRelease = 0.1
giBassDrumGain = 0.75
giBassDrumLChannel = 2
giBassDrumLTrigger = 2
giBassDrumRChannel = 3
giBassDrumRTrigger = 3

giSnareDrum1 ftgen 0, 0, 0, 1, "DrumKit/16298_ltibbits_snare_1_high_vol.flac", 0, 0, 0
giSnareDrum2 ftgen 0, 0, 0, 1, "DrumKit/16299_ltibbits_snare_1_low_vol.flac", 0, 0, 0
giSnareRim ftgen 0, 0, 0, 1, "DrumKit/16292_ltibbits_rim1_snare.flac", 0, 0, 0
giSnareDrumAttack = 0.01
giSnareDrumDecay = 0
giSnareDrumSustain = 1
giSnareDrumRelease = 0.1
giSnareDrumGain = 0.75
giSnareDrumChannel = 4
giSnareDrumTrigger = 4
giSnareRimTrigger = 100

giSnareReso1 ftgen 0, 0, 0, 1, "DrumKit/16300_ltibbits_snare_2_high_vol.flac", 0, 0, 0
giSnareReso2 ftgen 0, 0, 0, 1, "DrumKit/16301_ltibbits_snare_2_low_vol.flac", 0, 0, 0
giSnareResoAttack = 0.01
giSnareResoDecay = 0
giSnareResoSustain = 1
giSnareResoRelease = 0.1
giSnareResoGain = 0.75
giSnareResoChannel = 5
giSnareResoTrigger = 5

giFloorTom1 ftgen 0, 0, 0, 1, "DrumKit/45054_Matias.Reccius_floortom4.flac", 0, 0, 0
giFloorTom2 ftgen 0, 0, 0, 1, "DrumKit/45051_Matias.Reccius_floortom1.flac", 0, 0, 0
giFloorTomAttack = 0.01
giFloorTomDecay = 0
giFloorTomSustain = 1
giFloorTomRelease = 0.1
giFloorTomGain = 0.75
giFloorTomChannel = 6
giFloorTomTrigger = 6

giTom14_1 ftgen 0, 0, 0, 1, "DrumKit/45098_Matias.Reccius_tom14_4.flac", 0, 0, 0
giTom14_2 ftgen 0, 0, 0, 1, "DrumKit/45095_Matias.Reccius_tom14_1.flac", 0, 0, 0
giTom14Attack = 0.01
giTom14Decay = 0
giTom14Sustain = 1
giTom14Release = 0.1
giTom14Gain = 0.75
giTom14Channel = 7
giTom14Trigger = 7 

giTom13_1 ftgen 0, 0, 0, 1, "DrumKit/45094_Matias.Reccius_tom13_4.flac", 0, 0, 0
giTom13_2 ftgen 0, 0, 0, 1, "DrumKit/45091_Matias.Reccius_tom13_1.flac", 0, 0, 0
giTom13Attack = 0.01
giTom13Decay = 0
giTom13Sustain = 1
giTom13Release = 0.1
giTom13Gain = 0.75
giTom13Channel = 8
giTom13Trigger = 8

giTom12_1 ftgen 0, 0, 0, 1, "DrumKit/45090_Matias.Reccius_tom12_4.flac", 0, 0, 0
giTom12_2 ftgen 0, 0, 0, 1, "DrumKit/45087_Matias.Reccius_tom12_1.flac", 0, 0, 0
giTom12Attack = 0.01
giTom12Decay = 0
giTom12Sustain = 1
giTom12Release = 0.1
giTom12Gain = 0.75
giTom12Channel = 9
giTom12Trigger = 9

giTom10_1 ftgen 0, 0, 0, 1, "DrumKit/45086_Matias.Reccius_tom10_5.flac", 0, 0, 0
giTom10_2 ftgen 0, 0, 0, 1, "DrumKit/45082_Matias.Reccius_tom10_1.flac", 0, 0, 0
giTom10Attack = 0.01
giTom10Decay = 0
giTom10Sustain = 1
giTom10Release = 0.1
giTom10Gain = 0.75
giTom10Channel = 10
giTom10Trigger = 10

giHHClosed1 ftgen 0, 0, 0, 1, "DrumKit/16266_ltibbits_HH_A_Custom_closed_hard.flac", 0, 0, 0
giHHClosed2 ftgen 0, 0, 0, 1, "DrumKit/16267_ltibbits_HH_A_Custom_closed_soft.flac", 0, 0, 0
giHHFoot1 ftgen 0, 0, 0, 1, "DrumKit/16268_ltibbits_HH_A_Custom_foot1.flac", 0, 0, 0
giHHFoot2 ftgen 0, 0, 0, 1, "DrumKit/16269_ltibbits_HH_A_Custom_foot2.flac", 0, 0, 0
giHHOpen1 ftgen 0, 0, 0, 1, "DrumKit/16273_ltibbits_HH_A_Custom_half_open_hard.flac", 0, 0, 0
giHHOpen2 ftgen 0, 0, 0, 1, "DrumKit/16274_ltibbits_HH_A_Custom_half_open_soft.flac", 0, 0, 0
giHiHatAttack = 0.01
giHiHatDecay = 0
giHiHatSustain = 1
giHiHatRelease = 0.1
giHiHatGain = 0.75
giHiHatChannel = 11
giHiHatTrigger = 11

giCrash17_1 ftgen 0, 0, 0, 1, "DrumKit/16253_ltibbits_crash_A_medium_17_high_vol.flac", 0, 0, 0
giCrash17_2 ftgen 0, 0, 0, 1, "DrumKit/16254_ltibbits_crash_A_medium_17_low_vol.flac", 0, 0, 0
giCrash17Attack = 0.01
giCrash17Decay = 0
giCrash17Sustain = 1
giCrash17Release = 0.1
giCrash17Gain = 0.75
giCrash17Channel = 12
giCrash17Trigger = 12

giCrash18_1 ftgen 0, 0, 0, 1, "DrumKit/16248_ltibbits_crash_A_custom_18_high_vol.flac", 0, 0, 0
giCrash18_2 ftgen 0, 0, 0, 1, "DrumKit/16249_ltibbits_crash_A_custom_18_low_vol.flac", 0, 0, 0
giCrash18Attack = 0.01
giCrash18Decay = 0
giCrash18Sustain = 1
giCrash18Release = 0.1
giCrash18Gain = 0.75
giCrash18Channel = 13
giCrash18Trigger = 13

giCrashZ1 ftgen 0, 0, 0, 1, "DrumKit/16263_ltibbits_crash_Z_custom_projection_19_high_vol.flac", 0, 0, 0
giCrashZ2 ftgen 0, 0, 0, 1, "DrumKit/16264_ltibbits_crash_Z_custom_projection_19_low_vol.flac", 0, 0, 0
giCrashZTip ftgen 0, 0, 0, 1, "DrumKit/16265_ltibbits_crash_Z_custom_projection_19_tip.flac", 0, 0, 0
giCrashZAttack = 0.01
giCrashZDecay = 0
giCrashZSustain = 1
giCrashZRelease = 0.1
giCrashZGain = 0.75
giCrashZChannel = 14
giCrashZTrigger = 14

giCrashHHX1 ftgen 0, 0, 0, 1, "DrumKit/16258_ltibbits_crash_HHXplosion_18_high_vol.flac", 0, 0, 0
giCrashHHX2 ftgen 0, 0, 0, 1, "DrumKit/16259_ltibbits_crash_HHXplosion_18_low_vol.flac", 0, 0, 0
giCrashHHXAttack = 0.01
giCrashHHXDecay = 0
giCrashHHXSustain = 1
giCrashHHXRelease = 0.1
giCrashHHXGain = 0.75
giCrashHHXChannel = 15
giCrashHHXTrigger = 15

giChina16_1 ftgen 0, 0, 0, 1, "DrumKit/16239_ltibbits_china_A_China_High_16_high_vol.flac", 0, 0, 0
giChina16_2 ftgen 0, 0, 0, 1, "DrumKit/16240_ltibbits_china_A_China_High_16_low_vol.flac", 0, 0, 0
giChina16Attack = 0.01
giChina16Decay = 0
giChina16Sustain = 1
giChina16Release = 0.1
giChina16Gain = 0.75
giChina16Channel = 16
giChina16Trigger = 16

giChina18_1 ftgen 0, 0, 0, 1, "DrumKit/16243_ltibbits_china_oriental_trash_18_high_vol.flac", 0, 0, 0
giChina18_2 ftgen 0, 0, 0, 1, "DrumKit/16244_ltibbits_china_oriental_trash_18_low_vol.flac", 0, 0, 0
giChina18Attack = 0.01
giChina18Decay = 0
giChina18Sustain = 1
giChina18Release = 0.1
giChina18Gain = 0.75
giChina18Channel = 17
giChina18Trigger = 17

giRide1 ftgen 0, 0, 0, 1, "DrumKit/16279_ltibbits_ride_A_Ping_20_bow1.flac", 0, 0, 0
giRide2 ftgen 0, 0, 0, 1, "DrumKit/16280_ltibbits_ride_A_Ping_20_bow2.flac", 0, 0, 0
giRideBell1 ftgen 0, 0, 0, 1, "DrumKit/16278_ltibbits_ride_A_Ping_20_bell.flac", 0, 0, 0
giRideBell2 ftgen 0, 0, 0, 1, "DrumKit/16277_ltibbits_ride_A_Ping_20_bell_2.flac", 0, 0, 0
giRideAttack = 0.01
giRideDecay = 0
giRideSustain = 1
giRideRelease = 0.1
giRideGain = 0.75
giRideChannel = 18
giRideTrigger = 18

giSplash10_1 ftgen 0, 0, 0, 1, "DrumKit/16282_ltibbits_splash_A_custom_10_high_vol.flac", 0, 0, 0
giSplash10_2 ftgen 0, 0, 0, 1, "DrumKit/16283_ltibbits_splash_A_custom_10_low_vol.flac", 0, 0, 0
giSplash10Attack = 0.01
giSplash10Decay = 0
giSplash10Sustain = 1
giSplash10Release = 0.1
giSplash10Gain = 0.75
giSplash10Channel = 19
giSplash10Trigger = 19

giSplashZXT1 ftgen 0, 0, 0, 1, "DrumKit/16285_ltibbits_splash_zxt_flash_10_high_vol.flac", 0, 0, 0
giSplashZXT2 ftgen 0, 0, 0, 1, "DrumKit/16286_ltibbits_splash_zxt_flash_10_low_vol.flac", 0, 0, 0
giSplashZXTAttack = 0.01
giSplashZXTDecay = 0
giSplashZXTSustain = 1
giSplashZXTRelease = 0.1
giSplashZXTGain = 0.75
giSplashZXTChannel = 20
giSplashZXTTrigger = 20

/* MIDI #37 "Side Stick" */

tableiw giSideStick1, 37, giLayer1
tableiw giSideStick2, 37, giLayer2
tableiw giSideStickAttack, 37, giAttack
tableiw giSideStickDecay, 37, giDecay
tableiw giSideStickSustain, 37, giSustain
tableiw giSideStickRelease, 37, giRelease
tableiw giSideStickGain, 37, giGain
tableiw giSideStickChannel, 37, giChannel
tableiw giSideStickTrigger, 37, giTrigger

/* MIDI #35 "Bass Drum" */

tableiw giBassDrum1, 35, giLayer1
tableiw giBassDrum2, 35, giLayer2
tableiw giBassDrumAttack, 35, giAttack
tableiw giBassDrumDecay, 35, giDecay
tableiw giBassDrumSustain, 35, giSustain
tableiw giBassDrumRelease, 35, giRelease
tableiw giBassDrumGain, 35, giGain
tableiw giBassDrumLChannel, 35, giChannel
tableiw giBassDrumLTrigger, 35, giTrigger

/* MIDI #36 "Second Bass Drum" */

tableiw giBassDrum1, 36, giLayer1
tableiw giBassDrum2, 36, giLayer2
tableiw giBassDrumAttack, 36, giAttack
tableiw giBassDrumDecay, 36, giDecay
tableiw giBassDrumSustain, 36, giSustain
tableiw giBassDrumRelease, 36, giRelease
tableiw giBassDrumGain, 36, giGain
tableiw giBassDrumRChannel, 36, giChannel
tableiw giBassDrumRTrigger, 36, giTrigger

/* MIDI #38 "Snare Drum" */

tableiw giSnareDrum1, 38, giLayer1
tableiw giSnareDrum2, 38, giLayer2
tableiw giSnareDrumAttack, 38, giAttack
tableiw giSnareDrumDecay, 38, giDecay
tableiw giSnareDrumSustain, 38, giSustain
tableiw giSnareDrumRelease, 38, giRelease
tableiw giSnareDrumGain, 38, giGain
tableiw giSnareDrumChannel, 38, giChannel
tableiw giSnareDrumTrigger, 38, giTrigger

/* MIDI #39 "Snare Rim" */

tableiw giSnareRim, 39, giLayer1
tableiw giSnareDrumAttack, 39, giAttack
tableiw giSnareDrumDecay, 39, giDecay
tableiw giSnareDrumSustain, 39, giSustain
tableiw giSnareDrumRelease, 39, giRelease
tableiw giSnareDrumGain, 39, giGain
tableiw giSnareDrumChannel, 39, giChannel
tableiw giSnareRimTrigger, 39, giTrigger

/* MIDI #40 "Second Snare Drum" */

tableiw giSnareReso1, 40, giLayer1
tableiw giSnareReso2, 40, giLayer2
tableiw giSnareResoAttack, 40, giAttack
tableiw giSnareResoDecay, 40, giDecay
tableiw giSnareResoSustain, 40, giSustain
tableiw giSnareResoRelease, 40, giRelease
tableiw giSnareResoGain, 40, giGain
tableiw giSnareResoChannel, 40, giChannel
tableiw giSnareResoTrigger, 40, giTrigger

/* MIDI #41 "Floor Tom" */

tableiw giFloorTom1, 41, giLayer1
tableiw giFloorTom2, 41, giLayer2
tableiw giFloorTomAttack, 41, giAttack
tableiw giFloorTomDecay, 41, giDecay
tableiw giFloorTomSustain, 41, giSustain
tableiw giFloorTomRelease, 41, giRelease
tableiw giFloorTomGain, 41, giGain
tableiw giFloorTomChannel, 41, giChannel
tableiw giFloorTomTrigger, 41, giTrigger

/* MIDI #43 "Floor Tom" */

tableiw giFloorTom1, 43, giLayer1
tableiw giFloorTom2, 43, giLayer2
tableiw giFloorTomAttack, 43, giAttack
tableiw giFloorTomDecay, 43, giDecay
tableiw giFloorTomSustain, 43, giSustain
tableiw giFloorTomRelease, 43, giRelease
tableiw giFloorTomGain, 43, giGain
tableiw giFloorTomChannel, 43, giChannel
tableiw giFloorTomTrigger, 43, giTrigger

/* MIDI #45 "Tom 14" */

tableiw giTom14_1, 45, giLayer1
tableiw giTom14_2, 45, giLayer2
tableiw giTom14Attack, 45, giAttack
tableiw giTom14Decay, 45, giDecay
tableiw giTom14Sustain, 45, giSustain
tableiw giTom14Release, 45, giRelease
tableiw giTom14Gain, 45, giGain
tableiw giTom14Channel, 45, giChannel
tableiw giTom14Trigger, 45, giTrigger

/* MIDI #47 "Tom 13" */

tableiw giTom13_1, 47, giLayer1
tableiw giTom13_2, 47, giLayer2
tableiw giTom13Attack, 47, giAttack
tableiw giTom13Decay, 47, giDecay
tableiw giTom13Sustain, 47, giSustain
tableiw giTom13Release, 47, giRelease
tableiw giTom13Gain, 47, giGain
tableiw giTom13Channel, 47, giChannel
tableiw giTom13Trigger, 47, giTrigger

/* MIDI #48 "Tom 12" */

tableiw giTom12_1, 48, giLayer1
tableiw giTom12_2, 48, giLayer2
tableiw giTom12Attack, 48, giAttack
tableiw giTom12Decay, 48, giDecay
tableiw giTom12Sustain, 48, giSustain
tableiw giTom12Release, 48, giRelease
tableiw giTom12Gain, 48, giGain
tableiw giTom12Channel, 48, giChannel
tableiw giTom12Trigger, 48, giTrigger

/* MIDI #50 "Tom 10" */

tableiw giTom10_1, 50, giLayer1
tableiw giTom10_2, 50, giLayer2
tableiw giTom10Attack, 50, giAttack
tableiw giTom10Decay, 50, giDecay
tableiw giTom10Sustain, 50, giSustain
tableiw giTom10Release, 50, giRelease
tableiw giTom10Gain, 50, giGain
tableiw giTom10Channel, 50, giChannel
tableiw giTom10Trigger, 50, giTrigger

/* MIDI #42 "Closed Hi-Hat" */

tableiw giHHClosed1, 42, giLayer1
tableiw giHHClosed2, 42, giLayer2
tableiw giHiHatAttack, 42, giAttack
tableiw giHiHatDecay, 42, giDecay
tableiw giHiHatSustain, 42, giSustain
tableiw giHiHatRelease, 42, giRelease
tableiw giHiHatGain, 42, giGain
tableiw giHiHatChannel, 42, giChannel
tableiw giHiHatTrigger, 42, giTrigger

/* MIDI #44 "Pedal Hi-Hat" */

tableiw giHHFoot1, 44, giLayer1
tableiw giHHFoot2, 44, giLayer2
tableiw giHiHatAttack, 44, giAttack
tableiw giHiHatDecay, 44, giDecay
tableiw giHiHatSustain, 44, giSustain
tableiw giHiHatRelease, 44, giRelease
tableiw giHiHatGain, 44, giGain
tableiw giHiHatChannel, 44, giChannel
tableiw giHiHatTrigger, 44, giTrigger

/* MIDI #46 "Open Hi-Hat" */

tableiw giHHOpen1, 46, giLayer1
tableiw giHHOpen2, 46, giLayer2
tableiw giHiHatAttack, 46, giAttack
tableiw giHiHatDecay, 46, giDecay
tableiw giHiHatSustain, 46, giSustain
tableiw giHiHatRelease, 46, giRelease
tableiw giHiHatGain, 46, giGain
tableiw giHiHatChannel, 46, giChannel
tableiw giHiHatTrigger, 46, giTrigger

/* MIDI #49 "Crash 17" */

tableiw giCrash17_1, 49, giLayer1
tableiw giCrash17_2, 49, giLayer2
tableiw giCrash17Attack, 49, giAttack
tableiw giCrash17Decay, 49, giDecay
tableiw giCrash17Sustain, 49, giSustain
tableiw giCrash17Release, 49, giRelease
tableiw giCrash17Gain, 49, giGain
tableiw giCrash17Channel, 49, giChannel
tableiw giCrash17Trigger, 49, giTrigger

/* MIDI #57 "Crash 18" */

tableiw giCrash18_1, 57, giLayer1
tableiw giCrash18_2, 57, giLayer2
tableiw giCrash18Attack, 57, giAttack
tableiw giCrash18Decay, 57, giDecay
tableiw giCrash18Sustain, 57, giSustain
tableiw giCrash18Release, 57, giRelease
tableiw giCrash18Gain, 57, giGain
tableiw giCrash18Channel, 57, giChannel
tableiw giCrash18Trigger, 57, giTrigger

/* MIDI #58 "Crash Z" */

tableiw giCrashZ1, 58, giLayer1
tableiw giCrashZ2, 58, giLayer2
tableiw giCrashZAttack, 58, giAttack
tableiw giCrashZDecay, 58, giDecay
tableiw giCrashZSustain, 58, giSustain
tableiw giCrashZRelease, 58, giRelease
tableiw giCrashZGain, 58, giGain
tableiw giCrashZChannel, 58, giChannel
tableiw giCrashZTrigger, 58, giTrigger

/* MIDI #59 "Crash Z Tip" */

tableiw giCrashZTip, 59, giLayer1
tableiw giCrashZAttack, 59, giAttack
tableiw giCrashZDecay, 59, giDecay
tableiw giCrashZSustain, 59, giSustain
tableiw giCrashZRelease, 59, giRelease
tableiw giCrashZGain, 59, giGain
tableiw giCrashZChannel, 59, giChannel
tableiw giCrashZTrigger, 59, giTrigger

/* MIDI #56 "Crash HHX" */

tableiw giCrashHHX1, 56, giLayer1
tableiw giCrashHHX2, 56, giLayer2
tableiw giCrashHHXAttack, 56, giAttack
tableiw giCrashHHXDecay, 56, giDecay
tableiw giCrashHHXSustain, 56, giSustain
tableiw giCrashHHXRelease, 56, giRelease
tableiw giCrashHHXGain, 56, giGain
tableiw giCrashHHXChannel, 56, giChannel
tableiw giCrashHHXTrigger, 56, giTrigger

/* MIDI #52 "China 16" */

tableiw giChina16_1, 52, giLayer1
tableiw giChina16_2, 52, giLayer2
tableiw giChina16Attack, 52, giAttack
tableiw giChina16Decay, 52, giDecay
tableiw giChina16Sustain, 52, giSustain
tableiw giChina16Release, 52, giRelease
tableiw giChina16Gain, 52, giGain
tableiw giChina16Channel, 52, giChannel
tableiw giChina16Trigger, 52, giTrigger

/* MIDI #54 "China 18" */

tableiw giChina18_1, 54, giLayer1
tableiw giChina18_2, 54, giLayer2
tableiw giChina18Attack, 54, giAttack
tableiw giChina18Decay, 54, giDecay
tableiw giChina18Sustain, 54, giSustain
tableiw giChina18Release, 54, giRelease
tableiw giChina18Gain, 54, giGain
tableiw giChina18Channel, 54, giChannel
tableiw giChina18Trigger, 54, giTrigger

/* MIDI #51 "Ride" */

tableiw giRide1, 51, giLayer1
tableiw giRide2, 51, giLayer2
tableiw giRideAttack, 51, giAttack
tableiw giRideDecay, 51, giDecay
tableiw giRideSustain, 51, giSustain
tableiw giRideRelease, 51, giRelease
tableiw giRideGain, 51, giGain
tableiw giRideChannel, 51, giChannel
tableiw giRideTrigger, 51, giTrigger

/* MIDI #53 "Ride Bell" */

tableiw giRideBell1, 53, giLayer1
tableiw giRideBell2, 53, giLayer2
tableiw giRideAttack, 53, giAttack
tableiw giRideDecay, 53, giDecay
tableiw giRideSustain, 53, giSustain
tableiw giRideRelease, 53, giRelease
tableiw giRideGain, 53, giGain
tableiw giRideChannel, 53, giChannel
tableiw giRideTrigger, 53, giTrigger

/* MIDI #55 "Splash 10" */

tableiw giSplash10_1, 55, giLayer1
tableiw giSplash10_2, 55, giLayer2
tableiw giSplash10Attack, 55, giAttack
tableiw giSplash10Decay, 55, giDecay
tableiw giSplash10Sustain, 55, giSustain
tableiw giSplash10Release, 55, giRelease
tableiw giSplash10Gain, 55, giGain
tableiw giSplash10Channel, 55, giChannel
tableiw giSplash10Trigger, 55, giTrigger

/* MIDI #60 "Splash ZXT" */

tableiw giSplashZXT1, 60, giLayer1
tableiw giSplashZXT2, 60, giLayer2
tableiw giSplashZXTAttack, 60, giAttack
tableiw giSplashZXTDecay, 60, giDecay
tableiw giSplashZXTSustain, 60, giSustain
tableiw giSplashZXTRelease, 60, giRelease
tableiw giSplashZXTGain, 60, giGain
tableiw giSplashZXTChannel, 60, giChannel
tableiw giSplashZXTTrigger, 60, giTrigger
