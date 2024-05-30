# Calculadora equipada con las operaciones ariméticas necesarias

# Suma => a + b
# Esta es una función que toma dos parametros y los suma
def suma(a, b):
    if (type(a) != int and type(b) != int):
        print('los parametros no son enteros')
    elif (type(a) != int or type(b) != int):
        print('Uno de los parametros no es un entero. Acción denegada')
    else:
        return print(f"{a} + {b} = {a+b}")

# Resta => a - b
# Esta es una funcion que toma dos parametros y los resta
def resta(a, b):
    return print(f"{a} - {b} = {a-b}")

# Multiplicacion
def multiplicacion(a, b):
    return print(f"{a} x {b} = {a*b}")

# Division
def division(a, b):
    return print(f"{a} / {b} = {a/b}")

# Tabla de multiplicar => a*b = n
# Funcion que multiplica un numero por 10
def tablaMultiplicar(n: int, veces = 10):
    if (type(n) != int):
        print('El primer argumento no es un entero')
    else:
        for i in range(1, veces + 1):
            print(f"{n} x {i} = {n * i}")

def menuPrincipal():
    # Asistente: profesor chapatin
    print('Bienvenido al asistente virtual. Elija una opcion para comenzar a hacer mates')
    print('--------------------------------------------')
    # Menu principal de la calculadora. 5 opciones
    print('Opciones:\n1. Suma\n2.Resta\n3. Multiplicacion\n4. Division')

    # Recolección de opcion por parte del usuario
    opcionString = input('Ingrese su opcion: ')
    opcionInt = int(opcionString)
    a = 0
    b = 0

    if (opcionInt == 1):
        a = int(input('Ingrese el primer numero a sumar: '))
        b = int(input('Ingrese el segundo numero a sumar: '))
        suma(a, b)
    elif (opcionInt == 2):
        a = int(input('Ingrese el primer numero a restar: '))
        b = int(input('Ingrese el segundo numero a restar: '))
        resta(a, b)
    elif (opcionInt == 3):
        a = int(input('Ingrese el primer numero a multiplicar: '))
        b = int(input('Ingrese el segundo numero a multiplicar: '))
        multiplicacion(a, b)
    elif (opcionInt == 4):
        a = int(input('Ingrese el primer numero a dividir: '))
        b = int(input('Ingrese el segundo numero a dividir: '))
        division(a, b)
    else:
        print('Esta opción no existe')
        
        
menuPrincipal()
  
# tablaMultiplicar(True)
# suma(20, 4)
