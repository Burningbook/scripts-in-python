#gray image
import logging
import struct
import sys
import logging.handlers
if __name__ == '__main__':
	LOG_FILE='loginfo.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)
	handler.setFormatter(formatter)
	logger = logging.getLogger('loginfo')
	logger.addHandler(handler) 
	logger.setLevel(logging.DEBUG) 
	logger.info('begin')  
	grayLevel=[' ','.','+','%','*','#','&','&']
	image=open("lena.ppm.pgm",'rb')
	image.read(49)
	for item in range(0,512):
		for x in range(0,64*2):
			image.read(3)
			if(item%8==0):
				print(grayLevel[int(ord(image.read(1))//32)],end='')
			else:
				image.read(1)
			sys.stdout.softspace=0
		if(item%8==0):
			print("")
	image.close()
