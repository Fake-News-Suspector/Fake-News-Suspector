#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'http://www.bbc.com/news/world','http://www.bbc.com/news/world/asia',
                 'http://www.bbc.com/news/uk','http://www.bbc.com/news/business','http://www.bbc.com/news/technology',
                 'http://www.bbc.com/news/science_and_environment','http://www.bbc.com/news/stories',
                 'http://www.bbc.com/news/entertainment_and_arts','http://www.bbc.com/news/health','http://www.bbc.com/news/world/africa',
                  'http://www.bbc.com/news/world/australia','http://www.bbc.com/news/world/europe','http://www.bbc.com/news/world/latin_america',
                  'http://www.bbc.com/news/world/middle_east','http://www.bbc.com/news/world/us_and_canada'}
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-1]
            
                for link in soup.findAll('a',{'class':'title-link'}):
                    try:
                        
                        href ="http://www.bbc.com" + link.get('href')
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
