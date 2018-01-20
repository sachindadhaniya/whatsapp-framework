from app.mac import mac, signals
from app.utils import helper
from app.utils import requests_helper
import requests
import config
import re
import sys

@signals.message_received.connect
def handle(message):
    params = {}
    # CASE TEXT-MESSAGE
    if helper.is_text_message(message.message_entity):
        # Make This shit for python2 and python3
        if sys.version_info >= (3, 0):
            params['msg']  = message.text
            params['name'] = message.who_name
        else:
            params['msg']  = message.text.encode('utf-8')
            params['name'] = message.who_name.encode('utf-8')
        params['number']  = message.conversation
        params['media'] = 'text'
        params['caption'] = ''
        print("MSG FROM CLIENT %s => %s" % (message.conversation,params['msg']))
        requests_helper.request_get("192.168.0.107", "3000",'endpoint',params)
        
     # CASE MEDIA-MESSAGE
    elif helper.is_media_message(message.message_entity):
        print("media here....")
    else:
        print ("sem tratativa")
