import requests
import json
from api_keys import imgur_clientid, imgur_clientsecret

#(Client-ID)
CID = imgur_clientid


url_image = 'https://api.imgur.com/3/image'
url_album = 'https://api.imgur.com/3/album'


def upload_url(url):

    r = requests.post(url_image, data = {'image': url,
                                         'type': 'URL'}, headers = {'Authorization': 'Client-ID ' +  CID})

#    if r.get(status) == 200:
    data = r.json()
    #pprint(data)
    #data = r.text
    return data.get('data').get('id')
#    pprint(r.json())


def upload_local(fpath):

    r = request.post(url_image, data = {'image': open(fpath, 'rb').read(),
                                        'type': 'file'}, headers = {'Authorization': 'Client-ID ' + CID})
    data = r.json()
    return data.get('data').get('id')



def make_album(image_ids, title):

    r = requests.post(url_album, data = {'ids[]': image_ids.split(','),
                                         'title': title}, headers = {'Authorization': 'Client-ID ' + CID})
#    return r.json()
    data = r.json()
    return data.get('data').get('id')
