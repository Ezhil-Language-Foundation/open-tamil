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
public class Visitor {
    public void visit(AST obj) throws Exception {
        throw new Exception("method not implemented!");
    }
    
    public void visit(Word obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(ArgList obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(Function obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(UserWord obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(ExprCall obj) throws Exception {
        obj.visit(this);
    }
        
    public void visit(Number obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(Variable obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(Expr obj) throws Exception {
        obj.visit(this);
    }
    public void visit(ListAST obj) throws Exception {
        obj.visit(this);
    }
 
    public void visit(Repeat obj) throws Exception {
        obj.visit(this);
    }
 
}
