'''
 Crear una función llamada imprimir_hola_mundo que imprima por
 pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 programa principal.
'''
def imprimir_hola_mundo(a):
    print("Hola Mundo!")

imprimir_hola_mundo('')

'''
Crear una funcion llamada saludar_usuario(nombre) que reciba como
parametro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario('marcos'), debera
devolver: "Hola marcos!"Llamar a esta funcion desde el progrma
principal solicitando el nombre al usuario
'''
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input('Ingresa tu nombre. ')
saludar_usuario(nombre)

'''Crear una funcion llamada informacion_personal(nombre, apellido, edad,
residencia) que reciba cuatro parámetros e imprima: "soy [nombre][apellido], tengo [edad]
años y vivo en [residencia]". Pedir los datos al usuario y
llamar a esta funcion con los valores ingresados
'''
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")

nombre = input('Ingrese su nombre: ')
apellido = input('Su apellido: ')
edad = input('Su edad: ')
residencia = input('Su residencia: ')
informacion_personal(nombre, apellido, edad, residencia)

'''
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parametro y devuelva el area del circulo.
calcular_perimetro_circulo(radio)
que reciba el radio como parametro y devuelva el perimetro del circulo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los
resultados.
'''
def calcular_area_circulo(radio):
    radio = int(radio)
    return 3.1416 * radio*radio

def calcular_perimetro_circulo(radio):
    radio = int(radio)
    return (2*3.1416*radio)

radio = input('Ingrese el radio del circulo ')
print(f'El area del circulo es: {calcular_area_circulo(radio)}, y el perimetro {calcular_perimetro_circulo(radio)}.')



'''Crear una funcion llamada segundos_a_horas(segundos) que reciba
una cantidad ed segundos como parametro y devuelva la cantidad de horas
correspondiente. Solicitar al usuario los segundos y mostrar el resultado
usando esta funcion.
'''
def segudos_a_horas(segundos):
    print(segundos/3600)

segundos = int(input('Ingrese la cantidad de segundos. '))
segudos_a_horas(segundos)


'''Crear una función llamada tabla_multiplicar(numero) que reciba un
 número como parámetro y imprima la tabla de multiplicar de ese
 número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
'''
def tabla_multiplicar(numero):
    
    for x in range(1,11,1):
        print(f"{numero} * {x} = {numero*x}")
        print(' ')

numero = int(input('Ingrese un numero '))
tabla_multiplicar(numero)


'''
Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
'''
def operaciones_basicas(a,b):
    suma = a+b
    resta= a-b
    mult = a * b
    div = a / b
    return (suma, resta, mult, div)

num1 = int(input('ingrese primer valor: '))
num2 = int(input('ingrese segundo valor: '))
print(operaciones_basicas(num1,num2))


'''
 Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales
'''
def calcular_imc(pseo,altura):
    c=(peso /(altura**2))
    return round(c,2)


peso = int(input("Ingrese el peso en Kg: "))
altura = float(input("Ingrese la altura: "))



'''
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función.
 '''
def celcius_a_fahrenheit(c):
    f = (c * 1.8) + 32
    return f
grados_celcius=float(input('Ingrese los grados Celsius: '))



'''
Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función.
'''
def calcular_promedio(a,b,c):
    p = (a + b + c)/3
    return round(p,2)

num = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))
print(f'El promedio es {calcular_promedio(num,num2,num3)}')
