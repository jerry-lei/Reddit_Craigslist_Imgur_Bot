import urllib2

def cmake(CL_link):
    url = CL_link
    resp = urllib2.urlopen(url)
    ree = resp.read()

    title = ree
    title = title.split("<title>")[1]
    title = title.split("</title>")[0]

    price = ree
    price = price.split('<span class="price">')[1]
    price = price.split('</span>')[0]

    summary = ree
    summary = summary.split('"postingbody">')[1]
    summary = summary.split('</section>')[0]
    summary = summary.replace('<br>','')
    if "showcontact" in summary:
        summary = summary.split('<a href=')[0]

    img_links = ree
    img_links = img_links.split('var imgList =')[1]
    img_links = img_links.split('--></script>')[0]
    img_links = img_links.replace('"','') #strips quotes
    img_list = img_links.split(",")
    global fin_list
    fin_list = []

    for c1 in xrange(len(img_list)):
        if "url" in img_list[c1]:
            fin_list.append(img_list[c1].split('url:')[1])

    return [title,price,summary,fin_list]
