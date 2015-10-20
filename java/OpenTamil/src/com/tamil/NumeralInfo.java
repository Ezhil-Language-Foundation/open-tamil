/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */

package com.tamil;

import java.util.ArrayList;
import java.util.List;

public class NumeralInfo {
	List<String> filenames;
	String numeral;
	private String use_spc = "";
	
	NumeralInfo(String numeral_in, List<String> filenames_in) {
		this.filenames = filenames_in;
		this.numeral = numeral_in;
	}
	
	public NumeralInfo() {
		this.filenames = new ArrayList<String>();
		this.numeral = new String();
	}
	
	void add(String numeral_bit, String file_name) {		
		this.filenames.add(file_name);		
		this.numeral += this.use_spc + numeral_bit;
		this.use_spc = " ";
	}
	
	public List<String> getFilenames() {
		return filenames;
	}

	public String getNumeral() {
		return numeral;
	}
};