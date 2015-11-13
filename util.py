##changed into clist.py

import ast
import urllib2
import urllib

url = raw_input("Enter CL link: ")
print url

resp = urllib2.urlopen(url)

ree = resp.read()

print ree

title = ree
title = title.split("<title>")[1]
title = title.split("</title>")[0]
#print title

price = ree
price = price.split('<span class="price">')[1]
price = price.split('</span>')[0]
print price


summary = ree
summary = summary.split('"postingbody">')[1]
summary = summary.split('</section>')[0]
if "showcontact" in summary:
    summary = summary.split('<a href=')[0]

#print summary

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
while i < len(ree):
#    print ree[i].get('url')
    i+=1
#vals = ast.literal_eval(ree)


    


