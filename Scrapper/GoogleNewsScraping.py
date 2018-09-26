#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://news.google.com/news/headlines/section/topic/NATION.en_in/India?ned=in&hl=en-IN&gl=IN','https://news.google.com/news/headlines/section/topic/WORLD.en_in/World?ned=in&hl=en-IN&gl=IN',
                 'https://news.google.com/news/headlines/section/topic/BUSINESS.en_in/Business?ned=in&hl=en-IN&gl=IN','https://news.google.com/news/headlines/section/topic/TECHNOLOGY.en_in/Technology?ned=in&hl=en-IN&gl=IN','https://news.google.com/news/headlines/section/topic/ENTERTAINMENT.en_in/Entertainment?ned=in&hl=en-IN&gl=IN',
                 'https://news.google.com/news/headlines/section/topic/SPORTS.en_in/Sport?ned=in&hl=en-IN&gl=IN',
                 'https://news.google.com/news/headlines/section/topic/SCIENCE.en_in/Science?ned=in&hl=en-IN&gl=IN','https://news.google.com/news/headlines/section/topic/HEALTH.en_in/Health?ned=in&hl=en-IN&gl=IN'}
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-2]
            
                for link in soup.findAll('a',{'class':'nuEeue hzdq5d ME7ew'}):
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
