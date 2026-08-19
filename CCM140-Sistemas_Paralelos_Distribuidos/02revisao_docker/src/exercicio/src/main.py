import random
from time import sleep

random.seed()

while True:
    print(random.randint(1,10), flush=True)
    sleep(0.5)
