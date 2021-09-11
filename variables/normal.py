import math

class Normal:
    force = 0
    angle = 0

    def __init__(self, f, a):
        self.force = f
        self.angle = a

    @classmethod
    def push_force(self):
        return self.force * math.cos(math.degrees(self.angle))

norm = Normal(250, 50)
print(norm.push_force())