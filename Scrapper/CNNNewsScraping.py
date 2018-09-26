#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://edition.cnn.com/regions',
                 'https://edition.cnn.com/us','https://edition.cnn.com/africa','https://edition.cnn.com/americas',
                 'https://edition.cnn.com/asia','https://edition.cnn.com/china','https://edition.cnn.com/europe',
                 'https://edition.cnn.com/middle-east','https://edition.cnn.com/opinions','https://edition.cnn.com/politics',
                 'http://money.cnn.com/international','https://edition.cnn.com/entertainment','http://money.cnn.com/technology/',
                  'https://edition.cnn.com/sport','https://edition.cnn.com/travel',
                  'https://edition.cnn.com/style','https://edition.cnn.com/health'}
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-1]
                selector = 'h3.cd__headline > a'
                for link in soup.select(selector):
                    try:
                        try:
                            
                            href ="https://edition.cnn.com"+link.get('href')
                            #headlines = link.string
                            article =   Article(href)
                            article.download()
                            article.html
                            article.parse()
                            with open(filename+"_"+article.title,'w') as t:
                                    t.write("\t \t \t \t LINK TO NEWS \n"+href +"\n"+"\t \t \t \t HEADLINE \n"+article.title+"\n"+"\t \t \t \t CONTENT \n"+article.text+"\n")
                        except:
                            href ="http://money.cnn.com"+link.get('href')
                            #headlines = link.string
                            article =   Article(href)
                            article.download()
                            article.html
                            article.parse()
                            with open(filename+"_"+article.title,'w') as t:
                                    t.write("\t \t \t \t LINK TO NEWS \n"+href +"\n"+"\t \t \t \t HEADLINE \n"+article.title+"\n"+"\t \t \t \t CONTENT \n"+article.text+"\n")

                    except:
                        continue
                        
main_news() #trade_spider(page)
