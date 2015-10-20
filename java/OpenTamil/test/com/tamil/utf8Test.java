/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */
package com.tamil;

import junit.framework.TestCase;

import java.util.Arrays;
import java.util.List;
import java.util.HashMap;

import com.tamil.utf8;


/**
 *
 * @author Muthu Annamalai
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
    
    public void testGetLength() {
        String inputWord = "எழில்",inputWord2 = "கட்டளை";
        
        HashMap<String,Object> actual = utf8.get_length(inputWord);
        TestCase.assertEquals((int)actual.get("length"), 3);
        
        actual = utf8.get_length(inputWord2);
        TestCase.assertEquals((int)actual.get("length"), 4);
        
        List<String> expected = Arrays.asList(new String [] {"மெ","ன்","பொ","ரு","ள்"} );
        TestCase.assertEquals(utf8.get_length("மென்பொருள்").get("letters"),expected);
    }
    
    public void testGetLetters_TA() {
        String inputWord = "எழில்";
        //List<String> expected = Arrays.asList(new String [] {"எ","ழி","ல்"} );
        StringBuffer actual = new StringBuffer();
        for(String t : utf8.get_letters(inputWord)) {
            actual.append( t );
        }
        
        TestCase.assertEquals(inputWord,actual.toString());
        TestCase.assertEquals(utf8.get_letters("மென்பொருள்").size(),5);        
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
