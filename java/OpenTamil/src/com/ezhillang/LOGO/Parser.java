/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;

import java.util.ArrayList;
import java.util.ListIterator;

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
       System.out.println("tokens => "+n_tokens);
       parse();
       return true;
   }
   
   // recursive descent parser for the LOGO code
   private void parse() throws Exception {
       m_lexer.print();
       while ( m_lexer.hasNext() ) {      
        Token token = m_lexer.peek();
        if ( check(token,m_lexer.TO) ) {
            parseFunction();
        } else if ( check(token,m_lexer.REPEAT) ) {
            parseRepeat();
        } else {
            //parse word
            Interpreter.KnownWordFound isKnownWord = m_int.isKnownWord( token );
            if ( isKnownWord.found ) {
                parseKnownWord( token, isKnownWord.nargs );
            } else {
                throw new Exception("Issue with expressions - parse error - at token "+token.toString());
            }
        }
       }
   }
   
   private void parseRepeat() throws Exception {
       Repeat repeatAST = null;
       m_lexer.matchValue(m_lexer.REPEAT);
       AST times_expr = parseExpr();
       ListAST listAST = this.parseList();
       repeatAST = new Repeat(times_expr,listAST);
       m_ast.add( repeatAST );
   }
   
   // to function_name ==> :var1 :var2 ... :varN <=
   private ArgList parseAnyArgList() {
       ArgList args = new ArgList();
       while( m_lexer.hasNext() && (m_lexer.peek().m_kind == TokenKind.COLON) ) {
           m_lexer.matchKind(TokenKind.COLON);
           Token token = m_lexer.getNext();
           args.add(new Variable(token.getStringValue()));
       }
       return args;
   }
   
   // TO part is already used.
   private void parseFunction() throws Exception {
       ArgList args = null;
       m_lexer.matchValue(m_lexer.TO);
       Token fname = m_lexer.getNext();
       assert fname.m_kind == TokenKind.STRING;
       String fname_value = fname.m_value;
       Token iscolon = m_lexer.peek();
       if ( iscolon.m_kind == TokenKind.COLON ) {
            args = parseAnyArgList();
       } else {
           System.out.println("No arguments to function : "+fname_value);
       }
       m_int.addUserDefinedWord( fname_value, args);
       // anticipate the recursive function parsing and enter this function into the interpreter table
       ListAST functionBody = parseBody();
       // build a function
       // attach to the expr list
       m_lexer.matchValue("END");
       Function fcn = new Function( fname.m_value, args, functionBody );
       m_ast.add(fcn);
   }
   
   private boolean check(Token token, String lexeme) {
       return token.m_value.equalsIgnoreCase( lexeme );
   }
   
   // 10/29/16: N.B
   // goal to have basic parser that recognizes LOGO language constructs
   // without the infix expression parsing
   
   // key function
   // expr => 
   //       number | variable | list
   //      
   private AST parseExprTerm() throws Exception {
       AST rval = null;
       rval = parseExprFactor();
       if ( !m_lexer.hasNext() || m_lexer.peek().isCloseParenOrSQBR()  )
           return rval;
       Token token = m_lexer.peek();
       // production to factor
       if ( token.m_kind != TokenKind.PROD
               && token.m_kind != TokenKind.DIV ) {
           return rval;
       }
       
       AST lhs = rval;
       token = m_lexer.getNext();
       if ( token.m_kind == TokenKind.PROD 
          || token.m_kind == TokenKind.DIV ) {
          AST rhs = parseExprTerm();
          return new Expr( token.m_kind, lhs, rhs );
       }
       throw new Exception("malformed expression at "+token);
   }
   
   private AST parseExprFactor() throws Exception {
       AST rval = null;
       Token token = m_lexer.peek();
       Interpreter.KnownWordFound isKnownWord = m_int.isKnownWord( token );
       if ( token.m_kind == TokenKind.NUMBER ) {
           m_lexer.matchKind(TokenKind.NUMBER);
           rval = new Number( token.getNumericValue() );
           return rval;
       } else if ( token.m_kind == TokenKind.COLON ) {
           // var expr
           m_lexer.matchKind(TokenKind.COLON);
           token = m_lexer.getNext();
           rval = new Variable( token.getStringValue() );
           return rval;
       } else if ( token.m_kind == TokenKind.OPEN_PAREN )  {
           m_lexer.matchKind(TokenKind.OPEN_PAREN);
           rval = parseExpr();
           m_lexer.matchKind(TokenKind.CLOSE_PAREN);
           return rval;
       } else if ( isKnownWord.found ) {
               parseKnownWord( token, isKnownWord.nargs );
               rval = m_ast.removeLast();
               return rval;
       }
       throw new Exception("malformed expression at "+token);
   }
   
   private AST parseExpr() throws Exception {
       AST rval = null;
       Token token = m_lexer.peek();
       
       Interpreter.KnownWordFound isKnownWord = m_int.isKnownWord( token );
       if ( token.m_kind == TokenKind.NUMBER || 
          token.m_kind == TokenKind.COLON || 
          isKnownWord.found ) {
           AST lhs = null;
           lhs = parseExprTerm();
           if ( !m_lexer.hasNext() )
               return lhs;
           token = m_lexer.peek();
           if ( token.m_kind == TokenKind.ADD ||
              token.m_kind == TokenKind.SUB ) {
               token = m_lexer.getNext();
               AST rhs = parseExpr();
              return new Expr(token.m_kind,lhs,rhs); 
           } 
           
           return lhs;
       } else if ( token.m_kind == TokenKind.OPEN_SQBR ) {
           m_lexer.matchKind(TokenKind.OPEN_SQBR);
           return parseList();
       } else if ( token.m_kind == TokenKind.QUOTE ) {
           m_lexer.matchKind(TokenKind.QUOTE);
           token = m_lexer.getNext();
           return new Deref(token.m_value);
       }
       throw new Exception("cannot find any suitable expression at "+token);
   }
   
   // e.g. FD 90
   // e.g. 
   private void parseExprCallArgs(ListAST args,int nargs) throws Exception {
       for(int i=0; i<nargs; i++) {
           args.add( parseExpr() );
       }
   }
   
   // parse a known word startin @ token with arguments of 'intValue'
   private void parseKnownWord(Token token, int intValue) throws Exception {
       m_lexer.matchKind(TokenKind.STRING);
       String word_name = token.getStringValue();
       ListAST args = new ListAST();
       parseExprCallArgs(args,intValue);
       if ( args.size() != intValue ) {
           throw new Exception("Incorrect number of arguments for function "+word_name+". We expected "+intValue+" but received only "+args.size());
       }
       
       ExprCall call = new ExprCall( word_name, args );
       m_ast.add( call );
   }

    private ListAST parseList() throws Exception {
        ListAST list = new ListAST();
        m_lexer.matchKind(TokenKind.OPEN_SQBR);
        while( m_lexer.hasNext() ) {
           AST rval = null;
           Token token = m_lexer.peek();
           if ( token.m_kind == TokenKind.OPEN_SQBR) {
               rval = parseList(); // support nested lists
           } else if ( token.m_kind == TokenKind.CLOSE_SQBR) {
               break;
           } else if ( token.m_value.equalsIgnoreCase( m_lexer.REPEAT ) ) {
               parseRepeat();
               rval = m_ast.removeLast();
           } else {
               Interpreter.KnownWordFound isKnownWord = m_int.isKnownWord( token );
               if ( isKnownWord.found ) {
                  parseKnownWord( token, isKnownWord.nargs );
                  rval = m_ast.removeLast();
               } else {
                   rval = parseExpr();
               }
           }
           list.add(rval);
        }
        m_lexer.matchKind(TokenKind.CLOSE_SQBR);
        return list;
    }

    void print() {
        ListIterator<AST> itr = m_ast.getIterator();
        int idx = 1;
        while( itr.hasNext() ) {
            System.out.println( idx+" -> "+itr.next().toString());
            idx++;
        }
    }

   // body is basically a list without the '[' and ']' start/end tokens
   private ListAST parseBody() throws Exception {
        ListAST list = new ListAST();
        while( m_lexer.hasNext() ) {
           AST rval = null;
           Token token = m_lexer.peek();
           if ( token.m_kind == TokenKind.OPEN_SQBR) {
               rval = parseList(); // support nested lists
           } else if ( token.m_value.equalsIgnoreCase("END") ) {
               break;
           } else if ( token.m_value.equalsIgnoreCase("REPEAT") ) {
               parseRepeat();
               rval = m_ast.removeLast();
           } else {
               Interpreter.KnownWordFound isKnownWord = m_int.isKnownWord( token );
               if ( isKnownWord.found ) {
                  parseKnownWord( token, isKnownWord.nargs );
                  rval = m_ast.removeLast();
               } else {
                   rval = parseExpr();
               }
           }
           list.add(rval);
        }
        return list;
    }
}
