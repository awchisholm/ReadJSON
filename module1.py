import requests
import time
url = 'http://127.0.0.1:5000/'
timings = []
counter = 100
while counter > 0:
    start_the_clock = time.time_ns()
    re = requests.get(url)
    stop_the_clock = time.time_ns()
    time_taken = (stop_the_clock - start_the_clock)/1000000000
    timings.append(time_taken)
    counter -= 1

#print(re.json())
print(timings)