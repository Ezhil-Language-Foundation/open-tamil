/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import java.util.HashMap;
import java.util.Iterator;

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
  public Interpreter() {
      m_word_map = new WordMap();
      m_userdef_map = new WordMap();
      loadBuiltIns();
  }

    private void loadBuiltIns() {
        m_word_map.addWord("RT",1,"வலது");
        m_word_map.addWord("LT",1,"இடது");
        m_word_map.addWord("FW",1,"முன்");
        m_word_map.addWord("BW",1,"பின்");
        m_word_map.addWord("RESET",0,"அழி");
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

    
   // see which map has the definitions and extract nargs from them
    boolean isKnownWord(Token token, Integer nargs) {
       String word_name = token.getStringValue();
       
       Word ref = m_userdef_map.findWord(word_name);
       if ( ref == null )
           ref = m_word_map.findWord(word_name);
       
       // return the nargs
       if ( ref != null) {
           nargs = Integer.valueOf(ref.m_args);
       }
       return (ref != null);
    }
}
