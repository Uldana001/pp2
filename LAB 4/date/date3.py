from datetime import datetime

c_datetime = datetime.now()

c_datetime_new = c_datetime.replace(microsecond=0)

print("Datetime:", c_datetime)
print("Datetime without microseconds:", c_datetime_new)
"""
Datetime: 2025-03-15 01:28:05.612540
Datetime without microseconds: 2025-03-15 01:28:05
"""