/*
 ** (C) 2015 Muthiah Annamalai <ezhillang@gmail.com>
 ** This program is part of open-tamil library
 ** You may use this code under MIT License
 */

package com.tamil;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;

import com.tamil.Numeral;

import junit.framework.TestCase;

public class NumeralTest extends TestCase {

	protected void setUp() throws Exception {
		super.setUp();
	}

	protected void tearDown() throws Exception {
		super.tearDown();
	}
	
	public NumeralTest(String testName) {
	        super(testName);
	}

    public void test_teens(  ) throws Exception {
      	 // # 11-19
        String [] teens = {"பதினொன்று", " பனிரண்டு", "பதிமூன்று", "பதினான்கு", "பதினைந்து","பதினாறு", "பதினேழு", "பதினெட்டு", "பத்தொன்பது"};
        double start = 11.0;
		for(int idx=0; idx< teens.length; idx++) {
			String expected = teens[idx];
			runTest( start, expected );
			start += 1.0;
		}
	}
   
   public void test_100s() throws Exception {
        String [] hundreds = {"நூறு", "இருநூறு", "முன்னூறு", "நாநூறு","ஐநூறு", "அறுநூறு", "எழுநூறு", "எண்ணூறு", "தொள்ளாயிரம்"}; // #100 - 900
    	
        double start = 100.0;
		for(int idx=0; idx< hundreds.length; idx++) {
			String expected = hundreds[idx];
			runTest(start,expected);
			start += 100.0;
		}		
    }
    
	public void test_tens() throws Exception {
		//# 10-90
		String [] tens = {"பத்து", "இருபது", "முப்பது", "நாற்பது", "ஐம்பது","அறுபது", "எழுபது", "எண்பது", "தொன்னூறு"};
		String [] tens_actual = new String[tens.length];
		
		double start = 10.0;
		for(int idx=0; idx< tens.length; idx++) {
			tens_actual[idx] = Numeral.num2tamilstr(start).getNumeral();
			System.out.println(tens_actual[idx]);
			start += 10.0;
		}
		
		super.assertTrue(Arrays.equals(tens, tens_actual));
	}
	
	public void test_frac() throws Exception {
		double inputNumber = 1.375;
		String expected = "ஒன்று புள்ளி மூன்று ஏழு ஐந்து";
		runTest(inputNumber,expected);				
	}
	
	public void test_units() throws Exception {
		//# 0 - 10
		String [] units = {"பூஜ்ஜியம்", "ஒன்று", "இரண்டு", "மூன்று", "நான்கு","ஐந்து", "ஆறு", "ஏழு", "எட்டு", "ஒன்பது", "பத்து"};
		String [] units_actual = new String[units.length];
		
		double start = 0.0;
		for(int idx=0; idx< units.length; idx++) {
			units_actual[idx] = Numeral.num2tamilstr(start).getNumeral();
			System.out.println(units_actual[idx]);
			start += 1.0;
		}
		
		super.assertTrue(Arrays.equals(units, units_actual));
	}
	
	public void test_numerals() throws Exception {
		  // for numeral
	    final HashMap<Object,String> num_numeral = new HashMap<Object,String>();
    	num_numeral.put(0,"பூஜ்ஜியம்");
    	num_numeral.put(3060,"மூன்று ஆயிரத்தி அறுபது");
    	num_numeral.put(1,"ஒன்று");
    	num_numeral.put(2, "இரண்டு");
    	num_numeral.put(3, "மூன்று");
    	num_numeral.put(5, "ஐந்து");
    	num_numeral.put(10, "பத்து");
    	num_numeral.put(11, "பதினொன்று");
    	num_numeral.put(17, "பதினேழு");
    	num_numeral.put(19, "பத்தொன்பது");
    	num_numeral.put(20, "இருபது");
    	num_numeral.put(21, "இருபத்தி ஒன்று");
    	num_numeral.put(1051, "ஓர் ஆயிரத்தி ஐம்பத்தி ஒன்று");
    	num_numeral.put(100000, "ஒரு இலட்சம்");
    	num_numeral.put(100001, "ஒரு இலட்சத்தி ஒன்று");
    	num_numeral.put(10011, "பத்து ஆயிரத்தி பதினொன்று");
    	num_numeral.put(49, "நாற்பத்தி ஒன்பது");
    	num_numeral.put(50, "ஐம்பது");
    	num_numeral.put(55, "ஐம்பத்தி ஐந்து");
    	num_numeral.put(1000001, "பத்து இலட்சத்தி ஒன்று");
    	num_numeral.put(90, "தொன்னூறு");
    	num_numeral.put(99, "தொன்னூற்றி ஒன்பது");
    	num_numeral.put(100, "நூறு");
    	num_numeral.put(101, "நூற்றி ஒன்று");
    	num_numeral.put(1000, "ஓர் ஆயிரம்");
    	num_numeral.put(111, "நூற்றி பதினொன்று");
    	num_numeral.put(1011, "ஓர் ஆயிரத்தி பதினொன்று");
    	
    	Iterator<Entry<Object, String>> entries = num_numeral.entrySet().iterator();
    	
	    String [] expected = new String [num_numeral.size()];
	    String [] actual = new String [expected.length];
	    
	    for(int idx=0; idx< num_numeral.size(); idx++) {
	    	Entry<Object, String> kv =  entries.next();	    	
	    	double number = Double.valueOf( kv.getKey().toString() );
	    	String expected_numeral = kv.getValue();
	    	
	    	System.out.println("running -> "+number);
	    	String numeral = Numeral.num2tamilstr(number).getNumeral();
	    	System.out.println(numeral);
	    	
	    	expected[idx] = expected_numeral;
	    	actual[idx] = numeral;	    	
	    }
	    
	    super.assertTrue(Arrays.equals(expected, actual));
	}	
	
	public void test_3_digitNumber() throws Exception {
		double inputNumber = 123.0;
		String expected = "நூற்றி இருபத்தி மூன்று";
		runTest(inputNumber,expected);
	}

	public void test_12_digitNumber() throws Exception {
		double inputNumber = 1e12;
		String expected = "ஒரு இலட்சம் கோடி";
		runTest(inputNumber,expected);
	}	
	
	public void test_maxno() throws Exception {
		double maxno = 1e12 - 1.0;
		String expected = "தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது கோடியே தொன்னூற்றி ஒன்பது இலட்சத்தி தொன்னூற்றி ஒன்பது ஆயிரத்தி தொள்ளாயிரத்து தொன்னூற்றி ஒன்பது";
		runTest(maxno,expected);
	}
    
	// Utility
	public void runTest(double inputNumber,String expected) throws Exception {				
		String actual = Numeral.num2tamilstr(inputNumber).getNumeral();
		System.out.println(actual);
		super.assertEquals(expected, actual);
	}

}
