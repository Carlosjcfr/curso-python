###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0

while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: "))
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 10
while contador >= 1:
  print(contador)
  contador += -1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
contador = 1
suma = 0
while contador <= 20:
  if contador % 2 == 0:
    suma += contador

  contador += 1
print(f"La suma de los pares del 1 al {contador-1} es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
contador = 1
numero = 5
factorial = 1
while contador <= numero:
  factorial *= contador
  contador += 1
print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
char_min = 8
while True:
  # Solicitamos la contrseña
  print("Indica una contraseña con al menos 8 caracteres: ")
  password = input("Contraseña: ")
  pwd_len = len(password)

  # Validacion de la contraseña
  if pwd_len > char_min:
    #Exito! Mostramos mensjae de validacion con el nuemro de caracreres de la contraseña
    print(f"Excelente tu contrseña *** tiene {pwd_len} caracteres")
    break
  
  print("Tu contraseña no cumple con los requisitos! \nIntentalo de nuevo:")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

i = 1
while True:
  try:
    numero = int(input("Indica un numero: "))
    while i <= 10:
      print(f"{numero} x {i} = {numero*i}")
      i += 1
    break
  except ValueError:
    print("Error!, solo introducir números enteros")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

i = 1
primos = []
while True:
  try:
    n = int(input("Indica un numero entero positivo: "))
      if n <= 1: False #Excluimos negativos (redundante)
      if n == 2 True #Inlucluimos el 2 como numero primo
    while i <= n:
      i += 1
      if n % 2 == 0: False #Descarte de pares
      if n % i == 0: True #Es primo si es divisible por si mismo
      
      primos

    #Mostramos la lista de numeros primos  
    print(f"Primos positivos menores o iguales a {n}: {primos}")
    break
  except ValueError:
    print("Error!, solo introducir números enteros")


  #Consturimos una lista con todo los numeros posible desde 1 hasta n, excluyendo los que sabemos que no van a ser primos: 
  # Pares
  # Numeros que son divisibles por otros numeros con resto 0
