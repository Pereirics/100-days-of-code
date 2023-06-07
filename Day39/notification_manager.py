import os

from twilio.rest import Client

TWILIO_SID = "AC072adbd938bfde88d0f44817786150a1"
TWILIO_AUTH_TOKEN = os.environ.get("SMS_API_KEY")
TWILIO_VIRTUAL_NUMBER = "+13203772770"
TWILIO_VERIFIED_NUMBER = "+351932106455"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)
