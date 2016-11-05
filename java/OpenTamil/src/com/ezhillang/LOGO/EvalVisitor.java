/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை,
*/
package com.ezhillang.LOGO;

import java.util.ListIterator;

/**
 *
 * @author muthu
 */

class EvalVisitor extends Visitor {
    Interpreter m_int;
    
    void init(Interpreter interpreter) {
        m_int = interpreter;
        assert( m_int != null);
    }
    
    public EvalVisitor() {
        super();
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
        if ( obj == null)
            return;
                
        // create identifiers of the name in arglist with values on the stack
        for(int itr=obj.size()-1; itr >= 0; itr--) {
            AST arg_var = obj.m_args.get(itr);
            m_int.setInterpreter(arg_var,m_int.pop());
        }
    }
    
    public void visit(Function obj) throws Exception {
        /* evaluate function () code
            if ( obj.m_args != null )
                obj.m_args.visit(this);
            obj.m_function_body.visit(this);
        */
        // copy this function body into list of known functions for interpreter.
        System.out.println("Registering function => "+obj.m_name);
    }
    
    public void visit(Deref obj) throws Exception {
        m_int.push( m_int.getIdentifier( obj.m_var ) );
        return;
    }
    
    public void visit(UserWord obj) throws Exception {
        obj.visit(this);
    }
    
    // make function call: eval args and push onto call-stack, fetch the body, return value push onto call stack
    public void visit(ExprCall obj) throws Exception {
        Object [] args = null;
        if ( obj.m_args != null)
            args = new Object[obj.m_args.size()];
        // visit the args for the call
        visit( obj.m_args );
        for( int itr= obj.m_args.size() - 1; itr >= 0; itr--) {
            args[itr] = m_int.pop();
        }
        m_int.evaluate(m_int, obj.m_function, args);
    }
   
    // this is a constant
    public void visit(Number obj) throws Exception {
        m_int.push(new Double(obj.m_val));
        return;
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
