from datetime import datetime
from dateutil import tz

"""
return a string converted to localTime string in '%Y-%m-%d %H:%M:%S' format. 
"""
def convert_to_local_time(utc_string):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    # utc = datetime.strptime(utc_string, '%Y-%m-%d %H:%M:%S')
    utc = utc_string.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    return central.strftime('%Y-%m-%d %H:%M:%S')

