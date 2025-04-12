def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero."
    return x / y

def main():
    while True:
        print("\n--- Calculadora en Terminal ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion not in ['1', '2', '3', '4']:
            print("Opción no válida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números.")
            continue

        if opcion == '1':
            resultado = sumar(num1, num2)
        elif opcion == '2':
            resultado = restar(num1, num2)
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
        elif opcion == '4':
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
