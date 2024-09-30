print("Ejercicio N° 1")
for i in range(1, 101):
    print( i,end=" " )


print("")
print("Ejercicio N° 2")

for q in range (2 , 502, 2):
    print(q, end=" ")

print("")
print("Ejercicio N° 3")
for v in range(1, 101):
    if v % 10 == 0:
        print("baby")
    elif v % 5 == 0:
        print("ice ice")
    else:
        print(v)

print("")
print("Ejercicio N° 4")

suma = 0

for s in range(0, 500001, 2):
    suma += s

print("La suma total de los números pares es:", suma)

print("Ejercicio N° 5")


for r in range (2024 , 0 , -3):
    print(r, end=" ")
print("")
print("Ejercicio N° 6")

numInicial = 2
numFinal = 15
multiplo = 3

for m in range(numInicial, numFinal + 1):
    if m % multiplo == 0:
        print(m)
