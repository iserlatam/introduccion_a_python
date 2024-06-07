class Persona:
    def __init__(self, nombre, edad, color_piel = 'blanco'):
        # atributo de instancia
        self.nombre = nombre  
        # atributo de instancia
        self.edad = edad
        self.color_piel = color_piel

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años y tengo la piel {self.color_piel}")

    def envejecer(self):
        self.edad += 1
        
    def rejuvenecer(self):
        self.edad -= 1

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30, 'mestizo')
persona2 = Persona('Camilo', 18)

persona2.rejuvenecer()
persona2.saludar()

persona1.saludar()

# Acceder a métodos y atributos de instancia
# persona1.saludar()  
# persona1.envejecer()
# persona1.saludar() 
# persona1.envejecer()
# persona1.envejecer()
# persona1.envejecer()
# persona1.saludar()
# persona1.rejuvenecer()
# persona1.saludar()

