import requests
import json
import base64
from pprint import pprint

#(Client-ID)
CID = '07fed098fe20f1b'


url_image = 'https://api.imgur.com/3/image'
url_album = 'https://api.imgur.com/3/album'


def upload_url(url):

    r = requests.post(url_image, data = {'image': url,
                                         'type': 'URL'}, headers = {'Authorization': 'Client-ID ' +  CID})

    data = r.json()
    return data.get('data').get('id')

def upload_local(fpath):

    r = request.post(url_image, data = {'image': open(fpath, 'rb').read(),
                                        'type': 'file'}, headers = {'Authorization': 'Client-ID ' + CID})
    data = r.json()
    return data.get('id')

                    
    
def make_album(image_ids, title):

    r = requests.post(url_album, data = {'ids[]': image_ids,
                                         'title': title}, headers = {'Authorization': 'Client-ID ' + CID})
#    return r.json()
    pprint(r.json())


print upload_url('http://images.craigslist.org/00606_fE3EKdLWIVw_600x450.jpg')
