/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.tamil;

import java.util.ArrayList;
import java.util.Arrays;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class TamilStringTest extends TestCase {
    TamilString instance;
    String m_origString;
    public TamilStringTest(String testName) {
        super(testName);
        m_origString = "நிரலாக்க மொழி எழில் ஒரு தமிழ்";
        instance  = new TamilString(m_origString);
    }
    
    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }
    
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    public void testRotateRight() {
        TamilString obj = new TamilString("123");
        obj.rotate_right();
        assertEquals(obj.toString(),"231");
        // fluent x 2
        obj = new TamilString("1234");
        obj.rotate_right().rotate_right();
        assertEquals(obj.toString(),"3412");
    }
    
    /**
     * Test of toString method, of class TamilString.
     */
    public void testToString() {
        System.out.println("toString");
        String expResult = m_origString;
        String result = instance.toString();
        assertEquals(expResult, result);
    }

    /**
     * Test of letterIndexOf method, of class TamilString.
     */
    public void testLetterIndexOf() {
        System.out.println("letterIndexOf");
        TamilString newstr = new TamilString("எ");
        int pos = 0;// 'எ' 
        int expResult = 7-1;
        int result = newstr.letterIndexOf(pos);
        assertEquals(expResult, result);
    }

    /**
     * Test of length method, of class TamilString.
     */
    public void testLength() {
        System.out.println("length");
        int expResult = 19;
        int result = instance.length();
        assertEquals(expResult, result);
    }
    
    public void testArraySort() {
        ArrayList<TamilString> values = new ArrayList<TamilString>();
        for(String ts: m_origString.split(" ") ) {
            values.add( new TamilString(ts) );
        }
        String [] expected = new String [] {"எழில்", "ஒரு", "தமிழ்", "நிரலாக்க", "மொழி" };
        values.sort(TamilString.comparator);
        assertEquals(5,values.size());
        for(int pos=0;pos < expected.length; pos++) {
            String actual = values.get(pos).toString();
            assertEquals( expected[pos], actual );
        }
    }
}
