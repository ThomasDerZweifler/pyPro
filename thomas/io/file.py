f = open("ringelnatz.txt", "r")

lines = f.readlines()

words = []

for line in lines:
    fwords = line.split(" ")
    for word in fwords:
        indexof = word.find("\n")
        if indexof == 0:
            continue
        elif indexof > 0:
            word = word[0:indexof]
        words.append(word)

f.close()

print("Wortzahl: " + str(len(words)))