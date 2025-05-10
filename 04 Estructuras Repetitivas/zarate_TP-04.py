#1)
# Imprimir en pantalla todos los numeros enteros desde 0 hast 100 (incluyendo ambos extremos)
#en orden creciente, mostrando un numero por linea
'''
for cont in range(101):
    print(cont)
'''

#2)
#) Desarrolla un programa que solicite al usuario un número entero y determine la 
# cantidad de dígitos que contiene.
'''
num_entero = '1'
while (num_entero != '0'):
    num_entero=input(print(f'Ingresa un numero entero.\n O ingrese el numero cero para salir.' ))
    validacion = (',.' in num_entero)
    if validacion == False:
        num_entero = int(num_entero)
        for cont in range(1,num_entero + 1):
            break
        print(f"La cantidad de digitos del numero {num_entero} es de: {cont}")
    elif validacion == True:
        print("A ingresado un numeor con decimal.")          
'''
''''
#se pide al usuario que ingrese un numero entero.
num = input(print("Ingrese un numero entero"))
#la funcion len() retorna la longitud de un string, que en este caso es un numero pero
#pero se manipula como string
print(len(num))
'''

#Se podria mejorar --> 
# + aplicaciondo una validacion del numero ingresado, 
# + un bucle, en caso de querer saber la longitud de varios numeros






#3)
# Escribe un programa que sume todos los números enteros comprendidos entre 
# dos valores dados por el usuario, excluyendo esos dos valores. 
''''
num1  = int(input('Ingresa el primer numero entero: '))
num2 = int(input('ingresa el segundo numero entero: '))
suma=int(0)


for cont in range(num1+1,num2):
    
    suma = suma + cont
print(f'La suma de los valores entre ({num1}-{num2}) es de {suma}')

#--> Mejoras:
#              > Validación del entero
#              > Solucionar el tema del orden de los datos cargados
#              > Que sea un bucle hasta que el usuario lo desee
#              > Validacion de dato entero sin que se termine el programa
# La unica limitacion del programa es la validacion de tipo de dato.


#Carga de numeros enteros num1 y num2
num1 = int(input('Ingresa el primer numero entero: '))
num2 = int(input('Ingresa el segundo numero entero: '))
    
while not(num1 >= 0  and num2 >= 0 ):
    num1 = int(input('ERROR...Ingresa el primer numero entero: '))
    num2 = int(input('ERROR...Ingresa el segundo numero entero: '))

if (num1 == num2):
    print(f'Los valores {num1} y {num2} son iguales.')
else:
    #Se verifica el orden de los valores ingresados
    if num1 > num2:
        valor_fin = num1
        valor_inic = num2
    elif num2 > num1:
        valor_fin = num2
        valor_inic = num1
    suma = int(0) #definimos la variable acumuladora 'suma'
    #ciclo For para iterar entre los valores cargados
    for cont in range(valor_inic+1 ,valor_fin): #tener en cuenta el +1 en el valor inicio, para que no se incluya
        suma = suma + cont
    #Se muestra la suma de los valores ordenados, exceptuando los numeros cargados por el usuario.
    print(f'La suma de los valores entre ({valor_inic}-{valor_fin}) es de {suma}')
'''

#4)
# Elabora un programa que permita al usuario ingresar números enteros y los 
# sume en secuencia. El programa debe detenerse y mostrar el total acumulado 
# cuando el usuario ingrese un 0. 
'''
#definimos las variables para que ingrese al bucle while 
suma =int(0)
num=int(1)
#inicializamos el contador en 0.
cont=int(0)
#Si es distinto de cero se ejecuta el bucle.
while num!=0:
    
    cont+=1 # contador, por cada vuelta suma 1.
    num=int(input(f"Ingrese el {cont}° un numero entero, o '0' para salir. "))# varible cargada por el usuario
    suma += num #acumula el numero ingresado por el usuario en la varible suma.
print(f'Haz ingresado un total de {cont-1} números validos, el resultado es de: {suma}')
'''



#5)
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar 
# el número.
'''
import random

numero_random = random.randint(0,9)
print(numero_random)

print('Bienvenido al juego de numeros enteros random.')
print('Deberas adivinar el numero que numero es.. una pista esta entre 0 y 9, incluyendolos.')
print('-----------')
print("Si deseas salir del juego ingresa '*'. ")
print('')
print('Empecemos')
num = input('Igresa el primer numero.')
if num == '*':
    print('Nos vemos la proxima!')
else:
    num=int(num)
    while num != numero_random :
        num=int(input('Vuelve a intentar con otro numero. '))
        if not(num >= 0 and num<=9):
            print('Numero invalido.')
    print('Felicitaciones el numero era ',numero_random,'.')
'''
#6)
# Desarrolla un programa que imprima en pantalla todos los números pares
# comprendidos entre 0 y 100, en orden decreciente. 
'''
print('A continuacion se imprimiran los numero pares del 0 al 100, en orden decrecreciente.')
for n in range(100,0,-2):
    print(n)
'''
#7)
# Crea un programa que calcule la suma de todos los números comprendidos entre 0
# y un número entero positivo indicado por el usuario. 
'''
suma = 0
num_entero=int(input('Ingresa un numero entero positivo '))
for cont in range(0,num_entero):
    suma +=cont
print(f'La suma total entre 0 y {num_entero} es: {suma}')
'''

#8)
# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar 
# preparado para procesar 100 números con un solo cambio). 
'''
valor_fin = int(input('Ingrese la cantidad de numeros que van a ser cargados: '))
par,impar,negativo,positivo,ceros=0,0,0,0,0
for cont in range(1,valor_fin+1):
    num=int(input(f'Ingrese el numero {cont}°: '))
    if (num ==0):
        ceros+=1
    else:
        if(num % 2 == 0):
            par +=1
        else:
            impar += 1
        if num > 0:
            positivo +=1
        else:
            negativo+=1
print(f"En total se han ingresado {valor_fin} numeros, de los cuales: ")
print(f'Par/es: {par}')
print(f'Impar/es: {impar}')
print(f'Positivo/s: {positivo}')
print(f'Negativo/s: {negativo}')
print(f'Cero/s: {ceros}')
'''


#9)
# Elabora un programa que permita al usuario ingresar 100 números enteros y 
# luego calcule la media de esos valores. (Nota: puedes probar el programa con 
# una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 
'''
suma=0
valor_fin = int(input('Ingrese la cantidad de numeros que van a ser cargados: '))
for cont in range(1,valor_fin+1):
    num=int(input(f'Ingrese el {cont}°: '))
    suma +=num
media = suma / cont

print(f"La suma total de los {valor_fin} numeros cargados fue de {suma} y la media {media}")
'''   
#10)
#Escribe un programa que invierta el orden de los dígitos de un número 
# ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar
# 745.
'''
num_inver=0   
num = input('Ingrese el numero que quiera invertir: ')
num_inver= int(str(num)[::-1])
print(num_inver)
'''