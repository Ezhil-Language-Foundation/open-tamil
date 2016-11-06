/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.io.File;
import java.nio.file.Path;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.stage.Stage;

/**
 *
 * @author muthu
 */
public class Logo extends Application {
    int m_run = 0;
    final String [] files = {"lesson1.logo"}; //"basic.logo", "basicsquare.logo",

    synchronized int getCompleted() {
        return m_run;
    }
    
    synchronized void addCompleted() {
        m_run++;
    }

   @Override
    public void start(Stage primaryStage) throws Exception {
        final FxTurtleGraphics m_turtle = new FxTurtleGraphics();
        
        Platform.runLater(new Runnable() {
            @Override
            public void run() {
                while( getCompleted() < files.length ) {
                    try {
                        Interpreter m_int = new Interpreter();
                        m_int.m_add_delay = false; //animated hopefully!
                        m_int.setGraphicsInterface(m_turtle);   
                        m_turtle.start(primaryStage);
      
                        File resourcesDirectory = new File("test/com/ezhillang/LOGO");
                        String file = files[getCompleted()];
                        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                                ,file);
                        System.out.println("Parsing file => "+file);
                        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
                        m_parser.startParsing();
                        m_int.evaluate( m_parser.m_ast );
                        addCompleted();
                    } catch(Exception e) {
                        e.printStackTrace();
                    }
               }
            }
        });
    }
    
    void basic() throws Exception {        
        Interpreter m_int = new Interpreter();
       // m_int.setGraphicsInterface(m_turtle);   
       // m_turtle.start();

        File resourcesDirectory = new File("test/com/ezhillang/LOGO");
        String file = files[getCompleted()];
        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                ,file);
        System.out.println("Parsing file => "+file);
        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
        m_int.parseEval(m_parser);
    }

    public static void main(String [] args)  throws Exception {       
        launch(args);
        
        // Logo intp = new Logo();
        // intp.basic();
    }
}
