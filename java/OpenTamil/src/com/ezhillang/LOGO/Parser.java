/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
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
       m_lexer.match(m_lexer.REPEAT);
       AST times_expr = parseExpr();
       ListAST listAST = this.parseList();
       repeatAST = new Repeat(times_expr,listAST);
       m_ast.add( repeatAST );
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
       if ( !m_lexer.hasNext() )
           return rval;
       Token token = m_lexer.peek();
       // production to factor
       if ( token.m_kind != TokenKind.PROD
               && token.m_kind != TokenKind.DIV ) {
           return rval;
       }
       
       AST lhs = rval;
       AST rhs = parseExprTerm();
       token = m_lexer.getNext();
       if ( token.m_kind == TokenKind.PROD 
          || token.m_kind == TokenKind.DIV ) {
          return new Expr( token.m_kind, lhs, rhs );
       }
       throw new Exception("malformed expression at "+token);
   }
   
   private AST parseExprFactor() throws Exception {
       AST rval = null;
       Token token = m_lexer.peek();
       if ( token.m_kind == TokenKind.NUMBER ) {
           m_lexer.match(TokenKind.NUMBER);
           rval = new Number( token.getNumericValue() );
           return rval;
       } else if ( token.m_kind == TokenKind.COLON ) {
           // var expr
           m_lexer.match(TokenKind.COLON);
           token = m_lexer.getNext();
           rval = new Variable( token.getStringValue() );
           return rval;
       } else if ( token.m_kind == TokenKind.OPEN_PAREN )  {
           m_lexer.match(TokenKind.OPEN_PAREN);
           rval = parseExpr();
           m_lexer.match(TokenKind.CLOSE_PAREN);
           return rval;
       }
       throw new Exception("malformed expression at "+token);
   }
   
   private AST parseExpr() throws Exception {
       AST rval;
       Token token = m_lexer.peek();
       if ( token.m_kind == TokenKind.NUMBER || 
          token.m_kind == TokenKind.COLON ) {
           AST lhs = parseExprTerm();
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
           m_lexer.match(TokenKind.OPEN_SQBR);
           return parseList();
       } 
       throw new Exception("cannot find any suitable expression at "+token);
       //return null;
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
       m_lexer.match(TokenKind.STRING);
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
        m_lexer.match(TokenKind.OPEN_SQBR);
        while( m_lexer.hasNext() ) {
           AST rval = null;
           Token token = m_lexer.peek();
           if ( token.m_kind == TokenKind.OPEN_SQBR) {
               rval = parseList(); // support nested lists
           } else if ( token.m_kind == TokenKind.CLOSE_SQBR) {
               break;
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
        m_lexer.match(TokenKind.CLOSE_SQBR);
        return list;
    }

    void print() {
        ListIterator<AST> itr = m_ast.getIterator();
        int idx = 1;
        while( itr.hasNext() ) {
            System.out.println( idx+" -> "+itr.next());
            idx++;
        }
    }
}
