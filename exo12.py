number = input("Introduisez un nombre : ")
number = int(number)

last_number = None
sum_number = number

while number != last_number:
    last_number = number
    number = input("Introduisez un nombre : ")
    number = int(number)
    sum_number = sum_number + number

print("Somme : " + str(sum_number))

