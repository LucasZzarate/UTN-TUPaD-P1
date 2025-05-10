
#1
'''edad= int(input("Hola, ingrese su edad."))

if edad > 18 :
    print("Es mayor de edad.")
else:
    pass
''''

#2
''''

nota = float(input("Ingrese su nota, porfavor.")) 
if nota >= 6.0:
    print("Aprobado")
else:
    print("Desaprobado")
''''


#3
''''

num = int(input("Ingrese un número impar."))
if (num %2) == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")
''''


#4
''''
edad = int(input("Escriba su edad."))
if edad >= 30:
    print("Usted pertence a la categoría Adulto/a.")
elif edad >= 18 :
    print ("Usted pertence a la categoría de Adulto/a joven")
elif edad < 18 and edad >= 12:
    print('Pertences a la categoría de Adolecentes.')
elif edad < 12 and edad > 1:
    print("Perteneces a la categoría de Niños/as.")
else:
    print("Edad ingresada incorrecta.")
'''

#5
''''
contrasena = input("Ingrese una contraseña que contenga entre 8 y 14 caracteres.")
contrasena = str(contrasena)

if len(contrasena) >= 8 and len(contrasena) <=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de 8 a 14 caracteres.")
''''

#6
'''''
#importamos la libreria random
import random
#definimos la varibale numeros_aleatorios, con una lista que llame a la funcion random(enteros) entre el 1 y 100 hasta que el iterador sea 50 
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

#importe de la libreria statitics solo 3 funciones (mode=moda, median=mediana, mean=media)
from statistics import mode, median, mean

#uso la lista creada al alzar 
print(f"La moda es {mode(numeros_aleatorios)}.\nLa mediana es {median(numeros_aleatorios)}.\nY la media es {mean(numeros_aleatorios)}")

#defini las varibales que voy a usar en la estructura condicional
moda = mode(numeros_aleatorios)
mediana= median(numeros_aleatorios) 
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Hay sesgo positivo.")
elif media < mediana < moda:
    print("Hay sesgo negativo.")
else:
    print("Sin sesgo.")
''''

#7
''''
palabra = str(input("Ingrese una palabra o frase."))

list_vocales = ["a",'A', 'e','E','I', 'i', 'o','O', 'u','U']

if palabra[-1] in list_vocales :
    print(f"{palabra}!")
else :
    print(palabra)
''''

#8
''''
nombre = input("Ingesa tu nombre.")
num = input("Elige la modificacion que quieres para tu nombre.\n1. Nombre en mayúsculas.\n2.Nombre en mínusculas.\n3.Solo la primera letra con mayúscula.")
num = int(num)

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("El número ingresado no pertenece a una opción.")
''''

#9
''''
magnitud = int (input('Ingrese la magnitud del terremoto.'))

if magnitud < 3:
    print("\"Muy leve\"(imperceptible)")
elif magnitud >= 3 and magnitud < 4:
        print("\"Leve\" (ligeramente perceptible).")
elif magnitud >=4 and magnitud < 5:
        print("\"Moderado\" (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
        print("\"Fuerte\"(puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
        print("\"Muy Fuerte\" (puede causar daños significativos).")
elif magnitud >= 7:
        print("\"EXTREMO\" (puede causar graves daños a gran escala).")
'''

#10
''''
hemisferio = input("En que hemisferio se encuentra (N/S)")
dia = int(input ("En que día? (1-31)"))
mes = int(input("En que mes del mes? (1-12)"))

if hemisferio in ['N','n','Norte','norte']:
    if (dia > 0 and dia < 32) and (mes > 0 and mes < 13 ):
        if (mes == 12 and dia>=21) or (mes ==1 or mes ==2) or (mes == 3 and dia<=20):
            print("Invierno")
        elif (mes == 3 and dia>=21) or (mes ==4 or mes ==5) or (mes == 6 and dia<=20):
            print('Primavera')
        elif (mes == 6 and dia>=21) or (mes ==7 or mes ==8) or (mes == 9 and dia<=20):
            print('Verano')
        elif (mes == 9 and dia>=21) or (mes ==10 or mes ==11) or (mes == 12 and dia<=20):
            print("Otoño")
        else:
            pass
    else:
        print('Los valores ingresados no corresponden (dd/mm).')
elif hemisferio in ['S', 's','Sur', 'sur']:
    if (dia > 0 and dia < 32) and (mes > 0 and mes < 13 ):
        if (mes == 12 and dia>=21) or (mes ==1 or mes ==2) or (mes == 3 and dia<=20):
            print("Verano")
        elif (mes == 3 and dia>=21) or (mes ==4 or mes ==5) or (mes == 6 and dia<=20):
            print('Otoño')
        elif (mes == 6 and dia>=21) or (mes ==7 or mes ==8) or (mes == 9 and dia<=20):
            print('Invierno')
        elif (mes == 9 and dia>=21) or (mes ==10 or mes ==11) or (mes == 12 and dia<=20):
            print("Primavera")   
        else:
            pass
    else:
        print('Los valores ingresados no corresponden (dd/mm).') 
else:
    pass
    print('El hemisferio no corresponde.')
'''
print("apple" > "banana")
