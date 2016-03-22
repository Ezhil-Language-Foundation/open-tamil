/** include the sources for the com/tamil package from
// https://github.com/arcturusannamalai/open-tamil/blob/master/java/OpenTamil/src
*/
package com.tamil;


import java.util.HashMap;

import com.tamil.utf8;
import com.tamil.Numeral;

public class example {
  public static void main(String [] args) throws Exception {
      /* Example 1: Get length of a Tamil word */
      String inputWord = "எழில்",inputWord2 = "கட்டளை";
        
      HashMap<String,Object> actual = utf8.get_length(inputWord);
      System.out.println("Length of word "+ inputWord+ "= "+ actual.get("length") );
      
      /* Example 2: Get number of Tamil letters */
      //List<String> expected = Arrays.asList(new String [] {"எ","ழி","ல்"} );
        StringBuilder str_actual = new StringBuilder();
        for(String t : utf8.get_letters(inputWord)) {
            str_actual.append( t );
        }
       
        if ( !str_actual.equals(inputWord) ) 
          throw new Exception("this will never happen because open-tamil parsed the words for you!");
       
       /* Example 3: Convert number to a numeral */
      double number = 1011.0;
      /// you should see String numeral = "ஓர் ஆயிரத்தி பதினொன்று";
      System.out.println("running -> "+number);
	    String numeral = Numeral.num2tamilstr(number).getNumeral();
	    System.out.println(numeral);
  }
}
