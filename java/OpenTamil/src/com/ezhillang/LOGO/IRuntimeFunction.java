/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.ezhillang.LOGO;

/**
 *
 * @author muthu
 */
public interface IRuntimeFunction {
    void evaluate(Interpreter m_int, String function, Object[] args);
}
