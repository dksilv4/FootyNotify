from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json
import SportsNotificationsRequests as sport

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
    print(request.form)
    msg_body = request.form["Body"].replace(" ","")
    from_no = request.form['From']
    print(msg_body, from_no)
    print(pending)
    for temp in pending:
        if from_no == temp[0]:
            if msg_body.lower() == 'yes':
                response.message('You have subbed!')
                subscribers[temp[0]].append(temp[1])
                pending.remove(temp)
                json.dump(subscribers, open('SubList.txt', 'w+'))
                print('dumped')
                return str(response)
    if len(pending) < 1:
        print("Calling the API!")
        team_name = sport.search_for_name(msg_body)
        response.message('To confirm the subscription for the team {}, please reply with yes.'.format(team_name))
        pending.append([from_no, team_name])

    return str(response)


if __name__ == '__main__':
    app.run(debug=True)
