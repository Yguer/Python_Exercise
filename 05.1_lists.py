#Listas de Datos
names = ["Yuri", "Valeriya", "Valeria", "Alessio"]
print(type(names))

#Reemplazando un elemento de la lista:
names[1] = "Kobzeva"
print(names)

#Eligiendo valores de la lista:
print(names[0:2])
print(names[0:3])
print(names[1:3])

#Algo similar usando la funcion RANGE:
rango = list(range(0,10))
print(rango[0:2])