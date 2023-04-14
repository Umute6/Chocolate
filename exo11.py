from random import randint

a = randint(0,100)
b = randint(0,100)
 
answer = input("Quelle est la somme de " + str(a) + " + " + str(b) + " = " )
answer = int(answer)
errors = 0

while answer != (a + b):
    errors = errors + 1
    answer = input(str(a) + " + " + str(b) + " = ")
    answer = int(answer)

print("Tu as commis " + str(errors) + " erreur(s). ")


