
class RollingResistance:
    def __init__(self):
        self._total = 0
        self._coefficient = 0

    @property
    def coefficient(self):
        #Retorna un flotante como el valor del coeficiente de rolling resistance
        
        return self._coefficient

    @coefficient.setter
    def setCoefficient(self, args: list):
        # Calcula el coeficiente de Rolling Resistance y lo coloca
        # Recibe una sola tupla con 3 valores
        # -staticForce
        # -momentValentForce
        # -speed

        staticForce, momentValentForce, speed = args
        self._coefficient = staticForce + (momentValentForce*speed)

    @property
    def total(self):
        #Retorna un flotante como valor del Rolling Resistance total

        return self._total
    
    @total.setter
    def total(self, normal):
        # Calcula el valor del Rolling Resistance total
        # Recibe un argumento (normal)
        self._total = self.coefficient * normal


if __name__ == '__main__':
    normal = 3540.744003
    staticForce = 0.00252
    momentValentForce = 3.14e-5
    speed = 40.0

    test = RollingResistance()
    test.coefficient = (staticForce, momentValentForce, speed)
    print("Rolling Resistence coefficient: ", test.coefficient)
    test.total = normal
    print("Rolling Resistence Total: ", test.total)

