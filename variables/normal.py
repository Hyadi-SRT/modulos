import math

class Normal:
	def __init__(self, force, angle):
		self.force = force
		self.angle = angle

	def calcula_fuerza_pendiente(self):
		return self.force * math.cos(math.degrees(self.angle));

time = Normal(24, 5.1)
print(str(time.calcula_fuerza_pendiente()))
