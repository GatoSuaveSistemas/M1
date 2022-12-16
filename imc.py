print("Bienvenidos a mi calculadora IMC")  
while True:
    try:
        nombre = input("Ingrese su nombre: ")
        nombre[0]

        apellidos = input("Ingrese sus apellidos: ")
        apellidos[0]

        edad = float(input("Ingrese su edad: "))
        peso = float(input("Ingrese su peso: "))
        altura = float(input("Ingrese su altura: "))

        break

    except IndexError:
        print("Error: Ingrese caracteres en este campo")

    except ValueError:
        print("Error: Ingrese números en este campo")

# cálculo del IMC 
imc = peso / altura ** 2

print(nombre, apellidos, "tiene", edad, "años y su índice de masa corporal es", imc)