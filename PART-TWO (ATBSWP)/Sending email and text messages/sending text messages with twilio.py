Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from twilio.rest import Client
accountSID = 'AC9dab3f175f1baf64bbaab232a5b30bfb'
authToken = '2329fccd5c7d700d8626d7ee64dbf929'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+19474652359'
myCellPhone = '+2348107433641'
message = twilioCli.messages.create(body='Mr. Promise - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
message.to
'+2348107433641'
message.from_
'+19474652359'
message.body
'Sent from your Twilio trial account - Mr. Promise - Come here - I want to see you.'
message.status
'queued'
message.date_created
datetime.datetime(2022, 7, 23, 13, 2, 41, tzinfo=<UTC>)
message.date_sent == None
True
message.sid
'SMcbe8323a06f047f8ae12d62e066a76a7'
updatedMessage = twilioCli.messages.get(message.sid)
updatedMessage.status
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    updatedMessage.status
AttributeError: 'MessageContext' object has no attribute 'status'
updatedMessage = twilioCli.messages(message.sid).fetch()
updatedMessage.status
'delivered'
updatedMessage.date_sent
datetime.datetime(2022, 7, 23, 13, 2, 42, tzinfo=<UTC>)
