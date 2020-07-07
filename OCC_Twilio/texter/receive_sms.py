import os
from twilio.twiml.messaging_response import MessagingResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging, logging.config
import sys
from twilio.rest import Client
from texter.models import Response
import datetime
from django.utils import timezone

@csrf_exempt
def sms_reply(request):


    resp = MessagingResponse()
    #print >>sys.stderr,
    paylod = request.body.decode("utf-8").split('&')

    message_body = ''
    to_num = ''
    date = timezone.now()
    phone_number = ''
    response = ''
    #POST paylod
    for item in paylod:
        item = item.split('=')
        if item[0] == 'From':
            print( item[1][3:], file=sys.stderr)
            to_num = '+'+item[1][3:]
            #phone_number = item[1][3:]
        elif item[0] == 'Body':
            print( item[1], file=sys.stderr)
            if item[1].upper() == 'Y':
                response = 'Y'
                message_body = 'Thank you for confirming your appointment'
                resp.message("Thank you for your reply")
            elif item[1].upper() == 'N':
                response = 'N'
                message_body = 'Sorry that you will not make it'
                resp.message("Thank you for your reply")
            else:
                message_body = 'Please resond Y/N'

    #Respond based on user input
    account_sid = 'AC5bca5e1fe8572e4c10e0f66b6f63e9f8'
    auth_token = 'cb4fad176775963c18b8243709fa7625'

    client = Client (account_sid, auth_token)

    client.messages.create(
        to = to_num,
        from_='+14232056663',
        body= message_body
    )
    if response is 'Y' or response is 'N':
        p = Response(phone=str(to_num), response=response, reply_date=date)
        p.save()
        #return HttpResponse('invalid response')
    print(p, file=sys.stderr)
    return HttpResponse('valid response')
