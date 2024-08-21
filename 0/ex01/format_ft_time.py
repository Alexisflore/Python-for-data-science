import time as t
import datetime as dt

# Get the current time
now = t.time()

# Get the time in seconds since the epoch
print(f"Seconds since January 1, 1970: {now} or {now:.2e} in scientific notation")

# Get the current time Month Day Year
now = dt.datetime.now()
print(now.strftime("%b %d %Y"))