from datetime import datetime
from dateutil import tz

"""
return a string converted to localTime in '%Y-%m-%d %H:%M:%S' format. 
"""
def convert_to_local_time(utc, isString = False):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    if isString:
        utc = datetime.strptime(utc, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return central.strftime('%Y-%m-%d %H:%M:%S')


def convert_to_timestring(string):
    ts = string.replace(" AEST", "")
    ts = ts.replace(" AEDT", "")
    ts =  datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
    return ts.strftime('%Y-%m-%d %H:%M:%S')


print(convert_to_timestring("2020-02-07 08:27:21 AEDT"))