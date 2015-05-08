#!/usr/bin/python

#Calculate based on Reverse Polish Notation
import re
from decimal import *
def getPriority(inputDate):
	#get the priority of the symbol input
	return (inputDate in '+-')*1+(inputDate in '*/')*2+(inputDate=='^')*3
def notAdvanced(inputDate,target):
	return (getPriority(inputDate)<=getPriority(target) or inputDate==')')
def strToDecimal(inputDate):
	#convert the str to Decimal number
	try:
		return Decimal(inputDate)
	except:
		return inputDate
def infixToPostfix(inputDate):
	#convert infix to postfix
	swap=list()
	returnlist=list()
	dealedDate=re.findall("(?<![0-9])-?\d+\.?\d*|[^\d]",inputDate)
	normalized=list(map(strToDecimal,dealedDate))
	print(normalized)
	for item in normalized:
		if type(item)==Decimal :
			returnlist.append(item)
		elif (not bool(swap)) or item == '(':
			swap.append(item)
		elif item == ')':
			while True:
				tmp=swap.pop()
				if(tmp=='('):
					break
				returnlist.append(tmp)
		elif notAdvanced(item,swap[-1]):
			while bool(swap) and notAdvanced(item,swap[-1]):
				returnlist.append(swap.pop())
			swap.append(item)
		else:
			swap.append(item)
	while bool(swap):
		returnlist.append(swap.pop())
	return returnlist
def calculate(postfixFormat):
	#calculate the postfix
	add=lambda x,y:x+y
	sub=lambda x,y:x-y
	mul=lambda x,y:x*y
	div=lambda x,y:x/y
	rec=lambda x,y:x**y
	atom={'+':add,'-':sub,'*':mul,'/':div,'^':rec}
	stack=list()
	for item in postfixFormat:
		if(type(item)==Decimal):
			stack.append(item)
		else:
			a=stack.pop()
			b=stack.pop()
			stack.append(atom[item](b,a))
	return stack.pop()

if __name__ == '__main__':
	#test code 
	postfixFormat=infixToPostfix(input())
	print(postfixFormat)
	print(calculate(postfixFormat))
	input()

	
