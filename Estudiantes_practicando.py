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
elif opcion == 2:
    def naturales(num):
        if num == 0:
            return 0
        else:
            return num + naturales(num-1)
    num = int(input("Ingrese numero: "))
    print(naturales(num))
elif opcion == 3:
    def cuenta(n):
        if n == 0:
            return 0
        else:
            print(n)
            return n + cuenta(n-1)
    n = int(input("Ingrese el numero para iniciar la cuenta regresiva: "))
    cuenta = cuenta(n)
elif opcion == 4:
    print("Codigo en proceso...")
elif opcion == 5:
    def conteo(numero):
        if numero < 10:
            return 1
        else:


"""
    numero = input("Ingrese un numero: ")
    digitos = len(numero)
    print(f"El número posee {digitos} digitos")
"""