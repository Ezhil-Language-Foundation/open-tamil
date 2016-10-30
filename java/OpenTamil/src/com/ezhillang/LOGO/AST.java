/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை,
*/

/*
* Parse tree objects representing LOGO language objects
*/
package com.ezhillang.LOGO;

import java.util.ArrayList;
import java.util.ListIterator;

public class AST {
    void visit(Visitor v) throws Exception {
       v.visit(this);
    }
}

// always binary operators for now
class Expr extends AST {
    AST m_lhs;
    AST m_rhs;
    TokenKind m_op;

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

class Number extends AST {
    double m_val;
    
    Number(double val) {
        super();
        m_val = val;
    }
}

class Variable extends AST {
    String m_var;
    
    Variable(String val) {
        super();
        m_var = val;
    }
}

// define a function invocation with arguments
class ExprCall extends AST {
    ListAST m_args;
    String m_function;

    ExprCall(String word_name, ListAST args) {
        super();
        m_args = args;
        m_function = word_name;
    }
}

class Word extends AST {
    int m_args = 0;
    String m_word_name = null;
    String [] m_alias = null; //sometimes we like to have the Tamil name here
    boolean m_builtin = true;
    
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
    UserWord(String wordname, int arg) {
        super(wordname,arg);
        m_builtin = false;
    }
}

class ArgList extends AST {
    ArrayList<AST> m_args;
    int size() {
        return m_args.size();
    }
    ArgList() {
        super();
        m_args = new ArrayList<AST>();
    }
}

class Function extends AST {
    ArrayList<AST> m_function_body;
    ArgList m_args;
    String m_name;
    
    Function(String m_value, ArgList args, Object functionBody) {
        
    }
}

class Repeat extends AST {
    ListAST m_body;
    AST m_times;
    
    Repeat(AST times, ListAST body) {
        m_times = times;
        m_body = body;
    }
}

class ListAST extends AST {
    private ArrayList<AST> m_array;
    
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
    
    int size() {
        return m_array.size();
    }
    
    void add(AST ref) {
        m_array.add(ref);
    }
}