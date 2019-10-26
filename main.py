from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

account_sid = 'ACa2785a9fb95337394fca6899a00b6471'
auth_token = '7b32c31d0d7abd7b1cfef757c65469fd'
client = Client(account_sid, auth_token)

app = Flask(__name__)
subscribers = {}
try:
    with open('SubList.txt', 'r') as f:
        subscribers = json.load(f)
        print(subscribers)
except Exception as e:
    print(e)
pending = []


@app.route("/sms", methods=['GET', 'POST'])
def main():
    response = MessagingResponse()
    print(response)
    msg_body = request.form["Body"]
    from_no = request.form['From']

    if msg_body == 'cp':
        response.message("Confirm with YES.")
        pending.append([from_no, 'Crystal Palace'])
    for temp in pending:
        if from_no == temp[0]:
            if msg_body == 'yes':
                response.message('You have subbed!')
                subscribers[temp[0]] = [temp[1]]
                pending.remove(temp)
                json.dump(subscribers, open('SubList.txt', 'w+'))
                print('dumped')
    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
