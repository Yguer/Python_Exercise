edad = int(input("Que Edad Tienes? "))
mayor_edad = False

if edad>=18:
    mayor_edad = True
    print("Eres Mayor de Edad")
else:
    print("Eres Menor de Edad")

if mayor_edad == True:
    print("Eres Mayor de Edad")
#Otra forma mas abreviada:
if mayor_edad:
    print("Eres Mayor de Edad")