import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url=" https://www.yahoo.com/news/arkansas-becomes-third-u-state-add-medicaid-requirements-172829892--business.html"
driver = webdriver.Firefox(executable_path=r'C:\firefoxdriver\geckodriver.exe')
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,'html.parser')
print(sel_soup.find('a',{'class':'comments-title D(ib) Cur(p) Td(n) C(#000)'}))


"""
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request

class Client(QWebPage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
    def on_page_load(self):
        self.app.quit()
url='https://www.yahoo.com/news/ford-temporarily-layoff-2-000-hourly-employees-michigan-142659305--sector.html'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source,'lxml')
js_test = soup.find('div',attr={'class','D(ib) Fw(b) Mend(10px) Fz(14px) C($c-fuji-blue-1-a) Cur(p)'})
print(js_test.text)


my_url='https://www.yahoo.com/news/oklahoma-teachers-might-west-virginia-strike-walk-outs-055624171.html?nf=1'
from selenium import webdriver
driver = webdriver.Chrome("C:/chromedriver/chromedriver")
driver.get(my_url)
p_element = driver.find_element_by_class_name('D(ib) Fw(b) Mend(10px) Fz(14px) C($c-fuji-blue-1-a) Cur(p)')
print(p_element.text)

DIFFERENT SOLUTION IN JS
CASPERJS
PHANTOMJS

DIFFERENT SOLUTIONS IN PYTHON
Scraping without JS support:
import requests
from bs4 import BeautifulSoup
response = requests.get(my_url)
soup = BeautifulSoup(response.text)
soup.find(id="intro-text")
# Result:
<p id="intro-text">No javascript support</p>

Scraping with JS support:
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get(my_url)
p_element = driver.find_element_by_id(id_='intro-text')
print(p_element.text)
# result:
'Yay! Supports javascript'
You can also use Python library dryscrape to scrape javascript driven websites.

Scraping with JS support:
import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit(my_url)
response = session.body()
soup = BeautifulSoup(response)
soup.find(id="intro-text")
# Result:
<p id="intro-text">Yay! Supports javascript</p>
"""
