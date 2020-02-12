from time import sleep
import os

# this is assuming there is a newfile, therefore this should be used after a scrape.
# there contains error handling for missing or empty oldfile (in which it runs the scrape

def magic():

    # error handling ^_^

    try:
        open("old.dat", "r")
    except:
        open("old.dat", "x")
        print("get here")
    if os.stat("old.dat").st_size == 0:
        open("old.dat", "w")
        print("get here, empty")
        
    open("old.dat", "r").close()
    
    # set variables
    
    oldfile = open("old.dat", "r").read()
    newfile = open("new.dat", "r").read()
    
    # compare and set new files
    
    if oldfile != newfile:
        print("something has changed!")
        print("imagine that the text is now being sent")
        
        open("old.dat", "w").write(str(newfile))
        
    # rest and call scraper -- which will loop back to magic
    
    open("old.dat", "r").close()
    open("new.dat", "r").close()
    
    sleep(30)
    

magic()