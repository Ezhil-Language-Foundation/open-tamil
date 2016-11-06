/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை,
*/
package com.ezhillang.LOGO;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Queue;

public class Lexer {
    Queue<Token> m_tokens;
    String m_contents;
    String m_filename;
    static String TO = "TO";
    static String REPEAT = "REPEAT";
    boolean m_comment = false;
    
    public Lexer(String filename) {
        m_tokens = new java.util.ArrayDeque<Token>();
        m_contents = "";
        m_filename = filename;
    }
       
    /// iterators
    public boolean hasNext() {
        return m_tokens.size() > 0;
    }
    
    public Token peek() {
        return m_tokens.peek();
    }
    
    public boolean matchKind(TokenKind knd) {
        System.out.println("matching -> "+knd);
        return getNext().m_kind == knd;
    }
    
    public boolean matchValue(String tokval) {
        System.out.println("matching(2) -> "+tokval);
        return getNext().m_value.equalsIgnoreCase(tokval);
    }
    
    public Token getNext() {
        Token rval = m_tokens.remove();
        System.out.println( "getNext is => "+rval.toString());
        return rval;
    }
    
    // get tokens
    public Queue<Token> getAllTokens() {
        return m_tokens;
    }
    
    //returns number of tokens scanned from driver method
    public int scan() throws IOException, Exception {
        List<String> lines = Files.readAllLines( FileSystems.getDefault().getPath(m_filename), Charset.forName("UTF-8") );
        for(String line : lines) {
            m_comment = false; //reset
            line = line.trim();
            String[] parts = line.split("\\s+");
            for(String part : parts) {
                part = part.trim();
                // System.out.println(" ===> "+part);
                recognizeToken(part);
                // skip rest of comment
                if ( m_comment )
                    break;
            }
        }
        return m_tokens.size();
    }
    
    // utility methods
    /** 
     * WORDS:          FW BW ....
NUMBERS:        0, 0.1, 20
LISTS:          [1 2 3 5]
SYMBOLS:        "foo "bar
VARIABLES:      :foo :bar 
FUNCTION CALLS: COMMAND arg arg arg ...
                (COMMAND arg arg arg ...)
     */
    
    //skip first letter and recognizeToken for rest of trimmed string
    void checkAndProceed(String chunk) throws Exception {
        if ( chunk.length() > 1)
              recognizeToken( chunk.substring(1).trim() );
    }
    
    void recognizeToken(String chunk) throws Exception {
        if ( chunk.length() < 1 )
                return;
        
        Character c = chunk.charAt(0);
        if ( Character.isDigit(c) || c == '.' ) {
            int idx = 1;
            String rest_chunk = null;
            while( idx < chunk.length() ) {
                if ( !Character.isDigit( chunk.charAt(idx)) &&
                        chunk.charAt(idx) != '.') {
                    rest_chunk = chunk.substring(idx);
                    chunk = chunk.substring(0,idx);
                    break;
                }
                idx++;
            }
          addToken( chunk, TokenKind.NUMBER );
          if ( rest_chunk != null) 
               recognizeToken( rest_chunk.trim() );
        } else if ( c == ';') {
         m_comment = true;
         // beginning of a comment. skip the whole thing!
         return;
        } else if ( chunk.equalsIgnoreCase("+") ) {
          addToken( chunk, TokenKind.ADD );
        } else if ( chunk.equalsIgnoreCase("=") ) {
          addToken( chunk, TokenKind.EQ);
        } else if ( chunk.equalsIgnoreCase("-") ) {
          addToken( chunk, TokenKind.SUB );
        } else if ( chunk.equalsIgnoreCase("/") ) {
          addToken( chunk, TokenKind.DIV );
        } else if ( chunk.equalsIgnoreCase("*") ) {
          addToken( chunk, TokenKind.PROD );
        } else if ( c == ')' ) {
          addToken( c.toString(), TokenKind.CLOSE_PAREN );
          checkAndProceed( chunk );
        } else if ( chunk.equalsIgnoreCase("END") ) {
          addToken( chunk, TokenKind.END );
        } else if ( c == '(' ) {
          addToken( c.toString(), TokenKind.OPEN_PAREN );
          checkAndProceed( chunk );
        } else if ( c == '[' ) {
          addToken( c.toString(), TokenKind.OPEN_SQBR );
          checkAndProceed( chunk );
        } else if ( c == ']' ) {
          addToken( c.toString(), TokenKind.CLOSE_SQBR );
          checkAndProceed( chunk );
        } else if ( chunk.startsWith(":") ) {
          addToken( ":", TokenKind.COLON );
          checkAndProceed( chunk );
        } else if ( chunk.startsWith("\"") ) {
          addToken( "\"", TokenKind.QUOTE );
          if ( chunk.length() > 1) 
              recognizeToken( chunk.substring(1).trim() );
        } else if ( Character.isAlphabetic(c) ) {
           String [] parts_rval = getAlphabetString(chunk);
           chunk = parts_rval[0];
           String rest_chunk = parts_rval[1];
           addToken( chunk, TokenKind.STRING );
           if ( rest_chunk != null) 
               recognizeToken( rest_chunk.trim() );
        } else if ( c == '-' || c == '+' || c == '/' || c == '*' )  {
            recognizeToken( c.toString() );
            checkAndProceed(chunk);
        } else { 
            // most likely an error
            throw new Exception("failed.. lexing file "+ m_filename +" at '"+chunk+"'");
        }
    }
    
    String [] getAlphabetString(String chunk) {
            String [] rval = new String[2];
            int idx = 1;
            String rest_chunk = null;
            while( idx < chunk.length() ) {
                if ( !Character.isAlphabetic( chunk.charAt(idx) ) ) {
                    rest_chunk = chunk.substring(idx);
                    chunk = chunk.substring(0,idx);
                    break;
                }
                idx++;
            }
           rval[0] = chunk;
           rval[1] = rest_chunk;
           return rval;
    }
    
    void addToken( String val, TokenKind kind) {
        m_tokens.add(new Token(kind,val) );
    }
    
    // debug utility
    public void print() {
        System.out.println("Source => "+m_filename);
        for(Token tkn : m_tokens  ) {
            System.out.println(tkn);
        }
    }
}
