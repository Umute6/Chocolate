word = input("Donnez un mot : ")
the_list = ["a", "e", "i", "o", "u", "y"]

somme = 0
for i in word:
    if i in the_list:
        somme = somme + 1

print(somme)