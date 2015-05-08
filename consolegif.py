#!/usr/bin/python
#play image in console
import Image
import os
import sys
import time 

if __name__ == '__main__':
	gif=Image.open(sys.argv[1])
	gif.save("./t.bmp")
	os.system("python consoleimage.py ./t.bmp")	
	while True:
		try:
			gif.seek(gif.tell() + 1)
			gif.save("./t.bmp")
			if(os.system("python consoleimage.py ./t.bmp")!=0):
				os._exit(0) 	
		except EOFError:
			gif.seek(0)
			gif.save("./t.bmp")
			if(os.system("python consoleimage.py ./t.bmp")!=0):
				os._exit(0) 
		except  KeyboardInterrupt:
			os._exit(0)

