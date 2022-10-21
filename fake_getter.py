from datetime import datetime
import redis
import time

import msgpack

FPS = 5
RATE = 1 / FPS
KEY = 'NJ'

start = datetime.now()
nj_redis = redis.Redis(host='localhost', port=6379, db=0)
msgs = []
for i in range(1000):
    time.sleep(RATE)
    payload = nj_redis.get(KEY)
    payload = msgpack.unpackb(payload, raw=False)
    msgs.append(payload)
    print(msgs[-1])
print(f'Break: # msg {len(msgs)} - elapsed: {(datetime.now() - start).total_seconds()} [s]')