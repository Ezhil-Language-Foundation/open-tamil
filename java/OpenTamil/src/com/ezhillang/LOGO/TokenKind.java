/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
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
   EQ // '='
}
