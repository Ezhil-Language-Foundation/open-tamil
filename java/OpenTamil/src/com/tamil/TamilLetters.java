/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */

package com.tamil;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.lang.Integer;

public class TamilLetters extends HashMap<String,Object> {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String key_letters = "letters";
	private String key_length = "length";
	
	public TamilLetters() {
		this.put(key_letters, null );
		this.put(key_length, 0 );
	}
	
	public TamilLetters(List<String> letters,int length) {
		this.put(key_letters, letters );
		this.put(key_length, length );
	}
	
	@SuppressWarnings("unchecked")
	public List<String> getLetters() {
		return (List<String>) this.get(key_letters);
	}

	public int getLength() {
	    return Integer.valueOf(this.get(key_length).toString());
	}

	public static void sort(List<String> input) {
		Collections.sort(input, utf8.comparator);
		return;
	}
}
