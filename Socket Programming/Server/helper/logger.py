import os
import glob
import tarfile
import multiprocessing
from pathlib import Path
from datetime import datetime

SUCCESS = "SUCCESS"  # Log label for successful events E.g. Connection successfully established
INFO = "INFO"  # Log label for FYI events E.g. Printing data received from the client
WARNING = "WARNING"  # Log label for events which indicates to a potential problem E.g. Low disk space
ERROR = "ERROR"  # Log label for events which doesn't stop the application but a feature didn't work as expected
CRITICAL = "CRITICAL"  # Log label for events which

LOGS_DIRECTORY_PATH = os.getcwd() + '/Logs'
LOGS_BACKUP_DIRECTORY_PATH = os.getcwd() + '/Logs Backup'
FILE_PREFIX_FORMAT = "%Y_%m_%d_"
TIMESTAMP_PREFIX_FORMAT = "%Y-%m-%d, %H:%M:%S"

last_timestamp = None


def create_logs_directory():
    """
    Creates the directory 'Logs' and 'Logs Backup'.
    :return: None
    """
    Path(LOGS_DIRECTORY_PATH).mkdir(parents=True, exist_ok=True)
    Path(LOGS_BACKUP_DIRECTORY_PATH).mkdir(parents=True, exist_ok=True)


def _make_tarfile(output_filename, source_dir):
    """
    Compresses files as TAR.GZ files
    :param output_filename:
    :param source_dir:
    :return:
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def _take_backup(current_timestamp):
    """
    Takes backup of the log files.
    :param current_timestamp:
    :return: None
    """
    todays_log = current_timestamp.strftime(FILE_PREFIX_FORMAT) + "server.log"
    file_paths = glob.glob(LOGS_DIRECTORY_PATH + "/*.log")
    file_names = [path.split("/")[-1] for path in file_paths]
    if todays_log in file_names:
        file_names.remove(todays_log)
    for file in file_names:
        _make_tarfile(file[:-4], LOGS_DIRECTORY_PATH)


def log(label, msg):
    """
    Function to do log entry. Takes in two parameters label and message
    :param label: A predefined keyword indicating the type of log event
    :param msg: Logging event message
    :return: None
    """
    global last_timestamp  # Variable

    current_timestamp = datetime.now()

    if last_timestamp:
        if (current_timestamp - last_timestamp).days != 0:
            backup_process = multiprocessing.Process(target=_take_backup, args=(current_timestamp,))
            backup_process.start()

    file_prefix = current_timestamp.strftime(FILE_PREFIX_FORMAT)
    log_file = open("Logs/{}server.log".format(file_prefix), "a")  # ENSURE the I/O permission remains 'a'
    log_timestamp = "{}|".format(current_timestamp.strftime(TIMESTAMP_PREFIX_FORMAT))
    log_msg = log_timestamp + label + '|' + msg
    log_file.write(log_msg + "\n")
    log_file.close()
    last_timestamp = current_timestamp
    print(log_msg)
