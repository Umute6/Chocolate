#
n = input("Un entier entre 1 et 100 : ")
n = int(n)

while n < 1 or n > 100:
    n = input("Un entier entre 1 et 100 : ")
    n = int(n)

somme = 0  
for i in range(n + 1):
    somme = somme + i

print(somme)

print(n * (n + 1) / 2)
print(sum(range(n + 1)))   