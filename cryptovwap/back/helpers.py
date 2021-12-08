from datetime import datetime as dt
from dateutil.parser import isoparse


def dt_unix_datetime(unix):
    return dt.fromtimestamp(unix)


def dt_datetime_unix(date):
    return date.timestamp()


def dt_str_datetime(date):
    return isoparse(date)
