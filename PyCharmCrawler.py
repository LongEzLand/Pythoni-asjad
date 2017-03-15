from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse




class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]
    def getLinks(self, url):
        self.url=[]
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-type')== 'text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]
    def spider(url, word, maxPages):
        pagesToVisit=[url]
        numberVisited = 0
        foundWord = False
        while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
            numberVisited = numberVisited+1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numberVisited, "Visiting", url)
                parser = LinkParser()
                data, links = parser.getLinks()
                if data.find(word)>-1:
                    foundWord = True
                pagesToVisit = pagesToVisit + links
                print ("Tore!")
            except:
                print ("Halvasti")
        if foundWord:
            print("Sona", word, "leidsime aadressilt", url)
        else:
            print("Sellist sona ei leidnud")
            print("url")
            print(word)
            print(maxPages)


LinkParser.spider("http://www.ee", "Postimees", 200 )

