/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.util.HashMap;
import java.util.Stack;

public class Interpreter extends EvalVisitor implements IRuntimeFunction {
    //map of known words and implementations
    WordMap m_word_map;
    WordMap m_userdef_map;
    Stack<Object> m_stack;
    ITurtleGraphics m_turtle;
    
    //builtins
    Word word_fw, word_bw, word_home, word_rt, word_lt, word_cls, word_repcount;
    Stack<Double> m_repeat_count;
    boolean m_add_delay;
    
    // utility
    void parseEval(Parser p) throws Exception {
        p.startParsing();
        evaluate(p.m_ast);
    }
    
    public Interpreter() {
        super();
        m_add_delay = false; //change it later
        m_turtle = null;
        m_word_map = new WordMap();
        m_userdef_map = new WordMap();
        m_stack = new Stack<Object>();
        m_repeat_count = new Stack<Double>();
        loadBuiltIns();
    }
    
    Interpreter getInterpreter() {
        return this;
    }
    
    Object pop() {
        return m_stack.pop();
    }
    
    void setGraphicsInterface(ITurtleGraphics tgraphics) {
        m_turtle = tgraphics;
    }
    
    // start the evaluator
    void evaluate(ListAST ast) throws Exception {
        initialize();
        visit(ast);
    }
    
    void push(Object obj) {
        m_stack.push(obj);
    }
    
    private void loadBuiltIns() {
        word_rt = new Word("RT",1, new String [] { "வலது", "RIGHT" } );
        m_word_map.addWord(word_rt);
        
        word_lt = new Word("LT",1,new String [] { "இடது", "LEFT" } );
        m_word_map.addWord(word_lt);
        
        word_fw = new Word("FW",1,new String [] {"முன்","FD","FORWARD"});
        m_word_map.addWord( word_fw);
        
        word_bw = new Word("BW",1,new String [] {"பின்","BK","BACK","BACKWARD"});
        m_word_map.addWord( word_bw);
        
        word_cls = new Word("RESET",0,new String [] {"அழி","CLEAR","CLS"});
        m_word_map.addWord(word_cls);
        
        m_word_map.addWord("STOP",0,"நிறுத்து");
        m_word_map.addWord("CS",0,new String [] {"CLEAR","CLEARSCREEN","CLS","RESET","அழி"});
        m_word_map.addWord("PU",0,new String [] {"penup","எடு"});
        
        word_home = new Word("HOME",0,"வீடு");
        m_word_map.addWord(word_home);
        
        m_word_map.addWord("PD",0,new String [] {"pendown","வை"});
        m_word_map.addWord("COLOR",1,new String [] {"நிரம்","வண்ணம்"});
        
        word_repcount = new Word("REPCOUNT", 0, new String [] {"முறை"});
        m_word_map.addWord(word_repcount);
        
        m_word_map.addWord("PENWIDTH",1,"அகலம்");
        m_word_map.addWord("PRINT",1,"அச்சிடு");
        m_word_map.addWord("Random",1,"யூகி");
        m_word_map.addWord("MAKE",2,"செய்");
    }

    void addUserDefinedWord(String m_value, ArgList args) {
        m_userdef_map.addWord(m_value, (args != null) ? args.size() : 0);
    }

    // function
    @Override
    public void evaluate(Interpreter m_int, String function, Object[] args) throws Exception {
        int nargs = 0;
        if ( args != null) {
            nargs = args.length;
        }
        // do something - update the state of the interpreter
        System.out.println("Evaluate function => "+function+ ( nargs > 0 ? " with args "+ ( args[0].toString()) : ""));
        
        // evaluate repcount function here
        if ( word_repcount.matches(function) ) {
            push( m_repeat_count.peek() );
            return;
        }
        
        if ( m_turtle != null ) { 
            if ( word_rt.matches(function) ) {
                m_turtle.rotate_right( (Double) args[0]);
            } else if ( word_lt.matches(function) ) {
               m_turtle.rotate_left( (Double) args[0]);
            } else if ( word_fw.matches(function) ) {
               m_turtle.forward( (Double) args[0] );
            } else if ( word_bw.matches(function) ) {
               m_turtle.backward( (Double) args[0] );
            } else if ( word_cls.matches(function) ) {
               m_turtle.clear();
            } else if ( word_home.matches(function) ) {
                m_turtle.home();
            } else {
                System.out.println("Cannot find matches for function =>"+function);
            }
        }

        // possibly a user defined function
        // FIXME
        Word udef_function = m_userdef_map.findWord(function);
        if ( udef_function instanceof UserWord ) {
            UserWord uw = (UserWord) udef_function;
            uw.m_ref_impl.visit(this);
        } else if ( udef_function != null ) {
           // System.out.println( "We plan to extract function ["+udef_function.m_word_name+"] from the interpreter and run it");
           // pass
        }
        
        if ( m_add_delay ) {
            try {
                Thread.sleep(250); //0.25s pause between actions make for nice slow drawing
            } catch(Exception e) {
                //ignore
            }
        }
    }

    Object getIdentifier(String m_var) {
        System.out.println("ID read =>"+m_var);
        return m_var;
    }

    void setInterpreter(AST idname, Object pop) {
        System.out.println("Create interpreter variable => " + idname.toString() + " = "+pop.toString());
    }

    private void initialize() {
        if ( m_turtle == null )
            return;
        m_turtle.init();
    }
    
    public class KnownWordFound {
        public boolean found;
        public int nargs;
        KnownWordFound(boolean flag, int arg) {
            found = flag;
            nargs = arg;
        }
    }
    
   // see which map has the definitions and extract nargs from them
    KnownWordFound isKnownWord(Token token) {
       String word_name = token.getStringValue();
       return isKnownWord(word_name);
    }
    
    // overloaded utility
    KnownWordFound isKnownWord(String word_name) {
       Word ref = m_userdef_map.findWord(word_name);
       if ( ref == null )
           ref = m_word_map.findWord(word_name);   
       // return the nargs
       int nargs = (ref != null) ? (ref.m_args) : 0;
       return new KnownWordFound( ref != null, nargs);
    }
}

/**
 *
 * @author muthu
 */
class WordMap extends HashMap<String,Word> {
    WordMap() {
        super();
    }
   
    void addWord(Word w) {
       put(w.m_word_name,w);
   }
   
   void addWord(String wrd, int arg) {
        put(wrd, new Word(wrd,arg));
    }
    void addWord(String wrd, int arg, String alias) {
        put(wrd, new Word(wrd,arg,alias));
    }
    void addWord(String wrd, int arg, String [] alias) {
        put(wrd, new Word(wrd,arg,alias));
    }
    
    Word findWord(String ref_name) {
       Word ref = null;
       for(Word itr: this.values()) {
           if ( itr.matches( ref_name ) ) {
               ref = itr;
               break;
           }
       }
       return ref;
    }
}
