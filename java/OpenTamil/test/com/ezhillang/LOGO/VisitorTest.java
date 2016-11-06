/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
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

public class VisitorTest extends TestCase {    
    private static File resourcesDirectory = null;
    
    public VisitorTest(String testName) {
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
    
    public void testVisitor() throws IOException, Exception {
        doVisitorTest("basicsquare.logo");
        doVisitorTest("square.logo");
        doVisitorTest("basic.logo");
        doVisitorTest("squarefunction.logo");
        doVisitorTest("lesson1.logo");
        doVisitorTest("lesson2.logo");
        doVisitorTest("house.logo");
        doVisitorTest("recursive.logo");
    }
    
    public void doVisitorTest(String file) throws IOException, Exception {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                 ,file);
        System.out.println("Parsing file => "+file);
        Interpreter m_int = new Interpreter();
        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
        try {
            m_parser.startParsing();
            Visitor v = new Visitor();
            v.visit( m_parser.m_ast );
        } catch(Exception e) {
            // pass
        }
    }
}
