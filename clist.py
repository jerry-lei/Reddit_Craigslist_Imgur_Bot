import ast
import urllib2
import urllib
import os
#import json
#from BeautifulSoup import BeautifulSoup
#url = "http://newyork.craigslist.org/brx/boa/5293603888.html"

links = []
def cmake(a):
    url = a
    resp = urllib2.urlopen(url)
    ree = resp.read()

    
    global title
    title = ree
    title = title.split("<title>")[1]
    title = title.split("</title>")[0]

    global price 
    price = ree
    price = price.split('<span class="price">')[1]
    price = price.split('</span>')[0]

    global summary
    summary = ree
    summary = summary.split('"postingbody">')[1]
    summary = summary.split('</section>')[0]
#    summary = summary.strip('<br>')
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
    global links
    while i < len(ree):
        links.append(ree[i].get('url'))
        i+=1

    i = 0
    while i < len(links):
        urllib.urlretrieve(links[i], str(i) + '.jpg')
        i+=1

            
#vals = ast.literal_eval(ree)

def returnTitle():
    return title
def returnText():
    return summary
def returnLinks():
    return links
def returnPrice():
    return price
        
#cmake("http://newyork.craigslist.org/mnh/cto/5279903723.html")
cmake("http://newyork.craigslist.org/brk/cto/5303483432.html")
print "Title:" + returnTitle() + "\n"
print "Text:" + returnText() + "\n"
print "Image Links:" + str(returnLinks())
print "Price:" + returnPrice()
    


