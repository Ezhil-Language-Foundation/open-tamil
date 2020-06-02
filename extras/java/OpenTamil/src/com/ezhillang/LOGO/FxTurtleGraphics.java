/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import javafx.animation.AnimationTimer;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.shape.ArcType;
import javafx.stage.Stage;

/**
 *
 * @author muthu
 */
public class FxTurtleGraphics implements ITurtleGraphics {
    // co-ords
    double m_x, m_y;
    boolean m_penup;
    double m_angle;
    GraphicsContext gc = null;
    Group root = null;
    Canvas canvas = null;
    
    static final double C_x = 150.0, C_y = 150.0;
    
    public void init() {
        root = new Group();
        canvas = new Canvas(C_x*2, C_x*2);
        
        m_x = C_x;
        m_y = C_y;
        m_penup = true;
        m_angle = 90.0; //facing north :-)
    }
    
    public void start(Stage primaryStage) {
        init();
        primaryStage.setTitle("Drawing Operations Test");
        gc = canvas.getGraphicsContext2D();
        gc.setStroke(Color.BLUE);
        gc.setLineWidth(5);
       // gc.setFill(Color.ALICEBLUE);
       // gc.rect(m_x-30, m_y-30, m_x, m_y);
       // gc.fillText("Hello World", m_x, m_y);
        root.getChildren().add(canvas);
        primaryStage.setScene(new Scene(root));
        primaryStage.show();
        
    }

    @Override
    public void clear() {
        gc.setFill(Color.WHITE);
        gc.fillRect(0,0, C_x*2, C_y*2);
    }

    @Override
    public void home() {
        System.out.println("HOME =>");
        m_x = C_x;
        m_y = C_y;
        m_angle = 90.0;
    }

    @Override
    public void forward(double distance) {
        System.out.println("FW =>");
        if ( !m_penup )
            return;
        /* m_angle remains same
        * m_x, and m_y are udpated.
        */
        show();
        double n_x = m_x + distance*cos_theta();
        double n_y = m_y + distance*sin_theta();
        //draw a line
        gc.strokeLine(m_x, m_y, n_x, n_y);
        m_x=n_x;
        m_y=n_y;
    }

    @Override
    public void rotate_right(double angle) {
        m_angle -= angle;
    }
    
    @Override
    public void rotate_left(double angle) {
        m_angle += angle;
    }
    
    @Override
    public void backward(double distance) {
        System.out.println("BW =>");
        if ( !m_penup )
            return;
        show();
        m_angle += 180.0;
        double n_x=0.0, n_y=0.0;
        for(int i=0; i<51; i++) {
            double frac = (double)i/50.0;
            n_x = m_x + frac*distance*cos_theta();
            n_y = m_y + frac*distance*sin_theta();
            //draw a line
            gc.strokeLine(m_x, m_y, n_x, n_y);
            //sleep(100); //100ms sleep
        }
        m_x=n_x;
        m_y=n_y;
    }
    
    public void sleep(long msecs) {
        try {
            Thread.sleep(msecs);
        } catch(Exception e) {
            //pass
        }
    }
    @Override
    public void penup() {
        m_penup = true;
    }

    @Override
    public void pendown() {
        m_penup = false;
    }

    private double sin_theta() {
        return Math.sin(m_angle/180.0*Math.PI);
    }

    private double cos_theta() {
        return Math.cos(m_angle/180.0*Math.PI);
    }
    
    public void show(){ 
        System.out.println(toString());
    }
    
    @Override
    public String toString(){
        StringBuffer sb = new StringBuffer();
        sb.append("m_x="+m_x+" , m_y="+m_y+" ");
        return sb.toString();
    }
}
