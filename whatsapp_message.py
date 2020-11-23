from twilio.rest import Client

def message_automatic():
    twilio_SID = 'AC0bbb03803f50f0908757b6473a74833a'
    auth_token = 'f09fa44091eabb8c0d56eee8de462921'
    
    WhatsApp = Client(twilio_SID, auth_token)

    contacts_dir = {'Me' : '+916364691230'}

    for key,value in contacts_dir.items():
        print(key,value)
        message = WhatsApp.messages.create(
            body = 'Test message to {}'.format(key),
            from_= 'whatsapp: +14155238886',
            to='whatsapp:+916364691230' 
            )
        print(message.sid)

if __name__ == "__main__":
    message_automatic()




    