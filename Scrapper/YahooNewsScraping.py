#For Scraping NewsSite (YAHOO NEWS)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://www.yahoo.com/news/us/','https://www.yahoo.com/news/world/',
                 'https://www.yahoo.com/news/politics/','https://finance.yahoo.com/tech/','https://www.yahoo.com/news/science/',
                 'https://finance.yahoo.com/','https://www.yahoo.com/news/now-i-get-it',
                 'https://www.yahoo.com/gma','https://www.yahoo.com/news/originals/'}
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-2]
            
                for link in soup.findAll('a',{'class':'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)'}):
                    try:
                        
                        href ="https://www.yahoo.com/" + link.get('href')
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
