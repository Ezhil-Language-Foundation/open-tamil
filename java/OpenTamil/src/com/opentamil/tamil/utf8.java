/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */
package com.opentamil.tamil;
import java.lang.*;
import java.util.*;

/**
 *
 * @author Muthiah Annamalai
 */
public class utf8 {
/**

*/
    final static String ayudha_letter = "ஃ";
    final static String [] kuril_letters = new String [] {"அ", "இ", "உ", "எ", "ஒ"};
    final static String [] nedil_letters = new String [] {"ஆ", "ஈ", "ஊ", "ஏ", "ஓ"};
    
    final static String [] vallinam_letters = new String [] {"க்", "ச்", "ட்", "த்", "ப்", "ற்"};
    final static String [] mellinam_letters = new String [] {"ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்"};
    final static String [] idayinam_letters = new String [] {"ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"};
    
    final static String [] uyir_letters = new String [] {"அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ","ஓ","ஔ"};
    final static String [] mei_letters = new String [] {"க்","ச்","ட்","த்","ப்","ற்","ஞ்","ங்","ண்","ந்","ம்","ன்","ய்","ர்","ல்","வ்","ழ்","ள்" };
    final static String [] grantha_agaram_letters = new String [] {"க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள",
                                                                   "ஶ","ஜ","ஷ", "ஸ","ஹ","க்ஷ"};
    final static String [] accent_symbol_letters = new String [] {"","ா","ி","ீ","ு","ூ","ெ","ே","ை","ொ","ோ","ௌ","ஃ"};
    
    final static String [] uyirmei_letters = new String [] {
"க"  ,"கா"  ,"கி"  ,"கீ"  ,"கு"  ,"கூ"  ,"கெ"  ,"கே"  ,"கை"  ,"கொ"  ,"கோ"  ,"கௌ",
"ச"  ,"சா"  ,"சி"  ,"சீ"  ,"சு"  ,"சூ"  ,"செ"  ,"சே"  ,"சை"  ,"சொ"  ,"சோ"  ,"சௌ" , 
"ட"  ,"டா"  ,"டி"  ,"டீ"  ,"டு"  ,"டூ"  ,"டெ"  ,"டே"  ,"டை"  ,"டொ"  ,"டோ"  ,"டௌ", 
"த"  ,"தா"  ,"தி"  ,"தீ"  ,"து"  ,"தூ"  ,"தெ"  ,"தே"  ,"தை"  ,"தொ"  ,"தோ"  ,"தௌ",
"ப"  ,"பா"  ,"பி"  ,"பீ"  ,"பு"  ,"பூ"  ,"பெ"  ,"பே"  ,"பை"  ,"பொ"  ,"போ"  ,"பௌ" ,
"ற"  ,"றா"  ,"றி"  ,"றீ"  ,"று"  ,"றூ"  ,"றெ"  ,"றே"  ,"றை"  ,"றொ"  ,"றோ"  ,"றௌ",
"ஞ"  ,"ஞா"  ,"ஞி"  ,"ஞீ"  ,"ஞு"  ,"ஞூ"  ,"ஞெ"  ,"ஞே"  ,"ஞை"  ,"ஞொ"  ,"ஞோ"  ,"ஞௌ",
"ங"  ,"ஙா"  ,"ஙி"  ,"ஙீ"  ,"ஙு"  ,"ஙூ"  ,"ஙெ"  ,"ஙே"  ,"ஙை"  ,"ஙொ"  ,"ஙோ"  ,"ஙௌ",
"ண"  ,"ணா"  ,"ணி"  ,"ணீ"  ,"ணு"  ,"ணூ"  ,"ணெ"  ,"ணே"  ,"ணை"  ,"ணொ"  ,"ணோ"  ,"ணௌ",
"ந"  ,"நா"  ,"நி"  ,"நீ"  ,"நு"  ,"நூ"  ,"நெ"  ,"நே"  ,"நை"  ,"நொ"  ,"நோ"  ,"நௌ"  ,
"ம"  ,"மா"  ,"மி"  ,"மீ"  ,"மு"  ,"மூ"  ,"மெ"  ,"மே"  ,"மை"  ,"மொ"  ,"மோ"  ,"மௌ" ,
"ன"  ,"னா"  ,"னி"  ,"னீ"  ,"னு"  ,"னூ"  ,"னெ"  ,"னே"  ,"னை"  ,"னொ"  ,"னோ"  ,"னௌ", 
"ய"  ,"யா"  ,"யி"  ,"யீ"  ,"யு"  ,"யூ"  ,"யெ"  ,"யே"  ,"யை"  ,"யொ"  ,"யோ"  ,"யௌ", 
"ர"  ,"ரா"  ,"ரி"  ,"ரீ"  ,"ரு"  ,"ரூ"  ,"ரெ"  ,"ரே"  ,"ரை"  ,"ரொ"  ,"ரோ"  ,"ரௌ",
"ல"  ,"லா"  ,"லி"  ,"லீ"  ,"லு"  ,"லூ"  ,"லெ"  ,"லே"  ,"லை"  ,"லொ"  ,"லோ"  ,"லௌ" ,
"வ"  ,"வா"  ,"வி"  ,"வீ"  ,"வு"  ,"வூ"  ,"வெ"  ,"வே"  ,"வை"  ,"வொ"  ,"வோ"  ,"வௌ" , 
"ழ"  ,"ழா"  ,"ழி"  ,"ழீ"  ,"ழு"  ,"ழூ"  ,"ழெ"  ,"ழே"  ,"ழை"  ,"ழொ"  ,"ழோ"  ,"ழௌ" ,
    "ள"  ,"ளா"  ,"ளி"  ,"ளீ"  ,"ளு"  ,"ளூ"  ,"ளெ"  ,"ளே"  ,"ளை"  ,"ளொ"  ,"ளோ"  ,"ளௌ"};

    
    final static TreeSet<String> uyir_letter_set = new TreeSet( Arrays.asList(uyir_letters) );
    final static TreeSet<String> grantha_agaram_set = new TreeSet( Arrays.asList(grantha_agaram_letters) );
    final static TreeSet<String> accent_symbol_set = new TreeSet( Arrays.asList(accent_symbol_letters) );
    
    public static HashMap<String,Object> get_length(String text) {
        List<String> letters = utf8.get_letters(text);
        int length = letters.size();
        HashMap<String,Object> d = new HashMap();
        d.put("length", length);
        d.put("letters", letters);
        return d;
    }
    
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
        return utf8.uyir_letters.length;
    }
    public static int ayudha_len() {
        return 1;
    }
    public static int accent_len() {
        return utf8.accent_symbol_letters.length;
    }
    public static int grantha_agaram_len() {
        return utf8.grantha_agaram_letters.length;
    }
    public static int mei_len() {
        return utf8.mei_letters.length;
    }
    public static int agaram_len() {
        return utf8.mei_len();
    }
    
}
