from ssl import Options
import webbrowser
import requests
from gtts import gTTS 
from playsound import playsound
import selenium
from selenium import webdriver
import selenium.webdriver.common.keys
import eel
from selenium.webdriver.chrome.options import Options
from sqlalchemy import false, true
from halo import Halo
import tkinter
from tkinter import filedialog, Tk
import os
import upld
import eel

language = 'en'


@eel.expose

def imagerecon():
    #image=input("Enter the image path : \n")
    
    root = tkinter.Tk()
    #root.withdraw()
    currdir = os.getcwd()
    # #tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    tempfile = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please select Image')
    if tempfile:
        print ("You chose: %s" % tempfile.name)
        image = tempfile.name
    # else:
    #     print("No files selected")

    #image= imagedata.name
    root.withdraw()
    options=Options()
    options.headless=True
    print(image)

    driver = webdriver.Chrome('C:/Users/hanov/Desktop/Updated  Project/OSINT/web/chromedriver.exe',options=options)
    #driver = webdriver.Chrome('C:\\Users\\ADMIN\\Downloads\\Updated Hanu Project (1)\\Updated Hanu Project\\OSINT\\chromedriver.exe',options=options)
    
    try: 
        headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User_Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        url='http://www.google.co.in/searchbyimage/upload'
        secondurl={'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
        response = requests.post(url, files=secondurl,allow_redirects=False)
        fetch=response.headers['Location']
        #print(fetch)
        #req = ChromeDriverManager.get(fetch)
        req=requests.get(fetch,headers=headers)
        socialmedia=["instagram","facebook","twitter","linkedin","github","youtube","pinterest"]
        linklist=[]
        outtext="[+] Scan started......\n"
        outtext=outtext+"Checking whether the image is associated in any social media \n"
        outtext=outtext+"Scanning started in Instagram\n"
        outtext=outtext+"Scanning started in Github\n"
        outtext=outtext+"Scanning started in Facebook\n"
        outtext=outtext+"Scanning started in Twitter\n"
        outtext=outtext+"Scanning started in Linkedin\n"
 
        if(req.status_code == 200):
            driver.get(fetch)

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
                            for i in finallinks:
                                if sm in str(i):
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

            if c == 0:
                outtext="No social Media links associated with this image\n"
                aud=gTTS(text=outtext,lang=language,slow=False)
                aud.save("imageinvalid.mp3")
                playsound("imageinvalid.mp3")
                os.remove("imageinvalid.mp3")
            else:
               text="Image is associated with social media account"
               aud=gTTS(text=text,lang=language,slow=False)
               aud.save("imagevalid.mp3")
               playsound("imagevalid.mp3")
               os.remove("imagevalid.mp3")
               
                
    except Exception as e:
        print(e)
    return outtext


def main():
    eel.start('imagerecon.html', size=(1000, 605))
