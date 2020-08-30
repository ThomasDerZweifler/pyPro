f = open("ringelnatz.txt", "r")

lines = f.readlines()

words = []

for line in lines:
    fwords = line.rstrip("\n").split(" ")
    for word in fwords:
        if len(word) > 0:
            words.append(word)

f.close()

print("words: " + str(words))

print("Wortzahl: " + str(len(words)))