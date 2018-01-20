import sys, logging
from yowsup.layers.auth import AuthError
from yowsup.layers.axolotl.props import PROP_IDENTITY_AUTOTRUST
from yowsup.stacks import YowStackBuilder
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
from app.layer import MacLayer
from flask import Flask, request
from flask_restful import Resource, Api
import threading

from modules.restful_flask.message_send import message_send

app = Flask(__name__)
api = Api(app)

# PLUG more blueprints for, media send, etc...
app.register_blueprint(message_send)

credentials = ("55XXXXXXXX", "XXXXXXXXXXXXXXXXXXXX")
encryption = True

class MacStack(object):
    def __init__(self):
        builder = YowStackBuilder()

        self.stack = builder\
            .pushDefaultLayers(encryption)\
            .push(MacLayer)\
            .build()

        self.stack.setCredentials(credentials)
        #self.stack.setProp(MacLayer.PROP_CONTACTS,  list(config.contacts.keys()))
        self.stack.setProp(PROP_IDENTITY_AUTOTRUST, True)

    def start(self):
        print("WHATSAPP-FRAMEWORK RESTFUL STARTED")
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))

        try:
            #self.stack.loop(timeout=0.5, discrete=0.5)
            threading._start_new_thread(self.stack.loop, tuple((0.5, 0.5)))
        except AuthError as e:
            print("Auth Error, reason %s" % e)
        except KeyboardInterrupt:
            print("\nYowsdown")
            sys.exit(0)
            
if __name__ == "__main__":
    c = MacStack()
    c.start()
    print("SERVER STARTED...")
    app.run(host="192.168.0.107", port=5122,debug=False)