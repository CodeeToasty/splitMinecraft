#!/urs/bin/python3
import sys
import matplotlib.pyplot as plt
import numpy as np
from playsound import playsound


def realDraw(supp_total,step,pillars,y_increment):
	x=np.arange(supp_total+2)
	y=np.ones(supp_total+2)
	array_sol = [0]
	i=0
	while True:
		for _ in range(step):
			array_sol.append(1)
		if i==pillars:
			break
		array_sol.append(2)
		i+=1
	array_sol.append(0)
	array_sol=np.array(array_sol)
	plt.text(x[0]-3,y_increment+0.975,step)
	for i in x:
		if array_sol[i]==0:
			plt.plot(x[i], y[i]+y_increment,markersize=8, marker='s', 
			markerfacecolor='green',markeredgewidth=1,markeredgecolor='black')
		elif array_sol[i]==1:
			plt.plot(x[i], y[i]+y_increment,markersize=8, marker='s', 
			markerfacecolor='yellow',markeredgewidth=1,markeredgecolor='black')
		elif array_sol[i]==2:
			plt.plot(x[i], y[i]+y_increment,markersize=8,marker='s', 
			markerfacecolor='red',markeredgewidth=1,markeredgecolor='black')
	return y_increment+1

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
	plt.figure(figsize=(10, 5))
	if total<=0:
		print("ahah negative length very funny")
		return 1
	y_increment=0	
	for step in range(1, int(total+1)):
		supp_total=total
		pillars=0
		test,pillars = checkSplit(supp_total,step,pillars)
		if test==True:
			y_increment=realDraw(supp_total,step,pillars,y_increment)
	playsound('bruhsound.mp3')
	plt.title('Feasable Solutions')
	plt.axis('off')
	plt.show()

main(sys.argv[1:])





