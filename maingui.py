import eel
import nameInfo
import phoneNo
import emailinfo
import ipinfo
from urlscanner import urlscanner
import instausernamefinder
import urlscanner
import imagerecon
language = 'en'
eel.init('web')

@eel.expose
def nameinfo():
    nameInfo.main()

@eel.expose
def phoneno():
    phoneNo.main()

@eel.expose
def email():
    emailinfo.main()  

@eel.expose
def ip():
    ipinfo.main()

@eel.expose
def url():
    urlscanner.main()

@eel.expose
def instausername():
    instausernamefinder.main()          


@eel.expose
def imagerec():
    imagerecon.main()

eel.start('maingui.html', size=(1050, 615))

