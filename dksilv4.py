from datetime import datetime
from threading import Timer
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os


# sublist = open('SubList.txt', 'r').read().split('\n')
# for sub in sublist:
#     x = sub.split(', ')
#     print(x)


def hello_world():
    print("hello world")


class Verify:
    def __init__(self, message):
        # if message.from in sublist:
        #     pass
        if ''.join(message.lower()) == 'crystal palace':
            pass
            # send message to confirm sub
            # if confirmed add number to sub list with code

    def example(self):
        pass


account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')
client = Client(account_sid, auth_token)

# messages = client.messages.list(limit=20)
# for msg in messages:
#     x = client.messages(msg.sid).fetch()
#     print(x)

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    incText = request.form["Body"]
    if incText.lower() == 'diogo':
        resp.message("Diogo Reply.")
    else:
        resp.message("HI!")
    return str(resp)



if __name__ == '__main__':
    app.run(debug=True)
