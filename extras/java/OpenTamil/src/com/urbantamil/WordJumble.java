/*
 * Set of classess implementing the word jumble
 * 
 */
package com.urbantamil;

import com.tamil.TamilString;
import java.util.Collections;

/**
 *
 * @author muthu
 */
public class WordJumble {
    private static final int MAX_ATTEMPTS = 10000; 
    
    TamilString m_origWord, m_jumbledWord;
    
    public WordJumble(TamilString word) {
        m_origWord = new TamilString( word );
        m_jumbledWord = new TamilString( m_origWord );
        m_jumbledWord.rotate_right(); //basic sanity
    }
    
    public WordJumble(String word) {
        m_origWord = new TamilString( word );
        m_jumbledWord = new TamilString( m_origWord );
        m_jumbledWord.rotate_right(); //basic sanity
    }
    
    
    // try to shuffle really do something
    public boolean shuffle() {
        int attempts = 0;
        while( (attempts < MAX_ATTEMPTS) && m_jumbledWord.equals(m_origWord) ) {
            Collections.shuffle(m_jumbledWord);
            attempts++;
        }
        return (attempts < MAX_ATTEMPTS);
    }
    
    // update the puzzle as gameplay goes on
    public void udpateJumbledWord(TamilString str) {
        m_jumbledWord = str;
    }

    // see if the puzzle is solved during gameplay
    public boolean solved() {
        return m_jumbledWord.equals(m_origWord);
    }
    
    @Override
    public String toString() {
        return m_jumbledWord.toString();
    }
}
