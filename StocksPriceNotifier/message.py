from twilio.rest import Client
from tkinter import messagebox


def message(phone, stock, price, alertto):
    # Your Twilio account SID and authentication token
    try:
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        recipient_number = "your_phone_number"
        # Creating a Twilio client
        client = Client(account_sid, auth_token)

        # Sending an SMS message
        if alertto == "BUY":
            message = client.messages.create(
                body='%s has reached %s, you can BUY the stock now.'%(stock, price),
                from_='+15673131164',
                to=f'+91{recipient_number}'
            )
        else:
            message = client.messages.create(   
                body='%s has reached %s, you can SELL the stock now.'%(stock, price),
                from_='+15673131164',
                to=f'+91{recipient_number}'
            )
    except:
        messagebox.showinfo('Incorrect Phoneno.',"Create a account in twilio ")
