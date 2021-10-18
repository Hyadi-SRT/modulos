from autos import Quetzal

if __name__ == '__main__':
    quetzal = Quetzal(0, 600)

    print(f'El peso es : {quetzal.weight} N')
    print(f'La masa del auto es: {quetzal._mass} kg')
    print(f'La normal del auto es: {quetzal.normal}')
