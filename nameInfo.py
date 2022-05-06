import io
from msilib.schema import RemoveFile
import eel
import sys
import socket
from importlib_metadata import os
import pyfiglet
import requests
from gtts import gTTS  
from playsound import playsound
import requests
import webbrowser 
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.chrome.options import Options
from sqlalchemy import false, true

import re


R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

language = 'en'
eel.init('web')

@eel.expose
def Nameinfo(name):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }   
    try:
        options=Options()
        options.headless=True
      

        driver = webdriver.Chrome('C:/Users/hanov/Desktop/Updated  Project/OSINT/web/chromedriver.exe',options=options)
        #driver = webdriver.Chrome('C:\\Users\\ADMIN\\Downloads\\Updated Hanu Project (1)\\Updated Hanu Project\\OSINT\\chromedriver.exe',options=options)
        url="https://www.google.com/search?q="+name
        #response=requests.get(url,headers=headers)
        socialmedia=["instagram","facebook","twitter","linkedin","github","scholar","hackerearth","hackerrank","hackerone","tiktok","youtube","books","researchgate","publons","orcid","maps"]

        outtext = " Information Related to "+name
        driver.get(url)
        atags = driver.find_elements_by_class_name("g")
        c=0
        links = []
        #print(atags)
        anchors=[]
        for l in atags:
            newanchors = l.find_elements_by_tag_name("a")
            for i in newanchors:
                links.append(i.get_attribute('href'))

        #
        finallinks=[]
        check = false
        for i in socialmedia:
            sm=str(i)
            #print(sm)
            for j in links:
                if sm in str(j):
                    c=c+1
                    if len(finallinks)>0:
                        for k in finallinks:
                            if sm in str(k):
                                check = true
                    if check is false:
                        finallinks.append(j)
                        outtext=outtext+"[+]"+j+"\n" 
                    else:
                        check = false
                        
        print(finallinks)
        for i in finallinks:
            webbrowser.open(i)
            print(i)

        outtext=outtext+"\n"+ "[-] Checking for any pdf documents associated with this name ....."
        print(R+"[-] Checking for any pdf documents associated with this name .....")
        url="https://www.google.com/search?q=%22"+name+"%22+filetype%3Apdf&oq=%22"+name+"%22+filetype%3Apdf"
        #response=requests.get(url,headers=headers)
        driver.get(url)
        atags = driver.find_elements_by_class_name("g")
        c=0
        links = []
        #print(atags)
        anchors=[]
        for l in atags:
            newanchors = l.find_elements_by_tag_name("a")
            for i in newanchors:
                c=c+1
                links.append(i.get_attribute('href'))
                outtext=outtext+"[+]"+str(i.get_attribute('href'))+"\n" 


        if c == 0:   
    
            text="No Info about this person"
            aud=gTTS(text=text,lang=language,slow=False)
            aud.save("Invalid7.mp3")
            playsound("Invalid7.mp3")     
            os.remove("Invalid7.mp3")         
            outtext = "No Info about this person"  
        else:
            text="Person Found"
            aud=gTTS(text=text,lang=language,slow=False)
            aud.save("valid7.mp3")
            playsound("valid7.mp3")
            os.remove("valid7.mp3") 
          
                   
    except Exception as e:
        print(e)
    return outtext
        
   
def main():
    eel.start('nameinfo.html', size=(1000, 600))    