#!/bin/bash
# this script watches the WATCHDIR and upon new files, moves to DESTDIR
# when a new file is discovered it will kill the current photo on display (via fbi - frame buffer interface)
WATCHDIR=./PhotoBoothInput/
DESTDIR=./PhotoBoothCycle/

inotifywait -m -e create -e moved_to --format "%f" $WATCHDIR \
    | while read FILENAME
        do
         kill $(pgrep fbi)
         mv "$WATCHDIR/$FILENAME" "$DESTDIR/$FILENAME"
        done
