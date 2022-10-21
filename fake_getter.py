from datetime import datetime
import redis
import time

import msgpack

import cv2
import numpy as np

FPS = 5
RATE = 1 / FPS
KEY = 'NJ'

start = datetime.now()
nj_redis = redis.Redis(host='localhost', port=6379, db=0)
for i in range(1000):
    time.sleep(RATE)
    payload = nj_redis.get(KEY)
    payload = msgpack.unpackb(payload, raw=False)
    image = np.asarray(bytearray(payload['data']), dtype='uint8')
    payload['data'] = cv2.cvtColor(cv2.imdecode(image, cv2.IMREAD_UNCHANGED), cv2.COLOR_BGR2RGB)
print(f'GETTER DONE - elapsed: {(datetime.now() - start).total_seconds()} [s]') # 231 [s]