import osascript as os

def setVolume(vol):
    script = "set volume output volume " + str(vol)
    os.osascript(script)

volume = input("Set volume: ")
setVolume(volume)