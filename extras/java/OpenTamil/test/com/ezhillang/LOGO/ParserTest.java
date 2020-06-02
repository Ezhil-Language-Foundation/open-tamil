/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import junit.framework.TestCase;

public class ParserTest extends TestCase {    
    private static File resourcesDirectory = null;
    
    public ParserTest(String testName) {
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
    
    public void testParser2() throws Exception {
        doParserTest("lesson1.logo");    
    }
    
    public void testParser() throws IOException, Exception {        
        doParserTest("basicsquare.logo");
        doParserTest("square.logo");
        doParserTest("basic.logo");
        doParserTest("squarefunction.logo");
        doParserTest("lesson2.logo");
        doParserTest("house.logo");
        doParserTest("recursive.logo");
    }
    
    public void doParserTest(String file) throws IOException, Exception {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                 ,file);
        System.out.println("Parsing file => "+file);
        Interpreter m_int = new Interpreter();
        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
        m_parser.startParsing();
        m_parser.print();
    }
}
