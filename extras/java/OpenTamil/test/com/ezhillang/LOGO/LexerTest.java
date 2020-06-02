/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

// added ability to have line comments initiated by ';' 
import java.io.File;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.List;
import java.util.Queue;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class LexerTest extends TestCase {    
    private static File resourcesDirectory = null;
    
    public LexerTest(String testName) {
        super(testName);
    }
    
    @Override
    protected void setUp() throws Exception {
        super.setUp();
        resourcesDirectory = new File("test/com/ezhillang/LOGO");
    }
    
    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }
    
    public void testLexer() throws IOException {
        doLexerTest("dynspiral.logo",38);
        doLexerTest("hilbert.logo",197);
        doLexerTest("koch.logo",87);
        doLexerTest("spiral.logo",84);
        doLexerTest("basic.logo",17);
        doLexerTest("lesson1.logo",239);
        doLexerTest("basicsquare.logo",25);
        doLexerTest("square.logo",10);
    }
    
    public void doLexerTest(String file, int expResult) throws IOException {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                 ,file);
        Lexer instance = new Lexer(p.toAbsolutePath().toString());
        int result = -1;
        
        try {
            result = instance.scan();
        } catch(Exception e) {
            e.printStackTrace();
        }
        
        Queue<Token> tkn_result = instance.getAllTokens();
        instance.print();
        assertEquals(expResult, result);
    }
}
