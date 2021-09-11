import math

class Normal:
	def __init__(self, force, angle):
		self.force = force
		self.angle = angle

	def calcula_fuerza_pendiente(self):
		if self.angle > 0:
			return -self.force * math.cos(math.radians(self.angle))
		else:
			if self.angle < 0:
				return self.force * math.cos(math.radians(self.angle))
			else:
				return 0

time = Normal(24, 0)
print(str(time.calcula_fuerza_pendiente()))
