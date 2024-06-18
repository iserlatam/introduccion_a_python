from data.libros import libros

# Clase Libro para representar un libro individual
class Libro:
    def __init__(self):
        # Inicialización de clase Libro
        pass
    
    # Obtiene los libros existentes en nuestros datos y los imprime
    def obtener_libros():
        return libros
        
    def filtar_por_nombre(libro):
        
        for book in libros:
            if book["nombre"].lower() == libro.lower():
                return book
            
        return None
    
    def filtrar_por_precio(precio):
        return [book for book in libros if book["precio"] <= precio]

    def filtrar_por_genero(genero):
        return [book for book in libros if book["genero"].lower() == genero.lower()]

    def filtrar_por_nacionalidad(nacionalidad):
        return [book for book in libros if book["nacionalidad"].lower() == nacionalidad.lower()]

    def filtrar_por_autor(autor):
        return [book for book in libros if book["autor"].lower() == autor.lower()]
    