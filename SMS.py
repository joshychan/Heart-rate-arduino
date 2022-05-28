# -*- coding: utf-8 -*-
import os
from twilio.rest import Client

account_sid = 'Account ID' 
auth_token = 'Auth Token' 
client = Client(account_sid, auth_token) 


f = open('BPM.txt', 'r')
x = f.read()

numList = x.split("\n")
f.close()
for i in range(0, len(numList),1):
    numList[i] = numList[i].replace(",","")
    numList[i] = int(numList[i])

if numList[i] < 30:
        message = client.messages \
                .create(
                    body='This is an emergency.this persons heart is too low',
                    from_='Sender phone number',
                    to='receiver phone number '
                )

elif numList[i] > 130:
        message = client.messages \
            .create(
                body='This is an emergency, this persons heart rate is too high',
                from_='Sender phone number',
                to='+receiver phone number'
                )
     
else:
    print("Heart rate is normal")


        
    