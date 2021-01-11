/**
 * (C) 2021, Ezhil Language Foundation.
 *  This file is part of Open-Tamil for Rust language.
 */

pub const uyir: [char;12] = ['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ'];
pub const vowel_a :char = 'அ';
pub const vowel_aa:char = 'ஆ';
pub const vowel_i :char = 'இ';
pub const vowel_ii:char = 'ஈ';
pub const vowel_u  :char= 'உ';
pub const vowel_uu:char = 'ஊ';
pub const vowel_e:char  =  'எ';
pub const vowel_ee:char = 'ஏ';
pub const vowel_ai:char = 'ஐ';
pub const vowel_o:char  = 'ஒ';
pub const vowel_oo:char = 'ஓ';
pub const vowel_au:char = 'ஔ';
pub const aytham_letter:char = 'ஃ';
pub const ayudha_letter:char = 'ஃ';

pub const kuril_letters: [char;5] = ['அ', 'இ', 'உ', 'எ', 'ஒ'];
pub const nedil_letters: [char;7] = ['ஆ', 'ஈ', 'ஊ', 'ஏ', 'ஓ','ஐ','ஔ'];
pub const dipthong_letters: [char;2] = ['ஐ','ஔ'];

pub const pronoun_letters:[char;3]=['அ','இ','உ'];
pub const suttezhuththu:&'static [char;3]=&pronoun_letters;

pub const questionsuffix_letters:[char;3]=['ஆ','ஏ','ஓ'];
pub const vinaaezhuththu:&'static [char;3]=&questionsuffix_letters;

pub const vallinam_letters:[&str;6] = ["க்", "ச்", "ட்", "த்", "ப்", "ற்"];
pub const mellinam_letters:[&str;6] = ["ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்"];
pub const idayinam_letters:[&str;6] = ["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"];

pub const mei_letters:[&str;18] = ["க்","ச்","ட்","த்","ப்","ற்",
           "ஞ்","ங்","ண்","ந்","ம்","ன்",
           "ய்","ர்","ல்","வ்","ழ்","ள்" ];

pub const accent_symbols:[&str;13] = ["","ா","ி","ீ","ு","ூ",
          "ெ","ே","ை","ொ","ோ","ௌ","ஃ"];

pub const accent_aa:&str = accent_symbols[1];
pub const accent_i:&str  = accent_symbols[2];
pub const accent_u:&str  = accent_symbols[3];
pub const accent_uu:&str = accent_symbols[4];
pub const accent_e:&str  = accent_symbols[5];
pub const accent_ee:&str = accent_symbols[6];
pub const accent_ai:&str = accent_symbols[7];
pub const accent_o:&str  = accent_symbols[8];
pub const accent_oo:&str = accent_symbols[9];
pub const accent_au:&str = accent_symbols[10];

pub const pulli_symbols:[char;1] = ['்'];

pub const agaram_letters:[char;18] = ['க','ச','ட','த','ப','ற',
          'ஞ','ங','ண','ந','ம','ன',
          'ய','ர','ல','வ','ழ','ள'];
pub const mayangoli_letters:[char;8] = ['ண', 'ன', 'ந', 'ல',
            'ழ', 'ள', 'ர', 'ற'];

pub const consonant_ka:char =  'க';
pub const consonant_nga:char =  'ங';
pub const consonant_ca:char =  'ச';
pub const consonant_ja:char =  'ஜ';
pub const consonant_nya:char =  'ஞ';
pub const consonant_tta:char =  'ட';
pub const consonant_nna:char =  'ண';
pub const consonant_nnna:char =  'ன';
pub const consonant_ta:char =  'த';
pub const consonant_tha:char =  'த';
pub const consonant_na:char =  'ந';
pub const consonant_pa:char =  'ப';
pub const consonant_ma:char =  'ம';
pub const consonant_ya:char =  'ய';
pub const consonant_ra:char =  'ர';
pub const consonant_rra:char =  'ற';
pub const consonant_la:char =  'ல';
pub const consonant_lla:char =  'ள';
pub const consonant_llla:char = 'ழ';
pub const consonant_zha:char = 'ழ';
pub const consonant_va:char = 'வ';

pub const sanskrit_letters :[&str;6]= ["ஶ","ஜ","ஷ", "ஸ","ஹ","க்ஷ"];
pub const sanskrit_mei_letters:[&str;6] =["ஶ்","ஜ்","ஷ்", "ஸ்","ஹ்","க்ஷ்"];

pub fn trial_get_letters(x:&String) -> Vec<String> {
    let mut v: Vec<String> = Vec::new();
    let mut i:usize = 0;
    while i < x.len() {
        i = i+1;
    }
    v
}

/** Split a tamil-unicode stream into
* tamil characters (individuals).
*/
pub fn get_letters(x:&str) -> Vec<String> {
    /* Splits the @word into a character-list of tamil/english
    *characters present in the stream. This routine provides a robust tokenizer
    *for Tamil unicode letters. */
    let mut v: Vec<String> = Vec::new();
    let mut tmp:String=String::from("");
    for (idx,c) in x.chars().enumerate() {
        if x.is_char_boundary(idx) {
            if ( tmp.len() != 0 ) {
                v.push(format!("{}",tmp));
                v.push(format!("{}",c));
            } else {
                v.push(format!("{}",c));
            }
            tmp.clear();
        } else {
            tmp =  format!("{}{}",tmp,c);
        }
    }
    if tmp.len() != 0 {
        v.push(tmp);
    }
    v
}
