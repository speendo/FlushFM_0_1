from django.shortcuts import render
from mpd import MPDClient

import urllib.request, urllib.parse
    
# mpd instance variable
client = MPDClient()

client.timeout = 10
client.connect("localhost", 6600)

def index(request):
    print("Index loaded")
    return render(request, 'mpd_client/index.html',)
    
def play(request):
    print("button pressed")
    uri = request.POST['uri']
    if 'play' in request.POST:
        print("Play-button pressed")
        start_replay(get_uri(uri))
    else:
        print("Stop-button pressed")
        stop_repay()
    return render(request, 'mpd_client/index.html', {'uri': uri})

def get_uri(uri):
    print(uri)
    if uri.endswith(".m3u"):
                
        file = urllib.request.urlopen(uri)
        for line in file:
            line = line.decode(encoding='utf8')
            print(line)
            if line.startswith('http'):
                word = line.strip()
                print("Word: " + word)
                print("Ok, returning " + word)
                return word
    else:
        return uri
    

def start_replay(uri):
    client.clear()
    print("Sending \"" + uri + "\" to the client.")
    client.add(uri)
    client.play()


def stop_repay():
    client.stop()