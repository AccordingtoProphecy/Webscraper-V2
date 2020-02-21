import tkinter as tk
from twilio.rest import Client

root= tk.Tk()
w = 600
h = 400

canvas1 = tk.Canvas(root, width = w, height = h)
canvas1.pack()

Acount_Entry = tk.Entry (root) 
Auth_Entry = tk.Entry (root) 
To_Entry = tk.Entry (root) 
From_Entry = tk.Entry (root) 

canvas1.create_window(w/3*2, 90, window = Acount_Entry)
canvas1.create_window(w/3*2, 120, window = Auth_Entry)
canvas1.create_window(w/3*2, 150, window = To_Entry)
canvas1.create_window(w/3*2, 180, window = From_Entry)


Acount_Text = tk.Label(root, text = "Acount SID Here:")
Auth_Text = tk.Label(root, text = "Authorization Token Here:")
To_Text = tk.Label(root, text = "The Number Which You Want to Send It to:")
From_Text = tk.Label(root, text = "The Twilio Account Trial Number:")

canvas1.create_window(w/3, 90, window = Acount_Text)
canvas1.create_window(w/3, 120, window = Auth_Text)
canvas1.create_window(w/3, 150, window = To_Text)
canvas1.create_window(w/3, 180, window = From_Text)


def SendText ():  
	account_sid = Acount_Entry.get()
	auth_token = Auth_Entry.get()
	to_num = To_Entry.get()
	from_num = From_Entry.get()
	
	client = Client(account_sid, auth_token)

	message = client.messages.create(
		to = to_num,
		from_= from_num,
		body = "What up nerd")
	print (message.sid)
    
SendText = tk.Button(text = "Send Text", command = SendText)
canvas1.create_window(w/2, h/4*3, window = SendText)

root.mainloop()