#taken from imgur api python github
#link: https://github.com/Imgur/imgurpython/blob/master/examples/auth.py

from imgurpython import ImgurClient
#from helpers import get_input, get_config

#fixes conflict between py2 and py3
def get_input(string):
    try:
        return raw_input(string)
    except:
        return input(string)

def get_config():
    try:
        import ConfigParser
        return ConfigParser.ConfigParser()
    except:
        import configparser
        return configparser.ConfigParser()


def authenticate():
    config = get_config()
    config.read('auth.ini')
    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')
    client = ImgurClient(client_id, client_secret)

    authorization_url = client.get_auth_url('pin')


    # Authorization flow, pin example (see docs for other auth types)
    authorization_url = client.get_auth_url('pin')
    print("Go to the following URL: {0}".format(authorization_url))


    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")


    # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    print("Authentication successful! Here are the details:")
    print(" Access token: {0}".format(credentials['access_token']))
    print(" Refresh token: {0}".format(credentials['refresh_token']))
    return client
                               
if __name__ == "__main__":
    authenticate()
