import os
import tarfile
import multiprocessing
from pathlib import Path
from datetime import datetime

last_timestamp = None


def create_logs_directory():
    Path(os.getcwd() + '/Logs').mkdir(parents=True, exist_ok=True)


def create_backup_directory():
    Path(os.getcwd() + '/Logs Backup').mkdir(parents=True, exist_ok=True)


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def take_backup():
    pass


backup_process = multiprocessing.Process(target=make_tarfile, args=())


def log(label, msg):
    global last_timestamp  # DO NOT remove this reference to the global variable 'last_timestamp' created above
    current_timestamp = datetime.now()

    if (current_timestamp - last_timestamp).days != 0:
        backup_process.start()

    file_prefix = current_timestamp.strftime("%Y_%m_%d_")
    log_file = open("{}server.log".format(file_prefix), "a")  # ENSURE the I/O permission remains 'a'
    log_timestamp = "{} | ".format(current_timestamp.strftime("%Y-%m-%d, %H:%M:%S"))
    log_msg = log_timestamp + label + ' | ' + msg
    log_file.write(log_msg + "\n")
    log_file.close()
    last_timestamp = current_timestamp
    print(log_msg)
