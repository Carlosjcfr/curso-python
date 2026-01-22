###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre = input("Como te llamas?\n")
ciudad = input("En que ciudad vives?\n")

print(f"Encantado de conocerte {nombre} de {ciudad}")
### Completa aquí

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
entero = int(cadena)
decimal = float(entero)
dec_to_ent = int(3.99)

print(f"Tu entero {entero}")
print(f"Tu decimal {decimal}")
print(f"Que paso al convertir deciamla a entero?:\n{dec_to_ent}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
nombre = nombre
edad = int(input("Cual es tu edad?\n"))
altura = float(input("Cual es tu altura? ").replace(',','.'))

print(f"Hello! Me llamo {nombre}, tengo {edad} y mido {altura}.")
### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14
redondeo = round(pi)
resultado = int(redondeo/2)
print(f"El metodo de redondeo asigna {redondeo}")
print(f"El resultado es igual a {resultado}")