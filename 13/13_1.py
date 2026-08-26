print("="*40)
print("Q-1")
print("="*40)

import datetime as datetime

now = datetime.datetime.now()

print("Current date & Time: ",now)

print("="*40)
print("Q-2")
print("="*40)

import time

print("Current local time:", time.ctime())

print("Seconds since epoch:", time.time())

print("="*40)
print("Q-3")
print("="*40)

from datetime import datetime

now = datetime.now()

print("Format DD-MM-YYYY :", now.strftime("%d-%m-%Y"))
print("Format MM/DD/YYYY :", now.strftime("%m-%d-%Y"))

print("\n24-hour format (HH:MM:SS): ", now.strftime("%H:%M:%S"))
print("12-hour format (HH:MM:SS AM/PM): ", now.strftime("%I:%M:%S %p"))

print("="*40)
print("Q-4")
print("="*40)

from datetime import datetime, timedelta

date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 8, 25)

difference = date1 - date2

print("Days between dates:", difference.days)

today = datetime.now()
future_date = today + timedelta(days = 7)
print("Current date:", today.date())
print("Date after 7 Days:", future_date.date())

print("="*40)
print("Q-5")
print("="*40)

from datetime import datetime
date_str = "2024-01-01"
parsed_data = datetime.strptime(date_str, "%Y-%m-%Y" if len(date_str.split("-")[2]) == 4 else "%Y-%m-%d")
print("Datetime object:", parsed_data)

custom_str = parsed_data.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted string:", custom_str)

print("="*40)
print("Q-6")
print("="*40)

import time
def sample_fuction():
    return sum(i for i in range(100000))

start_time = time.time()
sample_fuction()
end_time = time.time()

execution_time = end_time - start_time

print(f"Fuction execution time: {execution_time:.6f} seconds")

print("="*40)
print("Q-7")
print("="*40)

from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
print("Current time in UTC:", utc_now.strftime("%Y-%m-%d %H:%M:%S"))

local_now = datetime.now()
print("Current local time:", local_now.strftime("%Y-%m-%d %H:%M:%S"))

print("="*40)
print("Q-8")
print("="*40)

import time

print(" --- Python Stopwatch --- ")
print("Press ENTER to START, ENTER to STOP, and Ctrl+c to EXIT.")

try:
    input("press Enter to start...")
    start_time = time.time()
    print("Stopwatch started...")

    input("press Enter to Stop...")
    end_time = time.time()

    elapesd_time = end_time - start_time
    print(f"Elapsed Time: {elapesd_time:.2f} seconds")
except KeyboardInterrupt:
    print("\nStopwatch stopped early.")

print("="*40)
print("Q-9")
print("="*40)

import time


total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Time remaining breakdown: {hours:02d}:{minutes:02d}:{seconds:02d}")


print("="*40)
print("Q-10")
print("="*40)

import calendar
from datetime import datetime

year = int(input("Enter a year to Check: "))

if calendar.isleap(year):
    print(f"{year} is a leap Year.")
else:
    print(f"{year} is not a leap year.")

print("="*40)
print("Q-11")
print("="*40)

from datetime import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")
parsed_date = datetime.strptime(date_input, "%Y-%m-%d")

day_name = parsed_date.strftime("%A")
print(f"The day of the Week for {date_input} is: {day_name}")

print("="*40)
print("Q-12")
print("="*40)

import time

reminder_msg = input("What should T remind you about? ")
seconds_to_wait = int(input("In how many seconds? "))

print(f"Reminder set for {seconds_to_wait} seconds from  now...")
time.sleep(seconds_to_wait)

print(f"\nREMINDER: {reminder_msg}")