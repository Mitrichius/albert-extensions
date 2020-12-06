# -*- coding: utf-8 -*-

"""Unix Time Converter.
Synopsis: <trigger> <filter>"""

from albertv0 import *
from datetime import datetime
from dateutil import parser
import time

__iid__ = "PythonInterface/v0.2"
__prettyname__ = "Unix Time Converter"
__version__ = "1.0"
__trigger__ = "ut "
__author__ = "Dmitry Kolosov"
__dependencies__ = ['python-dateutil']

def handleQuery(query):

    if not query.isTriggered:
        return

    # # avoid rate limiting
    time.sleep(0.1)
    if not query.isValid:
        return

    queryStripped = query.string.strip()

    if queryStripped:
        tsString = queryStripped
        dtString = queryStripped
    else:
        now = datetime.now()
        tsString = now.timestamp()
        dtString = now.strftime("%Y-%m-%d %H:%M:%S")

    results = []
    
    try:
        results.append(parseDateTime(dtString))
    except Exception:
        pass

    try:
        results.append(parseTimestamp(tsString))
    except Exception:
        pass

    return results    

def getDatetimeItem(dt):
    dtString = dt.strftime("%Y-%m-%d %H:%M:%S")
    return Item(id=__prettyname__,
        text=dtString,
        subtext="Date Time",
        completion=dtString,
        actions=[
            ClipAction("Copy", str(dtString))
        ]
    )

def getTimestampItem(ts):
    ts = str(int(ts))
    return Item(id=__prettyname__,
        text=ts,
        subtext="UTC Timestamp",
        completion=ts,
        actions=[
            ClipAction("Copy", ts)
        ]
    )

def parseDateTime(dtString):
    dt = parser.parse(dtString)
    ts = dt.timestamp()
    return getTimestampItem(ts)

def parseTimestamp(ts):
    dt = datetime.fromtimestamp(int(ts))
    return getDatetimeItem(dt)
