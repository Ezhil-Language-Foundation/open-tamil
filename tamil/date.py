# This Python file uses the following encoding: utf-8
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project

from __future__ import print_function
import time
import sys
PYTHON3 = sys.version > '3'

if PYTHON3:
    class long(int):
        pass

class BasicTamilTimeFormat:
    @staticmethod
    def format(year,month,month_day,week_day,hour,minute,second):
        print(DateUtils.tamil_month(month),month)
        print(DateUtils.tamil_weekday(week_day), week_day)
        print(DateUtils.get_hour_prefix(hour),hour)
    
#
# Index Attribute       Values
# 0     tm_year (for example, 1993)
# 1     tm_mon  range [1, 12]
# 2     tm_mday range [1, 31]
# 3     tm_hour range [0, 23]
# 4     tm_min  range [0, 59]
# 5     tm_sec  range [0, 61]; see (2) in strftime() description
# 6     tm_wday range [0, 6], Monday is 0
# 7     tm_yday range [1, 366]
# 8     tm_isdst        0, 1 or -1; see below


# 0-24
class DateUtils:
    YEAR = u"ஆண்டு"
    WEEK = u"வாரம்"
    MONTH = u"மாதம்"
    DAY = u"நாள்"
    DAY_SUFFIX = u"கிழமை"
    MINUTE = u"நிமிடம்"
    HOUR = u"மணி"
    TIME = u"நேரம்"
    WEEKDAYS_INDEX = [u"monday",u"tuesday",u"wednesday",u"thursday",u"friday",u"saturday",u"sunday"]
    WEEKDAYS = {u"monday" : u"திங்கள்",
                u"tuesday" : u"செவ்வாய்",
                u"wednesday" : u'புதன்',
                u"thursday" : u'வியாழன்',
                u'friday':u'வெள்ளி',
                u'saturday':u'சனிக்கிழமை',
                u'sunday':u'ஞாயிறு',
                }
    MONTHS_INDEX = [None,
                    u"January",
                    u"February",
                    u"March",
                    u"April",
                    u"May",
                    u"June",
                    u"July",
                    u"August",
                    u"September",
                    u"October",
                    u"November",
                    u"December"]
    MONTHS = {u'January':u'ஜனவரி',
              u'February':u'பிப்ரவரி',
              u'March':u'மார்ச்',
              u'April':u'ஏப்ரல்',
              u'May':u'மே',
              u'June':u'ஜூன்',
              u'July':u'ஜூலை',
              u'August':u'ஆகஸ்ட்',
              u'September':u'செப்டம்பர்',
              u'October':u'அக்டோபர்',
              u'November':u'நவம்பர்',
              u'December':u'டிசம்பர்'}

    @staticmethod
    def tamil_weekday(week_day):
        key = DateUtils.WEEKDAYS_INDEX[week_day]
        return DateUtils.WEEKDAYS[key]

    @staticmethod
    def tamil_month(month):
        key = DateUtils.MONTHS_INDEX[month]
        return DateUtils.MONTHS[key]
    
    @staticmethod
    def get_time(local_time=None,fmt=None):
        if not local_time:
            local_time = time.localtime()
        if not fmt:            
            fmt = BasicTamilTimeFormat
        year = local_time.tm_year
        month_day = local_time.tm_mday
        month = local_time.tm_mon
        week_day =local_time.tm_wday
        year_day = local_time.tm_yday            
        hour,minute,second = local_time.tm_hour,local_time.tm_min,local_time.tm_
        
        fmt.format(year,month,month_day,week_day,hour,minute,second)
        return None
    
    @staticmethod
    def get_hour_prefix(hour):
        assert ( hour >= 0 and hour <= 24)# "hour variable should be in [0,24] c
        if (hour <= 3) or (hour  >= 12+11):
            prefix = u"நள்ளிரவு" #u"nalliravu"
        elif hour <= 6:
            prefix = u"அதிகாலை" #u"vidikalai"
        elif hour < 12:
            prefix = u"காலை"#u"kalai"
        elif hour < (12+3):
            prefix = u"மத்தியானம்" #u"mathiyam"
        elif hour < (12+7):
            prefix = u"மாலை" #u"malai"
        elif hour < (12+11):
            prefix = u"இரவு" #u"iravu"
        else:
            assert False
        return prefix    

if __name__ ==  u"__main__":
    for hr in range(0,25):
        print(hr,DateUtils.get_hour_prefix(hr))
    for wkday_EN, wkday_TA in DateUtils.WEEKDAYS.items():
        print(wkday_EN, '->', wkday_TA)
    for wkday_EN, wkday_TA in DateUtils.MONTHS.items():
        print(wkday_EN, '->', wkday_TA)
    DateUtils.get_time(time.localtime())
