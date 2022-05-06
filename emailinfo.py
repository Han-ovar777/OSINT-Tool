import io
import os
import eel
import sys
import socket
import pyfiglet
import requests
from gtts import gTTS  
from playsound import playsound
import requests
import webbrowser
from bs4 import BeautifulSoup
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

language = 'en'
eel.init('web')


#@eel.expose
# def maincode():
#     mytext = "Welcome to Open Source Intelligence"
#     language = 'en'
#     myobj = gTTS(text=mytext, lang=language, slow=False) 
#     myobj.save("welcome.mp3") 
#     playsound("welcome.mp3") 

@eel.expose
def emailinfo(email):
    dictemail={}
    #email=input("Email address to check >> ")
    #url="https://app.verify-email.org/api/v1/mFyMW4NCYyyI8mRcK3mIzkIYNu1BnWskMNPabWyOJU007FVH1I/verify/"+email
    #url="http://apilayer.net/api/check?access_key=e676b3991499057e5a22de8a8ee23418&email="+email+"&smtp=1&format=1"
    url = "https://api.reacher.email/v0/check_email/"
    head = {"authorization": "32bc7a6a-5773-11ec-ac52-f5fd03b1cc6d"}
    payload = {"to_email":email}
    response = requests.post(url, json=payload, headers=head)
    #r = response.text
    #r=requests.get(url)
    dictemail=response.json()
    #print("Email     : ",dictemail.get('input'))
    #print("smtp code : ",dictemail.get('smtp_code'))
    stat=dictemail.get('is_reachable')
    language='en'
    
    if(stat != 'invalid'):
        text="Email address found "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid.mp3")
        playsound("valid.mp3")
        os.remove("valid.mp3")
        stats= 'True'
        #print(G+"Status     : "+stats)
        out=G+"Status     : "+stats

    else:
        text="Email address not found "
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("invalid.mp3")
        playsound("invalid.mp3")
        os.remove("invalid.mp3")
        stats= 'False'            
        #print(R+"Status     : "+stats)
        out=R+"Status     : "+stats
    return out
def main():
    eel.start('emailinfo.html', size=(1000, 600))
