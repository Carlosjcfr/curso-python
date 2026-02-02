print("\n--- Generador de Primos Optimizado (Filtro 2,3,5,7) ---")

while True:
    try:
        n = int(input("Introduce un número límite (N): "))
        if n < 0:
            print("Por favor, introduce un número positivo.")
            continue
        break
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# 1. Inicialización selectiva (Omitimos pares desde el inicio)
# Creamos una lista de False y solo marcamos impares como candidatos (True)
es_primo = [False] * (n + 1)

i = 3
while i <= n:
    es_primo[i] = True
    i += 2

# El 2 es el único par primo
if n >= 2:
    es_primo[2] = True

# 2. Pre-limpieza de múltiplos de los "4 grandes" (3, 5, 7)
# El 2 no necesita limpieza porque ya ignoramos los pares
primos_base = [3, 5, 7]
idx = 0
while idx < 3:
    p_base = primos_base[idx]
    if n >= p_base * p_base:
        multiplo = p_base * p_base
        while multiplo <= n:
            es_primo[multiplo] = False
            multiplo += p_base
    idx += 1

# 3. Bucle Maestro: Empezamos a comprobar desde el 11
# Solo evaluamos números que sigan siendo True e impares
p = 11
while p * p <= n:
    if es_primo[p]:
        # Tachamos sus múltiplos
        multiplo = p * p
        while multiplo <= n:
            es_primo[multiplo] = False
            multiplo += p
    p += 2  # Saltamos pares

# 4. Recolección de resultados
lista_primos = []
i = 2
while i <= n:
    if es_primo[i]:
        lista_primos.append(i)
    i += 1

print(f"\nPrimos encontrados hasta {n}:")
print(lista_primos)
print(f"Total: {len(lista_primos)} números primos.")