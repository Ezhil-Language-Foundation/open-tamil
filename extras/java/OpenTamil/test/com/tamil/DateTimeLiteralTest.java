/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tamil;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.TimeZone;
import junit.framework.TestCase;

/**
 * @author muthu
 */
public class DateTimeLiteralTest extends TestCase {
    
    public DateTimeLiteralTest(String testName) {
        super(testName);
    }
    
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }
    
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    public void testGetUtteranceDate() throws Exception {
        System.out.println("getUtteranceDate");
        byte day_of_week = 1;
        byte day = 20;
        byte month = 0;
        int year = 2016;
        //[நாள் ஜனவரி மாதம் ஒன்று வாரம் திங்கள் கிழமை பூஜ்ஜியம் தேதி பூஜ்ஜியம் ஆம் வருடம்]
        String expResult ="நாள் ஜனவரி மாதம் மூன்று ஆம் வாரம் செவ்வாய் கிழமை இருபது தேதி இரண்டு ஆயிரத்தி பதினாறு ஆம் வருடம்"; 
//"நாள் ஜனவரி மாதம் மூன்று ஆம் வாரம் செவ்வாய் கிழமை இரண்டு தேதி இரண்டு ஆயிரத்தி பதினாறு ஆம் வருடம்";
        String result = DateTimeLiteral.getUtteranceDate(day_of_week, day, month, year);
        assertEquals(expResult, result);
        //
        // TODO review the generated test code and remove the default call to fail.
    }
   
    public void testGetLocalDate() throws Exception {
        String expectedStr = "நாள் மார்ச் மாதம் நான்கு ஆம் வாரம் சனி கிழமை இருபத்தி ஆறு தேதி இரண்டு ஆயிரத்தி பதினாறு ஆம் வருடம்";
        assertTrue(DateTimeLiteral.getLocalDate().length() > 0);
    }
    
   public void testGetLocalTime() throws Exception {
       // இப்பொழுது இரவு நேரம் பத்து மணி ஐம்பத்தி ஏழு நிமிடம் முப்பத்தி ஒன்பது விநாடிகள்
       assertTrue(DateTimeLiteral.getLocalTime().length() > 0);
       return;
    }
    
    public void testAnyTime() throws Exception {
       TimeZone tz_est = java.util.TimeZone.getTimeZone("EST");
       
       Date date = new Date();   // given date
       Calendar calendar = GregorianCalendar.getInstance(); // creates a new calendar instance
       calendar.setTime(date);   // assigns today/now
       calendar.setTimeZone(tz_est); //set EST
       
       byte hr = (byte) calendar.get(Calendar.HOUR_OF_DAY); // 24h
       byte min = (byte) calendar.get(Calendar.MINUTE);//minute
       byte sec = (byte) calendar.get(Calendar.SECOND);
       
       assertTrue(DateTimeLiteral.getUtteranceTime(hr,min,sec).length() > 0);
       
       return;
    }
    
    public void testGetUtteranceTime() throws Exception {
        System.out.println("getUtteranceTime");
        byte hour = 5;
        byte min = 55;
        byte sec = 59;
        String expResult = "இப்பொழுது அதிகாலை நேரம் ஐந்து மணி ஐம்பத்தி ஐந்து நிமிடம் ஐம்பத்தி ஒன்பது விநாடிகள்";
        String result = DateTimeLiteral.getUtteranceTime(hour, min, sec);
        assertEquals(expResult, result);
        //" நள்ளிரவு நேரம்"
        expResult = "இப்பொழுது நள்ளிரவு நேரம்";
        hour = 0; min = 0; sec = 0;
        assertEquals(expResult,DateTimeLiteral.getUtteranceTime(hour,min,sec));
        // TODO review the generated test code and remove the default call to fail.
    }

    public void testGetMonth() {
        System.out.println("getMonth");
        byte month = 12;
        String expResult = "ஜனவரி";
        String result = DateTimeLiteral.getMonth(month);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
    }

    public void testGetDayOfWeek() {
        System.out.println("getDayOfWeek");
        byte day = 0;
        String expResult = "திங்கள்";
        String result = DateTimeLiteral.getDayOfWeek(day);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
    }

    public void testGetPozhuthu() {
        System.out.println("getPozhuthu");
        byte hourofday = 12;
        String expResult = "மத்தியானம்";
        for(byte i = 0; i < 25; i++){
            DateTimeLiteral.getPozhuthu(i);
        }
        String result = DateTimeLiteral.getPozhuthu(hourofday);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
    }
    
}
