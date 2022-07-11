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

/* Global reserved symbols */

sr = 44100
ksmps = 4

#ifdef Multichannel
nchnls = 20
#else
nchnls = 1
#endif

/* Settings */

#ifdef FFTSize
giFFT = $FFTSize
#else
giFFT = 1024
#endif

#ifdef HumanMorph
giHumanMorph = $HumanMorph
#else
giHumanMorph = 0.25
#endif

#ifdef HumanAmp
giHumanAmp = $HumanAmp
#else
giHumanAmp = 0.25
#endif

#ifdef HumanTime
giHumanTime = $HumanTime
#else
giHumanTime = 0.025
#endif

/* Configure MIDI routing */

massign 0, 0
massign 10, 1

/* DrumKit description */

giTableSize = 256

#include "DrumKit.inc"

/* 
    Instrument 
        p4 - Note
        p4 - Velocity
*/

giTriggerList ftgen 0, 0, giTableSize, 17, 0, -1

instr Instrument

    iNote = p4
    iVel = p5
    
    /* Reading instrument params */
    
    iLayer1 tablei iNote, giLayer1
    iLayer2 tablei iNote, giLayer2
    iAttack tablei iNote, giAttack
    iDecay tablei iNote, giDecay
    iSustain tablei iNote, giSustain
    iRelease tablei iNote, giRelease
    iGain tablei iNote, giGain
    iChannel tablei iNote, giChannel
    iTrigger tablei iNote, giTrigger

    /* Setting trigger */
    
    kTrigged init 0
    
    if (kTrigged < 1) then
        kStartTime timek
        tablew kStartTime, iTrigger, giTriggerList
        kTrigged = 1
    endif
    
    /* Check for instrument presence */
    
    if (iLayer1 > 0) then
    
        /* Setting note lenght */

        iLen1 = nsamp(iLayer1)/ftsr(iLayer1)
        if (iLayer2 > 0) then
            iLen2 = nsamp(iLayer2)/ftsr(iLayer2)
        else
            iLen2 = 0
        endif
        p3 = (iLen1 > iLen2) ? iLen1 : iLen2
    
        /* Oscillate samples */

        a1 loscil3 0dbfs, 1, iLayer1, 1, 0
        if (iLayer2 > 0) then
            a2 loscil3 0dbfs, 1, iLayer2, 1, 0
        endif

        /* Calculate morphing factor */
            
        iMorph gauss 1
        iMorph = iVel + giHumanMorph*iMorph
        if (iMorph < 0) then
            iMorph = 0
        endif
        if (iMorph > 1) then
            iMorph = 1
        endif
        
        /* Morphing */
        
        if (iLayer2 > 0) then
        
            f1 pvsanal a1, giFFT, giFFT/4, giFFT, 0
            f2 pvsanal a2, giFFT, giFFT/4, giFFT, 0
            
            iDelay = giFFT/sr
            
            fMorph pvsmorph f2, f1, iMorph, iMorph
            
            aMorph pvsynth fMorph
        
        else
        
            aMorph = a1
            
            iDelay = 0.001
            
        endif

        /* Calculate amplifying factor */
            
        iAmp gauss 1
        iAmp = iVel + giHumanAmp*iAmp
        if (iAmp < 0) then
            iAmp = 0
        endif
        
        /* Amplifying */
        
        aAmp = iGain*iAmp*aMorph
        
        /* Check for trigger */
        
        kTrigVal table iTrigger, giTriggerList
        kStopped init 0
        
        if (kStopped < 1) then
            if (kTrigVal > kStartTime) then
                kStopTime timek 
                kStopped = 1
            endif
        else
            kCurTime timek
            if (kCurTime/kr > kStopTime/kr + iDelay + iRelease) then
                turnoff
            endif
        endif
        
        /* Envelope */
        
        if (kStopped < 1) then
            aADSR linseg 0, iDelay, 0, iAttack, 1, iDecay, iSustain, 1, iSustain
        else
            aADSR linseg iSustain, iDelay, iSustain, iRelease, 0, 1, 0        
        endif
        
        aEnv = aAmp*aADSR        

        /* Output */
        
        aOutput = aEnv
    
    else
    
        printf_i "Warning: non-existing instrument at midi note %d", 1, iNote
        
        aOutput = 0
        turnoff
    
    endif
        
    /* Route to audio channel */
        
    if (nchnls > 1) then
        if (iChannel <= nchnls) then
            outch iChannel, aOutput
        else
            printf_i "Warning: audio channel %d truncated", 1, iChannel
        endif
    else
        outch 1, aOutput
    endif    

endin

/* Drum channel */

instr 1

    /* Check MIDI channel */

    iMIDIChannel midichn
    if (iMIDIChannel = 10) then

        /* Get note info */

        iNote notnum
        iVel veloc 0, 1
        
        /* Humanize time */
        
        iTime gauss 1
        iTime = giHumanTime/2 + iTime*giHumanTime/2
        if (iTime < 0) then
            iTime = 0
        endif
        
        /* Shedule note */
        
        schedule "Instrument", iTime, 1, iNote, iVel
        
    else
    
        printf_i "Warning: MIDI channel %d message recieved", 1, iMIDIChannel
        
    endif
   
endin
