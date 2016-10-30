/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

import java.util.ArrayList;

/**
 * LOGO needs parser with reference to Interpreter
 * @author muthu
 */
public class Parser {
   Lexer m_lexer;
   Interpreter m_int;
   ListAST m_ast;
   
   public Parser(String filename,Interpreter repl) {
       m_lexer = new Lexer(filename);
       m_ast = new ListAST();
       m_int = repl;
   }
   
   public boolean startParsing() throws Exception {
       int n_tokens = m_lexer.scan();
       parse();
       return true;
   }
   
   // recursive descent parser for the LOGO code
   private void parse() throws Exception {
       while ( m_lexer.hasNext() ) {      
        Token token = m_lexer.peek();
        if ( check(token,m_lexer.TO) ) {
            parseFunction();
        } else if ( check(token,m_lexer.REPEAT) ) {
            parseRepeat();
        } else {
            Integer nargs = new Integer(0); //parse this word
            boolean isKnownWord = m_int.isKnownWord( token, nargs);
            if ( isKnownWord ) {
                parseKnownWord( token, nargs.intValue() );
            } else {
                throw new Exception("Issue with expressions - parse error");
            }
        }
       }
   }
   
   private void parseRepeat() {
       
   }
   
   // to function_name ==> :var1 :var2 ... :varN <=
   private ArgList parseAnyArgList() {
       Token iscolon = m_lexer.peek();
       if ( iscolon.m_kind == TokenKind.COLON ) {
       
       }
       return new ArgList();
   }
   
   // TO part is already used.
   private void parseFunction() {
       ArgList args = null;
       assert m_lexer.match(m_lexer.TO);
       Token fname = m_lexer.getNext();
       assert m_lexer.match(TokenKind.STRING);
       Token iscolon = m_lexer.peek();
       if ( iscolon.m_kind == TokenKind.COLON ) {
            args = parseAnyArgList();
       }
       Object functionBody = null;
       m_int.addUserDefinedWord( fname.m_value, args);
       // anticipate the recursive function parsing and enter this function into the interpreter table
       // parseFunctionBody();
       // build a function
       // attach to the expr list
       Function fcn = new Function( fname.m_value, args, functionBody );
       m_ast.add(fcn);
   }
   
   private boolean check(Token token, String lexeme) {
        return token.m_value.equalsIgnoreCase( lexeme );
   }
   
   // parse a known word startin @ token with arguments of 'intValue'
   private void parseKnownWord(Token token, int intValue) {
       
       m_lexer.match(TokenKind.STRING);
   }
}
