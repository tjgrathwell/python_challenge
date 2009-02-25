# CALENDAR

from calendar import *
for i in range(1000,2000):
    if isleap(i):
        if weekday(i,1,1) == 3:
            if str(i)[-1] == '6':
                print i