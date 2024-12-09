import numpy as np
from urllib.request import urlopen
import time

trials = 20
required = 15
delay = 1

results = np.ones(trials)

print("madVR profile blind testing")
print(trials, "trials")

for n in range(trials):
    print("press Enter then block your eyes for a few second(s)")
    input()
    time.sleep(delay)
    test = np.random.randint(2)
    if test == 0:
        urlopen("http://127.0.0.1:5000/?devname=keys&cmd=ctrl(alt(1))&param=mpc-be64")
    else:
        urlopen("http://127.0.0.1:5000/?devname=keys&cmd=ctrl(alt(2))&param=mpc-be64")
    print("Guess which profile this is, 1 or 2:")
    guess = int(input())
    if guess - 1 != test:
        results[n] = 0
    if np.sum(results) < required:
        break

print(results)
        
if np.sum(results) < required:
    print("failed blind test")
else:
    print("passed blind test")

