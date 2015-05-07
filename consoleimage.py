#!usr/bin/python
#show a picture on the console
#run in python2
import sys
import Image
if __name__ == '__main__':
	grayLevel=[' ','.','-','+','*','%','#','&']
	img=Image.open(sys.argv[1])
	img.convert('L')
	for y in range(0,img.size[1]):
		for x in range(0,img.size[0]):
			if( x%(img.size[0]//64)==0 and y%(img.size[1]//32)==0):
				print grayLevel[int(img.getpixel((x,y))//32)],
			sys.stdout.softspace=0
		if(y%(img.size[1]//32)==0):
			print("")
