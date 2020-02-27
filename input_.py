import time
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import urllib.request

# Gets page
def getPageContents():
    page = requests.get("https://xkcd.com/")
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("meta", property="og:title")
    return title.get_text()

# Getting user input
userNum = input("What is your phone number? ")
twilioNum = input("What is your Twilio number? ")
twilioAuth = input("What is your Twilio authentification token? ")
twilioSID = input("What is your Twilio SID? ")
interval = input("How long do you want to wait between checks? ")

# Actual user
client = Client(twilioSID, twilioAuth)

getPageContents()