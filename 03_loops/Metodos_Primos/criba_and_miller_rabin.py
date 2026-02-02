import random

def miller_rabin(n, k=10):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def buscar_primos_en_rango_gigante(inicio, extension):
    print(f"Buscando primos en el rango: [{inicio}, {inicio + extension}]")
    
    # 1. Creamos el segmento (asumimos todos candidatos)
    candidatos = [True] * (extension + 1)
    
    # 2. Pre-filtro rápido: eliminamos múltiplos de primos muy pequeños
    # Esto ahorra llamar a Miller-Rabin innecesariamente
    primos_bajos = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for p in primos_bajos:
        # Encontramos el primer múltiplo de p en el rango
        primer_multiplo = (inicio + p - 1) // p * p
        if primer_multiplo < inicio: primer_multiplo += p
        
        # Tachamos en el segmento
        for j in range(primer_multiplo, inicio + extension + 1, p):
            if j != p: # No tachar el primo mismo si está en el rango
                candidatos[j - inicio] = False

    # 3. Miller-Rabin solo para los que pasaron el filtro
    primos_reales = []
    for i in range(len(candidatos)):
        num_actual = inicio + i
        if candidatos[i]:
            if miller_rabin(num_actual):
                primos_reales.append(num_actual)
                
    return primos_reales

# Probamos cerca de 10^60
inicio_rango = int(input("Indica el inicio del rango: "))
rango_busqueda = int(input("Indica el fin del rango: "))
resultados = buscar_primos_en_rango_gigante(inicio_rango, rango_busqueda)

print(f"\nSe encontraron {len(resultados)} primos:")
for p in resultados:
    print(p)