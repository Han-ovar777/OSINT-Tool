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
def number(phonenum):
    #phonenum = input("Enter Mobile Number with country code >> ")
    url = ("http://apilayer.net/api/validate?access_key=72bca5f5ec7113753aa4a8a98149d713&number="+phonenum)
    resp = requests.get(url)
    details = resp.json()
    print()
    
    if details['valid']== True:
            text="Entered Number Exists"
            aud=gTTS(text=text,lang=language,slow=False)
            aud.save("phonevalid.mp3")
            playsound("phonevalid.mp3") 
            os.remove("phonevalid.mp3")             
            # print("Country : "+ details['country_name'])
            # print("Location : "+ details['location'])
            # print("Carrier : "+ details['carrier'])   
            out = "Country : "+ details['country_name']+"\nLocation : "+ details['location']+"\nCarrier : "+ details['carrier'] 
    else:
            text="Sorry...Unable to find given Number"
            aud=gTTS(text=text,lang=language,slow=False)
            aud.save("phoneInvalid.mp3")
            playsound("phoneInvalid.mp3")
            os.remove("phonevInalid.mp3")
            
            out = text
    return out

def main():
    eel.start('phoneNo.html', size=(1000, 600))
