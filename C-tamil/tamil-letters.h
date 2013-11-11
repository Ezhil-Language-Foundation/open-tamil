/*
 * Copyright (C) 2007 Muthiah Annamalai <gnumuthu@users.sf.net>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */


#ifndef _TAMIL_LETTERS_H_
#define _TAMIL_LETTERS_H_

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define TA_ACCENT_LEN 13 /* 12 + 1*/
#define TA_AYUDHA_LEN 1
#define TA_UYIR_LEN    12
#define TA_MEI_LEN 18
#define TA_AGARAM_LEN 18
#define TA_SANSKRIT_LEN 4
#define TA_UYIRMEI_LEN (216) /* 18*12 */

/* List of letters you can use */
#define TA_AGARAM_k		Tamil_Agaram_Letters(TA_Agaram_k)
#define TA_AGARAM_c		Tamil_Agaram_Letters(TA_Agaram_s)
#define TA_AGARAM_t		Tamil_Agaram_Letters(TA_Agaram_t)
#define TA_AGARAM_th	Tamil_Agaram_Letters(TA_Agaram_th)
#define TA_AGARAM_pa	Tamil_Agaram_Letters(TA_Agaram_pa)
#define TA_AGARAM_Ra	Tamil_Agaram_Letters(TA_Agaram_Ra)
#define TA_AGARAM_gy	Tamil_Agaram_Letters(TA_Agaram_gy)
#define TA_AGARAM_Gy	Tamil_Agaram_Letters(TA_Agaram_Gy)
#define TA_AGARAM_na	Tamil_Agaram_Letters(TA_Agaram_na)
#define TA_AGARAM_nth	Tamil_Agaram_Letters(TA_Agaram_nth)
#define TA_AGARAM_ma	Tamil_Agaram_Letters(TA_Agaram_ma)
#define TA_AGARAM_na	Tamil_Agaram_Letters(TA_Agaram_na)
#define TA_AGARAM_ya	Tamil_Agaram_Letters(TA_Agaram_ya)
#define TA_AGARAM_ra	Tamil_Agaram_Letters(TA_Agaram_ra)
#define TA_AGARAM_la	Tamil_Agaram_Letters(TA_Agaram_la)
#define TA_AGARAM_va	Tamil_Agaram_Letters(TA_Agaram_va)
#define TA_AGARAM_zha	Tamil_Agaram_Letters(TA_Agaram_zha)
#define TA_AGARAM_La	Tamil_Agaram_Letters(TA_Agaram_La)

#define TA_MEI_ik	Tamil_Mei_Letters(TA_Mei_ik)
#define TA_MEI_ic	Tamil_Mei_Letters(TA_Mei_ic)
#define TA_MEI_it	Tamil_Mei_Letters(TA_Mei_it)
#define TA_MEI_ith	Tamil_Mei_Letters(TA_Mei_ith)
#define TA_MEI_ip	Tamil_Mei_Letters(TA_Mei_ip)
#define TA_MEI_iR	Tamil_Mei_Letters(TA_Mei_iR)
#define TA_MEI_ing	Tamil_Mei_Letters(TA_Mei_ing)
#define TA_MEI_inG	Tamil_Mei_Letters(TA_Mei_inG)
#define TA_MEI_inn	Tamil_Mei_Letters(TA_Mei_inn)
#define TA_MEI_inth	Tamil_Mei_Letters(TA_Mei_inth)
#define TA_MEI_im	Tamil_Mei_Letters(TA_Mei_im)
#define TA_MEI_in	Tamil_Mei_Letters(TA_Mei_in)
#define TA_MEI_iy	Tamil_Mei_Letters(TA_Mei_iy)
#define TA_MEI_ir	Tamil_Mei_Letters(TA_Mei_ir)
#define TA_MEI_il	Tamil_Mei_Letters(TA_Mei_il)
#define TA_MEI_iv	Tamil_Mei_Letters(TA_Mei_iv)
#define TA_MEI_izh	Tamil_Mei_Letters(TA_Mei_izh)
#define TA_MEI_iL	Tamil_Mei_Letters(TA_Mei_iL)

#define TA_UYIR_a	Tamil_Uyir_Letters(TA_Uyir_a)
#define TA_UYIR_A	Tamil_Uyir_Letters(TA_Uyir_A)
#define TA_UYIR_e	Tamil_Uyir_Letters(TA_Uyir_e)
#define TA_UYIR_E	Tamil_Uyir_Letters(TA_Uyir_E)
#define TA_UYIR_u	Tamil_Uyir_Letters(TA_Uyir_u)
#define TA_UYIR_U	Tamil_Uyir_Letters(TA_Uyir_U)
#define TA_UYIR_ya	Tamil_Uyir_Letters(TA_Uyir_Ya)
#define TA_UYIR_Ya	Tamil_Uyir_Letters(TA_Uyir_Ya)
#define TA_UYIR_i	Tamil_Uyir_Letters(TA_Uyir_i)
#define TA_UYIR_o	Tamil_Uyir_Letters(TA_Uyir_o)
#define TA_UYIR_O	Tamil_Uyir_Letters(TA_Uyir_O)
#define TA_UYIR_Ow	Tamil_Uyir_Letters(TA_Uyir_Ow)

/* Enumerations */

/*
 "k","க", "ik","க்",
 "s","ச","ic", "ச்",
 "t","ட","it","ட்",
 "th","த","ith","த்",
 "pa","ப", "ip","ப்",
 "Ra","ற","iR","ற்",
 
 "gy","ஞ","ing","ஞ்",
 "Gy","ங","inG", "ங்",
 "nna","ண","inn","ண்",
 "nth","ந","inth","ந்",
 "ma","ம", "im","ம்",
 "na","ன","in","ன்",
  
 "ya","ய","iy","ய்",
 "ra","ர","ir","ர்",
 "la","ல","il","ல்",
 "va","வ","iv","வ்",
 "zha","ழ","izh","ழ்",
 "La","ள","iL","ள்",
*/

/* This enumerator can index Tamil_Uyir_Letters */
enum TamilUyirLetters{
	TA_Uyir_a,TA_Uyir_A,TA_Uyir_e,TA_Uyir_E,
	TA_Uyir_u,TA_Uyir_U,TA_Uyir_ya,TA_Uyir_Ya,
	TA_Uyir_i,TA_Uyir_o,TA_Uyir_O,TA_Uyir_Ow 
};

enum TamilAgaramLetters {
	TA_Agaram_k, TA_Agaram_s, TA_Agaram_t,
	TA_Agaram_th, TA_Agaram_pa, TA_Agaram_Ra,
	TA_Agaram_gy, TA_Agaram_Gy, TA_Agaram_nna,
	TA_Agaram_nth, TA_Agaram_ma, TA_Agaram_na,
	TA_Agaram_ya, TA_Agaram_ra, TA_Agaram_la,
	TA_Agaram_va, TA_Agaram_zha, TA_Agaram_La
};

enum TamilMeiLetters {
	TA_Mei_ik, TA_Mei_ic, TA_Mei_it,
	TA_Mei_ith, TA_Mei_ip, TA_Mei_iR,
	TA_Mei_ing, TA_Mei_inG, TA_Mei_inn,
	TA_Mei_inth, TA_Mei_im, TA_Mei_in,
	TA_Mei_iy, TA_Mei_ir, TA_Mei_il, TA_Mei_iv,
	TA_Mei_izh, TA_Mei_iL
};

/* Total size of Table */
long int TamilSanskrit_Total_Size(void);

/* Lookup the index */
const char *TamilSanskrit_Letter(int idx);

/* Letter Accessor Functions */
const char *Tamil_Uyir_Letters(int idx);
const char *Tamil_Agaram_Letters(int idx);
const char *Tamil_Mei_Letters(int idx);
const char *Tamil_UyirMei_Letters(int mei_idx,int uyir_index);

#endif /* _TAMIL_LETTERS_H_ */
