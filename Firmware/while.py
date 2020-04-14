import time

start = time.time()

PERIOD_OF_TIME = 300 # 5min

while True:
    #... do something

    if time.time() > start + PERIOD_OF_TIME : break
