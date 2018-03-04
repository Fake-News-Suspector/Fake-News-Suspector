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
            #headlines = link.string
            #article =   Article(href)
            #article.download()
            #article.html
            #article.parse()
            #print(href) #to fetch particular articles link
            #print(article.title) #to fetch headlines
            #print(article.text) #to fetch body text of article
            #print(article.top_image) #to fetch image of news article
            comments_article(href)
                        
def comments_article(addr):
    url = addr
    source_code = requests.get(url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    
    #For name of commenter
    for commenter in soup.findAll('div',{'class':'D(ib) Fw(b) Mend(10px) Fz(14px) C($c-fuji-blue-1-a) Cur(p)'}):
            print(commenter.get_text())
    #For Comments    
    for comments in soup.findAll('div',{'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
            print(comments.get_text())
    #For Replies
    for replies in soup.findAll('div',{'class':'C($c-fuji-grey-l) Mb(2px) Fz(14px) Lh(20px) Pend(8px)'}):
            print(replies.get_text())
    #For Comment Likes
    for like in soup.findAll('button',{'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n) Mend(12px)'}):
            print(like.get_text())
    #For Comment Dislikes
    for dislike in soup.findAll('button',{'class':'O(n) Bgc(t) Bdc(t) M(0) P(0) Bd(n)'}):
            print(dislike.get_text())
    #For News Likes
    for happy in soup.findAll('span',{'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-green-1-b) Pend(6px)'}):
            print(happy.get_text())
    #For News Dislikes
    for sad in soup.findAll('span',{'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-red-2-a)'}):
            print(sad.get_text())
    #For News Neutrals    
    for neutrals in soup.findAll('span',{'class':'Pstart(3px) Fz(11px) Fw(b) C($c-fuji-orange-b) Pend(6px)'}):
            print(neutrals.get_text())
        #page+=1
main_news() #trade_spider(page)
