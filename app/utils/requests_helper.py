import traceback
import time
import requests
try:
    import urlparse
    from urllib import urlencode
except: # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode
    import urllib.request


def request_get(host,port,endpoint,params):

    url = 'http://'+host+":"+port+"/"+endpoint
    #print(url)
    #params = {'lang':'en','tag':'python'}

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)

    url_call = urlparse.urlunparse(url_parts)

    #print(url_call)

    req = requests.get(url_call, verify=False)
    
    return req.text

def http_get(host,port,endpoint,params):

    url = 'http://'+host+":"+port+"/"+endpoint
    #print(url)
    #params = {'lang':'en','tag':'python'}

    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)

    url_call = urlparse.urlunparse(url_parts)

    u = urllib.request.urlopen(url_call)

    return u.read().decode('utf-8')

def aliasToJid(calias):

    jid = "%s@s.whatsapp.net" % calias
    return jid