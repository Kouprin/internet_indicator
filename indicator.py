#!/usr/bin/python

from time import sleep, time
from anybar import AnyBar
from http.client import HTTPConnection, HTTP_PORT

ANYBAR_PORT = 1743
QUERIES = 3

status = [None for _ in range(QUERIES)]

def ping():
    tm = None
    try:
        cur = time()
        conn = HTTPConnection(host='google.com', port=HTTP_PORT, timeout=1)
        conn.request("HEAD", "/")
        conn.close()
        tm = (time() - cur) * 1000 # to ms
    except:
        pass
    return tm

id = 0
while True:
    status[id] = ping()
    success = 0
    sum = 0
    for tm in status:
        if tm:
            success += 1
            sum += tm
    if not success:
        AnyBar(port=ANYBAR_PORT).change('red')
    elif success < QUERIES or (sum / success) > 100:
        AnyBar(port=ANYBAR_PORT).change('yellow')
    else:
        AnyBar(port=ANYBAR_PORT).change('green')

    sleep(1)
    id = (id + 1) % QUERIES
