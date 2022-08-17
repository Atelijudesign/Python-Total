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
x = 6
y = 7
print("Mis numeros son: " +str(x)+  " y " +str(y))
print("Mis numeros son: {} y {}".format(x,y))
print("La suma de : {} y {} es igual a {}".format(x,y, x+y))

#Cademas Literales
color = "Rojo"
matricula = "'RBSG25'"
print(f"El auto es de color {color} y su matricula es {matricula}")
