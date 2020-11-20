from bs4 import BeautifulSoup
import requests

# https://playmodb.org/

# https://klicky-ersatzteile.de/


class Scraper() :

    def __init__(self):
        self.totalParts = 0
        self.klickyContained = 0

    def getTotalParts(self) :
        return self.totalParts

    def getKlickyContained(self) :
        return self.klickyContained

    def getDetailsByPartNumber(self, partNumber):
        pn = partNumber.get_text()
        partnumberUrl = "https://playmodb.org/cgi-bin/showpart.pl?partnum={0}".format(pn)
        print("\n> get {0}".format(partnumberUrl))
        detail = requests.get(partnumberUrl)
        soupDetail = BeautifulSoup(detail.content, 'html.parser')
        title = soupDetail.find("title").get_text()
        print(title)

        # https://playmodb.org/cgi-bin/category.pl?cat=Decoration;subcat=Flag

        # first href on page
        category = soupDetail.find('a', href=True).get_text()
        print(category)

        if category == "See Klicky details" :
            self.klickyContained += 1

        self.totalParts += 1
  
    def getPartNumbersBySetNumber(sefl, setNumber):
        page = requests.get("https://playmodb.org/cgi-bin/showinv.pl?setnum={0}".format(setNumber))
        soupPage = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        return soupPage.find_all(class_="listpartnumber")

    def getDetailsBySetNumber(self, setNumber):
        partNumbers = Scraper().getPartNumbersBySetNumber(setNumber)
        for partNumber in partNumbers :
            self.getDetailsByPartNumber(partNumber)
        
        return self.totalParts

fromSetNumer = 6682
setsCount = 3
toSetNumer = fromSetNumer + setsCount

fromSetNumer = 4000
setsCount = 1
toSetNumer = fromSetNumer + setsCount

totalParts = 0

scraper = Scraper()

for setNumber in range( fromSetNumer, toSetNumer ):
    print("\n> setNumber = {0}".format(setNumber))
    totalParts += scraper.getDetailsBySetNumber(setNumber)

print("\nfrom set number = {0} scraping {1} set(s) and totalParts = {2} (klicky contained: {3})".format(fromSetNumer, toSetNumer-fromSetNumer,totalParts, scraper.getKlickyContained()))

    
    

