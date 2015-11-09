import clist
import imgur

cl_url = 'http://newyork.craigslist.org/brx/cto/5307543255.html'

clist.cmake(cl_url)
title = clist.returnTitle()
text = clist.returnText()
count = clist.returnNum()
price = clist.returnPrice()


