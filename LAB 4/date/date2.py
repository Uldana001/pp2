from datetime import datetime, timedelta

current_datetime = datetime.now()

yesterday = current_datetime - timedelta(days=1)

tomorrow = current_datetime - timedelta(days=1)

print("Current date:", current_datetime.date())
print("Yesterday:", yesterday.date())
print("Tomorrow: ", tomorrow.date())
"""
Current date: 2025-03-15
Yesterday: 2025-03-14
Tomorrow:  2025-03-14
"""