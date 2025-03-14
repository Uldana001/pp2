from datetime import datetime

date1 = datetime(2025, 2, 15, 16, 29, 8)  
date2 = datetime(2025, 2, 20, 18, 45, 30)  

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()

print(f"The difference between {date2} and {date1} is {difference_in_seconds} seconds.")

# The difference between 2025-02-20 18:45:30 and 2025-02-15 16:29:08 is 440182.0 seconds.