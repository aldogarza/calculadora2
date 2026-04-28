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
            
    except Exception as e:
        print("Error:", e)