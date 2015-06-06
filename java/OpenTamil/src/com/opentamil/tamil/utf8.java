/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */
package com.opentamil.tamil;
import java.lang.*;
import java.util.*;
import java.util.stream.IntStream;

/**
 *
 * @author Muthiah Annamalai
 */
public class utf8 {
    final static String ayudha_letter = "";
    final static String [] uyir_letters = new String [] {};
    final static String [] mei_letters = new String [] {};
    final static String [] grantha_agaram_letters = new String [] {};
    final static String [] accent_symbol_letters = new String [] {};
    
    final static TreeSet<String> uyir_letter_set = new TreeSet( Arrays.asList(uyir_letters) );
    final static TreeSet<String> grantha_agaram_set = new TreeSet( Arrays.asList(grantha_agaram_letters) );
    final static TreeSet<String> accent_symbol_set = new TreeSet( Arrays.asList(accent_symbol_letters) );
    
    public static List<String> get_letters(String text) {
        List<String> letters = new ArrayList();
        int idx = 0, cp = 0;
        int [] cp_array = {0,0};
        String cp_as_letter;
        boolean not_empty = false;
        while( idx < text.length() ) {
            cp = text.codePointAt(idx);
            
            cp_array[0]=cp;
            cp_as_letter = new String(cp_array,0,1);
            
            if (utf8.uyir_letter_set.contains(cp_as_letter) ||
                    cp_as_letter.equals(utf8.ayudha_letter)) {
                letters.add(cp_as_letter); 
                not_empty = true;
            } else if ( utf8.grantha_agaram_set.contains(cp_as_letter) ) {
                letters.add(cp_as_letter); 
                not_empty = true;
            } else if ( utf8.grantha_agaram_set.contains(cp_as_letter) ) {
                if ( !not_empty ) {
                    // odd situation       
                    letters.add(cp_as_letter);
                    not_empty = true;
                } else {
                    String prev = letters.remove(letters.size()-1);
                    prev = prev + cp_as_letter;
                    letters.add(prev);
                }
            } else {
                if ( cp < 256 ) {
                    letters.add(cp_as_letter);
                } else {
                    if ( not_empty ) {
                        //concat with last letter
                        String prev = letters.remove(letters.size()-1);
                        prev = prev + cp_as_letter;
                        letters.add(prev);
                    } else {
                        letters.add(cp_as_letter);
                        not_empty = true;
                    }
                }
            }
            idx = idx + 1;
        }
        
        return letters;
    } 
    
    public static int tamil_len() {
        return 323;
    }
    public static int uyir_len() {
        return 12;
    }
    public static int ayudha_len() {
        return 1;
    }
    public static int accent_len() {
        return 13;
    }
    public static int agaram_len() {
        return 18;
    }
    public static int mei_len() {
        return 18;
    }
    
}
