#!/usr/bin/python
#show a picture on the console
#run in python2
import sys
import Image
import os
if __name__ == '__main__':
	grayLevel=[' ','.','-','+','*','%','#','&']
	img=Image.open(sys.argv[1])
	img.convert('L')
	picstr=''
	maxp=0
	minp=255
	for y in range(0,img.size[1]):
		for x in range(0,img.size[0]):
			if(x%(img.size[0]//64)==0 and y%(img.size[1]//32)==0):
				if(img.getpixel((x,y))>maxp):
					maxp=img.getpixel((x,y))
				if(img.getpixel((x,y))<minp):
					minp=img.getpixel((x,y))
	for y in range(0,img.size[1]):
		for x in range(0,img.size[0]):
			if( x%(img.size[0]//64)==0 and y%(img.size[1]//32)==0):
				picstr+=(grayLevel[(img.getpixel((x,y))-minp)*255/(maxp-minp)//32])
		if(y%(img.size[1]//32)==0):
			picstr+='\n'
	os.system("clear")			
	print picstr
