filename = 'txt/lorem.txt'
# filename = "txt/ctArtikel.txt"
# filename = "txt/ringelnatz.txt"

f = open(filename, "r")

# generate demotext: https://www.loremipsum.de/

# redundant words (stopwords): https://github.com/solariz/german_stopwords

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

goodLooking = True
if goodLooking :

    # all words with their frequences sorted descendant
    sort_orders = sorted(wordscloud.items(), key=lambda x: x[1], reverse=True)

    print(sort_orders)

    top10 = {}

    # words of the heigest ten frequences ()
    for item in sort_orders:
        if len(top10) > 9:
            break
        frequence = item[1]
        word = item[0]
        top10[frequence] = word

    print("most important (frequence representant) words: " + str(top10) )

goodLooking = True

import random

l = list(top10.keys())

print(l)

random.shuffle(l)

print(l)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 word cloud (' + filename+ ')'
        self.width = 600
        self.height = 600
        self.initUI()

    def getSpannedText(self, word, size):
        return "<span style='font-size:" + str(size) + "pt; color:white;'>" + word + " </span>"

    def average(self,lst): 
        return sum(lst) / len(lst) 

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.width, self.height)

        widget = QWidget()
        layout= QHBoxLayout()
        widget.setLayout(layout)

        s = ""
        maxSize = 100

        scale = maxSize / self.average(l)

        print(scale)

        for index in l:
            word = top10[index]
            size = index * scale

            s = s + self.getSpannedText(word, size)
            print("size: " + str(size))

        label = QLabel(word,self)
        label.setWordWrap(True)
        label.setText(s)

        layout.addWidget(label)

        self.setCentralWidget(widget)

        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())