from Calculadora import Calculadora

def menu():
    print("\n--- CALCULADORA TDD ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Exponencial (e^x)")
    print("0. Salir")

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
        
        elif opcion == "5":
            x = float(input("Número: "))
            print("Resultado:", Calculadora.raiz(x))

        elif opcion == "6":
            x = float(input("Exponente: "))
            print("Resultado:", Calculadora.exp(x))

        elif opcion == "0":
            print("Adiós")
            break

        else:
            print("Opción inválida")

        

    except Exception as e:
        print("Error:", e)