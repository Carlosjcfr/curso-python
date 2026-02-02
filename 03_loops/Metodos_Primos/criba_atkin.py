import math

def criba_atkin(limite):
    if limite < 2: return []
    if limite == 2: return [2]
    if limite == 3: return [2, 3]

    # Inicializamos la criba con False
    criba = [False] * (limite + 1)
    
    # Los resultados de las ecuaciones determinan la "primicidad" inicial
    raiz = int(math.sqrt(limite)) + 1

    for x in range(1, raiz):
        for y in range(1, raiz):
            
            # Ecuación 1
            n = 4 * x**2 + y**2
            if n <= limite and n % 12 in (1, 5):
                criba[n] ^= True # Operación XOR (invierte el estado)

            # Ecuación 2
            n = 3 * x**2 + y**2
            if n <= limite and n % 12 == 7:
                criba[n] ^= True

            # Ecuación 3
            n = 3 * x**2 - y**2
            if x > y:
                if n <= limite and n % 12 == 11:
                    criba[n] ^= True

    # Eliminamos los cuadrados de los números primos encontrados
    for r in range(5, raiz):
        if criba[r]:
            cuadrado = r**2
            for i in range(cuadrado, limite + 1, cuadrado):
                criba[i] = False

    # El 2 y 3 son casos especiales que el algoritmo no marca
    primos = [2, 3]
    primos.extend([i for i in range(5, limite + 1) if criba[i]])
    
    return primos

# Ejemplo de uso
n = int(input("Indica el limite: "))
resultado = criba_atkin(n)
print(f"Primos hasta {n}: {resultado}")