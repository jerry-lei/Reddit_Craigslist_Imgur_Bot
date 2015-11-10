import clist
import imgur
from pprint import pprint

cl_url = raw_input("CL: ")

clist.cmake(cl_url)
title = clist.returnTitle()
text = clist.returnText()
price = clist.returnPrice()
links = clist.returnLinks()
s = ''
i = 0
while i < len(links):
    #s += imgur.upload_url(links[i]).get('id') + ', '
    print imgur.upload_url(links[i]).get('id')
    i += 1
#pprint(imgur.make_album(s, title))

