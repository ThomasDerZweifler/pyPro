#f = open("ringelnatz.txt", "r")
f = open("lorem.txt", "r")

# https://www.loremipsum.de/

wordscloud = {}
words = []

for line in f.readlines():
    fwords = line.strip().split(" ")
    for word in fwords:
        word = word.replace('(','').replace(')','')
        if len(word) > 1:
            words.append(word)
            if word in wordscloud:
                wordscloud[word] = wordscloud[word] +1
            else:
                wordscloud[word] = 1
f.close()

print("words: " + str(words))

print("words count: " + str(len(words)))

print("words cloud: " + str(wordscloud))