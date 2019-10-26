from datetime import datetime
from threading import Timer
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


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


account_sid = 'ACa2785a9fb95337394fca6899a00b6471'
auth_token = '7b32c31d0d7abd7b1cfef757c65469fd'
client = Client(account_sid, auth_token)

# messages = client.messages.list(limit=20)
# for msg in messages:
#     x = client.messages(msg.sid).fetch()
#     print(x)

app = Flask(__name__)

confirming_num = []
confirming_code = []
subs = []
sublist = open('SubList.txt', 'r').read().split('\n')
for sub in sublist:
    x = sub.split(', ')
    subs.append(x)


def subscribe(num):
    for i in range(0, len(confirming_num) - 1):
        if num == confirming_num[i]:
            code = confirming_code[i]
            subs.append([confirming_num, confirming_code])
            number = '\n{}, {}'.format(num, code)
            sub_file = open('SubList.txt', 'a+')
            sub_file.write(number)


def check_sub(num):
    for subscriber in subs:
        if num == subscriber[0]:
            return True
    return False


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    print(request.form)
    requestForm = request.form
    from_body = requestForm["Body"]
    from_no = requestForm['From']
    if not check_sub(from_no):

        if from_body.lower() == 'crystal palace':
            resp.message("Please text YES to confirm subscription.")
            confirming_num.append(requestForm['From'])
            confirming_code.append('Crystal Palace')
        if from_no in confirming_num:
            if from_body == 'YES':
                resp.message("Thank you for your subscription!")
                print(from_no)
                subscribe(from_no)

        else:
            resp.message(
                "Hi! Thanks for texting but the option you gave us is invalid. Have a nice day! If you'd like to get a list of the available sevices please text HELP!")
    else:
        resp.message("This number is already subscribed to crystal palace.")
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
