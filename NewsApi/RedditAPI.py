import praw

reddit = praw.Reddit(client_id = 'NCGfJ_dLCKkLeQ',
                     client_secret = '-pzdUANPZk9hdNfXUlKAOuvvzHw',
                     username = 'priyamshah112',
                     password = '7738478888a',
                     user_agent='newsscrapper')

try:    
    news_query = 'Trip wire may have set off bomb in Austin, wounding two men: police'
    all = reddit.subreddit("all")
    for i in all.search(news_query, limit=100):
        print (i.title)
        print(i.url)
except:
    pass
