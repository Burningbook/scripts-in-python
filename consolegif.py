#!/usr/bin/python
#play image in console
import Image
import os
import sys
import time 

def oneFrame():
	gif.save("./t.bmp")
	if(os.system("python consoleimage.py ./t.bmp")!=0):
		os._exit(0) 
if __name__ == '__main__':
	gif=Image.open(sys.argv[1])
	oneFrame()
	while True:
		try:
			gif.seek(gif.tell() + 1)
			oneFrame()
		except EOFError:
			gif.seek(0)
			oneFrame()
		except  KeyboardInterrupt:
			os._exit(0)

