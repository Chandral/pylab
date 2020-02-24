import datetime as dt
from pytz import timezone


def date_to_unix(date_object):
    return date_object.replace(tzinfo=dt.timezone.utc).timestamp()

#
# dt_string = "2020-02-04 16:05:44"
# unix_stamp = 1580832344
# dt_obj = dt.datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
# print(int(date_to_unix(dt_obj)) == unix_stamp)  # Should print True
#
# print("~" * 50)
#
# current_time = dt.datetime.now()
# print(current_time)
# print(int(date_to_unix(current_time)))


dt_object = dt.datetime.now().replace(microsecond=0)
dt_unix = dt_object.replace(tzinfo=dt.timezone.utc).timestamp()
dt_unix2 = dt_object.replace(tzinfo=timezone("Asia/Rangoon")).timestamp()
print(dt_object)
print(dt_object.timestamp())
print(dt_unix)
print(dt_unix2)