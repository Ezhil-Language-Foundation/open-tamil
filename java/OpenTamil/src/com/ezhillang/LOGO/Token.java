/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/
package com.ezhillang.LOGO;
/**
 *
 * @author muthu
 */
public class Token {
    TokenKind m_kind;
    String m_value;
    
    public Token(TokenKind kind, String val) {
        m_kind = kind;
        m_value = val;
    }
    
    public String toString() {
        return "TokenKind "+ m_kind.toString() + " with value '"+ m_value+"'";
    }
    
    /// property accessors ///
    TokenKind getKind() {
        return m_kind;
    }
  
    double getNumericValue() {
        return Double.valueOf(m_value);
    }
    
    String getStringValue() {
        return m_value;
    }
    
    //// predicates ////
    boolean isOperator() {
        if ( m_kind == TokenKind.ADD ||
           m_kind == TokenKind.SUB ||
           m_kind == TokenKind.PROD||
           m_kind == TokenKind.DIV) {
            return true;
        }
        return false;
    }

    boolean isCloseParenOrSQBR() {
        return (m_kind == TokenKind.CLOSE_PAREN) || 
                (m_kind == TokenKind.CLOSE_SQBR); 
    }
}
