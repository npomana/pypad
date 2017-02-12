
import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")

import random
import pygame




def scroll(lp):
	# 8 because hight is 8
	# while loop, color is red and waits 50ms before changing next one
	but = 8
	while (but > 0):
		lp.LedCtrlXY(3,but,100,0,0)
		but -= 1
		pygame.time.wait(50)	



def main():
	mode = None

	# create an instance
	lp = launchpad.Launchpad();

	# check what we have here and override lp if necessary
	if lp.Check( 0, "mk2" ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0, "mk2" ):
			print("Loaded")
			mode = "Mk2"

	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()
	print('at individual light')	
	lp.LedCtrlXY(0,0,100,0,0)
	pygame.time.wait(500)
	#forget coordinates, doesn't wipe visuals.
	lp.ButtonFlush()

	#check above
	scroll(lp)
	
	#resets colors
	lp.Reset()

	sample =  lp.LedCtrlXY(1,1,0,64,0)
	print('attempting sound')


	pygame.mixer.init()
	pygame.mixer.load('01.wav')
	pygame.mixer.play()
	


	pygame.time.wait(2000)


	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

