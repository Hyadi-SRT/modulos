#Programa Reynpolds
#
#Programa que calcula el numero de Reynolds a partir de los parametros
#de densidad, velocidad relativa, diametro y voscosidad dinamica por medio de
#la funcion "calcula_numero_reynolds".
#
#Atributos:
#   densidad: Kg/m3
#   velocidad_relativa: m/s
#   diametro: m
#   viscosidad_dinamica: Kg/m*s

class Reynolds:

    def __init__(self, densidad, velocidad_relativa, diametro, viscosidad_dinamica):
        self.densidad = densidad
        self.velocidad_relativa = velocidad_relativa
        self.diametro = diametro
        self.viscosidad_dinamica = viscosidad_dinamica

    def calcula_numero_reynolds(self):
        return (self.densidad*self.velocidad_relativa*self.diametro) / self.viscosidad_dinamica


rey = Reynolds(125, 45, 0.8, 75.2)
print("Reynolds", str(rey.calcula_numero_reynolds()))