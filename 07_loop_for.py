#Loops: Whill run while the condition is met

names = ["Yuri", "Valeriya", "Valeria", "Alessio"]

#Listing all the positions from list:
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Listing all the positions using FOR
#for i in (1,2,3)
#print(i)

for i in names:
    print("Hola ", i)

#Listing every position within a range
for i in range(10):
    print(i)

for i in range(5,11):
    print(i)

#Listing every postition within a range 2 by 2
for i in range(1,10,2):
    print(i)

#We can also do range using Tupples:
num = (1, 5, 67, 90, 1000, 7)
for i in num:
    print(i)