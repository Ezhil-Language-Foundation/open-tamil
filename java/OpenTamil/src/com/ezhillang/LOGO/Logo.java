/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.awt.Insets;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.application.Platform;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.layout.VBoxBuilder;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;

/**
 *
 * @author muthu
 */
public class Logo extends Application {
    int m_run = 0;
    final String [] files = {"basic.logo", "basicsquare.logo"};
 
    synchronized int getCompleted() {
        return m_run;
    }
    
    synchronized void addCompleted() {
        m_run++;
    }
   
    @Override
    public void start(Stage primaryStage) throws Exception {
        final FxTurtleGraphics m_turtle = new FxTurtleGraphics();
        final Interpreter m_int = new Interpreter();
        m_int.setGraphicsInterface(m_turtle);   
        m_turtle.start(primaryStage);
      
        Platform.runLater(new Runnable() {
            @Override
            public void run() {
                try {
                    while( getCompleted() < files.length ) {
                        File resourcesDirectory = new File("test/com/ezhillang/LOGO");
                        String file = files[getCompleted()];
                        Path p = java.nio.file.FileSystems.getDefault().getPath( resourcesDirectory.getAbsolutePath()
                                ,file);
                        System.out.println("Parsing file => "+file);
                        Parser m_parser = new Parser( p.toAbsolutePath().toString(), m_int);
                        m_parser.startParsing();
                        m_int.evaluate( m_parser.m_ast );
                        addCompleted();
                        //Thread.sleep(2500);
                        //m_turtle.clear();
                    }
                } catch(Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }
    
    public static void main(String [] args)  throws Exception {       
        launch(args);
    }
}
