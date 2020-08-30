f = open("ringelnatz.txt", "r")

words = []

for line in f.readlines():
    fwords = line.strip().split(" ")
    for word in fwords:
        word = word.replace('(','').replace(')','')
        if len(word) > 0:
            words.append(word)

f.close()

print("words: " + str(words))

print("Wortzahl: " + str(len(words)))