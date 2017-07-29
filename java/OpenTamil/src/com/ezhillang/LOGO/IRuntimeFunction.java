package com.ezhillang.LOGO;

/**
 *
 * @author muthu
 */
public interface IRuntimeFunction {
    void evaluate(Interpreter m_int, String function, Object[] args)  throws Exception;
}
