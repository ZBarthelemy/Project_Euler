# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 11/14/16

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# This was infinetly easier using libraries =]
from datetime import date
from collections import Counter

counter = Counter()

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1

print counter[6]