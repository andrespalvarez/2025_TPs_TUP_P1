#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#funciones
def imprimir_hola_mundo(mensaje):
    return print(mensaje)

#principal
imprimir_hola_mundo("Hola Mundo!")

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), 
#deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#funciones
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#principal
saludar_usuario(input("Ingresa tu nombre: "))

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
#Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#principal

informacion_personal(input("Ingresa tu nombre: "),input("Ingresa tu apellido: "),input("Ingresa tu edad: "),input("Ingresa tu ciudad: " ))

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
#devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como 
#parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
#funciones para mostrar los resultados.

#librerias
import math

#funciones
def calcular_area_circulo(radio):
    return print(f"El area del circulo es {radio*(math.pi)**2}")

def calcular_perimetro_circulo(radio):
    return print(f"El perimetro del circulo es {radio*(math.pi)*2}")

#principal
rad=float(input("Ingresa el radio del circulo: "))
calcular_area_circulo(rad)
calcular_perimetro_circulo(rad)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#funciones
def segundos_a_horas(segundos):
    return print(f"{segundos}seg equivalen a {segundos/3600}hr.")

#principal
segundos=int(input("Ingresar la cantidad de segundos: "))
segundos_a_horas(segundos)

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#funciones
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")
    return

#principal
num=int(input("Ingresar el numero para obtener la tabla: "))
tabla_multiplicar(num)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado 
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar 
#los resultados de forma clara.

#funciones
def operaciones_basicas(a, b):
    operaciones=("suma", "resta 1", "resta 2", "multipliacion", "division 1", "division 2")
    resultados=(a+b,a-b,b-a,a*b,a/b,b/a)
    for x in range(len(operaciones)):
        print(f"{operaciones[x]} : {resultados[x]}")
    return

#principal

operaciones_basicas(int(input("ingresar numero 1: ")),int(input("ingresar numero 2: ")))

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
#función para mostrar el resultado con dos decimales.

#funciones
def calcular_imc(peso, altura):
    return print(f"Tu IMC es igual a {peso/altura**2}")

#principal

calcular_imc(float(input("ingresar peso: ")),float(input("ingresar altura: ")))

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#funciones
def celsius_a_fahrenheit(celsius):
    return print(f"{celsius}ºC equivalen a {celsius*9/5+32}ºF.")

#principal

celsius_a_fahrenheit(float(input("Ingresar temperatura en grados celsius: ")))


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.


#funciones
def calcular_promedio(a, b, c):
    return print(f"El promedio entre {a}, {b} y {c} es : {(a+b+c)/3}.")

#principal

calcular_promedio(int(input("Ingresar primer numero: ")), int(input("Ingresar segundo numero: ")), int(input("Ingresar tercer numero: ")))
