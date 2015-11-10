import requests
import json
import base64
from pprint import pprint

#(Client-ID)
CID = ''


url_image = 'https://api.imgur.com/3/image'
url_album = 'https://api.imgur.com/3/album'


def upload_url(url):

    r = requests.post(url_image, data = {'image': url,
                                         'type': 'file'}, headers = {'Authorization': 'Client-ID ' +  CID})

    return r.json()
#    pprint(r.json())


def upload_local(fpath):

    r = request.post(url_image, data = {'image': open(fpath, 'rb').read(),
                                        'type': 'file'}, headers = {'Authorization': 'Client-ID ' + CID})
    return r.json()
#    pprint(r.json())
                    
    
def make_album(image_ids, title):

    r = requests.post(url_album, data = {'ids[]': image_ids,
                                         'title': title}, headers = {'Authorization': 'Client-ID ' + CID})
#    return r.json()
    pprint(r.json())


upload_url('http://images.craigslist.org/00i0i_a7vgoXjFLS9_600x450.jpg')
