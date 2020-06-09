package com.ezhillang.RPNCalculator;

public class Token {	
	public static enum Kinds { NUMBER, LPAREN, RPAREN, FUNCTION, ADD_OP, SUB_OP, 
		DIV_OP, MUL_OP, PERC_OP, LOG_OP, LOG10_OP, EXP_OP,SIN_OP,COS_OP,TAN_OP,
		ASIN_OP,ATAN_OP,ACOS_OP,POWER_OP,UNARY_MINUS_OP};
	protected Kinds m_kind;
	protected String m_raw;
	public static boolean DEBUG = false;
	
	public static boolean isBinaryOp(Kinds k) {
		final Kinds [] unary_ops = new Kinds [] { Kinds.ADD_OP,Kinds.SUB_OP,Kinds.MUL_OP,Kinds.DIV_OP,
				Kinds.POWER_OP}; 
		for( int itr=0; itr <unary_ops.length; itr++) {
			if ( unary_ops[itr] == k)
				return true;
		}
		return false;
	}
	
	//number is not an OP
	public static boolean isUnaryOp(Kinds k) {
		final Kinds [] unary_ops = new Kinds [] { Kinds.LOG_OP, Kinds.LOG10_OP, Kinds.EXP_OP,Kinds.SIN_OP,Kinds.COS_OP,Kinds.TAN_OP,
				Kinds.ASIN_OP,Kinds.ATAN_OP,Kinds.ACOS_OP, Kinds.UNARY_MINUS_OP}; 
		for( int itr=0; itr <unary_ops.length; itr++) {
			if ( unary_ops[itr] == k)
				return true;
		}
		return false;
	}
	
	public static boolean isPrecedent(Token t1, Token t2) {
		
		Kinds first = t1.getKind(), second = t2.getKind();
		
		if ( DEBUG )
			System.out.println(t1+"?"+t2);
		
		assert first != Kinds.NUMBER && second != Kinds.NUMBER;
		
		//unary ops take precedencce
		if ( first != Kinds.RPAREN && second != Kinds.RPAREN ) {
			if ( isUnaryOp(first) )
				return true;
			if ( isUnaryOp(second))
				return false;
		}
		
		int rank_A = 0,rank_B=0;
		if ( first == Kinds.RPAREN) {
			rank_A = 12;
		} else if(first == Kinds.POWER_OP ) {
			rank_A = 11;
	    } else if(first == Kinds.DIV_OP || first == Kinds.MUL_OP ) {
			rank_A = 10;
		} else if (first == Kinds.PERC_OP) {
			rank_A = 9;
		} else if ( first == Kinds.SUB_OP) {
			rank_A = 8;
		} else if ( first == Kinds.LPAREN ) {
			rank_A = 7;
		} else {
			rank_A = 0;
		}
		
		if ( second == Kinds.RPAREN ) {
			rank_B = 12;
		} else if(second == Kinds.POWER_OP ) {
			rank_B = 11;
	    } else if(second == Kinds.DIV_OP || second == Kinds.MUL_OP ) {
			rank_B = 10;
		} else if (second == Kinds.PERC_OP) {
			rank_B = 9;
		} else if ( second == Kinds.SUB_OP) {
			rank_B = 8;
		} else if ( second == Kinds.LPAREN ) {
			rank_B = 7;
		} else {
			rank_B = 0;
		}
		
		if ( first == Kinds.SUB_OP && second == Kinds.SUB_OP )
			return true;
		
		return rank_A >= rank_B;
	}
	
	public String getRawToken() {
		return m_raw;
	}

	protected double m_val;
	
	public String toString(){
		return "Token("+m_raw+","+m_kind.toString()+")";
	}
	
	public Token(Token that) {
		this.m_kind = that.m_kind;
		this.m_raw = that.m_raw;
		this.m_val = that.m_val;
	}
	
	protected Token(String chunk, Kinds kind) {
		this.m_raw = chunk;
		this.m_kind = kind;
		this.m_val = Double.NaN;
	}
	
	protected Token(String chunk, double dval) {
		this.m_raw = chunk;
		this.m_kind = Kinds.NUMBER;
		this.m_val = dval;
	}
	
	public double getNumericValue() {
		assert this.m_kind == Kinds.NUMBER;
		return this.m_val;
	}
	
	public static Token parseToken(String chunk) throws Exception {
		String lean_chunk = chunk.trim().toLowerCase();
		if (lean_chunk.equals( "+" ) ) {
			return new Token(lean_chunk,Kinds.ADD_OP);
		} else if ( lean_chunk.equals("-") ) {
			return new Token(lean_chunk,Kinds.SUB_OP);
		} else if ( lean_chunk == "*") {
			return new Token(lean_chunk,Kinds.MUL_OP);
		} else if ( lean_chunk == "/") {
			return new Token(lean_chunk,Kinds.DIV_OP);
		} else if ( lean_chunk == "%") {
			return new Token(lean_chunk,Kinds.PERC_OP);
		} else if ( lean_chunk == "(" ) {
			return new Token(lean_chunk,Kinds.LPAREN);
		} else if ( lean_chunk == ")" ) {
			return new Token(lean_chunk,Kinds.RPAREN);			
		} else if ( lean_chunk == "log10" ) {
			return new Token(lean_chunk,Kinds.LOG10_OP);
		} else if ( lean_chunk == "log" ) {
			return new Token(lean_chunk,Kinds.LOG_OP);			
		} else if ( lean_chunk == "exp" ) {
			return new Token(lean_chunk,Kinds.EXP_OP);		
		} else if ( lean_chunk == "sin" ) {
			return new Token(lean_chunk,Kinds.SIN_OP);		
		} else if ( lean_chunk  == "cos" ) {
			return new Token(lean_chunk,Kinds.COS_OP);
		} else if ( lean_chunk == "tan" ) {
			return new Token(lean_chunk,Kinds.TAN_OP);		
		} else if ( lean_chunk == "asin" ) {
			return new Token(lean_chunk,Kinds.ASIN_OP);		
		} else if ( lean_chunk  == "acos" ) {
			return new Token(lean_chunk,Kinds.ACOS_OP);
		} else if ( lean_chunk == "atan" ) {
			return new Token(lean_chunk,Kinds.ATAN_OP);		
		} else if ( lean_chunk.equals("^") ) {
			return new Token(lean_chunk,Kinds.POWER_OP);
		}
		
		System.out.println(lean_chunk+"==?=="+lean_chunk.length());
		//LOG10_OP, EXP_OP,SIN_OP,COS_OP,TAN_OP,ASIN_OP,ATAN_OP,ACOS_OP
		
		
		try { 
			//most likely a number
			double dval = Double.valueOf(lean_chunk);
			return new Token(lean_chunk,dval);
		} catch (Exception e) {
			e.printStackTrace();
			throw new Exception("Cannot find matching token for '"+ lean_chunk+ "'! Functions are not supported yet");
		}
	}
	
	public Kinds getKind() {
		return m_kind;
	}
	
	public void setKind(Kinds kind) {
		this.m_kind = kind;
	}	
}
