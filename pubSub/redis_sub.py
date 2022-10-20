import time
import redis 

r = redis.Redis(host='localhost', port=6379, db=0)

p = r.pubsub()
p.subscribe("my-channel-1")

while True:
    message = p.get_message()
    if message:
        print(message)
    time.sleep(0.01)