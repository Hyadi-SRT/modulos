#Programa ForceBalance.py
#
#
#Programam que calcula el valor forceBalance a partir de los parametros 
#drag force, weight car, rolling resistance y angle por medio de la funcion
# "calcula_force_balance()" la cual ya considerea el valor de "weight_opposing_motion"
#pero puede ser calculado independientemente por la funcion 
# "calcula_weight_opposing_motion(weight_car, angle)"
#
#Atributos:
#	drag_force: Newtons
#	weight_car: Newtons
#	rolling resistance: Newtons
#	angle: grados
#

import math

class ForceBalance:

	def __init__(self, drag_force, weight_car, rolling_resistance, angle):
		self.drag_force = drag_force
		self.weight_car = weight_car
		self.rolling_resistance = rolling_resistance
		self.angle = angle

	def calcula_force_balance(self):
		return self.drag_force + self.calcula_weight_opposing_motion(self.weight_car, self.angle) + self.rolling_resistance

	def calcula_weight_opposing_motion(self, weight_car, angle):
		return weight_car * math.sin(math.radians(angle))


fb = ForceBalance(2587, 1200, 478.4, 0.12)
print("Force Balance: ", fb.calcula_force_balance())
print("Weight opposing motion: ", fb.calcula_weight_opposing_motion(2540, 0.12))	