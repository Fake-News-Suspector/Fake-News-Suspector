import pprint
import csv
import json
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
all_articles = newsapi.get_everything(q='U.S. bans government employees from travel to Mexican beach resort'
                                      ) 
myFile = open('Result.txt', 'w')
with myFile:
    for i in all_articles['articles']:
        myFile.write("author"+i['author']+"\n"+"description"+i['description']+"\npublishedAt"+i['publishedAt']+"\n"+"source"+i['source']+"\ntitle"+i['title']+"\nurl"+i['url']+'\nurlToImage'+i['urlToImage'])
readFile = open('Result.txt','r')
with readFile:
    
    for i in readFile:
        print(i)
            #writer.writerows(all_articles)   
#pprint.pprint(all_articles)
"""
Example of Attributes Searches over 30k+ news sites
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_parameter='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
"""
"""
{'articles': [{'author': 'Reuters Editorial',
               'description': 'MEXICO CITY (Reuters) - Citing a new security '
                              "threat in Mexico's Caribbean beach resort of "
                              'Playa del Carmen, the U.S. government is '
                              'prohibiting its employees from traveling there, '
                              'marking another blow to the battered '
                              "reputations of the country's most popular …",
               'publishedAt': '2018-03-09T01:30:37Z',
               'source': {'id': 'reuters', 'name': 'Reuters'},
               'title': 'U.S. bans government employees from travel to Mexican '
                        'beach resort',
               'url': 'https://www.reuters.com/article/us-mexico-violence/u-s-bans-government-employees-from-travel-to-mexican-beach-resort-idUSKCN1GL073',
               'urlToImage': 'https://s4.reutersmedia.net/resources_v2/images/rcom-default.png'},
              {'author': 'http://www.dailymail.co.uk/home/search.html?s=&authornamef=Reuters, '
                         'By Reuters',
               'description': 'MEXICO CITY, March 8 (Reuters) - Citing a new '
                              "security  threat in Mexico's Caribbean beach "
                              'resort of Playa del Carmen,  the U.S. '
                              'government is prohibiting...',
               'publishedAt': '2018-03-09T01:17:00Z',
               'source': {'id': 'daily-mail', 'name': 'Daily Mail'},
               'title': 'U.S. bans government employees from travel to '
                        'Mexican...',
               'url': 'http://www.dailymail.co.uk/wires/reuters/article-5480409/U-S-bans-government-employees-travel-Mexican-beach-resort.html',
               'urlToImage': 'http://i.dailymail.co.uk/i/pix/m_logo_636x382px.png'},
              {'author': None,
               'description': 'MEXICO CITY: Citing a new security threat in '
                              "Mexico's Caribbean beach resort of Playa del "
                              'Carmen, the U.S. government is prohibiting its '
                              'employees from travelling there, marking '
                              'another blow to the battered reputations of the '
                              "country's most popular tourist hu…",
               'publishedAt': '2018-03-09T01:25:15Z',
               'source': {'id': None, 'name': 'Channelnewsasia.com'},
               'title': 'US bans government employees from travel to Mexican '
                        'beach resort',
               'url': 'https://www.channelnewsasia.com/news/world/us-bans-government-employees-from-travel-to-mexican-beach-resort-10028246',
               'urlToImage': 'http://www.channelnewsasia.com/image/8695344/16x9/991/529/609aa1d555bc236155019d989012c2c5/hq/world.png'},
              {'author': 'Thomson Reuters',
               'description': "Citing a new security threat in Mexico's "
                              'Caribbean beach resort of Playa del Carmen, the '
                              'U.S. government is prohibiting its employees '
                              'from traveling there, marking another blow to '
                              "the battered reputations of the country's most "
                              'popular tourist hubs. Rough Cut …',
               'publishedAt': '2018-03-09T13:12:00Z',
               'source': {'id': 'reuters', 'name': 'Reuters'},
               'title': 'U.S. bans govt. employees from travel to Mexican '
                        'beach resort',
               'url': 'https://www.reuters.com/video/2018/03/09/us-bans-govt-employees-from-travel-to-me?videoId=407483151',
               'urlToImage': 'https://s2.reutersmedia.net/resources/r/?d=20180309&i=OV869XZ33&w=1200&r=OV869XZ33&t=2'},
              {'author': None,
               'description': "Citing a new security threat in Mexico's "
                              'Caribbean beach resort of Playa del Carmen, the '
                              'U.S. government is prohibiting its employees '
                              'from traveling there, marking another blow to '
                              "the battered reputations of the country's most "
                              'popular tourist hubs. Rough Cut …',
               'publishedAt': '2018-03-09T13:01:08Z',
               'source': {'id': None, 'name': 'Yahoo.com'},
               'title': 'U.S. bans govt. employees from travel to Mexican '
                        'beach resort',
               'url': 'https://www.yahoo.com/news/u-bans-govt-employees-travel-130108128.html',
               'urlToImage': 'https://s.yimg.com/uu/api/res/1.2/G_8aOhOOuvx_PFiji8ccIg--~B/aD01NDA7dz05NjA7c209MTthcHBpZD15dGFjaHlvbg--/http://media.zenfs.com/en-US/video/video.reutersnews.com/2018-03-09T130108Z_1_LOP000JVDVFCF_RTRMADP_BASEIMAGE-960X540_US-MEXICO-VIOLENCE-ROUGH-CUT.JPG'}],
 'status': 'ok',
 'totalResults': 5}
 """
