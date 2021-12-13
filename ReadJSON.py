import requests
import time
url = 'http://127.0.0.1:5000/'
start_the_clock = time.time_ns()
re = requests.get(url)
stop_the_clock = time.time_ns()

print(re.json())
print((stop_the_clock - start_the_clock)/1000000000)
