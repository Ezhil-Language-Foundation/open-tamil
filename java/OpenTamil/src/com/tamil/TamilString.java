/* (C) 2016 Muthu Annamalai
* 
*/
package com.tamil;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/** Class contains a list of UTF-8 letters as ArrayList<String> but provides interfaces like a String.
 * including a comparator methods etc.
 * @author muthu
 */
public class TamilString extends ArrayList<String> {    
    public static class TamilStringComparator implements Comparator<TamilString> {
        @Override
        public int compare(TamilString lA, TamilString lB) {
            int pos1, pos2;
            for(int itr=0; itr<Math.min(lA.length(),lB.length()); itr++) {
                pos1 = lA.letterIndexOf(itr);
                pos2 = lB.letterIndexOf(itr);
                if (pos1 == pos2 ) {
                   if ( pos1 != -1 )
                       continue;
                   if ( lA.get(itr).equals( lB.get(itr) ) )
                       continue;
                   return lA.get(itr).compareTo( lB.get(itr) );
                }
                return (pos1>pos2) ? 1: - 1;
            }

            // both are same by this point
            return 0;
        }
    }
    public static final TamilStringComparator comparator = new TamilStringComparator();
    private String m_orig_string;
    public TamilString(String obj) {
        super(utf8.get_letters(obj));
        m_orig_string = obj;
    }
    
    @Override
    public String toString() {
        return m_orig_string;
    }
    
    // return the index of letter @ position 'pos' within the tamil letters array 
    int letterIndexOf(int pos) {
        return utf8.all_tamil_letters.indexOf(get(pos));
    }
    
    public int length() {
        return super.size();
    }
}
