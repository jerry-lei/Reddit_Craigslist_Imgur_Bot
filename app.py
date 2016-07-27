import time
import praw
import working
import database
from clist_img import find_links
from api_keys import reddit_clientid, reddit_clientsecret, reddit_user, reddit_pass

r = praw.Reddit('Craiglist bot by /u/jerrylei98 /*==*\ Posting through /u/clbot-jerrylei98')
#r.set_oauth_app_info(client_id = reddit_clientid,
                     #client_secret = reddit_clientsecret,
                     #redirect_uri='http://162.243.63.270')
r.login(reddit_user, reddit_pass)

#Replies self posts
while True:
    subreddit = r.get_subreddit('jerrylei98')
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        #print comment.body
        if database.checkDB(comment.id,"com_log"):
            print "-Checking Comment-"
            temp = comment.body
            links = list(set(find_links(temp)))
            links = [c1 for c1 in links if 'craigslist.org/' in c1]
            s = ''
            if len(links) > 0:
                print "-Replying to Comment-"
                s = '**IMGUR MIRROR LINK(S)**\n\n'
                for c1 in xrange(len(links)):
                    try:
                        fin = working.imgur_album(links[c1])
                        s += "[" + fin[0] + "](https://imgur.com/a/" + fin[3] + ")\n\n"
                    except(IndexError):
                        print "-* NOT POST LINK *-"
                        pass
                if len(s) > 26:
                    comment.reply(s)
            database.intoDB3(comment.id)
    for submission in subreddit.get_new(limit=5):
        if database.checkDB(submission.id,"sub_log"):
            print "-Checking Submission-"
            links = list(set(find_links(submission.selftext)))
            links = [c1 for c1 in links if 'craigslist.org/' in c1]
            s = ''
            if len(links) > 0:
                print "-Replying to Submission-"
                s = '**IMGUR MIRROR LINK(S)**\n\n'
                for c1 in xrange(len(links)):
                    try:
                        fin = working.imgur_album(links[c1])
                        s += "[" + fin[0] + "](https://imgur.com/a/" + fin[3] + ")\n\n"
                    except(IndexError):
                        print "-* NOT POST LINK *-"
                        pass
                submission.add_comment(s)
            database.intoDB2(submission.id)
            #print s
    time.sleep(180)

"""Replies to link submissions
    while True:
        print '*/==Awake==\*'
        subreddit = r.get_subreddit('jerrylei98')
        for submission in subreddit.get_new(limit=10):
            link = submission.url
            if 'craigslist.org/' in link and database.checkDB(submission.id,cl_log):
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
"""
