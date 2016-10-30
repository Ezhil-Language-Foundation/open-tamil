/*
* Parse tree objects representing LOGO language objects
*/
package com.ezhillang.LOGO;

import java.util.ArrayList;

public class AST {
}

class Expr extends AST {
}

class ExprCall extends Expr {
    ExprCall () {
        super();
    }
}

class Word extends AST {
    int m_args = 0;
    String m_word_name = null;
    String m_alias = null; //sometimes we like to have the Tamil name here
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
        m_alias = alias;
    }
   
   boolean matches(String other_word) {
       return m_word_name.equalsIgnoreCase(other_word) || (m_alias != null  && m_alias.equalsIgnoreCase(other_word));
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

class ListAST extends AST {
    private ArrayList<AST> m_array;
    
    ListAST() {
        super();
        m_array = new ArrayList<AST>();
    }
    
    void add(AST ref) {
        m_array.add(ref);
    }
}