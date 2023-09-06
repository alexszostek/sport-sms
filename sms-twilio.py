# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACdc4a3abfabd69526d187529200b531de'
auth_token = '31e84398dcc6550acf59f6f7a8c8e09d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18443882749',
                     to='+19893131968'
                 )

print(message.sid)
