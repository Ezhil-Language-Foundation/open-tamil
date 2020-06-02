/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.urbantamil;

import com.tamil.TamilString;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.TreeSet;
import java.util.stream.Stream;

/**
 * A class to quickly l
 * @author muthu
 */
public class DictionaryWordList extends ArrayList<TamilString> {
    private File m_file;
    
    public DictionaryWordList(File ref_word_list) {
        super();//TamilString.comparator
        m_file = ref_word_list;
    }
    
    // load the words from the file m_file and return the loaded words
    public long load() throws FileNotFoundException {
        FileReader fs = new FileReader(m_file);
        BufferedReader bis = new BufferedReader(fs);
        try {
            String word;
            while((word = bis.readLine()) != null) {
                word = word.trim();
                if ( word.isEmpty() || word.length() < 1 )
                    continue;
                add(new TamilString(word));
            }
        } catch (IOException ioe) {
            //pass
        }
        
        return size();
    }
}
