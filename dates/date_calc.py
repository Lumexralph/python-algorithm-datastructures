from datetime import datetime

"""
I needed to work on a way to get the difference between dates
I came up with the below solution

Input example:
date_1 = Sun 10 May 2015 13:54:36 -0700
date_2 = Sun 10 May 2015 13:54:36 -0000
date_1 = Sat 02 May 2015 19:54:36 +0530
date_2 = Fri 01 May 2015 13:54:36 -0000
"""

date_pattern = "%a %d %b %Y %H:%M:%S %z"

# get the date from the matching pattern
dt_1 = datetime.strptime("Sat 02 May 2015 19:54:36 +0530", date_pattern)

dt_2 = datetime.strptime("Fri 01 May 2015 13:54:36 -0000", date_pattern)

# calculate the difference
time_delta = abs(dt_1 - dt_2)

# it produces a float which is typecasted to an integer
print(int(time_delta.total_seconds()))
