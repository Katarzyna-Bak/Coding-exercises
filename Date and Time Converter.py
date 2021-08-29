"""
Computer date and time format consists only of numbers,
for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May
2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and
time from computer format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more
readable format

Examples:
date_time("01.01.2000 00:00") == "1 January 2000
year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September
2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year
18 hours 1 minute"

NB: words "hour" and "minute" are to be used
only when time is 01:mm (1 hour) or hh:01 (1 minute).
In other cases "hours" and "minutes" should be used.

How it is used: To improve the understanding
between computers and humans.

Precondition :
0 < day <= 31
0 < month <= 12
0 < year <= 3000
0 <= hours < 24
0 <= minutes < 60
"""

def date_time(time: str):
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    time = time.split()

    return '{0} {1} {2} year {3} hour{4} {5} minute{6}'.format(int(time[0][:2]), months[int(time[0][3:5])], int(time[0][6:]), int(time[1][:2]), '' if int(time[1][:2]) == 1 else 's', int(time[1][3:]), '' if int(time[1][3:]) == 1 else 's')

print("Tests:")
print(date_time("01.01.2000 00:00"))
print(date_time("09.05.1945 06:30"))
print(date_time("20.11.1990 01:55"))