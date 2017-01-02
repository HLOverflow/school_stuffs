# check for battery level by polling every timewait seconds.
# warn me when battery level reached threshold level

import os
import Tkinter
import tkMessageBox
import time

# variables
debug=0
threshold = 75
timewait = 60

def handler(msg):
    # hide the Tk window
    window = Tkinter.Tk()
    window.wm_withdraw()
    # display only the messagebox
    tkMessageBox.showinfo("Battery alert", msg)
    
def getBattLvl():
    f = os.popen('powershell -c "$(get-wmiobject win32_battery).estimatedchargeremaining"')
    return int(f.read().strip())

if(debug):
    threshold = getBattLvl()+1
    timewait = 10

battLvl = getBattLvl()
while battLvl < threshold:
    time.sleep(timewait)
    battLvl = getBattLvl()
else:
    handler("Your battery reached %d percent. Please unplug charger." % battLvl)
