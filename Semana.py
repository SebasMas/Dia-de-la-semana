semana = ["Lunes","Martes","Miércoles","Jueves","Viernes"]

numero = int(input("Ingrese un número del 1 al 5: "))

resultado = semana.pop(numero-1)
print(resultado)
