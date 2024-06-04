#!/bin/bash
# this script will stop the scripts running in screens that move and show photos

sudo -u root screen -X -S watchIncoming quit
sudo -u root screen -X -S showMoved quit
echo "success: screens stopped"
