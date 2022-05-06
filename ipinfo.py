import requests
import eel
import os
import webbrowser
from gtts import gTTS  
from playsound import playsound

R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

language = 'en'
eel.init('web')

 

@eel.expose
def ipinfo(ip):
    ipinfo={}
    #ip=input("Ip address >> ")
    url="http://ip-api.com/json/"+ip
    r=requests.get(url)
    ipinfo=r.json()

    if ipinfo['status'] == 'success':
        lat=ipinfo['lat']
        lon=ipinfo['lon']        
        text ="Ip location Found "
        mytext = "IP location Found "
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("found.mp3") 
        playsound("found.mp3") 
        os.remove("found.mp3")
        text = text + 'Country     : '+ipinfo['country']+'\nRegion Name : '+ipinfo['regionName']+'\nCity        : '+ipinfo['city']+'Time zone   : '+ipinfo['timezone']+'\nISP         : '+ipinfo['isp']+'\nOpening Location in browser'
        mapurl = "https://maps.google.com/maps?q=%s,+%s" % (lat, lon)
        webbrowser.open(mapurl, new=2) 
        print('')
    else:
        text = "IP location not Found !!"
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False) 
        myobj.save("found.mp3") 
        playsound("found.mp3") 
        os.remove("found.mp3")
        
        print('')

        #out = text
    return text
    
def main():
    eel.start('ipinfo.html', size=(1000, 600))

