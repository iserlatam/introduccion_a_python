class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonid(self):
        return "Miau!"

def imprimir_sonido(animal):
    print(animal.hacer_sonido())

# Crear instancias de las subclases
mi_perro = Perro()
mi_gato = Gato()

# Llamar a la función usando polimorfismo
imprimir_sonido(mi_perro)
imprimir_sonido(mi_gato)   
