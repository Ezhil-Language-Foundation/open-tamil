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
/**
 *
 * @author muthu
 */
public interface ASTVisitor {
    //ASTVisitor(Interpreter obj);
    public void evaluate(Word ast,Interpreter ref);
}
