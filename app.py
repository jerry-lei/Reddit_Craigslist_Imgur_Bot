import time
import praw
import working
from api_keys import reddit_clientid, reddit_clientsecret, reddit_user, reddit_pass

r = praw.Reddit('Craiglist bot by /u/jerrylei98')
#r.set_oauth_app_info(client_id = reddit_clientid,
                     #client_secret = reddit_clientsecret,
                     #redirect_uri='http://162.243.63.270')
r.login(reddit_user, reddit_pass)
finished = []

while True:
    subreddit = r.get_subreddit('jerrylei98')
    for submission in subreddit.get_new(limit=10):
        link = submission.url
        if 'craigslist.org' in link and submission.id not in finished:
            fin = working.imgur_album(link)
            submission.add_comment(fin[0] + " - " + fin[1] + "\n\n[LINK TO IMGUR](https://" + fin[3] + ")")
            print "------- LINK: " + fin[3]
            finished.append(submission.id)
    time.sleep(60)
