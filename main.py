from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json

account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN_TWILIO'
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
    team_name = search(msg_body)
    response.append('To confirm the subscription for the team {}, please reply with yes.'.format(team_name))
    pending.append([from_no, team_name])
    for sub in subscribers:
        if sub == from_no:
            for team in sub[from_no]:
                if team == team_name:
                    response.message("You have already subscribed to {}.".format(team_name))

    for temp in pending:
        if from_no == temp[0]:
            if msg_body == 'yes':
                response.message('You have subbed!')
                subscribers[temp[0]] = [temp[1]]
                pending.remove(temp)
                json.dump(subscribers, open('SubList.txt', 'w+'))
                print('dumped')
    return str(response)

def search(input):


if __name__ == '__main__':
    app.run(debug=True)
