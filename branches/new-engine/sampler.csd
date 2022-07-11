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

gkHumanForce init $HumanForce
gkHumanTime init $HumanTime
gkHumanFalloff init $HumanFalloff

/* configure MIDI routing */

massign 0, 0
massign 10, 1

/* initalize Python and exec internal engine code */

pyinit

pyexeci "sampler.py"

/* configure trigger's container */

giInstruments ftgen 0, 0, 128, 17, 0, -1

/* load drumkit */

$DrumKitLoader

/* python to opcode wrappers */

opcode IsExists, i, i
    iMIDI xin
    iExists pycall1i "is_exists", iMIDI
    xout iExists
endop

opcode GetInstrument, i, i
    iMIDI xin
    iInstrument pycall1i "get_instrument", iMIDI
    xout iInstrument
endop

opcode GetNumTargets, i, i
    iMIDI xin
    iNumTargets pycall1i "get_num_targets", iMIDI
    xout iNumTargets
endop

opcode GetTargetChannel, i, ii
    iMIDI, iTarget xin
    iChannel pycall1i "get_target_channel", iMIDI, iTarget
    xout iChannel 
endop

opcode GetTargetADSR, iiii, ii
    iMIDI, iTarget xin
    iAttack, iDecay, iRelease, iSustain pycall4i "get_target_adsr", iMIDI, iTarget
    xout iAttack, iDecay, iRelease, iSustain
endop

opcode GetNumLayers, i, ii
    iMIDI, iTarget xin
    iNumLayers pycall1i "get_num_layers", iMIDI, iTarget
    xout iNumLayers
endop

opcode GetLayerVelocity, i, iii
    iMIDI, iTarget, iLayer xin
    iVelocity pycall1i "get_layer_vel", iMIDI, iTarget, iLayer
    xout iVelocity
endop

opcode GetLayerGain, i, iii
    iMIDI, iTarget, iLayer xin
    iGain pycall1i "get_layer_gain", iMIDI, iTarget, iLayer
    xout iGain
endop

opcode GetLayerSample, i, iii
    iMIDI, iTarget, iLayer xin
    iSample pycall1i "get_layer_sample", iMIDI, iTarget, iLayer
    xout iSample
endop

/* force fallof humanizer */

opcode HumanFalloff, i, iii

    iVel, iTime, iHuman xin
    
    if (giDebug > 0) then
        prints "sampler.csd: HumanFalloff\n"
    endif

    if (iHuman > 0) then
        iFalloffAlpha = - log(1 - 0.997)/iHuman
        iFalloff = 1 - exp(- iTime)/iFalloffAlpha
    else
        iFalloff = 1
    endif
        
    iFallVel = iVel*iFalloff
    
    if (giDebug > 0) then    
        print iVel
        print iTime
        print iHuman
        print iFalloff
        print iFallVel
    endif    

    xout iFallVel

endop

/* force humanizer */

opcode HumanForce, i, ii

    iVel, iHuman xin
    
    if (giDebug > 0) then
        prints "sampler.csd: HumanForce\n"
    endif    
    
    iForce gauss 1
    iForce = iVel + iHuman*iForce
    if (iForce < 0) then
        iForce = 0
    endif
    
    if (giDebug > 0) then
        print iVel
        print iHuman
        print iForce
    endif

    xout iForce
    
endop

/* time humanizer */

opcode HumanTime, i, i

    iHuman xin
    
    if (giDebug > 0) then
        prints "sampler.csd: HumanTime\n"
    endif      

    iTime gauss 1
    iTime = iTime/2 + iHuman*iTime/2
    if (iTime < 0) then
        iTime = 0
    endif
    
    if (giDebug > 0) then
        print iHuman
        print iTime
    endif          

    xout iTime
    
endop

/*  layers searcher */

opcode FindLayers, ii, iii

    iMIDI, iTarget, iVel xin
    
    if (giDebug > 0) then
        prints "sampler.csd: HumanTime\n"
    endif      

    iNumLayers GetNumLayers iMIDI, iTarget
    iTop = iNumLayers - 1
    iBottom = 0
    iLayer = 0
NextLayer:
        iLayerVel GetLayerVelocity iMIDI, iTarget, iLayer
        iTopVel GetLayerVelocity iMIDI, iTarget, iTop
        iBottomVel GetLayerVelocity iMIDI, iTarget, iBottom
        if (iLayerVel > iBottomVel) && (iLayerVel < iVel) then
            iBottom = iLayer
        endif
        if (iLayerVel < iTopVel) && (iLayerVel >= iVel) then
            iTop = iLayer
        endif
    loop_lt iLayer, 1, iNumLayers, NextLayer

    if (giDebug > 0) then
        print iMIDI
        print iTarget
        print iVel
        print iTop
        print iBottom
    endif          
    
    xout iTop, iBottom
    
endop

/* morph factor interpolation */

opcode InterpolateMorph, i, iii

    iTopVel, iBottomVel, iVel xin

    if (iTopVel == iBottomVel) then
        iMorph = 0
    else
        iMorph = (iVel - iBottomVel)/(iTopVel - iBottomVel)
    endif
        
    xout iMorph

endop

/*  instrument */

instr Instrument

    if (giDebug > 0) then
        prints "sampler.csd: Instrument\n"
    endif          

    /* load event parameters */

    iMIDI = p4
    iVel = p5
    
    /* get trigger */

    iTrigger GetInstrument iMIDI

    /* set trigger and calc period */

    iStartTime timek
    kStopped init 0

    iPeriod table iTrigger, giInstruments
    if (iPeriod > 0) then
        iPeriod = iStartTime - iPeriod
    else
        iPeriod = i(gkHumanFalloff)*kr
    endif

    tableiw iStartTime, iTrigger, giInstruments

    /* calculate falloff */

    iVel HumanFalloff iVel, iPeriod/kr, i(gkHumanFalloff)

    /* humanize hit force */

    iForce HumanForce iVel, i(gkHumanForce)

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

        /* get layers */

        iTopLayer, iBottomLayer FindLayers iMIDI, iTarget, iForce
        iTopGain GetLayerGain iMIDI, iTarget, iTopLayer
        iBottomGain GetLayerGain iMIDI, iTarget, iBottomLayer
        iTopWave GetLayerSample iMIDI, iTarget, iTopLayer
        iBottomWave GetLayerSample iMIDI, iTarget, iBottomLayer
        iTopVelocity GetLayerVelocity iMIDI, iTarget, iTopLayer
        iBottomVelocity GetLayerVelocity iMIDI, iTarget, iBottomLayer

        /* calculate morphing factor */

        iMorph InterpolateMorph iTopVelocity, iBottomVelocity, iForce

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

            aMorph = (iMorph*aTop + (1-iMorph)*aBottom)

        else

            fTop pvsanal aTop, giFFT, giFFT/4, giFFT*2, 0
            fBottom pvsanal aBottom, giFFT, giFFT/4, giFFT*2, 0
            fMorph pvsmorph fBottom, fTop, iMorph, iMorph
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

        /* output */

        aOutput = aEnv

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

        /* check for presence */

        iExists IsExists iMIDI

        if (iExists > 0) then

            /* humanize time */

            iTime HumanTime i(gkHumanTime)

            /* Shedule note */

            schedule "Instrument", iTime, 1, iMIDI, iVel

        else

            printf "warning(sampler.csd): non-existing instrument at midi note %d\n", 1, iMIDI

        endif

    else

        printf_i "warning(sampler.orc): MIDI channel %d message recieved\n", 1, iMIDIChannel

    endif

endin

</CsInstruments>