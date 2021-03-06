import tkinter as tk
from twilio.rest import Client
import os
import time as slp
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from datetime import time
from datetime import timedelta
from datetime import datetime
from time import gmtime, strftime
import requests


# set width and height of default window

root = tk.Tk()
w = 800
h = 400

# initialize scraper variables

oldscrape = 0
newscrape = 0
rng = ""

# draw entry and labels

canvas1 = tk.Canvas(root, width=w, height=h)
canvas1.pack()

Account_Entry = tk.Entry(root)
Auth_Entry = tk.Entry(root)
To_Entry = tk.Entry(root)
From_Entry = tk.Entry(root)
Check_Entry = tk.Entry(root)

canvas1.create_window(w/3*2, 90, window=Account_Entry)
canvas1.create_window(w/3*2, 120, window=Auth_Entry)
canvas1.create_window(w/3*2, 150, window=To_Entry)
canvas1.create_window(w/3*2, 180, window=From_Entry)
canvas1.create_window(w/3*2, 210, window=Check_Entry)


Account_Text = tk.Label(root, text="Account SID Here:")
Auth_Text = tk.Label(root, text="Authorization Token Here:")
To_Text = tk.Label(root, text="The Number Which You Want to Send It to:")
From_Text = tk.Label(root, text="The Twilio Account Trial Number:")
Check_Text = tk.Label(root, text="Scrape speed:")
Running = tk.Label(root, text=rng)

canvas1.create_window(w/3, 90, window=Account_Text)
canvas1.create_window(w/3, 120, window=Auth_Text)
canvas1.create_window(w/3, 150, window=To_Text)
canvas1.create_window(w/3, 180, window=From_Text)
canvas1.create_window(w/3, 210, window=Check_Text)
canvas1.create_window(w/2, 260, window=Running)

# def statements


def SendText():
    global newscrape
    account_sid = Account_Entry.get()
    auth_token = Auth_Entry.get()
    to_num = To_Entry.get()
    from_num = From_Entry.get()

    client = Client(account_sid, auth_token)  # verify client

# send text

    message = client.messages.create(
        to=to_num,
        from_=from_num,
        body=newscrape)
    print(message.sid)


def Compare():
    global oldscrape
    global newscrape
    today = date.today()
    day = today.weekday()
    hour = (datetime.time(datetime.now())).hour
    if day == 0 or day == 2 or day == 4:
        time = datetime.now()
        while(hour == 23 or hour == 12):
            Scrape()
            if oldscrape != newscrape:
                SendText()
                oldscrape = newscrape
            print(oldscrape)
            slp.sleep(int(Check_Entry.get()))


def Scrape():
    global newscrape

    page = requests.get("https://xkcd.com/")
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("meta", property="og:title")
    newscrape = title["content"]


TextButton = tk.Button(text="Send Text", command=Compare)
canvas1.create_window(w/2, h/4*3, window=TextButton)

root.mainloop()
