import datetime

LOG = open("Logs/server.log", "a")


def enter_log(label, msg):
    timestamp = "{} | ".format(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
    log_msg = timestamp + label + ' | ' + msg
    LOG.write(log_msg + "\n")
    print(log_msg)
