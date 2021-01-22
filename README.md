# gategod-rpi
requirements:
1. raspberry pi OS
2. user: pi
3. pyhon 3.7 (default in raspberry pi OS)

install:
in /home/pi/gategod
1. pip install google-cloud-pubsub
2. pip install RPi.GPIO
3. set gategod.cred in gategod.sh
4. put "sudo -u pi /home/pi/gategod/gategod.sh & " in /etc/rc.local
5. boot direct to CLI, NOT Desktop
