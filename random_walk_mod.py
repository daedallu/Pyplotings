from random import choice



class RandomWalk():
	def __init__(self, num_points=15000): #inicializa os atributos de um passeio
		self.num_points = num_points
		#Todos os passeios começam em (0,0)
		self.x_values=[0]
		self.y_values=[0]
	def get_step(self):
		self.direction=choice([1, -1])
		direc = self.direction
		self.distance=choice(list(range(0,8)))
		dist = self.distance
		self.step = direc*dist
		step = self.step
		return step
	def fill_walk(self):
		#continua dando passos até que o passeio alcance o tam desejado
		while len(self.x_values) < self.num_points:
		#Decide a direção a ser seguida e distância a ser percorrida nessa direção
				x_step = self.get_step()
				y_step = self.get_step()
				
			#Rejeita os movimentos que não vão a lugar nenhum
				if  x_step == 0 and y_step == 0:
					continue
			#Calcula os próximos valores de x e y.
				next_x = self.x_values[-1]+x_step
				next_y = self.y_values[-1]+y_step
			
				self.x_values.append(next_x)
				self.y_values.append(next_y)
