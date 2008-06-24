# http://www.pythonchallenge.com/pc/return/uzi.html

# calendar shows January 1??6, with a Monday the 26th visible and 29 days in the upcoming February

import calendar

# test 1006 through 1996
for i in xrange(100):
    year = int('1%02d6' % i)
    if not calendar.isleap(year):
        continue
    if calendar.weekday(year, 1, 26) == 0:
        print year
        
# day after 26th is mozart's birthday