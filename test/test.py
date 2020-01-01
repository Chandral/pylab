import multiprocessing
import time
import tarfile
import os.path


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


backup_process = multiprocessing.Process(target=make_tarfile, args=("server", "/home/chandral/MyGithub/pylab/test/server.log"))
counter = 0
while True:
    if counter == 5:
        backup_process.start()
    print(counter)
    time.sleep(1)
    counter += 1
