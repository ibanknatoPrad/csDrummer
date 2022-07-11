<CsoundSynthesizer>
<CsOptions>

$CsoundOptions

</CsOptions>
<CsInstruments>
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

/* settings */

ksmps = 4

nchnls = $NumChannels

giLowQuality = $LowQuality

giFFT = $FFTSize

giDebug = $Debug

/* controllable parameters */

giMaxHumanTime = $HumanTime
giMaxHumanFalloff = $HumanFalloff
giMaxHumanVel = 1

/* configure MIDI channels */

massign 0, 0
massign 10, 1

/* configure MIDI controllers */

giMIDICtlMSB = 20
giMIDICtlLSB = 52
giHumanForceCtl = 0
giHumanMorphCtl = 1
giHumanFalloff = 2
giHumanTimeCtl = 3

initc14 10, giMIDICtlMSB + giHumanForceCtl, giMIDICtlLSB + giHumanForceCtl, 0
initc14 10, giMIDICtlMSB + giHumanMorphCtl, giMIDICtlLSB + giHumanMorphCtl, 0
initc14 10, giMIDICtlMSB + giHumanFalloff, giMIDICtlLSB + giHumanFalloff, 0
initc14 10, giMIDICtlMSB + giHumanTimeCtl, giMIDICtlLSB + giHumanTimeCtl, 0

/* initalize Python and exec internal engine code */

pyinit

pyexeci "$SamplerScript"

pyruni {{

__sampler = Sampler()

# defs for loader

createInstrument = __sampler.createInstrument
createTechnique = __sampler.createTechnique
createTarget = __sampler.createTarget
createLayer = __sampler.createLayer
setTechniqueMIDI = __sampler.setTechniqueMIDI
setTargetChannel = __sampler.setTargetChannel
setTargetGain = __sampler.setTargetGain
setTargetADSR = __sampler.setTargetADSR
sortLayersByVel = __sampler.sortLayersByVel
setLayerVelocity = __sampler.setLayerVelocity
setLayerGain = __sampler.setLayerGain
setLayerSample = __sampler.setLayerSample
setSampleData = __sampler.setSampleData
setDebug = __sampler.setDebug
printDebug = __sampler.printDebug

# defs for user

isExists = __sampler.isExists
getInstrument = __sampler.getInstrument
getNumTargets = __sampler.getNumTargets
getTargetChannel = __sampler.getTargetChannel
getTargetGain = __sampler.getTargetGain
getTargetADSR = __sampler.getTargetADSR
getMorph = __sampler.getMorph
getNumLayers = __sampler.getNumLayers
getLayerVelocity = __sampler.getLayerVelocity
getLayerGain = __sampler.getLayerGain
getLayerSample = __sampler.getLayerSample
getSampleData = __sampler.getSampleData
humanFalloff = __sampler.humanFalloff
humanVelocity = __sampler.humanVelocity
humanTime = __sampler.humanTime

}}

pycalli "setDebug", giDebug

/* configure trigger's container */

giInstruments ftgen 0, 0, 128, 17, 0, -1

/* load drumkit */

$DrumkitLoader

pycalli "printDebug", 0

/* python to opcode wrappers */

opcode IsExists, i, i
    iMIDI xin
    iExists pycall1i "isExists", iMIDI
    xout iExists
endop

opcode GetInstrument, i, i
    iMIDI xin
    iInstrument pycall1i "getInstrument", iMIDI
    xout iInstrument
endop

opcode GetNumTargets, i, i
    iMIDI xin
    iNumTargets pycall1i "getNumTargets", iMIDI
    xout iNumTargets
endop

opcode GetTargetChannel, i, ii
    iMIDI, iTarget xin
    iChannel pycall1i "getTargetChannel", iMIDI, iTarget
    xout iChannel 
endop

opcode GetTargetGain, i, ii
    iMIDI, iTarget xin
    iGain pycall1i "getTargetGain", iMIDI, iTarget
    xout iGain
endop

opcode GetTargetADSR, iiii, ii
    iMIDI, iTarget xin
    iAttack, iDecay, iRelease, iSustain pycall4i "getTargetADSR", iMIDI, iTarget
    xout iAttack, iDecay, iRelease, iSustain
endop

opcode GetNumLayers, i, ii
    iMIDI, iTarget xin
    iNumLayers pycall1i "getNumLayers", iMIDI, iTarget
    xout iNumLayers
endop

opcode GetLayerVelocity, i, iii
    iMIDI, iTarget, iLayer xin
    iVelocity pycall1i "getLayerVelocity", iMIDI, iTarget, iLayer
    xout iVelocity
endop

opcode GetLayerGain, i, iii
    iMIDI, iTarget, iLayer xin
    iGain pycall1i "getLayerGain", iMIDI, iTarget, iLayer
    xout iGain
endop

opcode GetLayerSample, i, iii
    iMIDI, iTarget, iLayer xin
    iSample pycall1i "getLayerSample", iMIDI, iTarget, iLayer
    xout iSample
endop

opcode GetSampleData, i, i
    iSample xin
    iData pycall1i "getSampleData", iSample
    xout iData
endop

opcode HumanFalloff, i, iii
    iVel, iTime, iHuman xin
    iFallVel pycall1i "humanFalloff", iVel, iTime, iHuman
    xout iFallVel
endop

opcode HumanVelocity, i, ii
    iVel, iHuman xin
    iForce pycall1i "humanVelocity", iVel, iHuman
    xout iForce
endop

opcode HumanTime, i, i
    iHuman xin
    iTime pycall1i "humanTime", iHuman
    xout iTime
endop

opcode getMorph, iii, iii
    iMIDI, iTarget, iVel xin
    iTop, iBottom, iMorph pycall3i "getMorph", iMIDI, iTarget, iVel
    xout iTop, iBottom, iMorph
endop

/*  instrument */

instr Instrument

    if (giDebug > 0) then
        prints "sampler.csd: Instrument\n"
    endif          

    /* load event parameters */

    iMIDI = p4
    iVel = p5
    
    /* get human controllers values */
    
    iHumanForce ctrl14 10, giMIDICtlMSB + giHumanForceCtl, giMIDICtlLSB + giHumanForceCtl, \
        0, giMaxHumanVel
    iHumanMorph ctrl14 10, giMIDICtlMSB + giHumanMorphCtl, giMIDICtlLSB + giHumanMorphCtl, \
        0, giMaxHumanVel
    iHumanFalloff ctrl14 10, giMIDICtlMSB + giHumanFalloff, giMIDICtlLSB + giHumanFalloff, \
        0, giMaxHumanFalloff

    if (giDebug > 0) then
        print iHumanForce
        print iHumanMorph
        print iHumanFalloff    
    endif      
    
    /* get trigger */

    iTrigger GetInstrument iMIDI

    /* set trigger and calc period */

    iStartTime timek
    kStopped init 0

    iPeriod table iTrigger, giInstruments
    if (iPeriod > 0) then
        iPeriod = iStartTime - iPeriod
    else
        iPeriod = iHumanFalloff*kr
    endif

    tableiw iStartTime, iTrigger, giInstruments

    /* calculate falloff */

    iFalloffVel HumanFalloff iVel, iPeriod/kr, iHumanFalloff

    /* humanize hit force */

    iForce HumanVelocity iFalloffVel, iHumanForce
    
    /* humanize morphing */

    iMorph HumanVelocity iForce, iHumanMorph
    
    /* calculate engine delay */

    if (giLowQuality > 0) then
        iDelay = 0.001
    else
        iDelay = giFFT*2/sr
    endif

    /* set max release time */

    iMaxRelease = 0

    /* get num targets */

    iNumTargets GetNumTargets iMIDI

    /* process for each target */
    
    iTarget = 0    

NextTarget:

        /* get morph and layers */

        iTop, iBottom, iMorphFactor getMorph iMIDI, iTarget, iMorph
        iTopGain GetLayerGain iMIDI, iTarget, iTop
        iBottomGain GetLayerGain iMIDI, iTarget, iBottom
        iTopSample GetLayerSample iMIDI, iTarget, iTop
        iBottomSample GetLayerSample iMIDI, iTarget, iBottom
        iTopWave GetSampleData iTopSample
        iBottomWave GetSampleData iBottomSample

        /* recalculate note length */

        iLenTop = nsamp(iTopWave)/ftsr(iTopWave) + iDelay
        iLenBottom = nsamp(iBottomWave)/ftsr(iBottomWave) + iDelay
        iMaxLen = (iLenTop > iLenBottom) ? iLenTop : iLenBottom
        if (iMaxLen > p3) then
            p3 = iMaxLen
        endif

        /* oscillate samples */

        if (giLowQuality > 0) then

            aTop loscil iTopGain, 1, iTopWave, 1, 0
            aBottom loscil iBottomGain, 1, iBottomWave, 1, 0

        else

            aTop loscil3 iTopGain, 1, iTopWave, 1, 0
            aBottom loscil3 iBottomGain, 1, iBottomWave, 1, 0

        endif

        /* morphing */

        if (giLowQuality > 0) then

            aMorph = (iMorphFactor*aTop + (1-iMorphFactor)*aBottom)

        else

            fTop pvsanal aTop, giFFT, giFFT/4, giFFT*2, 0
            fBottom pvsanal aBottom, giFFT, giFFT/4, giFFT*2, 0
            fMorph pvsmorph fBottom, fTop, iMorphFactor, iMorphFactor
            aMorph pvsynth fMorph

        endif

        /* get adsr */

        iAttack, iDecay, iSustain, iRelease GetTargetADSR iMIDI, iTarget
        if (iRelease > iMaxRelease) then
            iMaxRelease = iRelease
        endif

        /* envelope */

        if (kStopped < 1) then
            aADSR linseg 0, iDelay, 0, iAttack, 1, iDecay, iSustain, 1, iSustain
        else
            aADSR linseg iSustain, iDelay, iSustain, iRelease, 0, 1, 0
        endif

        aEnv = aMorph*aADSR
        
        /* apply hit force */
        
        aForce = aEnv*iForce
        
        /* target gain */
        
        iGain GetTargetGain iMIDI, iTarget
        aGain = iGain*aForce

        /* output */

        aOutput = aGain

        /* get output channel */

        iChannel GetTargetChannel iMIDI, iTarget

        /* route to audio channel */

        if (nchnls > 1) then
            if (iChannel <= nchnls) then
                outch iChannel, aOutput
            else
                printf_i "warning(sampler.csd): audio channel %d not exists\n", 1, iChannel
            endif
        else
            outch 1, aOutput
        endif

    loop_lt iTarget, 1, iNumTargets, NextTarget

    /* check for trigger */

    kTrigVal table iTrigger, giInstruments

    if (kStopped < 1) then
        if (kTrigVal > iStartTime) then
        kStopTime timek
        kStopped = 1
        endif
    else
        kCurTime timek
        if (kCurTime/kr > kStopTime/kr + iDelay + iMaxRelease) then
        turnoff
        endif
    endif

endin

/* drum channel */

instr 1

    if (giDebug > 0) then
        prints "sampler.csd: instr 1 (MIDI event)\n"
    endif          

    /* check MIDI channel */
    
    iMIDIChannel midichn
    if (iMIDIChannel = 10) then

        /* get note info */

        iMIDI notnum
        iVel veloc 0, 1
    
        /* get human tiem controller */
    
        iHumanTime ctrl14 10, giMIDICtlMSB + giHumanTimeCtl, giMIDICtlLSB + giHumanTimeCtl, \
            0, giMaxHumanTime
    
        if (giDebug > 0) then
            print iHumanTime
        endif          

        /* check for presence */

        iExists IsExists iMIDI

        if (iExists > 0) then

            /* humanize time */

            iTime HumanTime iHumanTime

            /* Shedule note */

            schedule "Instrument", iTime, 1, iMIDI, iVel

        else

            printf_i "warning(sampler.csd): non-existing instrument at midi note %d\n", 1, iMIDI

        endif

    else

        printf_i "warning(sampler.orc): MIDI channel %d message recieved\n", 1, iMIDIChannel

    endif

endin

</CsInstruments>
</CsoundSynthesizer>    