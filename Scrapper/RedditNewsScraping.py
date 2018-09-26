#For Scraping NewsSite (Reddit)
import requests #Website request library
from bs4 import BeautifulSoup #Scraping Library
from newspaper import Article #Scraping News Body

 
#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        #For getting various categories of webpage
        url= {'https://www.reddit.com/r/news/','https://www.reddit.com/r/worldnews/?hl=undefined',
              'https://www.reddit.com/r/PoliticalDiscussion/','https://www.reddit.com/r/worldevents/',
              'https://www.reddit.com/r/geopolitics/','https://www.reddit.com/r/business/',
              'https://www.reddit.com/r/Economics/','https://www.reddit.com/r/environment/',
              'https://www.reddit.com/r/history/','https://www.reddit.com/r/humanrights/',
              'https://www.reddit.com/r/features/','https://www.reddit.com/r/UpliftingNews/',
              'https://www.reddit.com/r/NewsOfTheWeird/','https://www.reddit.com/r/fakenews/',
              'https://www.reddit.com/r/popular/?geo_filter=GLOBAL'
                 }
                 #+ str(page)


        for i in url:
                source_code = requests.get(i) #Server request for a url
                plain_text=source_code.text #Getting text file of webpage
                soup = BeautifulSoup(plain_text,'lxml') #parsing webpage
                filename = i.split('/')[-2]
            
                for link in soup.findAll('a',{'class':['title may-blank outbound','title may-blank ']}):
                    try:
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
                                href ="https://www.reddit.com"+link.get('href')
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
