from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa2785a9fb95337394fca6899a00b6471'
auth_token = '7b32c31d0d7abd7b1cfef757c65469fd'

from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

client = Client(account_sid, auth_token)
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
# This function replies to incoming messages. To be improved.
def sms_reply():
    data = request.args["Body"]
    print(data)

    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Add a message
    resp.message("Test Reply.")

    return str(resp)


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
