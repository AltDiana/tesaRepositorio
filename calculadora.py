def calculadora():
    print("Calculadora básica")
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    
    print("Operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("Resultado:", a + b)
    elif opcion == "2":
        print("Resultado:", a - b)
    elif opcion == "3":
        print("Resultado:", a * b)
    elif opcion == "4":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Error: división por cero")
    else:
        print("Opción inválida")

calculadora()