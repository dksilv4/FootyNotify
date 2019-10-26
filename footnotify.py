from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa14f2aadd6b055efaaf15bffd0940e21'
auth_token = '9ce072261b0aace7bb782da01248b07e'

from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
# This function replies to incoming messages. To be improved.
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Test Reply.")

    return str(resp)
    """def hello():
return ("Hello Team\n dogo \n alex")"""


if __name__ == "__main__":
    app.run(debug=True)

# This is how you can send text to a number
'''message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+441212854896',
                     to='+447535186331'
                 )
'''
