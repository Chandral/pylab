import os
import glob
import tarfile
from datetime import datetime
from pathlib import Path

logs_directory_path = os.getcwd() + '/Logs Backup'
Path(logs_directory_path).mkdir(parents=True, exist_ok=True)
base_path = os.path.join(os.getcwd(), "Logs")
print(base_path)
file_paths = glob.glob(base_path + "/*.log")
file_names = [path.split("/")[-1] for path in file_paths]
print(file_paths)


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


current_timestamp = datetime.now()
todays_file = current_timestamp.strftime("%Y_%m_%d_") + "server.log"
if todays_file in file_names:
    file_names.remove(todays_file)
for file in file_names:
    print(file)
    make_tarfile(file[:-4], base_path)
