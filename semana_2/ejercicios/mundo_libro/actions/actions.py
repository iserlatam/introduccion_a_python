from modules.classes import Libro

modeloLibro = Libro

# Función para obtener todos los libros a través de un modelo 
def obtener_libros():
    # Utilizamos el método listaDeLibros() para acceder a los datos
    # almacenados en la carpeta /data, que simula una base de datos real 
    libros = modeloLibro.obtener_libros()
    # Recorremos los libros (lista)
    for i in range(len(libros)):
        print(f"Libro No. {i+1} = Nombre: {libros[i]["nombre"]} - Autor: {libros[i]["autor"]}")

# Función para obtener un libro a través de un libro
def filtrar_por_nombre(nombre):
    resultado = modeloLibro.filtar_por_nombre(nombre)

    if resultado:
        print(resultado)
    else:
        print('libro no encontrado')    

# Función para filtrar libros por rango de precios
def filtrar_por_precio(precio):
    resultado = modeloLibro.filtrar_por_precio(precio)

    if resultado:
        print(resultado)
    else:
        print('libro/s no encontrado')  

# Función para filtrar libros por categoría
def filtrar_por_genero(genero):
    resultado = modeloLibro.filtrar_por_genero(genero)

    if resultado:
        print(resultado)
    else:
        print('libro no encontrado')    

# Función para filtrar libros por autor
def filtrar_por_autor(autor):
    resultado = modeloLibro.filtrar_por_autor(autor)

    if resultado:
        print(resultado)
    else:
        print('autor no encontrado')  

# Función para filtrar libros por nacionalidad
def filtrar_por_nacionalidad(nacionalidad):
    resultado = modeloLibro.filtrar_por_nacionalidad(nacionalidad)

    if resultado:
        print(resultado)
    else:
        print('nacionalidad no encontrado')