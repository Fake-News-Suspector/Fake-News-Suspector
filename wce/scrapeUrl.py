from bs4 import BeautifulSoup 
from newspaper import Article 
import csv
 
class url_query():
        
        def url_news(sstring):
                url= sstring
                print(url)
                data=[None]*2
                try:
                        article = Article(url)
                        article.download()
                        article.html
                        article.parse()
                        data[0]='100'
                        

                        data[1]=article.title
                        
                        print(*data)
                        # with open('real4.csv','a') as w:
                        #     writer = csv.writer(w)
                        #     writer.writerow(data)
                        # w.close()
                except Exception as e:
                    print(e)
                    pass
                                
        url_news('https://www.yahoo.com/news/gop-lawmaker-knocks-trump-putin-call-refuses-distance-president-135204872.html') 
