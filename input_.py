import time
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup4

# Gets page
page = requests.get("https://xkcd.com/")
print(page)

# Getting user input
userNum = str(input("What is your phone number? "))
twilioNum = str(input("What is your Twilio number? "))
twilioAuth = str(input("What is your Twilio authentification token? "))
twilioSID = str(input("What is your Twilio SID? "))

# Actual user
client = Client(twilioSID, twilioAuth)