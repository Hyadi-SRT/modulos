import multiplicacion 
import suma 

def sumaNumeros():
    print("Sumar")
    numeroA = int(input("Primer Numero: "))
    numeroB = int(input("Segundo Numero: "))
    print("La suma es: ", suma.suma(numeroA, numeroB))

def multiplicaNumeros():
     print("Multiplicar")
     numeroA = int(input("Primer Numero: "))
     numeroB = int(input("Segundo Numero: "))
     print("La multiplicacion es: ", multiplicacion.multiplicacion(numeroA, numeroB))
     
def menu():
    print("Mnu Principal")
    print("1.- Suma")
    print("2.- Multiplicacion")
    print("3.- Salir")
    return int(input("Seleccione Una Opcion"))

def loop():
    opcion = 0
    while opcion != 3:
        opcion = menu()
        if(opcion == 1):
            sumaNumeros()
        elif(opcion == 2):
            multiplicaNumeros()
        elif(opcion == 3):
            print("Adios XD")
        
loop()