#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for cont in range (101):
    print(cont)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene

numero = int(input("Ingresá un número entero: "))
digitos = 0
numero_original = numero

if numero == 0:
    digitos = 1
elif numero > 0:
    while  numero >= 1 :
        numero = numero / 10
        digitos = digitos + 1
elif numero < 0:
    while  numero <= -1 :
        numero = numero / 10
        digitos = digitos + 1

print("El número", numero_original, "tiene" ,digitos, "digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
aux = 0
suma = 0

if numero1<numero2:
    menor = numero1
    mayor = numero2
else:
    menor = numero2
    mayor = numero1

for aux in range ((menor+1),mayor):
    suma = suma + aux

print(f"La suma de los números entre {numero1} y {numero2} da como resultado {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma = 0
numero = int(input("Ingresá un número entero (0 para terminar): "))

while numero != 0:
    suma = suma + numero
    numero = int(input("Ingresá otro número entero (0 para terminar): "))

print (f"El resultaso de la suma de los números ingresados da {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0,9)
intento=1

numero=int(input("Ingresá un número entre 0 y 9:" ))
while numero != numero_aleatorio:
    numero=int(input("Ingresá un número entre 0 y 9:" ))
    intento +=1

print(f"Se tomaron {intento} intentos para adivinar el número.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente

for cont in range (98,0,-2):
    print(cont)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Ingresa un número entero positivo: "))
aux = 0
suma = 0

for aux in range (0,numero):
    suma = suma + aux

print(f"La suma de los números entre 0 y {numero} da como resultado {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

limite=100
pares= 0
impares= 0
positivos=0
negativos=0

for aux in range (0,limite):
    numero = int(input("Ingresa un número entero: "))
    aux += 1
    if numero == 0:
        pares +=1
    elif numero > 0:
        positivos +=1
        if (numero%2)==0:
            pares+=1
        else:
            impares+=1
    else:
        negativos+=1

print(f"De un total de {aux} números ingresados se registraron:")
print(f"{pares} números pares:")
print(f"{impares} números impares:")
print(f"{positivos} números positivos:")
print(f"{negativos} números negativos:")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor)

limite = 100
contador=0
media=0
suma=0

for contador in range (0,limite):
    numero = int(input("Ingresa un número entero: "))
    suma += numero
    contador += 1

media=suma/contador

print(f"La media de los números ingresados es {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingresa un número:"))
numero_aux = numero
invertido=0
digitos=0

while  numero_aux >= 1 :
    numero_aux = numero_aux / 10
    digitos = digitos + 1

for n in range(0,digitos):
    invertido=invertido+((numero//10**n)%10)*(10**(digitos-(n+1)))

print(f"El número {numero} con sus dígitos invertidos es {invertido}.")