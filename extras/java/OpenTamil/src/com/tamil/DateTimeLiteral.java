/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tamil;

/**
 2) Android Clock/Date-Time/Calendar View
        : Athikaalai : 
  Neram : Kalai    : 10 -a- kaal mani 30 vinadigal
  Neram : Pirpagal : 
        : Maalai   : 
        : Iravu    :
        : Nalliravu : 
        : $pozhuthu : 
        
  Naal  : marchu : 3-vathu vaaram : sani kizhamai : 19-aam thethi, 2016
  */
public class DateTimeLiteral {
    public static String getLocalTime() throws Exception {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        byte hr = (byte) now.getHour();
        byte min = (byte) now.getMinute();
        byte sec = (byte) now.getSecond();
        return getUtteranceTime(hr,min,sec);
    }
    
    public static String getLocalDate() throws Exception {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        byte day_of_week = (byte) (now.getDayOfWeek().getValue()-1);
        byte day = (byte) now.getDayOfMonth();
        int year = now.getYear();
        byte month = (byte) (now.getMonthValue() - 1);
        return getUtteranceDate(day_of_week,day,month,year);
    }
    
    // @day_of_week - 0 - 6 (Mon - Sunday)
    // @day - 
    public static String getUtteranceDate(byte day_of_week, byte day, byte month, int year) throws Exception {
         // Naal  : marchu : 3-vathu vaaram : sani kizhamai : 19-aam thethi, 2016
        StringBuffer sb = new StringBuffer();
        sb.append("நாள் ");
        sb.append(getMonth(month)+" மாதம் ");
        int week = 1+day/7;
        sb.append(Numeral.num2tamilstr(week).toString()+" ஆம் வாரம் ");
        sb.append(getDayOfWeek(day_of_week).toString()+" கிழமை ");
        sb.append(Numeral.num2tamilstr(day).toString()+" தேதி ");
        sb.append(Numeral.num2tamilstr(year).toString()+" ஆம் வருடம்");
        return sb.toString();
    }
    public static String getUtteranceTime(byte hour, byte min, byte sec) throws Exception {
       //   Neram : Kalai    : 10 -a- kaal mani 30 vinadigal
       StringBuffer sb = new StringBuffer(); 
       String pozhuthu = getPozhuthu(hour);
       if (hour > 12) {
           hour = (byte) (hour - 12);
       }
       
       sb.append("இப்பொழுது "+pozhuthu+" நேரம்");
       if ( hour > 0 ) {
        sb.append( " "+Numeral.num2tamilstr(hour).toString() );
        sb.append(" மணி");
       }
       if ( min > 0 ) {
        sb.append( " "+Numeral.num2tamilstr(min).toString() );
        sb.append(" நிமிடம்");
       }
       if ( sec > 0 ) {
           sb.append( " "+Numeral.num2tamilstr(sec).toString() );
           sb.append(" விநாடிகள்"); 
       }
       return sb.toString();
    }
    
    // 0 - 11 | Jan - Dec
    public static String getMonth(byte month) {
        final String [] MONTHS = new String [] { "ஜனவரி",
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
        "டிசம்பர்"};
        
        return MONTHS[month%MONTHS.length];
    }

    // 0 - 6. | Mon - Sun
    public static String getDayOfWeek(byte day) {
        final String [] WEEKDAYS = new String [] {"திங்கள்","செவ்வாய்","புதன்","வியாழன்","வெள்ளி","சனி","ஞாயிறு"};
        return WEEKDAYS[day%WEEKDAYS.length];
    }
    
    // hour of day 0 - 23 - as a pozhuthu string
    public static String getPozhuthu(byte hourofday) {
        int hour = ((int) hourofday)%24;
        String prefix = null;
        if ( (hour <= 3) || (hour  >= (12+11)) ) { 
            prefix = "நள்ளிரவு";
        } else if ( hour <= 6 ) {
            prefix = "அதிகாலை";
        } else if ( hour < 12 ) {
            prefix = "காலை"; //#u"kalai"
        } else if ( hour < (12+3) ) {
            prefix = "மத்தியானம்";// #u"mathiyam"
        } else if ( hour < (12+7) ) {
            prefix = "மாலை";// #u"malai"
        } else if (hour < (12+11)) {
            prefix = "இரவு"; // #u"iravu"
        } else { 
            assert false;
        }
        return prefix;    
    }
    
    /// describe a Gregorian/English calendar date object
    public class DateLiteral {
       private byte m_day, m_month;
       private int m_year;
        public DateLiteral(byte day, byte month, int year) {
            assert year > 0;
            assert month < 13 && month > 0;
            assert day > 0 && day < 32;
            m_day = day;
            m_month = month;
            m_year = year;
        }
        
        public byte getM_day() {
            return m_day;
        }

        public void setM_day(byte m_day) {
            this.m_day = m_day;
        }

        public byte getM_month() {
            return m_month;
        }

        public void setM_month(byte m_month) {
            this.m_month = m_month;
        }

        public int getM_year() {
            return m_year;
        }

        public void setM_year(int m_year) {
            this.m_year = m_year;
        }
    }
    
    ///describe a time object
    public class TimeLiteral {
        private byte m_sec, m_millisec, m_minute, m_hr;

        public byte getM_sec() {
            return m_sec;
        }

        public void setM_sec(byte m_sec) {
            this.m_sec = m_sec;
        }

        public byte getM_millisec() {
            return m_millisec;
        }

        public void setM_millisec(byte m_millisec) {
            this.m_millisec = m_millisec;
        }

        public byte getM_minute() {
            return m_minute;
        }

        public void setM_minute(byte m_minute) {
            this.m_minute = m_minute;
        }

        public byte getM_hr() {
            return m_hr;
        }

        public void setM_hr(byte m_hr) {
            this.m_hr = m_hr;
        }

        public long getM_epoch() {
            return m_epoch;
        }

        public void setM_epoch(long m_epoch) {
            this.m_epoch = m_epoch;
        }
        private long m_epoch;
        public TimeLiteral(byte hr, byte min, byte sec, byte millisec) {
            m_epoch = -1;
            m_sec = sec;
            m_millisec = millisec;
            m_hr = hr;
            m_minute = min;
        }
    }
}
