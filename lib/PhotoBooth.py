import subprocess
import RPi.GPIO as GPIO
import time
import glob
import os
import re

# this script listens for a button press (currently set to GPIO pin 11) and upon press calls photo capture
GPIO.setmode(GPIO.BOARD)
#11 is the 6th pin from closest to power, the 5th is ground
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
#so button should be on 5 and 6 counting columnwise with 1 at pin to the left on the power side

# file directory where photos are initially saved
fdir = "./PhotoBoothInput/"
# file directory where photos will be moved for cycling through photos on monitor/display
moveFdir = "./PhotoBoothCycle/"
# this requires running both watch-incoming-move.sh and watch-move-show.sh in a gnu screen session
# these screen sessions are run as root to circumvent /dev/tty permissions issues

# eg (sudo -u root runs as root): sudo -u root screen -S watchIncoming -dm bash -c '/home/pi/PiPhotoBooth/watch-incoming-move.sh'
# and: sudo -u root screen -S showMoved -dm bash -c '/home/pi/PiPhotoBooth/watch-move-show.sh'
# to attach to the screen session (must also run as root, since they were started by root):
# sudo -u root screen -r "session name"
# eg: sudo -u root screen -r watchIncoming
# can kill the screen session upon attaching with "ctrl+c" and "exit" 
# or when detached with: sudo -u root screen -X -S "session name" quit
# eg: sudo -u root screen -X -S watchIncoming quit

# so:
# 
# 1. if cycling through images on display: run the shell scripts for watching incoming images and moving to display directory
# 1.1: sudo -u root screen -S watchIncoming -dm bash -c '/home/pi/PiPhotoBooth/watch-incoming-move.sh'
# 1.2: sudo -u root screen -S showMoved -dm bash -c '/home/pi/PiPhotoBooth/watch-move-show.sh'
# 2: run this script as user pi with python: python ./PhotoBooth.py
# 3. clean up / stop with: 
# 3.1: screen -X -S watchIncoming quit
# 3.2: screen -X -S showMoved quit

#ESC will close fbi, enter and spacebar will advance photos faster
#ctrl+c for exiting the script

timeStamp = time.strftime("%Y%m%d-%H%M%S")

flist = glob.glob(moveFdir + '*.jpg')
# get file number from existing list of files in the moveFdir
try:
 flast = max(flist, key=os.path.getctime)
 print(flast)
 fnum = re.search('(\d{5})_',flast)
 fnum = int(fnum.group(1))
 print(fnum)
 i = fnum
except:
 i = 10000

try:
 while True:

  input_state = GPIO.input(11)

  if input_state == 0:
    i=i-1
    subprocess.run(["/usr/bin/libcamera-jpeg", "-o", f'{fdir}{i:05}_PhotoBooth_{timeStamp}.jpg'])
    print('photo captured')

    time.sleep(0.2)

except KeyboardInterrupt:

 GPIO.cleanup()
