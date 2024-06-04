#!/bin/bash
# this script will start the scripts that watch for incoming images, move the images to the cycle folder, and show the images with fbi

sudo -u root screen -S watchIncoming -dm bash -c 'lib/watch-incoming-move.sh'
sudo -u root screen -S showMoved -dm bash -c 'lib/watch-move-show.sh'
echo "success: screens started for cycling through photos"
