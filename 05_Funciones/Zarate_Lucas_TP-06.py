def contar_digito(numero, digito):
    if len(str(numero)) == 1:
        if numero == digito:
            return 1 # probe tambien devolver un array con dos valores [numero, 1] pero no me deja acceder
        else:
            return 0
    else:
        return contar_digito(numero // 10, digito) +1   # se que tengo que sumar lo que retorna y que tengo que recuperar el numero
        

print(contar_digito(236, 2))

def contar_digitow(numero, digito):
    numero = str(numero)
    digito = str(digito)

    if len(numero) == 1:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        fn = contar_digitow(numero[0:-1], digito) # se que tengo que sumar lo que retorna y que tengo que recuperar el numero
        return fn

#--------------------------------------------
'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci 
en la posición indicada. Posteriormente, muestra la serie completa 
hasta la posición que el usuario especifique
'''
def fibo(n):
    if n ==0 or n ==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

posicion = int(input("Ingrese un la posicion de fibonacci deseada: "))
print(f"La posicion {posicion} en sistema fibonacci equivale al numero {fibo(posicion)}")
#-----------------------------------------------
'''
Crea una función recursiva que calcule la potencia de un número
base elevado a un exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general
'''
#funcion recursiva
#calcular potencia
#ingresar potencia y numero
#utlizar formula m= N*N

def potencia_num(base,exponente):
    m=1
    p= exponente
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        m = base * (potencia_num(base,p-1))
    return m

print(potencia_num(14,3))
#-------------------------------------------
'''
Crear una función recursiva en Python que reciba un número entero positivo
en base decimal y devuelva su representación en binario como una cadena de 
texto. Cuando representamos un número en binario, lo expresamos usando 
solamente ceros (0) y unos (1), en base 2. Para convertir un número decimal 
a binario, se puede seguir este procedimiento:

1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número
binario.

Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es 
"1010".
'''
#ingreso de numero entero positivo en base decimal (del 1 al 10)
#devolver su represnetacion en binario como string



def num_valid(numero):
    if numero > 0 and numero <= 10:
        return True
    else:
        return False

"""
def conver_n_binario(n):
    if num_valid(n) == True:

    else:
        binario = n
        return 2 % (conver_n_binario(n // 2))
        
"""



numero = int(input('Ingrese número positivo.'))

num_valid(numero)

#---------------------------------------------
'''
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''

def es_palindromo(cadena):
    
    if len(cadena) == 1:
        return True
    elif len(cadena) == 2:
        return cadena[0] == cadena[-1:]
    else:
        return es_palindromo(cadena[1:-1])

print(es_palindromo("Anita lava la tina"))
#------------------------------------------------
'''
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)

'''

def suma_digitos(num):
    if num <= 9:
        return num
    else:
        return suma_digitos(num // 10) + (num - num // 10 * 10)

print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))
#-----------------------------------------------
'''
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)

'''
def contar_bloques(n):
    if n == 1:
        return n
    else:
        return contar_bloques(n-1) + n
    
print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))
#---------------------------------------------
'''
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
'''
