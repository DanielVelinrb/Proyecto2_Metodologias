import math

"""Funciòn que muestra un menù cuando se ejecuta el programa, 
se muestran 4 opciones para que el usuario pueda seleccionar que operaciòn desea realizar. """

def mostrar_menu():
    print("==== Calculadora ====")
    print("1. Operaciones matemáticas básicas")
    print("2. Operaciones trigonométricas")
    print("3. Operaciones adicionales")
    print("4. Resolver sistema de ecuaciones de segundo grado")
    print("5. Salir")


"""Funciòn para realizar operaciones matemàticas bàsicas, 
el usuario tendrà que ingresar dos nùmeros para realziar una de las operaciones de este apartado.
luego se mostrar un submenù para elegir que opraciòn bàsica realizarà el usuario."""
def realizar_operaciones_basicas():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /): ")
    
    resultado = None
    if operador == '+':
        resultado = suma(num1, num2)
    elif operador == '-':
        resultado = resta(num1, num2)
    elif operador == '*':
        resultado = multiplicacion(num1, num2)
    elif operador == '/':
        resultado = division(num1, num2)
    else:
        print("Operador inválido. Introduce un operador válido.")
    
    if resultado is not None:
        print("El resultado es: {:.2f}".format(resultado))


"""Funciòn para realizar operaciones trigonometricas,
el ususario ingresarà el valor del àngulo en grados, luego se despliega un menù
en el cual se elegirà que funciòn usar para el àngulo proporcionado.
"""
def realizar_operaciones_trigonometricas():
    angulo = float(input("Introduce el valor del ángulo en grados: "))
    opcion = int(input("Elige una opción:\n1. Seno\n2. Coseno\n3. Tangente\n"))
    
    resultado = None
    if opcion == 1:
        resultado = seno(angulo)
    elif opcion == 2:
        resultado = coseno(angulo)
    elif opcion == 3:
        resultado = tangente(angulo)
    else:
        print("Opción inválida. Introduce una opción válida.")
    
    if resultado is not None:
        print("El resultado es: {:.2f}".format(resultado))


"""Funciòn que muestra un menù cuando se elige la opcion de 'operaciones adicionales' el programa, 
muestran 3 opciones para que el usuario pueda seleccionar que operaciòn desea realizar. """
def realizar_operaciones_adicionales():
    print("Elige una operación adicional:")
    print("1. Raíz cuadrada")
    print("2. Potencia")
    print("3. Logaritmo")
    opcion = int(input("Opción (1-3): "))

    if opcion == 1:
        numero = float(input("Introduce un número para calcular la raíz cuadrada: "))
        resultado = math.sqrt(numero)
        print("La raíz cuadrada de {} es {:.2f}".format(numero, resultado))
    elif opcion == 2:
        base = float(input("Introduce la base: "))
        exponente = float(input("Introduce el exponente: "))
        resultado = math.pow(base, exponente)
        print("{} elevado a la {} es {:.2f}".format(base, exponente, resultado))
    elif opcion == 3:
        numero = float(input("Introduce un número para calcular el logaritmo natural: "))
        if numero <= 0:
            print("El número debe ser mayor que 0 para calcular el logaritmo.")
        else:
            resultado = math.log(numero)
            print("El logaritmo natural de {} es {:.2f}".format(numero, resultado))
    else:
        print("Opción inválida. Introduce un número válido.")


"""Funciòn para resolver un sistema de ecuaciones, 
el ususario proporciona los coeficientes de cada ecuaciòn, 
el sistema proporciona la respuesta si tiene soluciòn ùnica, 
sino se proporciona un mensaje."""
def resolver_sistema_ecuaciones():
    print("Ingrese los coeficientes para la primera ecuación (ax + by = c):")
    a1 = float(input("a: "))
    b1 = float(input("b: "))
    c1 = float(input("c: "))

    print("Ingrese los coeficientes para la segunda ecuación (ax + by = c):")
    a2 = float(input("a: "))
    b2 = float(input("b: "))
    c2 = float(input("c: "))

    x, y = resolver_ecuaciones(a1, b1, c1, a2, b2, c2)

    if x is None or y is None:
        print("El sistema de ecuaciones no tiene solución única.")
    else:
        print("El valor de x es: {:.2f}".format(x))
        print("El valor de y es: {:.2f}".format(y))


"""Funciòn que recibe dos numeros de tipo flotante y retorna la suma de los dos nùmeros"""
def suma(num1, num2):
    return num1 + num2


"""Funciòn que recibe dos numeros de tipo flotante y retorna la resta de los dos nùmeros"""
def resta(num1, num2):
    return num1 - num2


"""Funciòn que recibe dos numeros de tipo flotante y retorna el producto de los dos nùmeros"""
def multiplicacion(num1, num2):
    return num1 * num2


"""Funciòn que recibe dos numeros de tipo flotante y retorna la suma de los dos nùmeros"""
def division(num1, num2):
    if num2 == 0:
        print("Error: No es posible dividir entre cero.")
        return None
    return num1 / num2


"""Funciòn que recibe un nùmero de tipo flotante y retorna el seno del nùmero ingresado."""
def seno(angulo):
    return math.sin(math.radians(angulo))


"""Funciòn que recibe un nùmero de tipo flotante y retorna el coseno del nùmero ingresado."""
def coseno(angulo):
    return math.cos(math.radians(angulo))


"""Funciòn que recibe un nùmero de tipo flotante y retorna el tangente del nùmero ingresado."""
def tangente(angulo):
    return math.tan(math.radians(angulo))


"""Funciòn que recibe 6 coeficientes de tipo flotante y retorna el valor de la soluciòn x, y."""
def resolver_ecuaciones(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None, None

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

continuar = True

while continuar:
    mostrar_menu()
    opcion = int(input("Elige una opción (1-5): "))
    if opcion == 5:
        print("¡Hasta luego!")
        continuar = False
    else:
        if opcion == 1:
            realizar_operaciones_basicas()
        elif opcion == 2:
            realizar_operaciones_trigonometricas()
        elif opcion == 3:
            realizar_operaciones_adicionales()
        elif opcion == 4:
            resolver_sistema_ecuaciones()
        else:
            print("Opción inválida. Introduce un número válido.")
