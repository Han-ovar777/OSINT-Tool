import io
import eel
import os 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from halo import Halo
from gtts import gTTS  
from playsound import playsound
from instagramy import InstagramUser

language = 'en'
eel.init('web')


#@eel.expose
# def maincode():
#     mytext = "Welcome to Open Source Intelligence"
#     language = 'en'
#     myobj = gTTS(text=mytext+ lang=language+ slow=False) 
#     myobj.save("welcome.mp3") 
#     playsound("welcome.mp3") 

@eel.expose
def instainfo(username):
    #username=input("Username >> ")
    user=InstagramUser(username)
    outText= "-"*50 + "\n" + " "*15+"User name : "+username  + "\n" + "-"*50  + "\n" + "Full name >> "+user.fullname  + "\n" +"Biography >> "+user.biography  + "\n"  
    verify=user.is_verified
    if(verify == False):
        outText = outText+"Verified status >> Not Verified\n"
        
        ' '
    else:
        outText = outText+"Verified status >> Verified\n"
        ' '
    account=user.is_private
    if(account == False):
        outText = outText+"Account status >> Public account\n"
        ' '
    else:
        outText = outText+"Account status >> Private account\n"
        ' '
    if(user.website != None):
        outText = outText+"URL >> "+user.website +"\n"
        text="Person Found"
        aud=gTTS(text=text,lang=language,slow=False)
        aud.save("valid7.mp3")
        playsound("valid7.mp3")
        os.remove("valid7.mp3")

    userphoto=user.profile_picture_url
    outText = outText+"Profile Picture url >> "+userphoto+"\n"+ "Followers >> "+str(user.number_of_followers)+"\n"+ 'Following >> '+str(user.number_of_followings) +"\n"+ 'Posts posted >> '+str(user.number_of_posts) +"\n" +'Completed....'
    return outText

def main():
    eel.start('instausernamefinder.html', size=(1000, 600))
