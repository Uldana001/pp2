from datetime import datetime, timedelta

current_datetime = datetime.now()

new_datetime = current_datetime - timedelta(days=5)

new_date = new_datetime.date()

print("Current date:", current_datetime.date())
print("Date five days ago:", new_date)

"""
Current date: 2025-03-15
Date five days ago: 2025-03-10
"""
