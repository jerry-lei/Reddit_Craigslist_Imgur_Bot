import requets
import json
import base64
import clist


api_key = '11' #needs anon key

url_image = r'http://api.imgur.com/2/upload.json'

def upload_local(fpath, imgur_title):
    f = open(fpath, 'rb')
    bd = f.read()
    b64img = base64.b64encode(binary_data)

    dataa = {'key': api_key,
            'image': b64img,
            'title': imgur_title,
            }
    r = request.post(url, data = dataa)
    j = json.loads(r.text)

    pprint(j)


upload_local('1.jpg', 'test)
    
