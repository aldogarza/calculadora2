from Calculadora import Calculadora

def menu():
    print("\n--- CALCULADORA TDD ---")
    print("1. Sumar")

while True:
    menu()
    opcion = input("Elige opción: ")

    try:
        if opcion == "1":
            a = int(input("A: "))
            b = int(input("B: "))
            print("Resultado:", Calculadora.sumar(a, b))
        
        elif opcion == "2":
            a = int(input("A: "))
            b = int(input("B: "))
            print("Resultado:", Calculadora.restar(a, b))

        elif opcion == "3":
            a = int(input("A: "))
            b = int(input("B: "))
            print("Resultado:", Calculadora.multiplicar(a, b))

        elif opcion == "4":
            a = float(input("A: "))
            b = float(input("B: "))
            print("Resultado:", Calculadora.dividir(a, b))
        

    except Exception as e:
        print("Error:", e)