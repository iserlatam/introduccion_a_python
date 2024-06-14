from data.libros import libros

# Clase Libro para representar un libro individual
class Libro:
    def __init__(self):
        # Inicialización de clase Libro
        pass
    
    # Obtiene los libros existentes en nuestros datos y los imprime
    def listaDeLibros():
        return libros
        
    def buscarLibro(libro):
        libroTemp = 0
        
        # Recorrer lista de libros
        for i in range(len(libros)):
            # Validar si existe el libro
            if libros[i]["nombre"] == libro:
                libroTemp = libros[i]
            else:
                libroTemp = libroTemp
        
        if type(libroTemp) == 'int':
            return False
        else:
            return libroTemp
        
    def buscarLibroAvanzado(libro):
        
        for book in libros:
            if book["nombre"].lower() == libro.lower():
                return book
            
        return None
            
    def busquedaGeneral(self, busqueda):
        pass
    