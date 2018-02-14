#python

import shlex, subprocess, random

sleep_futures = []

for i in range(0,10):
    sleep_length = random.randint(0, 10)
    args = shlex.split("sleep {}".format(sleep_length))
    future = subprocess.Popen(args, stdout=subprocess.PIPE)
    sleep_futures.append(future)


sleep_results = []
for future in sleep_futures:
    future.wait()
    print("future is ready")
    sleep_results.append(future.communicate())
