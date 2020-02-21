from time import sleep
import os

oldscrape = 0
newscrape = 1

# this is assuming there is a newfile, therefore this should be used after a scrape.
# there contains error handling for missing or empty oldfile (in which it runs the scrape

def magic():
    global oldscrape
    global newscrape

    if oldscrape != newscrape:
        print("something has changed!")
        print("imagine that the text is now being sent")
        
        oldscrape = newscrape

    sleep(30)
    

magic()