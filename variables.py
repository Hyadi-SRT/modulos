from math import radians, cos, sin

def normal(angle, force):
    angle = radians(angle)
    return force*cos(angle)

def weight_x(angle, force):
    angle = radians(angle)
    return force*sin(angle)

def tractive_force(torque, radio):
    return torque*radio

def dynamic_pressure(density, relative_velocity):
    return (density * relative_velocity**2)/2

def lift_force(drag_area, dynamic_pressure, clift_coeficient):
    return  drag_area*dynamic_pressure*clift_coeficient

def pitch_moment(drag_area, dynamic_pressure, coefficient, Lw):
    return drag_area*dynamic_pressure*coefficient*Lw

class RollingResistance:
    def __init__(self):
        self._total = 0
        self._coefficient = 0

    def coefficient(self) -> float:
        #Retorna un flotante como el valor del coeficiente de rolling resistance
        return self._coefficient

    def make_coefficient(self,static_force, moment_valent_force, velocity) -> None:
        # Calcula el coeficiente de Rolling Resistance y lo coloca
        # Recibe una sola tupla con 3 valores
        # -staticForce
        # -moment_valent_force
        # -velocity
        self._coefficient = static_force + (moment_valent_force*velocity)

    def total(self, normal : float) -> None:
        # Calcula el valor del Rolling Resistance total
        # Recibe un argumento (el valor de la normal)
        return self._coefficient * normal
    
class DragForce:
    def __init__(self) -> None:
        self._coefficient = 0
    
    def value(self, dynamic_presure:float, area: float):
        return self._coefficient*area*dynamic_presure
    
    def coefficient(self):
        return self._coefficient

    def make_coefficient(self, value):
        self._coefficient = value



if __name__ == '__main__':

    rollin = RollingResistance()

    rollin.make_coefficient(0.00252,3.14e-5,40)
    
    n = normal(-3, 3558.4)
    w_x= weight_x(-3, 3558.4)

    print(f"Rolling coefficient = {rollin.coefficient()}")
    print(f"Rolling resistance = {rollin.total(n)}")
    print(f"Normal = {n}")
    print(f"W en x: {w_x}")

    dp = dynamic_pressure(1.25, 15)

    drag = DragForce()

    area=0.11
    drag.make_coefficient(1)

    print(dp)
    print(f"Drag value: {drag.value(dp, area)}")
    dp=dynamic_pressure(1.25,24)

    print(dp)
    print(f"New Drag:{drag.value(dp, area)}")
