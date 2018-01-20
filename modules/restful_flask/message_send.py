from flask import Blueprint, request
from flask import current_app
from app.mac import mac, signals

message_send = Blueprint('message_send', __name__)

@message_send.route("/SendPostMessage", methods=['POST'])
def SendPostMessage():
    msg = request.values.get('msg', '')
    number = request.values.get('number', '')
    if (msg != '' and number != ''):
        mac.send_message_to(msg, number)
        print("TEXT TO CLIENT: "+ number +" => " + msg)
        return "True"
    else:
        return "False"