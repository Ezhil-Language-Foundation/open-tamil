/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.util.ListIterator;

/**
 *
 * @author muthu
 */
public class Visitor {
    public void visit(AST obj) throws Exception {
        throw new Exception("visit method not implemented for objects of type"+obj.getClass().toString());
    }
    
    public void visit(Deref obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(Word obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(ArgList obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(Function obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(UserWord obj) throws Exception {
        obj.visit(this);
    }
    
    public void visit(ExprCall obj) throws Exception {
        //pass
    }
        
    public void visit(Number obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(Variable obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(Expr obj) throws Exception {
        //obj.visit(this);
    }
    
    public void visit(ListAST obj) throws Exception {
       ListIterator<AST> itr = obj.getIterator();
       while( itr.hasNext() ) {
           itr.next().visit(this);
       }
    }
 
    public void visit(Repeat obj) throws Exception {
        //pass
    }
 
}
