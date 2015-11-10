import clist
import imgur

cl_url = raw_input("CL: ")

clist.cmake(cl_url)
title = clist.returnTitle()
text = clist.returnText()
price = clist.returnPrice()
links = clist.returnLinks()

i = 0
while i < len(links):
    links[i] = imgur.upload_url(links[i]).get('id')
    i += 1

imgur.make_album(links, title)

