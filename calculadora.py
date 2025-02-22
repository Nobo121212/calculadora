from fractions import Fraction

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def fraccion(num, den):
    if den == 0:
        return "Error: División por cero"
    return Fraction(num, den)

while True:
    print("\nCalculadora - Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Fracción")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == '6':
        print("Saliendo de la calculadora...")
        break
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            print("Resultado:", suma(num1, num2))
        elif opcion == '2':
            print("Resultado:", resta(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado:", division(num1, num2))
    elif opcion == '5':
        num = int(input("Ingresa el numerador: "))
        den = int(input("Ingresa el denominador: "))
        print("Resultado:", fraccion(num, den))
    else:
        print("Opción no válida, intenta de nuevo.")
