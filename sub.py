import os
import time
from google.cloud import pubsub
import RPi.GPIO
import RPi.GPIO as GPIO
import time

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.HIGH)

# open gate function
def openGate():
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(26, GPIO.HIGH)

subscriber = pubsub.SubscriberClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='gategod-armor',
    topic='yanji',  
)
subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id='gategod-armor',
    sub='sub_name_yanji',
)

# need to create subscription on gcloud
#subscriber.create_subscription(
#    name=subscription_name, topic=topic_name)

def callback(message):
    print(message.data)
    openGate()
    message.ack()

subscription = subscriber.subscribe(subscription_name, callback=callback)

print('Listening for messages on {}'.format(subscription_name))
while True:
    time.sleep(60)

GPIO.cleanup()
