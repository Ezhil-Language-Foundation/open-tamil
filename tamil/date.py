# This Python file uses the following encoding: utf-8
# (C) 2015 Muthiah Annamalai
# This file is part of open-tamil project

import sys
import time
from datetime import datetime as datetime_cpy
from typing import Type

PYTHON3 = sys.version > "3"
assert PYTHON3, "This module requires Python 3"

TA_WEEKDAYS_SHORT = [
    "திங்கள்",
    "செவ்வாய்",
    "புதன்",
    "வியாழன்",
    "வெள்ளி",
    "சனி",
    "ஞாயிறு",
]

TA_WEEKDAYS_FULL = [
    "திங்கட்கிழமை",
    "செவ்வாய்க்கிழமை",
    "புதன்கிழமை",
    "வியாழக்கிழமை",
    "வெள்ளிக்கிழமை",
    "சனிக்கிழமை",
    "ஞாயிற்றுகிழமை",
]

TA_MONTHS = [
    "ஜனவரி",
    "பிப்ரவரி",
    "மார்ச்",
    "ஏப்ரல்",
    "மே",
    "ஜூன்",
    "ஜூலை",
    "ஆகஸ்ட்",
    "செப்டம்பர்",
    "அக்டோபர்",
    "நவம்பர்",
    "டிசம்பர்",
]


class datetime(datetime_cpy):  # noqa
    def __get_ta_str_item(self, code: str) -> str:
        if code == "a":
            return TA_WEEKDAYS_SHORT[self.weekday()]
        if code == "A":
            return TA_WEEKDAYS_FULL[self.weekday()]
        if code == "b" or code == "B":
            return TA_MONTHS[self.month - 1]
        if code == "p":
            if self.hour < 12:
                return "முற்பொழுது"
            else:
                return "பிற்பொழுது"
        return self.strftime(f"%{code}")

    def strftime_ta(self, fmt: str) -> str:
        """An alternate `strftime` implementation that creates a date string with
        Tamil literals.

        Example usage:

        >>> from tamil.date import datetime
        >>> d = datetime(2022, 1, 25, 9, 30)
        >>> d.strftime_ta("%a %d, %b %Y")
        'செவ்வாய் 25, ஜனவரி 2022'
        >>> d.strftime_ta("%A (%d %b %Y) %p %I:%M")
        'செவ்வாய்க்கிழமை (25 ஜனவரி 2022) முற்பொழுது 09:30'

        :param fmt: Format string compatible with `datetime.strftime`
        :return: string representation of the date in Tamil literals and Arabic Numerals
        """
        tokens = []
        i = 0
        while i < len(fmt):
            c = fmt[i]
            if c == "%":
                tokens.append(self.__get_ta_str_item(fmt[i + 1]))
                i += 1
            else:
                tokens.append(c)
            i += 1
        return "".join(tokens)


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
    def tamil_weekday(week_day: int) -> str:
        """Returns name of the weekday in Tamil

        >>> from tamil.date import DateUtils as DU
        >>> DU.tamil_weekday(0)
        'திங்கள்'

        :param week_day: day of the week as an integer from 0..6 with 0 being
            Monday and 6 for Sunday, similar to value of `date.weekday` of the
            Python standard library
        :return: Tamil names of the week days
        """
        key = DateUtils.WEEKDAYS_INDEX[week_day]
        return DateUtils.WEEKDAYS[key]

    @staticmethod
    def tamil_month(month: int) -> str:
        """Returns the name of the months in Tamil

        >>> from tamil.date import DateUtils as DU
        >>> DU.tamil_month(1)
        'ஜனவரி'

        :param month: number of the month from 1..12 with 1 being January & 12
            being December, similar to the value of `date.month` from the standard
            library
        :return: Name of the month in Tamil
        """
        key = DateUtils.MONTHS_INDEX[month]
        return DateUtils.MONTHS[key]

    @staticmethod
    def get_time(
            local_time: time.struct_time = None, fmt: Type[BasicTamilTimeFormat] = None
    ):
        """Get the localtime in Tamil

        :param local_time: OPTIONAL - time.struct_time object to get a specific
            time in Tamil
        :param fmt: OPTIONAL - a class that has a static function named `format`
            similar to the :class:`.BasicTamilTimeFormat`
        :return: current or specified local time in Tamil
        """
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
    def get_hour_prefix(hour: int) -> str:
        """Returns the descriptive prefix based on the value of the hour.

        .. csv-table::
           :header: "Hour Range", "Prefix returned"

           "0-3, 23", நள்ளிரவு
           3-6, அதிகாலை
           7-11, காலை
           12-14, மத்தியானம்
           15-18, மாலை
           19-22, இரவு

        Usage:

        >>> from tamil.date import DateUtils as DU
        >>> DU.get_hour_prefix(4)
        'அதிகாலை'
        >>> DU.get_hour_prefix(20)
        'இரவு'

        :param hour: integer denoting the hour of the day 0..23
        :return: Prefix for the hour in Tamil
        :raises: ValueError if the value of hour is less than 0 or more than 23
        """
        if not 0 <= hour < 24:  # "hour variable should be in [0,24] c
            raise ValueError("Hour should be between 0 to 23 (inclusive)")

        if (hour <= 3) or (hour >= 12 + 11):
            return "நள்ளிரவு"  # u"nalliravu"
        elif hour <= 6:
            return "அதிகாலை"  # u"vidikalai"
        elif hour < 12:
            return "காலை"  # u"kalai"
        elif hour < (12 + 3):
            return "மத்தியானம்"  # u"mathiyam"
        elif hour < (12 + 7):
            return "மாலை"  # u"malai"
        return "இரவு"  # u"iravu"


if __name__ == "__main__":
    for hr in range(0, 25):
        print(hr, DateUtils.get_hour_prefix(hr))
    for wkday_EN, wkday_TA in list(DateUtils.WEEKDAYS.items()):
        print(wkday_EN, "->", wkday_TA)
    for wkday_EN, wkday_TA in list(DateUtils.MONTHS.items()):
        print(wkday_EN, "->", wkday_TA)
    print(DateUtils.get_time(time.localtime()))
