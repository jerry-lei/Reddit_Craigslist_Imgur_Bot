from clist_img import *
import imgur
from logger import *

#@logger
def imgur_album(link):
    post = cmake(link)
    print 'CREATING: ' + post[0]
    s = ''
    c1 = 0
    links = post[3]
    while c1 < len(links):
        s += str(imgur.upload_url(links[c1])) + ', '
        c1 += 1

    album_id = imgur.make_album(s,post[0])
    return [post[0], post[1], post[2], album_id]

#imgur_album("http://newyork.craigslist.org/fct/cto/5674742667.html")
