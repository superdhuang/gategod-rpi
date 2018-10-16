#!/bin/sh

# create google service account and generate credential json file
# run this script in /etc/rc.local in background

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/gategod/gategod.cred

while true
do
	/usr/bin/python /home/pi/gategod/sub.py
done
