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
    msg_body = request.form["Body"]
    from_no = request.form['From']
    print(msg_body, from_no)
    if "SUBSCRIBE" in msg_body == True:
        for temp in pending:
            if from_no == temp[0]:
                if msg_body == 'yes':
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
    elif "LAST" in msg_body == True:
        '''insert last fixture code here'''
        return str(response)
    elif "NEXT" in msg_body == True:
        '''insert next fixture code here'''
        return str(response)
    elif "LINEUP" in msg_body == True:
        '''insert lineup for last fixture code here'''
        return str(response)
    elif "LIVE" in msg_body == True:
        '''insert live fixture code here'''
        return str(response)
if __name__ == '__main__':
    app.run(debug=True)

# TODO: Complete function call i.e.
# TODO:SUBSCRIBE team_name (to subscribe) LAST team_name (for last game)  NEXT team_name (for next game) LINEUP team_name (for next lineup) LIVE team_name (for live fixture)
