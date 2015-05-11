#!/usr/bin/python
import os,time,random,sys,termios,threading
def Onepic(snake=' '*32*16):
	print('score:'+str(score)+'\n================================|')
	for i in range(0,16):
		print (snake[i*32:(i+1)*32]+'|')
	print ('================================|')
class position():
	def __init__(self,x,y):
		self.x=x
		self.y=y	
def run():
	global direction
	direction='right'
	while(1):
		button=sys.stdin.read(1)
		direction='up' if(button=='w' and direction!='down') \
		else ('down' if(button=='s' and direction!='up') 
		else ('left' if(button=='a' and direction!='right')	
		else ('right' if(button=='d' and direction!='left') else direction)))
		time.sleep(0.2)	
if __name__ == "__main__":
	fd = sys.stdin.fileno()
	new = termios.tcgetattr(fd)
	new[3] = new[3] & ~termios.ICANON
	termios.tcsetattr(fd, termios.TCSADRAIN, new)
	tempstr=[' ']*32*17
	snakebody=[position(0,0),position(1,0)] 
	score=0
	threading.Thread(target=run,args='').start()
	while (1):
		for pos in snakebody:
			tempstr[pos.x*2+32*pos.y]='*'
		if(not '#' in tempstr):
			randx=random.randint(0,255)
			while (tempstr[randx*2] == '*'):
				randx= 0 if(randx>254) else randx+1
			tempstr[randx*2]='#'
		os.system('clear')
		Onepic("".join(tempstr))
		for pos in snakebody:
			tempstr[pos.x*2+32*pos.y]=' '
		time.sleep(0.5-score/500 if score<250 else 0)
		tempbody=snakebody[0]
		del snakebody[0]
		snakebody.append(position(snakebody[-1].x+int(direction=='right')-int(direction=='left'),\
			snakebody[-1].y-int(direction=='up')+int(direction=='down')))
		if(tempstr[snakebody[-1].x*2+snakebody[-1].y*32]=='#'):
			snakebody.insert(0,tempbody)
			score+=1
		for a in snakebody[0:-1]:
			if((snakebody[-1].x == a.x and snakebody[-1].y==a.y) or (not snakebody[-1].x in range(0,16)) \
				or (not snakebody[-1].y in range(0,16))):
				print('gameover!\nyou score is '+str(score))
				os._exit(0)
