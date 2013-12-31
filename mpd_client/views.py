from django.shortcuts import render
from mpd import MPDClient
    
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
        start_replay(uri)
    else:
        print("Stop-button pressed")
        stop_repay()
    return render(request, 'mpd_client/index.html', {'uri': uri})

def start_replay(uri):
    print("access start_replay()")
    client.clear()
    client.add(uri)
    client.play()


def stop_repay():
    client.stop()