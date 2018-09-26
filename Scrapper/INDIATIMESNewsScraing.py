#For Scraping NewsSite (INDIATimes)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://www.indiatimes.com/news/','https://www.indiatimes.com/news/world/',
                 'https://www.indiatimes.com/news/sports/','https://www.indiatimes.com/news/weird/','https://www.indiatimes.com/trending/',
                 }
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-1]
            
                for link in soup.findAll('a',{'class':'caption'}):
                    try:
                        
                        href =link.get('href')
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
