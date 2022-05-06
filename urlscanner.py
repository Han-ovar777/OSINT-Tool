import eel
import requests
from playsound import playsound
import time
from bs4 import BeautifulSoup
import json
language = 'en'
eel.init('web')

@eel.expose
def urlscanner(inurl):
    #inurl=input("URL >> ")
    text = 'url >> '+inurl +"\n"
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': '9d6e86c348da5d5f2ba847a2eea049dbd6f08595e9099bb98ad1d37663077682', 'url':inurl}
    response = requests.post(url, data=params)
    dictres=response.json()
    scanid=dictres['scan_id']
    text = text +"[+] Checking URl......\n"
    scanurl = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': '9d6e86c348da5d5f2ba847a2eea049dbd6f08595e9099bb98ad1d37663077682', 'resource': scanid }
    response = requests.get(scanurl, params=params)
    dictreport=response.json()
    text= text+'Total Scanning >> '+str(dictreport['total'])+"\n"
    sites=dictreport['scans'] 
    for x in sites:
        text+=x+"\n"
        #print(sites[x])
        for y in sites[x]:
            text=text+"       "+str(y)+" : "+str(sites[x][y])+"\n"    
    return text
def main():
    eel.start('urlscanner.html', size=(1000, 600))

