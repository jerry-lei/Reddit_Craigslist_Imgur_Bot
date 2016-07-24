from clist_img import *
import imgur
from logger import *

@logger
def imgur_album(link):
    post = cmake(link)

    s = ''
    c1 = 0
    links = post[3]
    while c1 < len(links):
        s += imgur.upload_url(links[c1]) + ', '
        c1 += 1

    album_id = imgur.make_album(s,post[0])
    return "imgur.com/a/" + album_id

imgur_album("http://newyork.craigslist.org/fct/cto/5674742667.html")
