# import dependencies
from datetime import *

# create object with current date/time values
today = datetime.today()
print('Today Is:', today)


# loop to display each attribute value individually
for attr in \
    ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print(attr,':\t', getattr(today, attr))

# display time using dot notation
print('Time:', today.hour, ':', today.minute, sep='')

# assign formated day and month names to variables
day = today.strftime('%A')
month = today.strftime('%B')
print('Date:', day, month, today.day)