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

print("words count: " + str(len(words)))

sort_orders = sorted(wordscloud.items(), key=lambda x: x[1], reverse=True)

top10 = {}

for item in sort_orders:
    if len(top10) > 9:
         break
    top10[item[1]] = item[0]

print("most important words: " + str(top10) )

