/*
* (C) 2016 Muthiah Annamalai
* Tests for Open-Tamil Java Libraries
 */
package com.tamil;

import java.util.ArrayList;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class TamilDocumentStatisticsTest extends TestCase {
    
    public TamilDocumentStatisticsTest(String testName) {
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

    /**
     * Test of getTotalWords method, of class TamilDocumentStatistics.
     */
    public void testGetTotalWords() {
        System.out.println("getTotalWords");
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        long expResult = 5L;
        instance.add("hello darkness my old friend");
        long result = instance.getTotalWords();
        assertEquals(expResult, result);
    }

    /**
     * Test of getTotalLetters method, of class TamilDocumentStatistics.
     */
    public void testGetTotalLetters() {
        System.out.println("getTotalLetters");
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        long expResult = 65L;
        instance.add("Days	 நாட்கள்\n" +
"Monday	 திங்கட்கிழமை\n" +
"Tuesday	 செவ்வாய்கிழமை\n" +
"Wednesday	 புதன்கிழமை\n" +
"Thursday வியாழக்கிழமை");
        long result = instance.getTotalLetters();
        assertEquals(expResult, result);
    }

    /**
     * Test of getTotalLines method, of class TamilDocumentStatistics.
     */
    public void testGetTotalLines() {
        System.out.println("getTotalLines");
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        long expResult = 5L;
                instance.add("Days	 நாட்கள்\n" +
"Monday	 திங்கட்கிழமை\n" +
"Tuesday	 செவ்வாய்கிழமை\n" +
"Wednesday	 புதன்கிழமை\n" +
"Thursday வியாழக்கிழமை");
        long result = instance.getTotalLines();
        assertEquals(expResult, result);
        
    }

    /**
     * Test of getWordWithMaxFrequency method, of class TamilDocumentStatistics.
     */
    public void testGetWordWithMaxFrequency() {
        System.out.println("getWordWithMaxFrequency");
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        String expResult = "jar";
        instance.add("jar bar car jar jar");
        String result = instance.getWordWithMaxFrequency();
        assertEquals(expResult, result);
    }
    
    /**
     * Test of getAllWordsByFrequency method, of class TamilDocumentStatistics.
     */
    public void testGetAllWordsByFrequency() {
        System.out.println("getAllWordsByFrequency");
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        String expResult = "1";
        long expResultFreq = 4L;
        instance.add("1 2 3 1 1 2 3 1 4 5 6 7 9 10");
        ArrayList<TamilDocumentStatistics.WordFrequency> result = instance.getAllWordsByFrequency();
        //FIXME:
        assertEquals(expResult, result.get(0).word);
        assertEquals(expResultFreq,result.get(0).frequency);
   }

    /**
     * Test of add method, of class TamilDocumentStatistics.
     */
    public void testReset() {
        System.out.println("add");
        String input = "";
        TamilDocumentStatistics instance = new TamilDocumentStatistics();
        long old_result = instance.add("நேரம்  மணி நிமிடம்").getTotalWords();
        long result = instance.reset().getTotalWords();
        long expResult = 0L;
        assertEquals(3,old_result);
        assertEquals(expResult, result);
    }
    
}
