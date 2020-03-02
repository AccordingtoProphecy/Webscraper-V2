import tkinter as tk
from twilio.rest import Client
import os
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime
from time import gmtime, strftime


# set width and height of default window

root= tk.Tk()
w = 600
h = 400

# initialize scraper variables

oldscrape = 0
newscrape = 0

# draw entry and labels

canvas1 = tk.Canvas(root, width=w, height=h)
canvas1.pack()

Account_Entry = tk.Entry (root) 
Auth_Entry = tk.Entry (root) 
To_Entry = tk.Entry (root) 
From_Entry = tk.Entry (root) 
Check_Entry = tk.Entry (root) 

canvas1.create_window(w/3*2, 90, window = Account_Entry)
canvas1.create_window(w/3*2, 120, window = Auth_Entry)
canvas1.create_window(w/3*2, 150, window = To_Entry)
canvas1.create_window(w/3*2, 180, window = From_Entry)
canvas1.create_window(w/3*2, 210, window = Check_Entry)


Account_Text = tk.Label(root, text = "Account SID Here:")
Auth_Text = tk.Label(root, text = "Authorization Token Here:")
To_Text = tk.Label(root, text = "The Number Which You Want to Send It to:")
From_Text = tk.Label(root, text = "The Twilio Account Trial Number:")
Check_Text = tk.Label(root, text = "Scrape speed:")

canvas1.create_window(w/3, 90, window = Account_Text)
canvas1.create_window(w/3, 120, window = Auth_Text)
canvas1.create_window(w/3, 150, window = To_Text)
canvas1.create_window(w/3, 180, window = From_Text)
canvas1.create_window(w/3, 210, window = Check_Text)

# def statements

def SendText ():  
	account_sid = Account_Entry.get()
	auth_token = Auth_Entry.get()
	to_num = To_Entry.get()
	from_num = From_Entry.get()
	
	client = Client(account_sid, auth_token) # verify client

    # send text

	message = client.messages.create(
		to = to_num,
		from_= from_num,
		body = "name jeff")
	# print (message.sid)

def Compare():
	global oldscrape
	global newscrape
	day = today.weekday()
	hour = strftime("%H", gmtime())
	if day == 0 or day == 2 or day == 4:
		time = datetime.now()
		while(hour == "23" or hour == "00"):
			if time == datetime.now() + timedelta(seconds = Check_Entry.get()):
				time = datetime.now()
				if oldscrape != newscrape:
					SendText()
					oldscrape = newscrape
    
def Scrape():
    global newscrape
    
    url = urllib.request.urlopen("https://www.xkcd.com/")
    data = url.read()
    soup = BeautifulSoup(data, 'html.parser')
    newscrape = soup
    Compare()


    
TextButton = tk.Button(text = "Send Text", command = Scrape)
canvas1.create_window(w/2, h/4*3, window = TextButton)

root.mainloop()