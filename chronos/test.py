import pytz, time
from datetime import datetime as dt

date_string = "15-01-2020"  # String in DD-MM-YYYY format which will be converted to datetime object
date_object = dt.strptime(date_string, "%d-%m-%Y")  # Datetime object
UTC = pytz.timezone("UTC")  # Declaring UTC timezone
date_object = UTC.localize(date_object)  # Setting timezone of 'date_object' to UTC
print(date_object.strftime("%s"))
expected_unix_timestamp = 1579046400  # Verified this on https://www.unixtimestamp.com/index.php

print("Expected UNIX timestamp based on https://www.unixtimestamp.com/index.php")
print(">>> " + str(expected_unix_timestamp))  # Prints 1579046400
print("Unix timestamp returned")
print(">>> " + str(time.mktime(date_object.timetuple())))  # Prints 1579026600.0

print("~"*200)