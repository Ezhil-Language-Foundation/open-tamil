/*
 */
package com.urbantamil;

import com.tamil.TamilString;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class WordJumbleTest extends TestCase {
    
    public WordJumbleTest(String testName) {
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

    public void testShuffle() {
        System.out.println("shuffle");
        WordJumble instance = new WordJumble("INSTANCE");
        boolean expResult = true;
        boolean result = instance.shuffle();
        assertEquals(expResult, result);
        assertFalse("INSTANCE".compareTo( instance.toString() ) == 0 );
    }

    public void testUdpateJumbledWord() {
        System.out.println("udpateJumbledWord");
        TamilString str = new TamilString("1234");
        str.rotate_right().rotate_right();
        WordJumble instance = new WordJumble("1234");
        instance.udpateJumbledWord(str);
        assertEquals(instance.toString(),str.toString());
    }

    public void testSolved() {
        System.out.println("udpateJumbledWord");
        TamilString str = new TamilString("1234");
        str.rotate_right().rotate_right();
        WordJumble instance = new WordJumble(str);
        assertTrue( instance.shuffle() );
        assertFalse(instance.solved());
        instance.udpateJumbledWord(str);
        assertTrue(instance.solved());
    }
}
