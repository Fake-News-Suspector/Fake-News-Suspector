#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://www.wsj.com/news/world','https://www.wsj.com/news/us',
                 'https://www.wsj.com/news/politics','https://www.wsj.com/news/economy','https://www.wsj.com/news/business',
                 'https://www.wsj.com/news/technology','https://www.wsj.com/news/markets','https://www.wsj.com/news/opinion',
                 'https://www.wsj.com/news/life-arts','https://www.wsj.com/news/realestate','https://www.wsj.com/news/magazine',
                 'https://www.wsj.com/news/types/africa-news','https://www.wsj.com/news/types/asia-news','https://www.wsj.com/news/types/canada-news',
                  'https://www.wsj.com/news/types/china-news','https://www.wsj.com/news/types/europe-news',
                  'https://www.wsj.com/news/types/latin-america-news','https://www.wsj.com/news/types/middle-east-news'}
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-1]
            
                for link in soup.findAll(['a','h3'],{'class':['subPrev headline','headline','headline subPrev']}):
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
