from math import radians, cos

class Normal:
    def __init__(self):
	    self._force = 0
	    self._angle = 0

    @property
    def value(self):
        #Regresa la fuerza multiplicada por el coseno del angulo

        return self._force*cos(self._angle)

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        #Conviere el angulo a radianes y lo guarda
        #Esto suponiendo que nos llega el angulo en grados, debido a que 
        #math.cos() requiere angulos en radianes
        self._angle = radians(value)

    @property
    def force(self) -> float:
        return self._force
    
    @force.setter
    def force(self, value):
        #Recibe una fuerza en newtons y se guardan
        self._force = value

    


class RollingResistance:
    def __init__(self):
        self._total = 0
        self._coefficient = 0

    @property
    def coefficient(self) -> float:
        #Retorna un flotante como el valor del coeficiente de rolling resistance
        return self._coefficient

    @coefficient.setter
    def coefficient(self, args : tuple) -> None:
        # Calcula el coeficiente de Rolling Resistance y lo coloca
        # Recibe una sola tupla con 3 valores
        # -staticForce
        # -momentValentForce
        # -speed

        staticForce, momentValentForce, speed = args
        self._coefficient = staticForce + (momentValentForce*speed)

    @property
    def total(self) -> float:
        #Retorna un flotante como valor del Rolling Resistance total

        return self._total
    
    @total.setter
    def total(self, normal : float) -> None:
        # Calcula el valor del Rolling Resistance total
        # Recibe un argumento (el valor de la normal)
        self._total = self.coefficient * normal
    
if __name__ == '__main__':
    normal = Normal()
    normal.angle=5.71
    normal.force=3558.4

    rollin = RollingResistance()

    rollin.coefficient = (0.00252,3.14e-5,40)
    
    rollin.total = normal.value

    print(f"Rolling coefficient = {rollin.coefficient}")
    print(f"Rolling resistance = {rollin.total}")
    print(f"Normal = {normal.value}")
