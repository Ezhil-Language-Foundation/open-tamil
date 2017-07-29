/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, 2017 முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.ListIterator;
import java.util.Queue;
import static junit.framework.Assert.assertEquals;
import static junit.framework.Assert.assertTrue;
import junit.framework.TestCase;

public class InterpreterTest extends TestCase {    
    private static File resourcesDirectory = null;
    
    public InterpreterTest(String testName) {
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
        
    public void testInterpreter() throws IOException, Exception {
        doInterpTest("basicsquare.logo");
        doInterpTest("square.logo");
        doInterpTest("basic.logo");
        doInterpTest("squarefunction.logo");
        doInterpTest("lesson1.logo");
        doInterpTest("lesson2.logo");
        doInterpTest("house.logo");
        doInterpTest("recursive.logo");
    }
    
    public void doInterpTest(String file) throws IOException, Exception {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath(),file);
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
        m_int.evaluate( m_parser.m_ast );
    }
}
