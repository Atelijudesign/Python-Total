#Tipo de datos
#string "Hola Mundo"
#integer (int) 150,1,85
#floating (float) 1.25,25.5
#listas (lst) ["sal",2,-3,4.5,"marte",0]
#diccionarios (dic) {'color':'rojo','arte':'cine'}
#tuples (tup) ('lun','mar','mier','jue','vier')
#sets (set) {'a','b','c','d','e'}
#booleanos (bool) True,False

#Variables
# nombre = "Juan"
# nombre = "Andres"
# name = input("Dime tu nombre:")
# print("Tu nombre es: "+name)

#Integer and Floats

# mi_numero = 1
# type(mi_numero)
# print(type(mi_numero))
#
# edad = input("Ingresa tu edad: ")
# print("Tu edad es: "+edad)

#Conversion Implicita
# num1 = 6
# num2 = 8.5
# num1 = num1 + num2
# print(type(num1))
# print(type(num2))
# print(num1)

#COnversion Explicita

# num1= 8.5
# print(num1)
# print(type(num1))
#
# num2 = int(num1)
# print(num2)
# print(type(num2))
# edad = input("Dime tu edad: ")
# edad = int(edad)
# nueva_edad = 1 +edad
# print(nueva_edad)

#Formatear Cadenas
# x = 6
# y = 7
# print("Mis numeros son: " +str(x)+  " y " +str(y))
# print("Mis numeros son: {} y {}".format(x,y))
# print("La suma de : {} y {} es igual a {}".format(x,y, x+y))

#Cademas Literales
# color = "Rojo"
# matricula = "'RBSG25'"
# print(f"El auto es de color {color} y su matricula es {matricula}")

#Operaciones matematicas
# print("---------------------")
# x=6
# y= 5
# z = 7
# print(f"La suma de {x} mas {y} es igual a {x+y}")
# print(f"La multiplicacion  de {x} por {y} es igual a {x*y}")
# print(f"La division  de {x} dividido {y} es igual a {x/y}")
# print(f"La resta de {x} menos {y} es igual a {x-y}")
# print(f"El modulo  de {z} mas {y} es igual a {z%y}")
# print(f" {x} elevado a {y} es igual a {x**y}")

# print("Redondeo")
# x = 9.6568
# y = 205
# z = x*y
# print(round(z,2))
# num1 = round(13/2,0)
# print(num1)
# print(type(num1))
#Desafio día 2
print("Desafio día 2")
nombre = input("Por favor ingrese su nombre: ")
ventas = int(input("Indique sus ventas totales del mes: "))

#Formula para calcular la comision
comision = round(ventas*13/100,2)

ventaTotal = ventas+comision

print(f"Hola {nombre}, tus comision  de este mes fue: ${comision}. Tu total a pagar es: ${ventaTotal}")
