/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */

package com.tamil;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.logging.*;

public class Numeral {	
	public static NumeralInfo num2tamilstr(double value) throws Exception {
		return IndianNumeral.toString(value);
	};
};

class StringUtils {
	public static String join(String[] strings, String separator) {
		final int startIndex = 0;
	    StringBuffer sb = new StringBuffer();
	    for (int i=startIndex; i < strings.length; i++) {
	        if (i != startIndex) sb.append(separator);
	        sb.append(strings[i]);
	    }
	    return sb.toString();
	}
};

class IndianNumeral {			
		private static Logger Log = Logger.getLogger("com.tamil.Numeral");
		
		final static String [] units = {"பூஜ்ஜியம்","ஒன்று","இரண்டு","மூன்று","நான்கு","ஐந்து","ஆறு", "ஏழு","எட்டு","ஒன்பது", "பத்து"}; // 0-10
		final static String [] teens = {"பதினொன்று"," பனிரண்டு","பதிமூன்று","பதினான்கு","பதினைந்து","பதினாறு","பதினேழு","பதினெட்டு","பத்தொன்பது"};// 11-19    
		final static String [] tens = {"பத்து","இருபது","முப்பது","நாற்பது","ஐம்பது","அறுபது","எழுபது","எண்பது","தொன்னூறு"}; //# 10-90
		final static String [] tens_suffix = {"இருபத்தி","முப்பத்தி","நாற்பத்தி","ஐம்பத்தி","அறுபத்தி","எழுபத்தி","எண்பத்தி","தொன்னூற்றி"}; // # 10+-90+    
		final static String [] hundreds = {"நூறு","இருநூறு","முன்னூறு","நாநூறு","ஐநூறு","அறுநூறு","எழுநூறு","எண்ணூறு","தொள்ளாயிரம்"};   // #100 - 900
		final static String [] hundreds_suffix = {"நூற்றி","இருநூற்றி","முன்னூற்று","நாநூற்று","ஐநூற்று","அறுநூற்று","எழுநூற்று","எண்ணூற்று","தொள்ளாயிரத்து"}; //#100+ - 900+
		    
		final static String one_thousand_prefix = "ஓர்";
		final static String [] thousands = {"ஆயிரம்","ஆயிரத்தி"};
		
		final static String one_prefix = "ஒரு";
		final static String  [] lakh = {"இலட்சம்","இலட்சத்தி"};
		final static String [] crore = {"கோடி","கோடியே"};
		
		final static String pulli = "புள்ளி";
		    
		final static double n_one = 1.0;
		final static double n_ten = 10.0;
		final static double n_hundred = 100;
		final static double n_thousand = 1000;
		final static double n_lakh = 100.0*n_thousand;
		final static double n_crore = (100.0*n_lakh);
		
		final static HashMap<Object,String[]> suffix_base = new HashMap<Object,String[]>();
	    static
	    {
	    		suffix_base.put( n_crore, crore);
				suffix_base.put( n_lakh, lakh);
				suffix_base.put( n_thousand, thousands);		
		};
					
	    final static HashMap<Object,String> suffix_file_map = new HashMap<Object,String>();
	    static
	    {
				suffix_file_map.put(n_crore,"crore");
				suffix_file_map.put(n_lakh,"lakh");
				suffix_file_map.put(n_thousand ,"thousands");			
	    };
	    
	    // for WAV filename
	    final static HashMap<Object,String[]> file_map = new HashMap<Object,String[]>();
	    static 
	    {
	    	file_map.put( n_crore, new String [] {"one_prefix","crore_0"});
	    	file_map.put( n_lakh, new String [] {"one_prefix","lakh_0"});
	    	file_map.put( n_thousand, new String []  {"one_thousand_prefix", "thousands_0"});
	    	file_map.put( n_hundred , new String [] {"hundreds_0"}); // #special
	    	file_map.put( n_ten , new String [] {"units_10"});
	    	file_map.put( n_one , new String [] {"units_1"});
	    }
	    
	    // for numeral
	    final static HashMap<Object,String[]> num_map = new HashMap<Object,String[]>();
	    static 
	    {
	    	num_map.put( n_crore, new String [] {one_prefix,crore[0]});
	    	num_map.put( n_lakh, new String [] {one_prefix,lakh[0]});
	    	num_map.put( n_thousand, new String []  {one_thousand_prefix, thousands[0]});
	    	num_map.put( n_hundred , new String [] {hundreds[0]}); // #special
	    	num_map.put( n_ten , new String [] {units[10]});
	    	num_map.put( n_one , new String [] {units[1]});
	    }
	    
	    final static double [] all_bases = {n_crore, n_lakh, n_thousand, n_hundred, n_ten,n_one};
	    
	    static NumeralInfo toString(double number) throws Exception {
			return toString(number,new NumeralInfo());
		}
		
		static NumeralInfo toString(double number,NumeralInfo rval) throws Exception {			
			Log.log(Level.INFO,"number => "+Double.toString(number));
			
			if ( number < 0.0 ) {
				throw new Exception("num2tamilstr does not handle -ve inputs");
			} else if ( number > 1e12 ) {
				throw new Exception("num2tamilstr input is too large");  
			}
					
			// handle fractional parts and exit
		    if (( number > 0.0) && (number < 1.0)) {
		    	rval.add(IndianNumeral.pulli,"pulli");
		        String number_str = Double.toString(number).replace("0.","");
		        for(int idx=0; idx < number_str.length(); idx++ ) {
		        	String digit = number_str.substring(idx,idx+1);		       
		        	Log.log(Level.INFO, "dbl value frac/digit -> "+digit);
		            rval.add(  IndianNumeral.units[Integer.valueOf(digit)%units.length], "units_"+digit );		            
		        }
		        return rval;		    
		    };
			
		    List<Double> allowed_bases = new ArrayList<Double>();
		    
		    //filter : allowed bases		  
		    for(int itr = 0; itr < all_bases.length; itr++) {
		    	double base = all_bases[itr];
		    	if ( number >= base) {
		    		allowed_bases.add(Double.valueOf(base));
		    		break;
		    	}
		    };
		    
		    
    	    /**
				core algorithm for the integral part of the number
		   */
		    final int itr=0;
		    if ( !allowed_bases.isEmpty() ) {
		    	Double n_base_dbl = allowed_bases.get(itr);
		    	double n_base = n_base_dbl.doubleValue();
		    	if( number == n_base ) {
		    		String numeral = StringUtils.join(IndianNumeral.num_map.get(n_base_dbl), " ");
		    		
		    		String [] values = IndianNumeral.file_map.get( n_base_dbl );
		    		if ( values.length == 1 ) {
		    			rval.add( numeral, values[0] );
		    		} else {
		    			for( int itr2 = 0; itr2 < values.length -2 ; itr2++) {
		    				rval.filenames.add(values[itr2]);
		    			}
		    			rval.add( numeral, values[values.length-1]);
		    		}
		    		return rval;
		    	}
		    	
		    	double quotient_number = Math.floor( number/n_base );
		    	double residue_number = number - n_base*quotient_number;
		    	boolean residue_is_zero = Math.abs(residue_number) <= Double.MIN_NORMAL*50.0;
		    	
		    	if ( n_base == IndianNumeral.n_one ) {  
		    		Log.log(Level.INFO,"units --->");
		    		int integer_part = (int) number%10;
		    		double frac = number - (double) integer_part;
		    		boolean frac_is_zero = (Math.abs(frac) <= Double.MIN_NORMAL*50.0);
		    		
		    		if ( !frac_is_zero) {
		    			// pure fractional		    			
		    			rval.add( IndianNumeral.units[integer_part] , "units_"+Integer.toString(integer_part) );		    		
		    			IndianNumeral.toString(frac,rval);
		    			return rval;
		    		} else {
		    			//pure integer
		    			rval.add( IndianNumeral.units[integer_part], "units_"+Integer.toString(integer_part));
		    			return rval;
		    		}
		    		
		    	} else if ( n_base == IndianNumeral.n_ten ) {
		    		
		    		if ( residue_is_zero) {
		                rval.add( IndianNumeral.tens[(int)quotient_number-1], "tens_"+Integer.toString((int)(quotient_number-1)));
		                return rval;
		    		}
		    		
		            if ( number < 20.0 ) {		                
		                rval.add(IndianNumeral.teens[(int)number-10-1],"teens_"+Integer.toString((int)number-10-1));
		                return rval;
		            }
		            
		            rval.add(IndianNumeral.tens_suffix[(int)quotient_number-2],"tens_suffix_"+Integer.toString((int)quotient_number-2));		            
		    	} else if ( n_base == IndianNumeral.n_hundred ) {
		    	    if ( residue_is_zero ) {
		                rval.add( IndianNumeral.hundreds[(int)quotient_number-1], "hundreds_"+Integer.toString((int)quotient_number-1));
		                return rval;
		    	    }
		            rval.add( IndianNumeral.hundreds_suffix[(int)quotient_number-1],"hundreds_suffix_"+Integer.toString((int)quotient_number-1) );
		    	} else {
		    		if ( quotient_number == 1.0 ) {
		    			if ( n_base == IndianNumeral.n_thousand ) {
		    				rval.add(IndianNumeral.one_thousand_prefix, "one_thousand_prefix");
		    			} else {
		    				rval.add(IndianNumeral.one_prefix, "one_prefix");
		    			}
		    		} else {
		    			IndianNumeral.toString(quotient_number,rval);
		    		}
		    	}
		    	
		    	String suffix;
		    	                    
		    	if ( n_base >= IndianNumeral.n_thousand ) {
		    		String [] sfx_base_values = IndianNumeral.suffix_base.get(n_base_dbl);		    	
		    		suffix = sfx_base_values[ (residue_number >= 1.0) ? 1 : 0 ];		    		
		    		String suffix_filename = IndianNumeral.suffix_file_map.get( n_base_dbl ) +"_"+
		    						  Integer.toString( (residue_number >= 1) ? 1: 0 );
		    		
		    		rval.add(suffix,suffix_filename);
		    		
		    		if ( residue_number == 0.0 )
		    			return rval;
		    	}
		    	
		    	IndianNumeral.toString( residue_number, rval);
		    	return rval;
		    }
		    
		    //number has to be 0
		    rval.add(units[0], "units_0");
		    return rval;
		}
};
