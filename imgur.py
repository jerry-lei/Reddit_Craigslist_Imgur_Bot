import requests
import json
import base64
import clist
from pprint import pprint


api_key = #(Client-ID)


url_image = 'https://api.imgur.com/3/image'

def upload_local():#fpath):#, imgur_title):
    #f = open(fpath, 'rb')
    #bd = f.read()
    #b64img = base64.b64encode(bd)

    r = requests.post(url_image, data = {'image': 'http://images.craigslist.org/00D0D_43QSLR3T8xM_600x450.jpg',#open(fpath, 'rb').read(),
                                         'type': 'file'},
                                         headers = {'Authorization': 'Client-ID ' +  api_key})
                                         
    pprint(r.json())

upload_local()

#upload_local('0.jpg')#, 'test')    

    
