print("======MENÚ DE RETOS RECURSIVOS======")
print("1. Invertir una cadena de texto")
print("2. Calcular la suma de los primeros números naturales")
print("3. Imprimir una cuenta regresiva")
print("4. Sumar los digitos de un número")
print("5. Contar cuantos digitos tiene un número")
print("6. Salir")
print("Seleccione una opción: ")
opcion = int(input())
if opcion == 1:
    def invertida(inversion):
        if len(inversion) <= 1:
            return inversion
        else:
            return inversion[-1] + invertida(inversion[:-1])
    inversion = input("Ingrese la palabra que desea invertir: ")
    palabra_invertida = invertida(inversion)
    print(f"La palabra {inversion} de forma invertida es: {palabra_invertida}")