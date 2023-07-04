import matplotlib.pyplot as plt
#from random_walk import RandomWalk
import random_walk_mod  as r_w



while True:
	save_or_show=input("Save directly (s) or show (else)?\n> ")
	dotnum = int(input("Enter an integer value for points amount, please:\n> "))
	#Cria um passeio aleatório e plota os pontos 
	rw = r_w.RandomWalk(dotnum)
	rw.fill_walk()
	#Define o tam da janela de plotagem 
	plt.figure(figsize=(10, 6))
	point_num = list(range(rw.num_points))
	plt.scatter(0, 0, c='blue', edgecolors='none', s=50)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50)
	plt.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Greens, edgecolor='none',s=5)
	#plt.axes().get_xaxis().set_visible(False)
	#plt.axes().get_yaxis().set_visible(False)
	
	if  save_or_show == 's':
		namePath=input("Name:\n> ")
		plt.savefig(f'{namePath}.png', bbox_inches='tight')
		
	else:
		plt.show()
	keep_running=input("Make another walk? (y/n):\n> ")
	if  keep_running=='n':
		break
