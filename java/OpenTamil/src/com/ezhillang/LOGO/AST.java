/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை,
*/

/*
* Parse tree objects representing LOGO language objects
*/
package com.ezhillang.LOGO;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.ListIterator;

public abstract interface AST {    
    public void visit(Visitor v) throws Exception;
}

// always binary operators for now
class Expr implements AST {
    AST m_lhs;
    AST m_rhs;
    TokenKind m_op;

   public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
   
   @Override
   public String toString() {
       return m_lhs.toString() + " "+m_op+" "+ m_rhs.toString();
   }
    
   Expr( TokenKind kind, AST lhs, AST rhs) {
       m_lhs = lhs;
       m_rhs = rhs;
       m_op = kind;
   }
   boolean isBinaryExpr() {
       return m_lhs != null && m_rhs != null;
   }
   
   boolean isUnaryExpr() {
       return m_lhs != null && m_rhs == null;
   }
   
   boolean isArithmeticExpr() {
        if ( m_op != TokenKind.ADD 
         && m_op != TokenKind.SUB 
         && m_op != TokenKind.PROD 
         && m_op != TokenKind.DIV ) {
            return false;
        }
        return true;
   }
}

class Number implements AST {
    double m_val;
    
   public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
   
   @Override
   public String toString() {
       return String.valueOf(m_val);
   }
   
    Number(double val) {
        super();
        m_val = val;
    }
}

class Variable implements AST {
    String m_var;
   
    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
   @Override
   public String toString() {
       return m_var;
   }
   
    Variable(String val) {
        super();
        m_var = val;
    }
}

// define a function invocation with arguments
class ExprCall implements AST {
    ListAST m_args;
    String m_function;

    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
   @Override
   public String toString() {
       StringBuffer sb = new StringBuffer(m_function);
       sb.append("( ");
       ListIterator<AST> itr = m_args.getIterator();
       while( itr.hasNext() ) {
           sb.append(itr.next().toString());
           if ( itr.hasNext() )
               sb.append(",");
       }
       sb.append(")");
       return sb.toString();
   }
   
    ExprCall(String word_name, ListAST args) {
        super();
        m_args = args;
        m_function = word_name;
    }
    
}

class Deref implements AST {
    String m_var;
    Deref(String var) {
        m_var = var;
    }
    
    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
    @Override
    public String toString() {
        return "\""+m_var;
    }
}

class Word implements AST {
    int m_args = 0;
    String m_word_name = null;
    String [] m_alias = null; //sometimes we like to have the Tamil name here
    boolean m_builtin = true;

   @Override
   public String toString() {
       return m_word_name;
   }
   
   public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
   
   static Word buildUserWord(String wordname, int args, String alias) {
       Word user_word = new Word( wordname, args,alias);
       user_word.m_builtin = false;
       return user_word;
   }
   
   Word(String wordname) {
        m_word_name = wordname;
        m_args = 0;
        m_alias = null;
    }
    
   Word(String wordname, int args) {
        m_word_name = wordname;
        m_args = args;
        m_alias = null;
    }
    
   Word(String wordname, int args, String alias) {
        m_word_name = wordname;
        m_args = args;
        m_alias = new String [] { alias };
    }
   
    Word(String wordname, int args, String [] alias) {
        m_word_name = wordname;
        m_args = args;
        m_alias = alias;
    }
    
   boolean matches(String other_word) {
       
       if ( m_word_name.equalsIgnoreCase(other_word) )
           return true;
       
       if (m_alias != null) {  
           for(String alt_name: m_alias) {
               if ( alt_name.equalsIgnoreCase(other_word))
                   return true;
           }
       }
       return false;
   }
}

class UserWord extends Word {
    Function m_ref_impl = null;
   
    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
    UserWord(String wordname, int arg) {
        super(wordname,arg);
        m_builtin = false;
    }
}

class ArgList implements AST {
    ArrayList<AST> m_args;
    
    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
    int size() {
        return m_args.size();
    }
    
    void add(AST obj) {
        m_args.add(obj);
    }
    
    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        Iterator<AST> itr = m_args.iterator();
        while(itr.hasNext()) {
            sb.append(" :"+itr.next().toString());
        }
        return sb.toString();
    }
    
    ArgList() {
        super();
        m_args = new ArrayList<AST>();
    }
}

class Function implements AST {
    ListAST m_function_body;
    ArgList m_args;
    String m_name;
    
    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
   @Override
   public String toString() {
       return "TO "+ m_name + " "+(m_args != null ? m_args.toString(): "") + "\n"+ 
               ((m_function_body != null) ? m_function_body.toString() : "") +"\n END";
   }
   
    Function(String fname, ArgList args, ListAST functionBody) {
        m_name = fname;
        m_args = args;
        m_function_body = functionBody;
    }
}

class Repeat implements AST {
    ListAST m_body;
    AST m_times;

    public void visit(Visitor v) throws Exception {
       v.visit(this);
   }
    
   @Override
   public String toString() {
       return "REPEAT "+ m_times.toString() + "  ["+ m_body.toString() +"]";
   }
   
    Repeat(AST times, ListAST body) {
        m_times = times;
        m_body = body;
    }
}

class ListAST implements AST {
    private ArrayList<AST> m_array;
    
    public void visit(Visitor v) throws Exception {
        for(AST ast_obj : m_array ) {
            ast_obj.visit(v);
        }
   }
   
    ListAST() {
        super();
        m_array = new ArrayList<AST>();
    }
    
    AST peek(int pos) {
        return m_array.get(pos);
    }

    AST remove(int pos) {
        return m_array.remove(pos);
    }

    AST removeLast() {
        int pos = m_array.size() - 1;
        return m_array.remove(pos);
    }
    
    ListIterator<AST> getIterator() {
        return m_array.listIterator();
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        ListIterator<AST> itr = getIterator();
        while ( itr.hasNext() ) {
            sb.append( itr.next().toString() );
            sb.append("\n");
        }
        
        return sb.toString();
    }
   
    int size() {
        return m_array.size();
    }
    
    void add(AST ref) {
        m_array.add(ref);
    }
}