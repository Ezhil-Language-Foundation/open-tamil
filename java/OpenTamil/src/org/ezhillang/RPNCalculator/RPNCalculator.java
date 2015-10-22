/*
 * (c) 2015, Muthiah Annamalai
 */

package org.ezhillang.RPNCalculator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;

import org.ezhillang.RPNCalculator.Token.Kinds;

//represent a token within the calculator

class Operand extends Token {
	Operand(String raw, double val) {
		super(raw,val);
	}
	
	Operand(Token tok) {				
		super(tok);
		Token.Kinds kind = tok.getKind();
		assert kind == Token.Kinds.NUMBER;
	}
}

class Operator extends Token {
	Operator(Token tok) {				
		super(tok);
		
		Token.Kinds kind = tok.getKind(); 
		//token kind cannot be number
		assert kind != Token.Kinds.NUMBER;
		this.m_val = Double.NaN;		
	}
}

public class RPNCalculator {
	List<Token> m_toks;
	Stack<Operand> operand_stack;
	Stack<Operator> operator_stack;
	
	public RPNCalculator(List<Token> toks) {
		m_toks = toks;
		operand_stack  = new Stack<Operand>();
		operator_stack  = new Stack<Operator>();
	}
	
	protected Operand simple_eval() throws Exception {
		Operator op = operator_stack.pop();
		Token.Kinds op_kind = op.getKind();
		
		Operand op_B = null, op_result = null;
		Operand op_A = operand_stack.pop();
		double dbl_op_A = op_A.getNumericValue(),dbl_op_B = Double.NaN,result = Double.NaN;
		
		if ( op_kind == Token.Kinds.ADD_OP ) {
			op_B = operand_stack.pop();
			dbl_op_B = op_B.getNumericValue();
			result = dbl_op_A + dbl_op_B;				
		} else if (  op_kind == Token.Kinds.SUB_OP ) {
			op_B = operand_stack.pop();				
			dbl_op_B = op_B.getNumericValue();
			result = dbl_op_B - dbl_op_A;
		} else if ( op_kind == Token.Kinds.MUL_OP ) {
			op_B = operand_stack.pop();				
			dbl_op_B = op_B.getNumericValue();
			result = dbl_op_A * dbl_op_B;				
		} else if ( op_kind == Token.Kinds.DIV_OP ) {
			op_B = operand_stack.pop();				
			dbl_op_B = op_B.getNumericValue();
			result = dbl_op_A / dbl_op_B;
		} else if ( op_kind == Token.Kinds.PERC_OP ) {
			op_B = operand_stack.pop();
			dbl_op_B = op_B.getNumericValue();
			result = (100.00*dbl_op_B)/dbl_op_A ;
		}
		op_result = new Operand(Double.toString(result),result);
		return op_result;
	}
	
	double eval() throws Exception {						
		
		Iterator<Token> tok_itr = m_toks.iterator();
		while( tok_itr.hasNext() ) {
			Token tok = tok_itr.next();
			if ( tok.m_kind == Token.Kinds.NUMBER ) {
				operand_stack.push(new Operand(tok));
				continue;
			}
			//no precedence yet. this tok is an operator
			operator_stack.push(new Operator(tok));
		}
		
		while( !operator_stack.isEmpty() ) {
			Operand op_result = this.simple_eval();
			operand_stack.push(op_result);
		}
		
		
		Operand val = operand_stack.pop();
		return val.getNumericValue();
	}
	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {		
		
		// TODO Auto-generated method stub
		//System.out.println("Hello World!");
		//String [] chunks = {"55","+","95","-","10"};
		//String [] chunks = {"55","%","100.0","-","10"};
		String [] chunks = {"5","*","4","-","3"};
		List<Token> toks = new ArrayList<Token>();
		for(String chunk:chunks) {
			toks.add( Token.parseToken(chunk) );
			System.out.println(toks.get(toks.size()-1).toString());
		}
		RPNCalculator rpnc = new RPNCalculator(toks);
		System.out.println(rpnc.eval());
		
	}

}
