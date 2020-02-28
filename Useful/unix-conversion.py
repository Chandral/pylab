from datetime import datetime as dt
from datetime import timezone

dt_object = dt.now()
dt_unix = dt_object.replace(tzinfo=dt.timezone.utc).timestamp()
dt_unix2 = dt_object.replace(tzinfo=timezone("Asia/Rangoon")).timestamp()
print(dt_object)
print(dt_object.timestamp())
print(dt_unix)
print(dt_unix2)