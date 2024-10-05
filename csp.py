#/usr/bin/env python3

import json
import requests
import webbrowser 
from os import system
import time 


data = {}

#loading function which makes the loading animation
def loading():
    system("clear")
    print("Loading") 
    time.sleep(0.3) 
    system("clear") 
    print("Loading.") 
    time.sleep(0.3) 
    system("clear") 
    print("Loading..") 
    time.sleep(0.3) 
    system("clear") 
    print("Loading...")

#this defines the get_reults function 
def get_results(): 
#this is where the user inputs their url
    image = input("enter your url here:")
#clears sytem which gets rid of all previous words 
    system('clear')
    #calls the loading function 
    loading()
    loading()
    loading()
    loading()
    loading()
    loading()
    system("clear")
#this makes the data var global ehich just means i am able to us it anywhere in this program
    global data
    #this is the data var, this is where the api endpoint is stored and where user request json data hence the "requests.get" the way this is done is through the .format which replaces the curly brakckets which is right after "url=" with users image so the ai knows what its looking for
    data = requests.get("https://api.trace.moe/search?url={}"
    .format(image)
  ).json()
# this is the title var which is where i extract the title key from the result list
    title = data ['result'][0]['filename']
#same as the one before 
    similarity =  data ['result'][0]['similarity']
    #these print statements print the title, and the accuracy 
    print("title:"+title)
    print("\n\n")
    print("similarity:",similarity)

#prints nothing to add more space between lines 
print('\n')

#this defines the "vid" function
def vid():
#this extracts data from the results list in this case the first result and the key named "video"
    video = data['result'][0]['video']
    #this opens the webrowser automaticly 
    webbrowser.open(url = video, new=1, autoraise=True)


keepgoing= True 
   #this is the begining of a wile loop 
while keepgoing == True:
    #this tells the loop that is keepgoing = true then to restart the program basically 
    get_results()
    #line break 
    print('\n')
    #this is asking if the user would like to watch the video that their picture comes from
    action = input('would you like to play the video the picture comes from?(y/n)')
    #this is saying that if they yes they run the "vid" function (.lower() automatically makes anything the input lower case)
    if action.lower() == 'y' or action.lower() == 'yes':
        #this prints the vid function
        vid()
        #this is saying if they say no then keepgoing is false and it wont run get results again 
    elif action.lower() == 'n' or action.lower() == 'no':
        keepgoing = False 
    else:
        #this is saying if they type anything else besides yes or no then to print what is in the print statement
        print("you may only asnwer yes or no")
        keepgoing=True 


#this is input asking the user if they would like to run the program again
    programExit = input('would you like to find another anime?(y/n)')
    #this is saying if yes then start the program again
    if programExit.lower() == 'y' or programExit.lower() == 'yes':
        keepgoing=True
        system('clear')
        #this is saying if no then end the program and print "hope to see you soon"
    elif programExit.lower() == 'n' or programExit.lower() == 'no':
        keepgoing = False 
        system ('clear')
        print('hope to see you soon!')
    else:
        #this is saying if they put anything else besides yes or no then to print whats below
        print('you may only answer yes or no')
        keepgoing=True 
    



#https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg
