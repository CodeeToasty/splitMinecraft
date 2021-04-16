#!/urs/bin/python3
import sys

def drawSolution(length, step, pillars):
	i=0
	print("L", end='')
	while True:
		for j in range(step):
			print("#", end='')
		if i == pillars:
			break
		print("@",end='')
		i+=1
	print("L")

def checkSplit(length, step, p):
	while True:
		length-=step
		if length<=0:
			break
		length-=1
		p+=1
	if length==0:
		return True, p
	return False, p

def main(argv):
	total=int(sys.argv[1])
	if total<=0:
		print("ahah negative length very funny")
		return 1
	print("feasable solutions: ")
	for step in range(1, int(total+1)):
		supp_total=total
		pillars=0
		test,pillars = checkSplit(supp_total,step,pillars)
		if test==True:
			print(step, end=' ')
			drawSolution(supp_total,step,pillars)

main(sys.argv[1:])
