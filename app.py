import time
import praw
import working
import database
from api_keys import reddit_clientid, reddit_clientsecret, reddit_user, reddit_pass

r = praw.Reddit('Craiglist bot by /u/jerrylei98')
#r.set_oauth_app_info(client_id = reddit_clientid,
                     #client_secret = reddit_clientsecret,
                     #redirect_uri='http://162.243.63.270')
r.login(reddit_user, reddit_pass)

while True:
    print '*Awake*'
    subreddit = r.get_subreddit('jerrylei98')
    for submission in subreddit.get_new(limit=10):
        link = submission.url
        if 'craigslist.org' in link and database.checkDB(submission.id):
            try:
                fin = working.imgur_album(link)
                database.intoDB(submission.id, fin[3])
                submission.add_comment(fin[0] + " - " + fin[1]
                                       + "\n\n**[LINK TO IMGUR](https://imgur.com/a/" + fin[3] + ")**\n\n>"
                                       + fin[2])
                print "------- LINK: https://imgur.com/a/" + fin[3]
            except(IndexError):
                print "NOT POST LINK"
                pass
    time.sleep(60)
