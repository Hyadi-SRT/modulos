from math import radians, cos, sin

def normal(angle: float, weight: float) -> float:
    # Calcular la normal de la fuerza de 
    # gravedad que ejerce el auto sobre el 
    # suelo
    # Parametros:
    #   angle : Radianes
    #   weight: Newtons
    return weight*cos(angle)

def weight_x(angle, force) -> float:
    #Calcular el peso que se opone al movimiento
    #Parametros:
    #   angle : Radianes
    #   force : Newtons
    return force*sin(angle)

def tractive_force(torque, radio):
    # Calcular la fuerza de traccion
    #Parametros: 
    #   torque : Newton-Metro
    #   radio  : No sé si en cm o m
    return torque*radio

def dynamic_pressure(density, relative_velocity):
    #Calcular la presion dinamica
    #Parametros:
    #   density : kg/m^3
    #   relative_velocity : m/s 

    return (density * relative_velocity**2)/2

def lift_force(drag_area, dynamic_pressure, lift_coeficient):
    #Calcular la fuerza de elevacion
    #Parametros:
    #   drag_area : Metros cuadrados
    #   dynamic_pressure : Pascales
    #   lift_coeficient : -
    return  drag_area*dynamic_pressure*lift_coeficient

def pitch_moment(drag_area, dynamic_pressure, coefficient, Lw):
    #Calcula el momento de cabeceo
    #Parametros:
    #   drag_area: Metros cuadrados
    #   dynamic_pressure: Pascales
    #   coefficient: - 
    #   Lw: - 
    return drag_area*dynamic_pressure*coefficient*Lw


def regenerative_charge(torque_motor, rotational_speed,efficiency_motor, 
    battery_voltage):

    return (torque_motor*rotational_speed*efficiency_motor)/battery_voltage

def torque_motor(torque_wheel, efficiency_transmission, speed_reduction):

    return torque_wheel*efficiency_transmission/speed_reduction

def torque_wheel(drag_force,rolling_resistance,radius_wheel, weight_x):

    return radius_wheel*(abs(weight_x)-drag_force-rolling_resistance)


def pendiente(x_1,y_1,x_2,y_2):

    return(y_2 - y_1)/(x_2 - x_1)

def reynolds(densidad, velocidad_relativa, diametro, viscosidad_dinamica):

    return (densidad*velocidad_relativa*diametro) / viscosidad_dinamica

def calcula_force_balance(drag_force,weight_x,rolling_resistance):

		return drag_force + weight_x + rolling_resistance

def aceleration(tractive_force, drag_force, rolling_resistance, effective_mass):
    return (tractive_force - drag_force - rolling_resistance) /effective_mass


class RollingResistance:
    def __init__(self):
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
