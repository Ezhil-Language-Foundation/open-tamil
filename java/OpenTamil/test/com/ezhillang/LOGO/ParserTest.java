/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ListIterator;
import java.util.Queue;
import static junit.framework.Assert.assertEquals;
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
    
    public void testParser() throws IOException, Exception {
        doParserTest("basicsquare.logo");
        doParserTest("square.logo");
        doParserTest("basic.logo");
    }
    
    public void doParserTest(String file) throws IOException, Exception {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                 ,file);
        System.out.println("Parsing file => "+file);
        Interpreter m_int = new Interpreter();
        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
        try {
            assertTrue( m_parser.startParsing() );
        } catch(Exception e) {
            e.printStackTrace();
            m_parser.print();
            throw new Exception(e);
        }
        m_parser.print();
    }
}
