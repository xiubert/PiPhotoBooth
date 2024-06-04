#!/bin/bash
# this script detects when files are moved to DESTDIR and triggers frame buffer interface (fbi) to show the image
DESTDIR=./PhotoBoothCycle

inotifywait -m -e create -e moved_to --format "%f" $DESTDIR \
    | while read FILENAME
        do
	 sleep 0.5
 	 fbi -noverbose -d /dev/fb0 -T 1 -a -t 5 "$DESTDIR"/*.jpg
        done
