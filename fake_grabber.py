from datetime import datetime
import json
import string
import random
import redis
import time

FPS = 10
RATE = 1 / FPS
KEY = 'NJ'

grabber_redis = redis.Redis(host='localhost', port=6379, db=0)

ascii_letters = string.ascii_letters
N = len(ascii_letters)

start = datetime.now()
for i in range(1000):
    time.sleep(RATE)
    idx = random.randint(0, N-1)
    _d = ascii_letters[idx:]
    payload = {'d1': _d, 'd2': _d, 'd3': _d}
    grabber_redis.set(KEY, json.dumps(payload))
print(f'GRABBER DONE - elapsed: {(datetime.now() - start).total_seconds()} [s]')
