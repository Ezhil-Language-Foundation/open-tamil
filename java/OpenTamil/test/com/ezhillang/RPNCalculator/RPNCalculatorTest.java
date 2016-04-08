/*
 * (C) 2015-2016 Muthu Annamalai
 * This test + files are part of open-tamil Java package
 */
package com.ezhillang.RPNCalculator;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import junit.framework.TestCase;

/**
 *
 * @author muthu
 */
public class RPNCalculatorTest extends TestCase {

    //basic trig: C^(0) + S^(0) =  1

    String pi2str = Double.toString(Math.PI);
    String quart_pi2str = Double.toString(Math.PI / 4);

    public RPNCalculatorTest(String testName) {
        super(testName);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
    }

    @Override
    protected void tearDown() throws Exception {
        super.tearDown();
    }

    public void test_patterns() throws Exception {
        Pattern p = Pattern.compile("\\s+");
        String[] chunks = p.split("123 + 456 - 10 ^ 2");
        for (String s : chunks) {
            System.out.println(s + "|" + s.length());
        }
        test_pair(chunks, 479.00, true);
        //test_pair(chunks,100,true); 
    }

    public void tests_passing() throws Exception {
        // 1 + 2^5 - 2 = 1  + 32 - 2 = 31
        test_pair(new String[]{"1", "+", "2", "^", "5", "-", "2"}, 31);

        //associativity of power should add up
        test_pair(new String[]{"2", "^", "3"}, 8.0);
        test_pair(new String[]{"2", "^", "3", "+", "-1"}, 7.0);
        test_pair(new String[]{"3", "^", "2"}, 9.0);
        test_pair(new String[]{"3", "^", "2", "+", "1"}, 10.0);

        //tan
        test_pair(new String[]{"tan", quart_pi2str, "*", "tan", quart_pi2str}, 1.0, !true);//verbose		
        test_pair(new String[]{"tan", pi2str}, 0.0, false);//verbos

        //basic trig: C^(0) + S^(0) =  1		
        test_pair(new String[]{"sin", pi2str, "*", "sin", pi2str}, 0.0);//verbose
        test_pair(new String[]{"sin", pi2str, "*", "sin", pi2str, "+", "cos", "3.1415", "*", "cos", "3.1415"}, 1.0, false);//verbose

		//test brackets
        //test_pair(new String [] {"(","5","-","3",")","*","2"},4);
        test_pair(new String[]{"log10", "10"}, 1);
        test_pair(new String[]{"log", Double.toString(Math.E)}, 1.0);

        test_pair(new String[]{"55", "+", "95", "-", "10"}, 140.0);
        test_pair(new String[]{"55", "%", "100.0", "-", "10"}, 45.0);
        test_pair(new String[]{"5", "*", "4", "-", "3"}, +17.0);
        test_pair(new String[]{"-37", "-", "10", "-", "5"}, -52.0);
        test_pair(new String[]{"100", "/", "10", "/", "5"}, 2.0);
        test_pair(new String[]{"100", "/", "10", "-", "1", "+", "1", "/", "5"}, 9.2);

        //sub is left associative
        test_pair(new String[]{"5", "-", "6", "*", "7", "-", "10"}, -47);
		//String [] chunks = {"(","5","-","6",")","*","(","7","-","10",")"}; //3

        //% % and / are also left associative
        test_pair(new String[]{"5", "%", "10", "%", "20"}, 250);
    }

    static void test_pair(String[] chunks, double expected_val) throws Exception {
        test_pair(chunks, expected_val, false);
    }

    static void test_pair(String[] chunks, double expected_val, boolean verbose) throws Exception {
        List<Token> toks = new ArrayList<Token>();
        for (String chunk : chunks) {
            toks.add(Token.parseToken(chunk));
            if (verbose) {
                System.out.println(toks.get(toks.size() - 1).toString());
            }
        }
        RPNCalculator rpnc = new RPNCalculator(toks);
        double actual = rpnc.eval();
        if (verbose || true) {
            System.out.println("Testing => " + chunks[0] + chunks[1] + "|actual =>" + actual + "| expected => " + expected_val);
        }

        boolean isExact = Double.compare(actual, expected_val) == 0;
        boolean isAppx = (Math.abs(expected_val - actual) < 1e-6);
        boolean neither_appx_nor_exact = !(isExact || isAppx);

        if (neither_appx_nor_exact) {
            throw new Exception("Failed testing => " + chunks[0] + chunks[1] + "|actual =>" + actual + "| expected => " + expected_val);
        }
    }
}
