word = input("Mot (end pour finir): ")
num_words = 0

while word != "end":
    num_words = num_words + 1
    if word[0] == "t":
        print(word + " !!!")
    word = input("Mot (end pour finir): ")

print(num_words)
