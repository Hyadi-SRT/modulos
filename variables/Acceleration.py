"""
Programa que calcula la aceleracion instantanea.

Parametros:
	tractive_force: Newtons
	drag_force: Newtons
	rolling_resistance: Newtons
	effective_mass: Kilogramos

Retornofuncion: 
	calcula_aceleration(): devuelve el valor de la aceleracion instantnea
"""

class Acceleration:

	def __init__(self, tractive_force, drag_force, rolling_resistance, effective_mass):
		self.tractive_force = tractive_force;
		self.drag_force = drag_force;
		self.rolling_resistance = rolling_resistance;
		self.effective_mass = effective_mass;

	def calcula_aceleration(self):
		return (self.tractive_force - self.drag_force - self.rolling_resistance) /self.effective_mass


a = Acceleration(24,74,74,1574)
print(a.calcula_aceleration())
