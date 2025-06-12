#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

#funciones

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#principal

nro = int(input("Ingresa un numero entero positivo: "))
print(f"Los factoriales de los nros. entre 1 y {nro} son: ")
for i in range (1,(nro+1)):
    print(f"/{factorial(i)}", end="")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

# funciones

def fibonacci(n):
    if n== 0:
        return 0
    elif n== 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#principal

nro = int(input("Ingresa un numero entero positivo: "))
print(f"Los {nro} primeras posiciones de la serie de Fibonacci son: ")
print(fibonacci(0), end="")
for i in range (1,(nro+1)):
    print(f"+{fibonacci(i)}", end="")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula n^m = n*n^(m-1). Prueba esta función en un algoritmo general.

# funciones

def exponente(n,m):
    if m==0:
        return 1
    else:
        return n*exponente(n,m-1)

#principal

n=int(input("Indicar numero:"))
m=int(input("Indicar exponente:"))
print(f"{n} elevado a la {m} da como resultado: {exponente(n,m)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
#procedimiento:

# funciones

def binario(nro):
    if nro==1:
        return "1"
    else:
        return str(nro%2)+binario(nro//2)

#principal

nro=int(input("Indicar numero en base 10: "))

print(f"{nro} convertido a binario da como resultado {binario(nro)[::-1]}")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

def inversion(cadena):
    if len(cadena)==0:
        return ""
    else:
        return cadena[len(cadena)-1]+inversion(cadena[:-1])

def es_palindromo(palabra):
    if inversion(palabra)==palabra:
        return True
    else:
        return False

palabra=str(input("Ingresá una cadena sin espacios ni tildes: "))

invalido=True
while invalido==True:
    invalido=False
    for i in palabra:
        if i in ("áéíóú "):
            invalido=True
    if invalido==True: 
        palabra=str(input("ERROR.Ingresá otra cadena sin espacios ni tildes: "))

print(f"Estado de la condición PALINDROMO para cadena {palabra}: {es_palindromo(palabra)} ")

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

#funciones

def suma_digitos(n):
    if n==0:
        return 0
    else:
        return (n%10)+suma_digitos(n//10)

#principal

nro=int(input("Ingresar un número entero positivo:"))

print(f"La suma de los digitos de {nro} da como resultado: {suma_digitos(nro)}")

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

#funciones
def contar_bloques(n):
    if n==1:
        return 1
    else:
        return n+contar_bloques(n-1)

#principal
base=int(input("ingresar las cantidad de bloques de la base: "))

print(f"Se necesitarán {contar_bloques(base)} bloques para armar una pirámide de base {base} bloques.")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
#Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4
#contar_digito(123456, 7) → 0

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
#Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4
#contar_digito(123456, 7) → 0

#funciones

def contar_digito(n, digito):
    if n==0:
        return 0
    else:
        if n%10 == digito:
            contador=1
        else:
            contador=0            
        return contador+contar_digito(n//10, digito)

#principal

nro=int(input("Ingresar un número: "))
dig=int(input("Ingresar un dígito a contar: "))

print(f"El dñigito {dig} aparece {contar_digito(nro,dig)} veces en el nro. {nro}.")