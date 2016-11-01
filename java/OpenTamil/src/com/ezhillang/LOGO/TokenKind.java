/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை,
*/
package com.ezhillang.LOGO;

/**
 *
 * @author muthu
 */
public enum TokenKind {
   COLON, // :
   NUMBER, // [0-9\.]+
   WORD, // [a-z]+
   OPEN_SQBR, // [
   CLOSE_SQBR, // ]
   OPEN_PAREN, // (
   CLOSE_PAREN, // )
   QUOTE, //" 
   STRING, // '[a-z]+
   ADD, //+
   SUB, //-
   PROD, //*
   DIV,// '/'
   EQ, // '='
   END // 'END'
}
