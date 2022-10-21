"""
{
"data": <bytes> #Byte array RGB ordinato per righe, colonne, canali (Height, Width, 3),
"timestamp": <INT>, # timestamp in nanosecondi del momento di acquisizione del frame
"size": {
"width": <INT>, # numero colonne
"height": <INT> # numero righe
},
"position": { # dati da ultima lettura del GPS, in generale antecedente il momento di acquisizione del frame
	"timestamp": <INT>, # timestamp in nanosecondi ultima lettura del GPS
            "longitude": <FLOAT>,
            "latitude": <FLOAT>,
            "altitude": <FLOAT>,
            "track": <FLOAT>, # angolo rispetto a Nord magnetico
            	"speed": <FLOAT>, # velocità in m/s
"eph": <FLOAT>, # stima dell’errore di posizionamento orizzontale in metri
"eps": <FLOAT>, # stima dell’errore di velocità orizzontale in metri/s
"epd": <FLOAT> # stima dell’errore di track in gradi

},
"exposure": {
	"shutter_speed": <INT>, # Velocità shutter in µs
	"gain": <FLOAT>, # Guadagno in db, o ISO se troviamo conversione
"aperture": <FLOAT>, # Apertura iride
"flocal_length": <FLOAT> # focale della lente
}
}

"""

from datetime import datetime
# import json
from pathlib import Path
import string
import random
import redis
import time

import cv2

import msgpack

FPS = 10
RATE = 1 / FPS
KEY = 'NJ'

# read_img = lambda x: cv2.cvtColor(cv2.imread(x), cv2.COLOR_BGR2RGB)
# IMG = read_img('c56d7c9f-image_2022-10-12_14-52-25.807501.jpg')
# print(f'READ IMG: {IMG}')

IMG_BYTES = Path('c56d7c9f-image_2022-10-12_14-52-25.807501.jpg').read_bytes()
# print(f'IMG BYTES: {len(IMG_BYTES)}')

grabber_redis = redis.Redis(host='localhost', port=6379, db=0)

ascii_letters = string.ascii_letters
N = len(ascii_letters)

start = datetime.now()
for i in range(1000):
    time.sleep(RATE)
    idx = random.randint(0, N-1)
    _d = ascii_letters[idx:]
    payload = {'data': IMG_BYTES, 'timestamp': 12345, 'd3': _d}
    payload = msgpack.packb(payload, use_bin_type=True)
    # grabber_redis.set(KEY, json.dumps(payload))
    grabber_redis.set(KEY, payload)
print(f'GRABBER DONE - elapsed: {(datetime.now() - start).total_seconds()} [s]') # 101 [s]
