# csDrummer
Csound Record a drum session in a virtual studio
First of all you need Csound 5.09 or late. Versions before 5.09 have a serious bug in morphing opcode. Software works but this results in a more synthetic sounds.

After you obtain Csound and choose MIDI file enter this in command-line: csound -o Output.wav -F Input.mid -T -d Drummer.orc Generated sound will be written to Output.wav and rendering will be terminated when the end of MIDI file is reached.

You may also use additional options: csound -o Output.wav -F Input.mid -T -d --omacro:Option=Value Drummer.orc

Available options: | Realtime | Set it to any value to use the low quality realtime mix-morphing (SVN version only) | |:---------|:------------------------------------------------------------------------------------| | Multichannel | Set it to any value to generate multichannel audio file. | | HumanAmp | Value of 0..1. Affects the hit force altering. | | HumanMorph | Value of 0..1. Affects the morphing altering. | | HumanTime | Value in sec. Affects the hit moment altering. | | HumanFalloff | Value in sec. Affects hit force falling off at high speed. (SVN version only) |

You can also refer to Csound command-line options. http://www.csounds.com/manual/html/CommandFlagsCategory.html
