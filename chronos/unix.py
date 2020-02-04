import datetime, time
times = "2020-02-04 16:05:44"
unix_time = 1580832344
dt_obj = datetime.datetime.strptime(times, "%Y-%m-%d %H:%M:%S")
a = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
# print((time.mktime(dt_obj.timetuple())))
# a = (dt_obj.date() - datetime.date(1970, 1, 1))
# # datetime.timedelta(18276)
# a = (dt_obj.date() - datetime.date(1970, 1, 1)).total_seconds()
# print(a)

def convert_to_unix_timestamp(*date_strings):
    """
    Converts a list of strings representing dates to UNIX timestamp and returns those UNIX timestamps as a list.
     The date string is expected to be in DD-MM-YYYY format.
    :param date_strings: List of date strings
    :return: List of UNIX timestamps
    """
    print(date_strings)
    unix_stamps = []
    for date in date_strings:
        date_object = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        unix_stamps.append((date_object.date() - datetime.date(1970, 1, 1)).total_seconds())
    return unix_stamps


print(convert_to_unix_timestamp(a))