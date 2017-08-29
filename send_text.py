from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC912377635cf696326d351b064a3578a8"
# Your Auth Token from twilio.com/console
auth_token  = "31dc4a4187a4f247d47edfae524277a2"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+447514149133", 
    from_="+447481358355",
    body="Ciao pollo, questo e' il primo SMS che genero con un mio programma!"
    )

print(message.sid)
