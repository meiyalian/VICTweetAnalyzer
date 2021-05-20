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

