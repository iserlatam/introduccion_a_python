import math

# Calculadora trigonométrica para un profesor
# Funcionalidades: calcular razones trigonometricas, 
# calcular promedio de un estudiante

# Funcion promedio
def promedio():
    print('Comencemos a calcular promedios :D')
    print('Introduzca las notas (Introduzca el numero 6 para comenzar a promediar): ')
    print('---------------------------------------')
    
    contadorNota = 1
    estado = True
    
    # Crear lista de notas vacía
    notas = list()
    
    # Ciclo que pregunta varias notas al tiempo
    while estado:
        # Preguntar la nota
        nota = float(input(f"Introduzca la nota {contadorNota}: "))

        # Validar si la nota es correcta o si es el comando salir
        # Comando salir: 6
        if (nota == 6):
            break
        if (nota > 5):
            print('Esta nota no es valida. Solo notas del 1 al 5')
        else:
            # Anexar una nueva nota a la lista
            notas.append(nota)
            # Incrementar el contador por cada nota nueva
            contadorNota += 1
            
    # Acomulador de valor de notas total
    totalNotas = 0.0
    resultado = 0
    
    if (len(notas) == 0):
        print('Adiós')
    else:
        #  Acomular notas
        for i in range(len(notas)):
            totalNotas += notas[i]
        # Calcular promedio y establecer resultado
        resultado = totalNotas / len(notas)

    print(resultado)
    

# Funcion razones trigonometricas
def menuRazones():
    # Renderizar menu para escoger la razon
    print("1. Seno\n2. Coseno\n3. Tangente")
    
    # Solicitamos la opcion
    opcionString = input('Ingrese su opcion: ')
    opcionInt = int(opcionString)
    
    angulo = float(input('Ingrese el angulo a calcular (en grados): '))
    anguloARadianes = math.radians(angulo)
    
    if (opcionInt == 1):
        # Seno
        return print(f"Su angulo es: {angulo} y su seno (en radianes) es: {math.sin(anguloARadianes)}")
    elif(opcionInt == 2):
        # Coseno
        
        pass
    elif (opcionInt == 3):
        # Tangente
        pass
    else:
        print('opcion incorrecta')
    # Realizar la opcion

# Renderizar o mostrar menu principal
def menuPrincipal():
    # Bienvenida y opciones principales
    print('Trigoasistente: su baúl de herramientas para sus clases de trigonometría')
    print('--------------------------------------------------')
    print('Seleccione una opción: ')
    print('1. Calcular promedio de un estudiante')
    print('2. Calcular razones trigonometricas')

    # Elección de opción
    opcionString = input('Ingrese su opcion: ')
    opcionInt = int(opcionString)

    if (opcionInt == 1):
        promedio()
    elif(opcionInt == 2):
        menuRazones()
    else:
        pass

# Iniciar menu principal 
menuPrincipal()
