import math

# Calculadora trigonométrica para un profesor
# Funcionalidades: calcular razones trigonometricas, 
# calcular promedio de un estudiante

# Funcion promedio
def promedio():
    print('Comencemos a calcular promedios :D')
    print('Introduzca las notas (Introduzca el numero 6 para comenzar para salir y  promediar): ')
    print('---------------------------------------')
    
    contadorNota = 1
    estado = True
    
    # Crear lista de notas vacía
    notas = list()
    
    # Ciclo que pregunta varias notas al tiempo
    while estado:
        # Preguntar la nota
        try:
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
        except:
                print("Caracter no valide, digite solo numeros")
    # hasta aqui llega el bucle WHILE
    
    
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
        
    print("*********************************************")
    print(f"\n Su promedio de notas es : {resultado}\n")
    print("*********************************************")
    salir =input("escriba 1 si desea ir al menu principal. ".upper())
    if salir == 1:
        menuPrincipal()
    

# Funcion razones trigonometricas
#def menuRazones():
    
    # while True:
    #     # Renderizar menu para escoger la razon
    #     print("\nSeleccione la operación matemática:")
    #     print("1. Seno")
    #     print("2. Coseno")
    #     print("3. Tangente")
    #     print("4. Volver al menú principal")

    #     # Solicitamos la opcion
        
    #     opcionString = input('Ingrese su opción: ')
    #     opcionInt = int(opcionString)
        
    #     if opcionInt != 4:
    #         angulo = float(input('Ingrese el ángulo a calcular (en grados): '))
    #         anguloARadianes = math.radians(angulo)
        
    #     if opcionInt == 1:
    #         # Seno
    #         print(f"Su ángulo es: {angulo} y su seno (en radianes) es: {math.sin(anguloARadianes)}")
    #     elif opcionInt == 2:
    #         # Coseno
    #         print(f"Su ángulo es: {angulo} y su coseno (en radianes) es: {math.cos(anguloARadianes)}")
    #     elif opcionInt == 3:
    #         # Tangente
    #         print(f"Su ángulo es: {angulo} y su tangente (en radianes) es: {math.tan(anguloARadianes)}")
    #     else:
    #         print('Opción incorrecta, por favor intente nuevamente.')
    #         break

# FUCINONES PARA HACER UNA OPERACION MAPEADAS A UNA CLAVE DE UN DICCIONES POR EJEMPLO 
# 1: calcular_seno,
def calcular_seno(angulo):
    anguloRedondeado = round(angulo,3)
    seno =round(math.sin(anguloRedondeado),3)
    return f"\n Su ángulo es: {anguloRedondeado} y su seno : {seno}"

def calcular_coseno(angulo):
    anguloRedondeado = round(angulo)
    return f"\n Su ángulo es: {anguloRedondeado} y su coseno :  {math.cos(anguloRedondeado)}"

def calcular_tangente(angulo):
    anguloRedondeado = round(angulo)
    return f"\n Su ángulo es: {anguloRedondeado} y su tangente :  {math.tan(anguloRedondeado)}"

def menuRazones():
    operaciones = {
        1: calcular_seno,
        2: calcular_coseno,
        3: calcular_tangente
    }

    while True:
        # Renderizar menú para escoger la razón
        print("\nSeleccione la operación matemática:")
        print("1. Seno")
        print("2. Coseno")
        print("3. Tangente")
        print("4. Volver al menú principal")

        # Solicitamos la opción
        try:
            opcionInt = int(input('Ingrese su opción: '))
            
            if opcionInt == 4:
                break

            if opcionInt in operaciones:
    
                angulo = float(input('Ingrese el ángulo a calcular (en grados): '))
                anguloARadianes = math.radians(angulo)
          
            # llama la funcion asociada a la clave dentro del diccionari o 
                resultado = operaciones[opcionInt](anguloARadianes)
                print(resultado)
        
            else:
                print('\n\n Opción incorrecta, por favor intente nuevamente.')
        except ValueError: 
                print("valor no valido el float tiene una letra ".upper())
                menuRazones()

# Renderizar o mostrar menú principal
def menuPrincipal():
    while True:
        # Bienvenida y opciones principales
        print('Trigoasistente: su baúl de herramientas para sus clases de trigonometría')
        print('--------------------------------------------------')
        print('Seleccione una opción: ')
        print('1. Calcular promedio de un estudiante')
        print('2. Calcular razones trigonométricas')
        print('3. Salir')

        # Elección de opción
        opcionInt = int(input('Ingrese su opción: '))

        if opcionInt == 1:
            promedio()  # Asumiendo que la función promedio() está definida en otra parte
        elif opcionInt == 2:
            menuRazones()
        elif opcionInt == 3:
            print("Saliendo del programa...")
            break
        else:
            print('Opción incorrecta, por favor intente nuevamente.')
 

# Iniciar menu principal 
menuPrincipal()