#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(96)

#Music

s2=Y05_STRINGS_2
s1=Y05_STRINGS_1
piano=Y05_PIANO_2
piano2=Y05_PIANO_1
piano3=Y06_PIANO
a1=Y21_ALERT_1
g1=Y05_GUITAR_1
t1=YG_POP_TAMBOURINE_1
piano4=Y09_PIANO_1

fitMedia(s1, 7, 1, 5)
fitMedia(s2,1, 5, 9)
fitMedia(a1, 3, 7, 11) # transition 
fitMedia(piano2, 1, 9, 17)
fitMedia(piano3, 1, 17, 21)
fitMedia(g1,2, 9, 17)
fitMedia(t1, 4, 5, 9)
fitMedia(YG_RNB_SHAKER_1, 5, 4, 9)
fitMedia(piano4, 6, 13, 17)
fitMedia(piano3, 8, 18, 22)

#Effect
setEffect(2, VOLUME, GAIN, -1, 9, -1, 17)
setEffect(3, VOLUME, GAIN, 6, 7.5, 10, 11.5)
setEffect(4, VOLUME, GAIN, 7, 5, 7, 9)
setEffect(5, VOLUME, GAIN, -15, 3, -15, 9)
setEffect(6, VOLUME, GAIN, -20, 13, 5, 17)
setEffect(7, VOLUME, GAIN, -30, 1, 0, 4) # music fade in at the beginning
setEffect(7, DELAY, DELAY_TIME, 500)
setEffect(7, DELAY, DELAY_FEEDBACK, -10.0)
setEffect(8, VOLUME, GAIN, -50, 18, -50, 21)
setEffect(8, VOLUME, GAIN, 0, 21, -30, 22) #music fade out at the end


finish()
