import os
import tarfile
import multiprocessing
from pathlib import Path
from datetime import datetime

last_timestamp = None
LOG_FILE_PREFIX_FORMAT = "%Y_%m_%d_"
LOG_LINE_PREFIX_FORMAT = "%Y-%m-%d, %H:%M:%S"


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


backup_process = multiprocessing.Process(target=make_tarfile, args=())


def log(label, msg):
    global last_timestamp  # DO NOT remove this reference to the global variable 'last_timestamp' created above
    current_timestamp = datetime.now()

    if (current_timestamp - last_timestamp).days != 0:
        backup_process.start()

    file_prefix = current_timestamp.strftime(LOG_FILE_PREFIX_FORMAT)
    log_file = open("{}server.log".format(file_prefix), "a")  # ENSURE the I/O permission remains 'a'
    log_timestamp = "{} | ".format(current_timestamp.strftime(LOG_LINE_PREFIX_FORMAT))
    log_msg = log_timestamp + label + ' | ' + msg
    log_file.write(log_msg + "\n")
    log_file.close()
    last_timestamp = current_timestamp
    print(log_msg)
