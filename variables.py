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
        # -moment_valent_force
        # -velocity

        staticForce, moment_valent_force, velocity = args
        self._coefficient = staticForce + (moment_valent_force*velocity)

    @property
    def total(self) -> float:
        #Retorna un flotante como valor del Rolling Resistance total

        return self._total
    
    @total.setter
    def total(self, normal : float) -> None:
        # Calcula el valor del Rolling Resistance total
        # Recibe un argumento (el valor de la normal)
        self._total = self.coefficient * normal

class DynamicPressure:
    def __init__(self) -> None:
        self._density = 0
        self._relative_velocity = 0
        self._value = 0
    
    @property
    def value(self) -> float:
        return (self._density * self._relative_velocity**2)/2
    
    @property
    def density(self):
        return self._density
    
    @density.setter
    def density(self, value):
        self._density = value
    
    @property
    def relative_velocity(self):
        return self._relative_velocity

    @relative_velocity.setter
    def relative_velocity(self, value):
        self._relative_velocity = value
    
class DragForce:
    def __init__(self, dp:DynamicPressure) -> None:
        self._coefficient = 0
        self._area = 0
        self._dynamic_pressure = dp.value
    
    @property
    def value(self):
        return self._coefficient*self._area*self._dynamic_pressure
    
    @property
    def coefficient(self):
        return self._coefficient
    @coefficient.setter
    def coefficient(self, value):
        self._coefficient = value

    @property
    def area(self):
        return self._area
    @area.setter
    def area(self, value):
        self._area = value


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

    dp = DynamicPressure()
    dp.density=1.25
    dp.relative_velocity=15

    drag = DragForce(dp)

    drag.area=0.11
    drag.coefficient=1

    print(drag.value)
