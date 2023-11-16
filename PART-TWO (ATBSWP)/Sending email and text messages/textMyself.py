#! python3
# textMyself.py - Defines the textmyself() function that texts a message passed to it as a string.

from twilio.rest import Client

accountSID = 'AC9dab3f175f1baf64bbaab232a5b30bfb'
authToken = '2329fccd5c7d700d8626d7ee64dbf929'
myNumber = '+2348107433641'
twilioNumber = '+19474652359'

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)