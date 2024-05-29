# Definir una funcion de suma sin argumentos
def suma():
    return 1 + 1

# Definir una funcion de resta con argumentos
def restar(a, b):
    return a - b

# Variables globales vs variables locales
c = 5       # 'c' es una variable global ya que no pertenece a ninguna función o algo similar.
def globalesVsLocales(a, b):
    return (a - c) * b      # En este caso, accedemos a la variable 'a' y 'b' que son locales y a 'c' que es global.

print(globalesVsLocales(10, 2))        # Salida => 10
