import time
import requests
#from bs4 import BeautifulSoup4

# Gets page and prints HTML, entirely for testing purposes at the moment
page = requests.get("https://xkcd.com/")
print(page.text)

# Getting user input
userNum = str(input("What is your phone number? "))
twilioNum = str(input("What is your Twilio number? "))
twilioAuth = str(input("What is your Twilio authentification token? "))