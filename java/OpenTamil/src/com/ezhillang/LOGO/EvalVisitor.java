/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import java.util.ListIterator;

/**
 *
 * @author muthu
 */
/**
 *
 * @author muthu
 */
public class EvalVisitor extends Visitor {
    Interpreter m_int;
    public static void evaluate(AST root, Interpreter ref) throws Exception {
        EvalVisitor evaluator = new EvalVisitor(ref);
        root.visit(evaluator);
    }
    
    public EvalVisitor(Interpreter interpreter) {
        m_int = interpreter;
        assert( m_int != null);
    }
    /////////// evaluator implementation ////////////////////
    public void visit(ListAST obj) throws Exception {
        ListIterator<AST> itr = obj.getIterator();
        while( itr.hasNext() ) {
            AST ref_obj = itr.next();
            ref_obj.visit( this );
        }
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
    
    // make function call: eval args and push onto call-stack, fetch the body, return value push onto call stack
    public void visit(ExprCall obj) throws Exception {
        obj.visit(this);
    }
   
    // this is a constant
    public void visit(Number obj) throws Exception {
        obj.visit(this);
    }
    
    //access sym table and return the value pointed by variable
    public void visit(Variable obj) throws Exception {
        obj.visit(this);
    }
    
   public void visit(Repeat obj) throws Exception {
        obj.m_times.visit(this);
        obj.m_body.visit(this);
    }
    
    //evaluate the expression: unary binary etc etc.
    public void visit(Expr obj) throws Exception {
        if ( !obj.isArithmeticExpr() || !obj.isBinaryExpr() ) {
            throw new Exception("Arithmetic binary expression expected at "+obj.toString());
        }

        obj.m_lhs.visit(this);
        obj.m_rhs.visit(this);
        
        Double rhs = (Double) m_int.pop();
        Double lhs = (Double) m_int.pop();
        double d_rhs = rhs.doubleValue();
        double d_lhs = lhs.doubleValue();
        double d_res = 0.0;
        switch( obj.m_op ) {
            case ADD:
                d_res = d_rhs + d_lhs;
                break;
            case SUB:
                d_res = d_lhs - d_rhs;
                break;
            case PROD:
                d_res = d_lhs * d_rhs;                
                break;
            case DIV:
                d_res = d_lhs / d_rhs;                
                break;
        }
        m_int.push(new Double(d_res));
    }
}
