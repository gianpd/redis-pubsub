import time
import string
import random

import redis

TOPIC = 'my-channel-1'

r = redis.Redis(host='localhost', port=6379, db=0)

ascii_letters = string.ascii_letters

for i in range(100):
    msg = f'A Fake msg {ascii_letters[:random.randint(0, len(ascii_letters))]}'
    r.publish(TOPIC, msg)
    time.sleep(0.0001)