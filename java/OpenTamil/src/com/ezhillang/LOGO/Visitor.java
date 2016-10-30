/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
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
