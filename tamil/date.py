# This Python file uses the following encoding: utf-8
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project

import time
import sys

PYTHON3 = sys.version > "3"
assert PYTHON3, "This module requires Python 3"


class BasicTamilTimeFormat:
    @staticmethod
    def format(year, month, month_day, week_day, hour, minute, second):
        return " ".join(
            [
                DateUtils.tamil_month(month),
                str(week_day),
                DateUtils.tamil_weekday(week_day),
                DateUtils.get_hour_prefix(hour),
                str(minute),
                str(second),
            ]
        )


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

TamilLunarMonths = list(
    zip(
        [
            "சித்திரை",
            "வைகாசி",
            "ஆனி",
            "ஆடி",
            "ஆவணி",
            "புரட்டாசி",
            "ஐப்பசி",
            "கார்த்திகை",
            "மார்கழி",
            "தை",
            "மாசி",
            "பங்குனி",
        ],
        [30, 31, 31, 31, 31, 30, 29, 29, 29, 29, 29, 30],
    )
)

TamilSeasonsMonths = {
    "இளவேனில்": ["சித்திரை", "வைகாசி"],
    "கோடை": ["ஆனி", "ஆடி"],
    "கார்": ["ஆவணி", "புரட்டாசி"],
    "குளிர்": ["ஐப்பசி", "கார்த்திகை"],
    "பனி": ["மார்கழி", "தை", "மாசி", "பங்குனி"],
}


# 0-24
class DateUtils:
    YEAR = "ஆண்டு"
    WEEK = "வாரம்"
    MONTH = "மாதம்"
    DAY = "நாள்"
    DAY_SUFFIX = "கிழமை"
    MINUTE = "நிமிடம்"
    HOUR = "மணி"
    TIME = "நேரம்"
    WEEKDAYS_INDEX = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    WEEKDAYS = {
        "monday": "திங்கள்",
        "tuesday": "செவ்வாய்",
        "wednesday": "புதன்",
        "thursday": "வியாழன்",
        "friday": "வெள்ளி",
        "saturday": "சனிக்கிழமை",
        "sunday": "ஞாயிறு",
    }
    MONTHS_INDEX = [
        None,
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    MONTHS = {
        "January": "ஜனவரி",
        "February": "பிப்ரவரி",
        "March": "மார்ச்",
        "April": "ஏப்ரல்",
        "May": "மே",
        "June": "ஜூன்",
        "July": "ஜூலை",
        "August": "ஆகஸ்ட்",
        "September": "செப்டம்பர்",
        "October": "அக்டோபர்",
        "November": "நவம்பர்",
        "December": "டிசம்பர்",
    }

    @staticmethod
    def tamil_weekday(week_day):
        key = DateUtils.WEEKDAYS_INDEX[week_day]
        return DateUtils.WEEKDAYS[key]

    @staticmethod
    def tamil_month(month):
        key = DateUtils.MONTHS_INDEX[month]
        return DateUtils.MONTHS[key]

    @staticmethod
    def get_time(local_time=None, fmt=None):
        if not local_time:
            local_time = time.localtime()
        if not fmt:
            fmt = BasicTamilTimeFormat
        year = local_time.tm_year
        month_day = local_time.tm_mday
        month = local_time.tm_mon
        week_day = local_time.tm_wday
        year_day = local_time.tm_yday
        hour, minute, second = local_time.tm_hour, local_time.tm_min, local_time.tm_sec
        return fmt.format(year, month, month_day, week_day, hour, minute, second)

    @staticmethod
    def get_hour_prefix(hour):
        assert hour >= 0 and hour <= 24  # "hour variable should be in [0,24] c
        if (hour <= 3) or (hour >= 12 + 11):
            prefix = "நள்ளிரவு"  # u"nalliravu"
        elif hour <= 6:
            prefix = "அதிகாலை"  # u"vidikalai"
        elif hour < 12:
            prefix = "காலை"  # u"kalai"
        elif hour < (12 + 3):
            prefix = "மத்தியானம்"  # u"mathiyam"
        elif hour < (12 + 7):
            prefix = "மாலை"  # u"malai"
        elif hour < (12 + 11):
            prefix = "இரவு"  # u"iravu"
        else:
            assert False
        return prefix


if __name__ == "__main__":
    for hr in range(0, 25):
        print(hr, DateUtils.get_hour_prefix(hr))
    for wkday_EN, wkday_TA in list(DateUtils.WEEKDAYS.items()):
        print(wkday_EN, "->", wkday_TA)
    for wkday_EN, wkday_TA in list(DateUtils.MONTHS.items()):
        print(wkday_EN, "->", wkday_TA)
    print(DateUtils.get_time(time.localtime()))
