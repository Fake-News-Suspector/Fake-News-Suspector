import requests
from bs4 import BeautifulSoup
from newspaper import Article


#def trade_spider(max_pages)
def main_news():
    #page=1
    #while page <= max_pages:
        url = 'https://www.yahoo.com/news/us/' #+ str(page)
        source_code = requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        for link in soup.findAll('a',{'class':'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)'}):
            href ="https://www.yahoo.com/" + link.get('href')
##            #headlines = link.string
##            article =   Article(href)
##            article.download()
##            article.html
##            article.parse()
##            print("\t \t \t \t LINK TO NEWS \n"+href +"\n") #to fetch particular articles link
##            print("\t \t \t \t HEADLINE \n"+article.title+"\n") #to fetch headlines
##            print("\t \t \t \t CONTENT \n"+article.text+"\n") #to fetch body text of article
##            print("\t \t \t \t IMAGE LINK \n"+article.top_image+"\n") #to fetch image of news article
            comments_article(href)
                        
def comments_article(addr):
        url = addr
        source_code = requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text,'lxml')
        #print(soup.prettify())
    #For name of commenter
        for commenter in soup.findAll('div',attrs={'class':'D(ib) Fw(b) Mend(10px) Fz(14px) C($c-fuji-blue-1-a) Cur(p)'}):
            print("\t \t \t \t COMMENTER  \n"+commenter.get_text()+"\n")
    #For Comments    
        for comments in soup.findAll('div',attrs={'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
            print("\t \t \t \t COMMENTS \n"+comments.get_text()+"\n")
    #For Replies
        for replies in soup.findAll('div',attrs={'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
            print("\t \t \t \t REPLIES \n"+replies.get_text()+"\n")
    #For Comment Likes
        for like in soup.findAll('button',attrs={'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n) Mend(12px)'}):
            print("\t \t \t \t LIKE ON COMMENT \n"+like.get_text()+"\n")
    #For Comment Dislikes
        for dislike in soup.findAll('button',attrs={'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n)'}):
            print("\t \t \t \t DISLIKE ON COMMENT \n"+dislike.get_text()+"\n")
    #For News Likes
        for happy in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-green-1-b) Pend(6px)'}):
            print("\t \t \t \t LIKES ON NEWS \n"+happy.get_text()+"\n")
    #For News Dislikes
        for sad in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-red-2-a)'}):
            print("\t \t \t \t DISLIKE ON NEWS \n"+sad.get_text()+"\n")
    #For News Neutrals    
        for neutrals in soup.findAll('span',attrs={'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-orange-b) Pend(6px)'}):
            print("\t \t \t \t NEUTRALS ON NEWS \n"+neutrals.get_text()+"\n")
        #page+=1
main_news() #trade_spider(page)
