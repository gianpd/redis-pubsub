from datetime import datetime
import redis
import time

FPS = 5
RATE = 1 / FPS
KEY = 'NJ'

start = datetime.now()
nj_redis = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
msgs = []
for i in range(1000):
    time.sleep(RATE)
    msgs.append(nj_redis.get(KEY))
    print(msgs[-1])
print(f'Break: # msg {len(msgs)} - elapsed: {(datetime.now() - start).total_seconds()} [s]')