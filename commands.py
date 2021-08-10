import osascript as os

def setVolume(vol):
    script = "set volume output volume " + str(vol)
    os.osascript(script)

def setBrightness(bright):
    script = "set brightness " + str(bright)
    os.osascript(script)

# testing
# volume = input("Set volume: ")
# setVolume(volume)