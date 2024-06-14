# Archivo: mundo_libro.py
# Ejercicio: Librería "Mundo Libro"
# Acciones: mostrar, agregar, eliminar y filtrar por categoria y autor

# Importaciones de paquetes, modulos y dependencias
# from package import module

# Clases
from modules.classes import Libro

# Instanciamos nuestra clase principal que es la que interactuará con nuestra
# base de datos
modeloLibro = Libro

# Función para obtener todos los libros a través de un modelo 
def obtener_libros():
    # Utilizamos el método listaDeLibros() para acceder a los datos
    # almacenados en la carpeta /data, que simula una base de datos real 
    libros = modeloLibro.listaDeLibros()
    
    # Recorremos los libros (lista)
    for i in range(len(libros)):
        print(f"Libro No. {i+1} = Nombre: {libros[i]["nombre"]} - Autor: {libros[i]["autor"]}")
        
    # print(libros)

# Función para obtener un libro a través de un libro
def obtener_libro():
    resultadoLibro = modeloLibro.buscarLibro("1984")
    resultadoLibroAvanzado = modeloLibro.buscarLibroAvanzado('1988')
    
    # if resultadoLibro == False:
    #     print("No se encontró este libro")
    # else:
    #     print(resultadoLibro)
        
    # Manera corta
    if resultadoLibroAvanzado:
        print(resultadoLibroAvanzado)
    else:
        print('libro no encontrado')
        

# Función para agregar un nuevo libro a la colección
def agregar_libro(coleccion, libro):
    # Código para agregar el libro a la colección
    pass

# Función para filtrar libros por categoría
def filtrar_por_categoria(coleccion, categoria):
    # Código para filtrar los libros por categoría
    pass

# Función para filtrar libros por autor
def filtrar_por_autor(coleccion, autor):
    # Código para filtrar los libros por autor
    pass

# Función para filtrar libros por rango de precios
def filtrar_por_precio(coleccion, precio_min, precio_max):
    # Código para filtrar los libros por rango de precios
    pass

# Función para buscar libro por nombre
def buscar_libro_por_nombre(coleccion, nombre):
    # Código para buscar el libro por nombre
    pass

# Función principal para la ejecución del programa
def main():
    coleccion = []    
    # Código para la interacción con el usuario (añadir, filtrar, buscar libros, etc.)
    # obtener_libros()
    obtener_libro()
    

# Inicialización de clase __main__ para el renderizado del menu principal
if __name__ == "__main__":
    main()
