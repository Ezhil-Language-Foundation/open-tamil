/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.io.File;
import java.io.IOException;
import java.nio.file.Path;

public class CLI {    
    private static File resourcesDirectory = null;
        
    public static void cli_main(String args[]) throws Exception {
       resourcesDirectory = new File("test/com/ezhillang/LOGO");
       CLI obj = new CLI();
       obj.doParserTest("squarefunction.logo");
    }
    
    public void doParserTest(String file) throws IOException, Exception {
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                 ,file);
        System.out.println("Parsing file => "+file);
        Interpreter m_int = new Interpreter();
        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
        m_int.parseEval(m_parser);
    }
}
