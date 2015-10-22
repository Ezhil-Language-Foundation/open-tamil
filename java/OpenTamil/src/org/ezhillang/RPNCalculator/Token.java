package org.ezhillang.RPNCalculator;

public class Token {	
	public static enum Kinds { NUMBER, LPAREN, RPAREN, FUNCTION, ADD_OP, SUB_OP, DIV_OP, MUL_OP, PERC_OP };
	protected Kinds m_kind;
	protected String m_raw;
	
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
		String lean_chunk = chunk.trim();
		if (lean_chunk == "+") {
			return new Token(lean_chunk,Kinds.ADD_OP);
		} else if ( lean_chunk == "-") {
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
		}
		
		try { 
			//most likely a number
			double dval = Double.valueOf(lean_chunk);
			return new Token(lean_chunk,dval);
		} catch (Exception e) {
			e.printStackTrace();
			throw new Exception("Cannot find matching token! Functions are not supported yet");
		}
	}
	
	public Kinds getKind() {
		return m_kind;
	}
	
	public void setKind(Kinds kind) {
		this.m_kind = kind;
	}	
}
