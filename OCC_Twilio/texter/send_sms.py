import os
from twilio.rest import Client
from django.http import HttpResponse

def run(request):
    account_sid = 'AC5bca5e1fe8572e4c10e0f66b6f63e9f8'
    auth_token = 'cb4fad176775963c18b8243709fa7625'

    client = Client (account_sid, auth_token)

    client.messages.create(
        to = '+14234830892',
        from_='+14232056663',
        body='Hi NAME. Will you be making it to your appointment on DATE? Respond Y/N.'
    )
    return HttpResponse('Sent text')
