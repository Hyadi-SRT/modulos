
class Componente:
    def __init__(self) -> None:
        self._temperatura = 0

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        self._temperatura = value


class ComponenteElectrico(Componente):
    def __init__(self) -> None:
        super().__init__()
        self._voltaje = 0
        self._corriente = 0
    
    @property
    def voltaje(self):
        return self._voltaje
    
    @voltaje.setter
    def voltaje(self, value):
        self._voltaje = value
    
    @property
    def corriente(self):
        return self._corriente
    
    @corriente.setter
    def corriente(self, value):
        self._corriente = value


class ComponenteMecanico(Componente):
    def __init__(self) -> None:
        super().__init__()

class ComponenteMeteorologico(Componente):
    def __init__(self) -> None:
        super().__init__()

class Motor(ComponenteElectrico):
    def __init__(self) -> None:
        super().__init__()
        
    def potencia(self):
        return self._corriente*self._voltaje
        
class Auto:
    def __init__(self, masa = 600.0) -> None:
        self._velocidad = 0
        self._distancia = 0
        self._masa = masa
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, value):
        self._velocidad = value

    @property
    def distancia(self):
        return self._distancia
    
    @distancia.setter
    def distancia(self,value):
        self._distancia=value

    @property
    def weight(self):
        return self._masa*9.81
    