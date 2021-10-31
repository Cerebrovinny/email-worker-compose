import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print('Waiting messages ...')

    while True:
        message = json.loads(r.blpop('sender')[1])
        #email sending emulation
        print('Sending the message:', message['subject'])
        sleep(randint(15, 45))
        print('Message', message['subject'], 'sent!')