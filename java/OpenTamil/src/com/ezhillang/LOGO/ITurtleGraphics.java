/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

/**
 *
 * @author muthu
 */
public interface ITurtleGraphics {
    void init();
    void clear();
    
    void home();
    void penup();
    void pendown();
    void forward(double distance);
    void backward(double distance);
    void rotate_right(double angle);
    void rotate_left(double angle);
}
