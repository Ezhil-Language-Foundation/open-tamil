/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */
package com.opentamil.tamil;

import junit.framework.TestCase;
import java.lang.String;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author muthu
 */
public class utf8Test extends TestCase {
    
    public utf8Test(String testName) {
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
    
    public void testGetLetters_EN() {
        List<String> expected = Arrays.asList(new String [] {"f","o","o","l"} );
        StringBuffer actual = new StringBuffer();
        for(String t : utf8.get_letters("AlAnTuRiNg")) {
            actual.append( t );
        }
        
        TestCase.assertEquals("AlAnTuRiNg",actual.toString());
        TestCase.assertEquals(utf8.get_letters("fool"),expected);
    }
    
    public void testSizes() {
        TestCase.assertEquals(utf8.tamil_len(),323);
        TestCase.assertEquals(utf8.uyir_len(),12);
        TestCase.assertEquals(utf8.mei_len(),18);
        TestCase.assertEquals(utf8.agaram_len(),18);
        TestCase.assertEquals(utf8.accent_len(),13);
        TestCase.assertEquals(utf8.ayudha_len(),1);
    }
}
