def programa_principal():
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    # Solicitud de los datos edad y nombre 

    if edad >= 18:
        print(f"¡Hola, {nombre}! Eres mayor de edad.")
    else:
        print(f"¡Hola, {nombre}! Eres menor de edad.")
# Confirmar mayoria de edad

# Mini Calculadora
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            print(f"Suma: {num1 + num2}")
            print(f"Resta: {num1 - num2}")
            print(f"Multiplicación: {num1 * num2}")

            if num2 != 0:
                print(f"División: {num1 / num2}")
            else:
                print("No se puede dividir por cero.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce números.")

#Juego de Adivinanza
    numero_secreto = 4
    adivinado = False
    print("\n¡Vamos a jugar a adivinar un número!")
    print("Estoy pensando en un número entre 1 y 10.")

# Comandos para los intentos del juego
    while not adivinado:
        try:
            intento = int(input("¿Cuál es tu suposición? "))
            if intento == numero_secreto:
                print(f"¡Felicidades, {nombre}! ¡Adivinaste el número secreto ({numero_secreto})!")
                adivinado = True
            elif intento < numero_secreto:
                print("Demasiado bajo. ¡Inténtalo de nuevo!")
            else:
                print("Demasiado alto. ¡Inténtalo de nuevo!")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

    while True:
        continuar = input("¿Deseas continuar con la mini calculadora? (s/n): ").lower()
        if continuar == 's':
            # Solicitud para repetir la calculadora
            while True:
                try:
                    num1 = float(input("Introduce el primer número: "))
                    num2 = float(input("Introduce el segundo número: "))

                    print(f"Suma: {num1 + num2}")
                    print(f"Resta: {num1 - num2}")
                    print(f"Multiplicación: {num1 * num2}")

                    if num2 != 0:
                        print(f"División: {num1 / num2}")
                    else:
                        print("No se puede dividir por cero.")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, introduce números.")
        elif continuar == 'n':
            print(f"¡Adiós, {nombre}! Gracias por jugar.")
            break
        else:
            print("Respuesta no válida. Por favor, introduce 's' o 'n'.")

# Ejecutar el programa principal
if __name__ == "__main__":
    programa_principal()