#Loops: Se ejecuta mientras la condicion se cumpla

names = ["Yuri", "Valeriya", "Valeria", "Alessio"]

#Listando cada una de las posiciones de la lista:
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Listando cada una de las posiciones usando un Loop FPR
#for i in (1,2,3)
#print(i)

for i in names:
    print("Hola ", i)

#Listando cada una de las posiciones de una rango
for i in range(10):
    print(i)

for i in range(5,11):
    print(i)

#Listando cada una de las posiciones de una rango de 2 en 2
for i in range(1,10,2):
    print(i)

#Tamnbien podemos hacer un Loop de Tupples:
num = (1, 5, 67, 90, 1000, 7)
for i in num:
    print(i)