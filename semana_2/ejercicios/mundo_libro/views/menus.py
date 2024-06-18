# Paquete de python que maneja el tiempo
import time
# Paquete de python que maneja los archivos y comandos del ordenador
from os import system
from actions import actions

# Renderizar menu para acciones correspondientes a la administracion de libros
def menuAdministrarLibros():
    system('clear')
    print('>>>>>>>> __ADMINISTRAR LIBROS__')
    print('Agregue, edite y elimine libros desde un solo lugar')
    print('-------------------------------------------------')
    print('1. Agregar libros')
    print('2. Editar libros')
    print('3. Eliminar libros')
    print('4. Volver atrás')
    print('-------------------------------------------------')
    
    opt = int(input('> Introduzca la opción: '))

# Renderizar menu para acciones correspondientes a la consulta de libros
def menuConsultarLibros(acciones = actions):
    system('clear')
    print('>>>>>>>> __INICIO__')
    print('Consulte y filtre libros por nombre, precios, etc')
    print('-------------------------------------------------')
    print('0. Mostrar todos los libros')
    print('1. Consultar por nombre')
    print('2. Consultar por precio')
    print('3. Consultar por genero')
    print('4. Consultar por nacionalidad')
    print('5. Consultar por autor')
    print('6. Volver atrás')
    print('-------------------------------------------------')
    
    opt = int(input('> Introduzca la opción: '))

    # Alternativa a switch case. Solo funciona para las versiones iguales o superiores a la 10
    match opt:
        case 0:
            system('clear')
            print('-------------------------------------------------')
            acciones.obtener_libros()
            print('-------------------------------------------------')
            wait = input('Presione ENTER para volver al menu de consultas ')
            menuConsultarLibros()
        case 1:
            system('clear')
            nombre = input('Introduzca el nombre del libro que quiere buscar: ')
            print('-------------------------------------------------')
            acciones.filtrar_por_nombre(nombre)
            print('-------------------------------------------------')
            input('Presione ENTER para volver al menu de consultas ')
            menuConsultarLibros()
        case 2:
            system('clear')
            precio = float(input('Introduzca el precio máximo: '))
            print('-------------------------------------------------')
            acciones.filtrar_por_precio(precio)
            print('-------------------------------------------------')
            input('Presione ENTER para volver al menu de consultas ')
        
            menuConsultarLibros()
        case 3:
            system('clear')
            genero = input('Introduzca el género: ')
            print('-------------------------------------------------')
            acciones.filtrar_por_genero(genero)
            print('-------------------------------------------------')
            input('Presione ENTER para volver al menu de consultas ')
        
            menuConsultarLibros()
        case 4:
            system('clear')
            nacionalidad = input('Introduzca la nacionalidad: ')
            print('-------------------------------------------------')
            acciones.filtrar_por_nacionalidad(nacionalidad)
            print('-------------------------------------------------')
            input('Presione ENTER para volver al menu de consultas ')
            menuConsultarLibros()
        case 5:
            system('clear')
            autor = input('Introduzca el autor: ')
            print('-------------------------------------------------')
            acciones.filtrar_por_autor(autor)
            print('-------------------------------------------------')
            input('Presione ENTER para volver al menu de consultas ')
            menuConsultarLibros()
        case 6:
            menuPrincipal()
        case _:
            print('Opción inválidad, vuelva a intentar')
            # Librería de python que maneja el tiempo para simular un temporizador
            time.sleep(2)
            # Comando de limpieza de consola para Linux
            system('clear')
            menuConsultarLibros()
            
# Funcion que renderiza el menu principal
def menuPrincipal():
    # Limpia la consola de la terminal en Linux
    # Use system('cls') para windows
    system('clear')
    print('>>>>>>>> __INICIO__')
    print('Bienvenido a mundo libro. ¿Qué desea hacer el día de hoy?')
    print('-------------------------------------------------')
    print('1. Administrar libros')
    print('2. Consultar libros')
    print('3. Salir')
    print('-------------------------------------------------')
    
    opt = int(input('> Introduzca la opción: '))
    
    # Alternativa a switch case. Solo funciona para las versiones iguales o superiores a la 10
    match opt:
        case 1:
            # Menu para administrar libros
            menuAdministrarLibros()
        case 2:
            # Menu para consultar libros
            menuConsultarLibros()
        case 3:
            # Comando para terminar la ejecucion del programa
            exit(200)
        case _:
            print('Opción inválidad, vuelva a intentar')
            # Librería de python que maneja el tiempo para simular un temporizador
            time.sleep(2)
            # Comando de limpieza de consola para Linux
            system('clear')
            menuPrincipal()