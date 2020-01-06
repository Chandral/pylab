from datetime import datetime, timedelta
from pytz import timezone

TIMESTAMP_PREFIX_FORMAT = "%Y-%m-%d, %H:%M:%S"

ts = int("1571897721")
utc = datetime.utcfromtimestamp(ts)
print(utc)
print(utc + timedelta(hours=6, minutes=30))
print(utc.astimezone(timezone("Asia/Rangoon")))

def unix_to_rangoon_tz(unix_stamp):
    str_to_int = int