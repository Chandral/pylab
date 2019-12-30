import datetime
import time

log = open("socket_server_log.txt", "a")

while True:
    timestamp = datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
    log.write("[{}]".format(timestamp) + "\n")
    print(timestamp)
    time.sleep(1)


