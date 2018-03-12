import pprint
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
all_articles = newsapi.get_everything(q='In bow to NRA, Trump throws gun purchase age to states, courts',
                                      )
pprint.pprint(all_articles)
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
