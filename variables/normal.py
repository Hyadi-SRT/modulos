import math

class Normal:
    force = 0
    angle = 0

    def __init__(self, f, a):
        self.force = f
        self.angle = a

 
    def display(self):
        print(str(self.force)+ " " + str(self.angle))

    @classmethod
    def push_force(self):
        return self.force * math.cos(self.aGrados(self.angle))

    @classmethod
    def aGrados(self, radianes):
        return (math.pi * radianes) / 180


norm = Normal(250, 50)
print (norm.display())
print(norm.aGrados(50))
print(norm.push_force())