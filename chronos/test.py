from datetime import date, datetime, timedelta

last_timestamp = None
LOG_FILE_PREFIX_FORMAT = "%Y_%m_%d_"
LOG_LINE_PREFIX_FORMAT = "%Y-%m-%d, %H:%M:%S"


def write_to_file(file_prefix, log_timestamp, label, msg, last_timestamp):
    log_file = open("{}server.log".format(file_prefix), "a")
    log_timestamp = "{} | ".format(log_timestamp.strftime(LOG_LINE_PREFIX_FORMAT))
    log_msg = log_timestamp + label + ' | ' + msg
    log_file.write(log_msg + "\n")
    log_file.close()
    last_timestamp = log_timestamp
    print(log_msg)


def log(label, msg):
    global last_timestamp  # DO NOT remove this reference to the global variable 'last_timestamp' created above
    current_timestamp = datetime.now()

    if last_timestamp:
        if (current_timestamp - last_timestamp).days == 0:
            log_file_prefix = current_timestamp.strftime(LOG_FILE_PREFIX_FORMAT)
            write_to_file(log_file_prefix, current_timestamp, label, msg)
            last_timestamp = current_timestamp
        else:
            log_file_prefix = current_timestamp.strftime(LOG_FILE_PREFIX_FORMAT)
    else:
        log_file_prefix = current_timestamp.strftime(LOG_FILE_PREFIX_FORMAT)
        write_to_file(log_file_prefix, current_timestamp, label, msg)
        last_timestamp = current_timestamp

