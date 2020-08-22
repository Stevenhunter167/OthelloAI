import requests
from config import PORTNUMBER
from Global import data

def get(route, data):
    r = requests.get(f'http://127.0.0.1:{PORTNUMBER}' + route, params=data)
    print(r.url)

def log(message):
    # get('/consoleout', data={'message':message})
    data['console'].append(message)

def enqueue(queuename, x, maxcount=10):
    data[queuename].append(x)
    if len(data[queuename]) > maxcount:
        data[queuename].pop(0)