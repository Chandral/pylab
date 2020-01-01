import datetime
import tarfile
import os.path


LOG = open("Logs/server.log", "a")


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def enter_log(label, msg):
    timestamp = "{} | ".format(datetime.datetime.now().strftime("%Y/%m/%d, %H:%M:%S"))
    log_msg = timestamp + label + ' | ' + msg
    LOG.write(log_msg + "\n")
    print(log_msg)
