from datetime import datetime
import pytz
a='Asia/Kolkata'
tz=pytz.timezone(a)
b=datetime.now(tz)
print(b)