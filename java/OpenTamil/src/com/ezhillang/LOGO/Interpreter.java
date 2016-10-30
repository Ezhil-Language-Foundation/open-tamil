/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Stack;

/**
 *
 * @author muthu
 */
class WordMap extends HashMap<String,Word> {
    WordMap() {
        super();
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

public class Interpreter {
    //map of known words and implementations
    WordMap m_word_map;
    WordMap m_userdef_map;
    Stack<Object> m_stack;
  
    public Interpreter() {
        m_word_map = new WordMap();
        m_userdef_map = new WordMap();
        m_stack = new Stack();
        loadBuiltIns();
    }
    
    Object pop() {
        return m_stack.pop();
    }
    
    void push(Object obj) {
        m_stack.push(obj);
    }
    
    private void loadBuiltIns() {
        m_word_map.addWord("RT",1,"வலது");
        m_word_map.addWord("LT",1,"இடது");
        m_word_map.addWord("FW",1,new String [] {"முன்","FD","FORWARD"});
        m_word_map.addWord("BW",1,new String [] {"பின்","BK","BACKWARD"});
        m_word_map.addWord("RESET",0,new String [] {"அழி","CLEAR","CLS"});
        m_word_map.addWord("STOP",0,"நிறுத்து");
        m_word_map.addWord("CS",0,"அழி");
        m_word_map.addWord("PU",0,"எடு");
        m_word_map.addWord("HOME",0,"வீடு");
        m_word_map.addWord("PD",0,"வை");
        m_word_map.addWord("COLOR",1);
        m_word_map.addWord("PENWIDTH",1);
        m_word_map.addWord("PRINT",1);
    }

    void addUserDefinedWord(String m_value, ArgList args) {
        m_userdef_map.addWord(m_value, (args != null) ? args.size() : 0);
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
       KnownWordFound knf;
       String word_name = token.getStringValue();
       
       Word ref = m_userdef_map.findWord(word_name);
       if ( ref == null )
           ref = m_word_map.findWord(word_name);
       
       // return the nargs
       int nargs = (ref != null) ? (ref.m_args) : 0;
       return new KnownWordFound( ref != null, nargs);
    }
}
