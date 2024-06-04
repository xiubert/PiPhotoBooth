#!/bin/bash
mkdir -p PhotoBoothCycle
mkdir -p PhotoBoothInput
lib/startScreens.sh
python lib/PhotoBooth.py
lib/stopScreens.sh

