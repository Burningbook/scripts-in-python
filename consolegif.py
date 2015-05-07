#!/usr/bin/python
#play image in console
import Image
import os
import sys
import time 

if __name__ == '__main__':
	gif=Image.open(sys.argv[1])
	gif.save("./t.bmp")
	os.system("clear")
	time.sleep(1)
	os.system("python consoleimage.py ./t.bmp")	
	while True:
		try:
			gif.seek(gif.tell() + 1)
			gif.save("./t.bmp")
			time.sleep(0.2)
			os.system("clear")
			os.system("python consoleimage.py ./t.bmp")	
		except:
			break;