/* This file maybe distributed under terms of MIT License.
* Copyright (c) 2016, முத்தையா அண்ணாமலை, 
*/

package com.ezhillang.LOGO;
import com.tamil.*;
import java.util.List;

/**
 *
 * @author muthu
 */
public class TamilLexer extends Lexer {
final static String REPEAT = "மீண்டும்";
final static String FD = "முன்";
final static String BK = "பின்";
final static String RT = "வலது";
final static String LT = "இடது";
final static String PU = "எடு"; // - penup
final static String PD = "வை"; // - pendown
final static String HOME = "வீடு"; //
final static String CS = "அழி"; // - clear screen
final static String TO = "செய்"; // TO
    public TamilLexer(String filename) {
        super(filename);
    }
    
    @Override
    String [] getAlphabetString(String ta_chunk) {
        String [] rval = new String[2];
        int idx = 0;
        String actual = ta_chunk;
        String rest_chunk = null;
        System.out.println(" ==> "+ ta_chunk);
        List<String> chunk = com.tamil.utf8.get_letters(ta_chunk);
        while( idx < chunk.size() ) {
            if ( ! com.tamil.utf8.is_tamil_letter( chunk.get(idx) ) ) {
                StringBuffer sb = new StringBuffer();
                for( int x =0; x < idx; x++ ) {
                    sb.append( chunk.get(x) );
                }
                actual = sb.toString();
                sb = new StringBuffer();
                for( int x =idx; x < chunk.size(); x++ ) {
                    sb.append( chunk.get(x) );
                }
                rest_chunk = sb.toString();
                break;
            }
            idx++;
        }
       System.out.println(actual+" -> "+rest_chunk);
       rval[0] = actual;
       rval[1] = rest_chunk;
       return rval;
    }
}
