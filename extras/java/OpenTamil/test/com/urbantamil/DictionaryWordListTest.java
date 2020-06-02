/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.urbantamil;

import java.io.File;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class DictionaryWordListTest extends TestCase {
    
    public DictionaryWordListTest(String testName) {
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

    public void testLoad() throws Exception {
        System.out.println("load");
        String workingDir = System.getProperty("user.dir");
        String path = workingDir+File.separator+"test\\com\\urbantamil\\dummy_word_list.txt";
        File fileObj = new File(path);
        DictionaryWordList instance = new DictionaryWordList(fileObj);
        long expResult = 16L;
        long result = instance.load();
        assertEquals(expResult, result);
   } 
}
