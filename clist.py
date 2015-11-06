import ast
import urllib2
import urllib
#import json
#from BeautifulSoup import BeautifulSoup
#url = "http://newyork.craigslist.org/brx/boa/5293603888.html"
links = []
title
summary 
def cmake(a):
    url = a
    resp = urllib2.urlopen(url)
    ree = resp.read()

    title = ree
    title = title.split("<title>")[1]
    title = title.split("</title>")[0]


    summary = ree
    summary = summary.split('"postingbody">')[1]
    summary = summary.split('</section>')[0]
    if "showcontact" in summary:
        summary = summary.split('<a href=')[0]


    ree = ree.split('var imgList =')[1]
    ree = ree.split('var imageText ')[0]
    ree = ree[3: len(ree) - 4]
    ree = ree.split("},{")
    i = 0
    while i < len(ree):
        ree[i] = '{' + ree[i] + '}'
        i+=1
    i = 0
    while i < len(ree):
        ree[i] = ast.literal_eval(ree[i])
        i+=1
    i = 0
    #while i < len(ree):
    #    print ree[i].get('url')
    #    i+=1
    while i < len(ree):
        links.append(ree[i].get('url'))
        i+=1
    
#vals = ast.literal_eval(ree)

def returnTitle():
    return title
def returnText():
    return summary
def returnLinks():
    return links
        
cmake("http://newyork.craigslist.org/lgi/cto/5303380345.html")
print "Title:" + returnTitle() + "\n"
print "Text:" + returnText() + "\n"
print "Image Links:" + str(returnLinks())
    


