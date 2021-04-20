/**
 * (C) 2021, Ezhil Language Foundation.
 *  This file is part of Open-Tamil for Rust language.
 */
pub const UYIR: [char; 12] = ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ'];
pub const UYIR_LETTERS: &'static [char; 12] = &UYIR;
pub const VOWEL_A: char = 'அ';
pub const VOWEL_AA: char = 'ஆ';
pub const VOWEL_I: char = 'இ';
pub const VOWEL_II: char = 'ஈ';
pub const VOWEL_U: char = 'உ';
pub const VOWEL_UU: char = 'ஊ';
pub const VOWEL_E: char = 'எ';
pub const VOWEL_EE: char = 'ஏ';
pub const VOWEL_AI: char = 'ஐ';
pub const VOWEL_O: char = 'ஒ';
pub const VOWEL_OO: char = 'ஓ';
pub const VOWEL_AU: char = 'ஔ';
pub const AYTHAM_LETTER: char = 'ஃ';
pub const AYUDHA_LETTER: char = 'ஃ';

pub const KURIL_LETTERS: [char; 5] = ['அ', 'இ', 'உ', 'எ', 'ஒ'];
pub const NEDIL_LETTERS: [char; 7] = ['ஆ', 'ஈ', 'ஊ', 'ஏ', 'ஓ', 'ஐ', 'ஔ'];
pub const DIPTHONG_LETTERS: [char; 2] = ['ஐ', 'ஔ'];

pub const PRONOUN_LETTERS: [char; 3] = ['அ', 'இ', 'உ'];
pub const SUTTEZHUTHTHU: &'static [char; 3] = &PRONOUN_LETTERS;

pub const QUESTIONSUFFIX_LETTERS: [char; 3] = ['ஆ', 'ஏ', 'ஓ'];
pub const VINAAEZHUTHTHU: &'static [char; 3] = &QUESTIONSUFFIX_LETTERS;

pub const VALLINAM_LETTERS: [&str; 6] = ["க்", "ச்", "ட்", "த்", "ப்", "ற்"];
pub const MELLINAM_LETTERS: [&str; 6] = ["ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்"];
pub const IDAYINAM_LETTERS: [&str; 6] = ["ய்", "ர்", "ல்", "வ்", "ழ்", "ள்"];

pub const MEI_LETTERS: [&str; 18] = [
    "க்", "ச்", "ட்", "த்", "ப்", "ற்", "ஞ்", "ங்", "ண்", "ந்", "ம்", "ன்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்",
];

pub const ACCENT_SYMBOLS: [char; 13] = [
    '\u{0}', 'ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ', 'ஃ',
];

pub const ACCENT_AA: char = ACCENT_SYMBOLS[1];
pub const ACCENT_I: char = ACCENT_SYMBOLS[2];
pub const ACCENT_U: char = ACCENT_SYMBOLS[3];
pub const ACCENT_UU: char = ACCENT_SYMBOLS[4];
pub const ACCENT_E: char = ACCENT_SYMBOLS[5];
pub const ACCENT_EE: char = ACCENT_SYMBOLS[6];
pub const ACCENT_AI: char = ACCENT_SYMBOLS[7];
pub const ACCENT_O: char = ACCENT_SYMBOLS[8];
pub const ACCENT_OO: char = ACCENT_SYMBOLS[9];
pub const ACCENT_AU: char = ACCENT_SYMBOLS[10];

pub const PULLI_SYMBOLS: [char; 1] = ['்'];

pub const AGARAM_LETTERS: [char; 18] = [
    'க', 'ச', 'ட', 'த', 'ப', 'ற', 'ஞ', 'ங', 'ண', 'ந', 'ம', 'ன', 'ய', 'ர', 'ல', 'வ', 'ழ', 'ள',
];
pub const MAYANGOLI_LETTERS: [char; 8] = ['ண', 'ன', 'ந', 'ல', 'ழ', 'ள', 'ர', 'ற'];

pub const CONSONANT_KA: char = 'க';
pub const CONSONANT_NGA: char = 'ங';
pub const CONSONANT_CA: char = 'ச';
pub const CONSONANT_JA: char = 'ஜ';
pub const CONSONANT_NYA: char = 'ஞ';
pub const CONSONANT_TTA: char = 'ட';
pub const CONSONANT_NNA: char = 'ண';
pub const CONSONANT_NNNA: char = 'ன';
pub const CONSONANT_TA: char = 'த';
pub const CONSONANT_THA: char = 'த';
pub const CONSONANT_NA: char = 'ந';
pub const CONSONANT_PA: char = 'ப';
pub const CONSONANT_MA: char = 'ம';
pub const CONSONANT_YA: char = 'ய';
pub const CONSONANT_RA: char = 'ர';
pub const CONSONANT_RRA: char = 'ற';
pub const CONSONANT_LA: char = 'ல';
pub const CONSONANT_LLA: char = 'ள';
pub const CONSONANT_LLLA: char = 'ழ';
pub const CONSONANT_ZHA: char = 'ழ';
pub const CONSONANT_VA: char = 'வ';

pub const SANSKRIT_LETTERS: [&str; 6] = ["ஶ", "ஜ", "ஷ", "ஸ", "ஹ", "க்ஷ"];
pub const SANSKRIT_MEI_LETTERS: [&str; 6] = ["ஶ்", "ஜ்", "ஷ்", "ஸ்", "ஹ்", "க்ஷ்"];

pub const GRANTHA_MEI_LETTERS: [&str; 24] = [
    "க்",
    "ச்",
    "ட்",
    "த்",
    "ப்",
    "ற்",
    "ஞ்",
    "ங்",
    "ண்",
    "ந்",
    "ம்",
    "ன்",
    "ய்",
    "ர்",
    "ல்",
    "வ்",
    "ழ்",
    "ள்",
    "ஶ்",
    "ஜ்",
    "ஷ்",
    "ஸ்",
    "ஹ்",
    "க்ஷ்",
];
pub const GRANTHA_AGARAM_LETTERS: [&str; 24] = [
    "க",
    "ச",
    "ட",
    "த",
    "ப",
    "ற",
    "ஞ",
    "ங",
    "ண",
    "ந",
    "ம",
    "ன",
    "ய",
    "ர",
    "ல",
    "வ",
    "ழ",
    "ள",
    "ஶ",
    "ஜ",
    "ஷ",
    "ஸ",
    "ஹ",
    "க்ஷ",
];

pub const UYIRMEI_LETTERS: [&str; 216] = [
    "க", "கா", "கி", "கீ", "கு", "கூ", "கெ", "கே", "கை", "கொ", "கோ", "கௌ", "ச", "சா", "சி", "சீ",
    "சு", "சூ", "செ", "சே", "சை", "சொ", "சோ", "சௌ", "ட", "டா", "டி", "டீ", "டு", "டூ", "டெ", "டே",
    "டை", "டொ", "டோ", "டௌ", "த", "தா", "தி", "தீ", "து", "தூ", "தெ", "தே", "தை", "தொ", "தோ", "தௌ",
    "ப", "பா", "பி", "பீ", "பு", "பூ", "பெ", "பே", "பை", "பொ", "போ", "பௌ", "ற", "றா", "றி", "றீ",
    "று", "றூ", "றெ", "றே", "றை", "றொ", "றோ", "றௌ", "ஞ", "ஞா", "ஞி", "ஞீ", "ஞு", "ஞூ", "ஞெ", "ஞே",
    "ஞை", "ஞொ", "ஞோ", "ஞௌ", "ங", "ஙா", "ஙி", "ஙீ", "ஙு", "ஙூ", "ஙெ", "ஙே", "ஙை", "ஙொ", "ஙோ", "ஙௌ",
    "ண", "ணா", "ணி", "ணீ", "ணு", "ணூ", "ணெ", "ணே", "ணை", "ணொ", "ணோ", "ணௌ", "ந", "நா", "நி", "நீ",
    "நு", "நூ", "நெ", "நே", "நை", "நொ", "நோ", "நௌ", "ம", "மா", "மி", "மீ", "மு", "மூ", "மெ", "மே",
    "மை", "மொ", "மோ", "மௌ", "ன", "னா", "னி", "னீ", "னு", "னூ", "னெ", "னே", "னை", "னொ", "னோ", "னௌ",
    "ய", "யா", "யி", "யீ", "யு", "யூ", "யெ", "யே", "யை", "யொ", "யோ", "யௌ", "ர", "ரா", "ரி", "ரீ",
    "ரு", "ரூ", "ரெ", "ரே", "ரை", "ரொ", "ரோ", "ரௌ", "ல", "லா", "லி", "லீ", "லு", "லூ", "லெ", "லே",
    "லை", "லொ", "லோ", "லௌ", "வ", "வா", "வி", "வீ", "வு", "வூ", "வெ", "வே", "வை", "வொ", "வோ", "வௌ",
    "ழ", "ழா", "ழி", "ழீ", "ழு", "ழூ", "ழெ", "ழே", "ழை", "ழொ", "ழோ", "ழௌ", "ள", "ளா", "ளி", "ளீ",
    "ளு", "ளூ", "ளெ", "ளே", "ளை", "ளொ", "ளோ", "ளௌ",
];

// total tamil letters in use, including sanskrit letters
pub const TAMIL_LETTERS: [&str; 345] = [
    /* Uyir */
    "அ",
    "ஆ",
    "இ",
    "ஈ",
    "உ",
    "ஊ",
    "எ",
    "ஏ",
    "ஐ",
    "ஒ",
    "ஓ",
    "ஔ",
    /* Ayuda Ezhuthu */
    "ஃ",
    /* Mei */
    "க்",
    "ச்",
    "ட்",
    "த்",
    "ப்",
    "ற்",
    "ஞ்",
    "ங்",
    "ண்",
    "ந்",
    "ம்",
    "ன்",
    "ய்",
    "ர்",
    "ல்",
    "வ்",
    "ழ்",
    "ள்",
    /* Sanskrit (Mei) */
    "ஜ்",
    "ஷ்",
    "ஸ்",
    "ஹ்",
    /* Agaram */
    "க",
    "ச",
    "ட",
    "த",
    "ப",
    "ற",
    "ஞ",
    "ங",
    "ண",
    "ந",
    "ம",
    "ன",
    "ய",
    "ர",
    "ல",
    "வ",
    "ழ",
    "ள",
    /* Sanskrit (Vada Mozhi) */
    "ஜ",
    "ஷ",
    "ஸ",
    "ஹ",
    /* Uyir Mei */
    "க",
    "கா",
    "கி",
    "கீ",
    "கு",
    "கூ",
    "கெ",
    "கே",
    "கை",
    "கொ",
    "கோ",
    "கௌ",
    "ச",
    "சா",
    "சி",
    "சீ",
    "சு",
    "சூ",
    "செ",
    "சே",
    "சை",
    "சொ",
    "சோ",
    "சௌ",
    "ட",
    "டா",
    "டி",
    "டீ",
    "டு",
    "டூ",
    "டெ",
    "டே",
    "டை",
    "டொ",
    "டோ",
    "டௌ",
    "த",
    "தா",
    "தி",
    "தீ",
    "து",
    "தூ",
    "தெ",
    "தே",
    "தை",
    "தொ",
    "தோ",
    "தௌ",
    "ப",
    "பா",
    "பி",
    "பீ",
    "பு",
    "பூ",
    "பெ",
    "பே",
    "பை",
    "பொ",
    "போ",
    "பௌ",
    "ற",
    "றா",
    "றி",
    "றீ",
    "று",
    "றூ",
    "றெ",
    "றே",
    "றை",
    "றொ",
    "றோ",
    "றௌ",
    "ஞ",
    "ஞா",
    "ஞி",
    "ஞீ",
    "ஞு",
    "ஞூ",
    "ஞெ",
    "ஞே",
    "ஞை",
    "ஞொ",
    "ஞோ",
    "ஞௌ",
    "ங",
    "ஙா",
    "ஙி",
    "ஙீ",
    "ஙு",
    "ஙூ",
    "ஙெ",
    "ஙே",
    "ஙை",
    "ஙொ",
    "ஙோ",
    "ஙௌ",
    "ண",
    "ணா",
    "ணி",
    "ணீ",
    "ணு",
    "ணூ",
    "ணெ",
    "ணே",
    "ணை",
    "ணொ",
    "ணோ",
    "ணௌ",
    "ந",
    "நா",
    "நி",
    "நீ",
    "நு",
    "நூ",
    "நெ",
    "நே",
    "நை",
    "நொ",
    "நோ",
    "நௌ",
    "ம",
    "மா",
    "மி",
    "மீ",
    "மு",
    "மூ",
    "மெ",
    "மே",
    "மை",
    "மொ",
    "மோ",
    "மௌ",
    "ன",
    "னா",
    "னி",
    "னீ",
    "னு",
    "னூ",
    "னெ",
    "னே",
    "னை",
    "னொ",
    "னோ",
    "னௌ",
    "ய",
    "யா",
    "யி",
    "யீ",
    "யு",
    "யூ",
    "யெ",
    "யே",
    "யை",
    "யொ",
    "யோ",
    "யௌ",
    "ர",
    "ரா",
    "ரி",
    "ரீ",
    "ரு",
    "ரூ",
    "ரெ",
    "ரே",
    "ரை",
    "ரொ",
    "ரோ",
    "ரௌ",
    "ல",
    "லா",
    "லி",
    "லீ",
    "லு",
    "லூ",
    "லெ",
    "லே",
    "லை",
    "லொ",
    "லோ",
    "லௌ",
    "வ",
    "வா",
    "வி",
    "வீ",
    "வு",
    "வூ",
    "வெ",
    "வே",
    "வை",
    "வொ",
    "வோ",
    "வௌ",
    "ழ",
    "ழா",
    "ழி",
    "ழீ",
    "ழு",
    "ழூ",
    "ழெ",
    "ழே",
    "ழை",
    "ழொ",
    "ழோ",
    "ழௌ",
    "ள",
    "ளா",
    "ளி",
    "ளீ",
    "ளு",
    "ளூ",
    "ளெ",
    "ளே",
    "ளை",
    "ளொ",
    "ளோ",
    "ளௌ", /* Sanskrit Uyir-Mei */
    "ஶ",
    "ஶா",
    "ஶி",
    "ஶீ",
    "ஶு",
    "ஶூ",
    "ஶெ",
    "ஶே",
    "ஶை",
    "ஶொ",
    "ஶோ",
    "ஶௌ",
    "ஜ",
    "ஜா",
    "ஜி",
    "ஜீ",
    "ஜு",
    "ஜூ",
    "ஜெ",
    "ஜே",
    "ஜை",
    "ஜொ",
    "ஜோ",
    "ஜௌ",
    "ஷ",
    "ஷா",
    "ஷி",
    "ஷீ",
    "ஷு",
    "ஷூ",
    "ஷெ",
    "ஷே",
    "ஷை",
    "ஷொ",
    "ஷோ",
    "ஷௌ",
    "ஸ",
    "ஸா",
    "ஸி",
    "ஸீ",
    "ஸு",
    "ஸூ",
    "ஸெ",
    "ஸே",
    "ஸை",
    "ஸொ",
    "ஸோ",
    "ஸௌ",
    "ஹ",
    "ஹா",
    "ஹி",
    "ஹீ",
    "ஹு",
    "ஹூ",
    "ஹெ",
    "ஹே",
    "ஹை",
    "ஹொ",
    "ஹோ",
    "ஹௌ",
    "க்ஷ",
    "க்ஷா",
    "க்ஷி",
    "க்ஷீ",
    "க்ஷு",
    "க்ஷூ",
    "க்ஷெ",
    "க்ஷே",
    "க்ஷை",
    "க்ஷொ",
    "க்ஷோ",
    "க்ஷௌ",
];
pub const UYIRMEI_OFFSET:usize = 12+1+18+2;
pub const DAY: &str = "௳";
pub const MONTH: &str = "௴";
pub const YEAR: &str = "௵";
pub const DEBIT: &str = "௶";
pub const CREDIT: &str = "௷";
pub const RUPEE: &str = "௹";
pub const NUMERAL: &str = "௺";
pub const SRI: &str = "\u{0bb6}\u{0bcd}\u{0bb0}\u{0bc0}"; // #SRI -ஶ்ரீ
pub const KSHA: &str = "\u{0b95}\u{0bcd}\u{0bb7}"; // #KSHA - க்ஷ
pub const KSH: &str = "\u{0b95}\u{0bcd}\u{0bb7}\u{0bcd}"; // #KSH - க்ஷ்
pub const INDIAN_RUPEE: &str = "₹";
pub const TAMIL_SYMBOLS: [&'static str; 11] = [
    DAY,
    MONTH,
    YEAR,
    DEBIT,
    CREDIT,
    RUPEE,
    NUMERAL,
    SRI,
    KSHA,
    KSH,
    INDIAN_RUPEE,
];

/* length of the definitions */
pub fn accent_len() -> usize {
    ACCENT_SYMBOLS.len()
}
pub fn ayudha_len() -> usize {
    1
}
pub fn uyir_len() -> usize {
    UYIR_LETTERS.len()
}
pub fn mei_len() -> usize {
    MEI_LETTERS.len()
}
pub fn agaram_len() -> usize {
    AGARAM_LETTERS.len()
}
pub fn uyirmei_len() -> usize {
    UYIRMEI_LETTERS.len()
}
pub fn tamil_len() -> usize {
    TAMIL_LETTERS.len()
}

pub fn uyir(idx: usize) -> char {
    UYIR_LETTERS[idx]
}
pub fn agaram(idx: usize) -> char {
    AGARAM_LETTERS[idx]
}
pub fn mei(idx: usize) -> String {
    MEI_LETTERS[idx].to_string()
}
pub fn uyirmei(idx: usize) -> String {
    UYIRMEI_LETTERS[idx].to_string()
}

pub fn tamil247() -> Vec<String> {
    let mut _tamil247: Vec<String> = vec![];
    _tamil247.push(AYUDHA_LETTER.to_string());
    for letter in UYIR_LETTERS.iter() {
        _tamil247.push(letter.to_string());
    }
    for letter in MEI_LETTERS.iter() {
        _tamil247.push(letter.to_string());
    }
    for letter in UYIRMEI_LETTERS.iter() {
        _tamil247.push(letter.to_string());
    }
    _tamil247
}

/**
mei_to_agaram("ழ்") => ழ
*/
pub fn mei_to_agaram(in_syllable: String) -> String {
    match GRANTHA_MEI_LETTERS.iter().position(|&x| x == in_syllable) {
        Some(mei_pos) => {
            let agaram_a_pos: usize = 0;
            uyirmei_constructed(mei_pos, agaram_a_pos)
        }

        None => in_syllable,
    }
}

/**
def uyirmei_constructed( mei_idx, uyir_idx):
    """ construct uyirmei letter give mei index and uyir index """
    idx,idy = mei_idx,uyir_idx
    assert ( idy >= 0 and idy < uyir_len() )
    assert ( idx >= 0 and idx < 6+mei_len() )
    return grantha_agaram_letters[mei_idx]+accent_symbols[uyir_idx]
*/
pub fn uyirmei_constructed(mei_idx: usize, uyir_idx: usize) -> String {
    match uyir_idx {
        0 => {
            format!("{}", GRANTHA_AGARAM_LETTERS[mei_idx])
        }
        _ => {
            format!(
                "{}{}",
                GRANTHA_AGARAM_LETTERS[mei_idx], ACCENT_SYMBOLS[uyir_idx]
            )
        }
    }
}

pub fn is_tamil_unicode_predicate(_x: char) -> bool {
    let ranges: [i32; 2] = [2946, 3066];
    let x = _x as i32;
    x >= ranges[0] && x <= ranges[1]
}

pub fn getidx(letter: String) -> usize {
    let mut itr: usize = 0;
    loop {
        if itr == TAMIL_LETTERS.len() {
            panic!("Cannot find letter in Tamil arichuvadi");
        } else if letter == TAMIL_LETTERS[itr] {
            break;
        } else {
            itr = itr + 1
        }
    }
    itr
}

/*
    """check if the word has any occurance of any tamil letter """
    # list comprehension is not necessary - we bail at earliest
*/
pub fn has_tamil(word: &str) -> bool {
    for c in word.chars() {
        let cstr = c.to_string();
        if TAMIL_LETTERS.iter().any(|x| *x == cstr) {
            return true;
        }
    }
    false
}

pub fn get_letters_length(word: &str) -> usize {
    get_letters(word).len()
}

/**
* Split a tamil-unicode stream into
* tamil characters (individuals).
*/
pub fn get_letters(x: &str) -> Vec<String> {
    /* Splits the @word into a character-list of tamil/english
     *characters present in the stream. This routine provides a robust tokenizer
     *for Tamil unicode letters. */
    const SPL_SYMBOLS: [char; 12] = ['்', 'ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை', 'ொ', 'ோ', 'ௌ'];
    let mut v: Vec<String> = Vec::new();
    let mut tmp: String = String::from("");
    for c in x.chars() {
        if SPL_SYMBOLS.iter().any(|x| *x == c) {
            let z = v.pop();
            match z {
                Some(zz) => {
                    tmp.push_str(&zz);
                }
                _ => {}
            }
        }

        if tmp.len() != 0 {
            tmp.push(c);
            v.push(tmp.clone());
            tmp.clear();
        } else {
            v.push(c.to_string());
        }
    }
    v
}

pub fn split_mei_uyir(uyirmei_char:&str) -> Vec<String> {
    /**
    This function split uyirmei compound character into mei + uyir characters
    and returns in tuple.

    Input : It must be unicode tamil char, V=vowel, C=char, VC=compound VC.
    Output: (mei,uyir) if it is VC, otherwise return input if it is V, or C.
    Written By : Arulalan.T
    Date : 22.09.2014

    **/
    let match_char = |x:&char| -> bool { *x == uyirmei_char.chars().next().unwrap() };

    let is_uyir : bool = UYIR_LETTERS.iter().any(match_char);
    let is_mei : bool = GRANTHA_MEI_LETTERS.iter().any(|x| { *x == uyirmei_char });
    if is_uyir  {
        return vec!["".to_string(),uyirmei_char.to_string()];
    } else if is_mei  {
        return vec![uyirmei_char.to_string(),"".to_string()];
    }
    // has to be uyirmei letters.
    let uyirmeiidx : usize = TAMIL_LETTERS.iter().position( |x|{ *x == uyirmei_char } ).unwrap() - UYIRMEI_OFFSET;

    //# calculate uyirmei index
    let uyiridx:usize = uyirmeiidx%12;
    let mut midx : usize = ((uyirmeiidx-uyiridx)/12);
    if midx >= 2 {
        midx = (midx - 2);
    }
    midx = midx%GRANTHA_MEI_LETTERS.len();
    let meiidx : usize = midx;
    let gmei = String::from(GRANTHA_MEI_LETTERS[meiidx].to_string());
    let guyir = String::from(UYIR_LETTERS[uyiridx].to_string());
    println!("{},{}",gmei,guyir);
    return vec![gmei,guyir]
}

pub fn get_letters_elementary(word:&str) -> Vec<String> {
    let mut retval = Vec::<String>::new();
    for w in get_letters(word) {
        let result = split_mei_uyir(&w);
        retval.push(result[0].to_string());
        retval.push(result[1].to_string());
    }
    retval
}

pub fn all_tamil(word: &str) -> bool {
    get_letters(&word)
        .iter()
        .all(|x| is_tamil_unicode_predicate(x.chars().next().unwrap()))
}

pub fn istamil_prefix(word: &str) -> bool {
    /* check if the given word has a tamil prefix. Returns
     * either a True/False flag
     */
    match word.len() {
        0 => false,
        _ => {
            let letters = get_letters(&word);
            TAMIL_LETTERS.iter().any(|x| x == &letters[0])
        }
    }
}

pub fn join_mei_uyir(mei_char:&str, uyir_char:&str) -> String {
    /**
    *This function join mei character and uyir character, and retuns as
    *compound uyirmei unicode character.
    *
    *Inputs:
    *    mei_char : It must be unicode tamil mei char.
    *    uyir_char : It must be unicode tamil uyir char.
    */
    if mei_char.len() == 0 {
        return uyir_char.to_string();
    }
    if uyir_char.len() == 0 {
        return mei_char.to_string();
    }
    let match_uyir = |x:&char| -> bool { *x == uyir_char.chars().next().unwrap() };
    let uyiridx : usize = UYIR_LETTERS.iter().position(match_uyir).unwrap();
    let meiidx : usize = GRANTHA_MEI_LETTERS.iter().position( |x|{ *x == mei_char } ).unwrap(); 
    //# calculate uyirmei index
    let uyirmeiidx = (meiidx+2) * 12 + uyiridx;
    println!("{},{},{}",uyiridx,meiidx,uyirmeiidx);
    return TAMIL_LETTERS[UYIRMEI_OFFSET+uyirmeiidx].to_string()
}

pub fn join_letters_elementary(elements:&Vec<String>) -> String {
    /**
    * @elements[i] : argaram letter (க)
    * @elements[i+1] : kombu symbol ( \u{0bcd} )
    *           = க்
    */
    if elements.len() % 2 != 0 {
        panic!("input has to be an even numbered list");
    }
    let mut result = String::from("");
    for i in 0..(elements.len()/2) {
        result.push_str( &mut join_mei_uyir(&elements[2*i],&elements[2*i+1]) );
    }
    result
}

pub fn reverse_word(word: &str) -> String {
    let letters = get_letters(word);
    let mut word_out = String::from("");
    for letter in letters.iter().rev() {
        word_out.push_str(letter);
    }
    word_out
}

pub fn classify_letter(letter:&str) -> String {
    assert!(letter.len()<=10,"classify letter can work on only 1 letter word!");
    let eq_letter = |x:&&str|->bool{ *x==letter };
    let first_letter = letter.chars().next().unwrap();
    let eq_char = |x:&char|->bool{ *x == first_letter };
    if UYIR_LETTERS.iter().any(eq_char) {
        if KURIL_LETTERS.iter().any(eq_char) {
            return "<Kuril/UyirLetter>".to_owned()
        } else if NEDIL_LETTERS.iter().any(eq_char) {
            return "<Nedil/UyirLetter>".to_owned()
        } else if first_letter == AYTHAM_LETTER {
            return "<Ayudham/UyirLetter>".to_owned()
        }
        return "<UyirLetter>".to_owned()
    } else if MEI_LETTERS.iter().any(eq_letter) {
        if MELLINAM_LETTERS.iter().any(eq_letter) {
            return "<Mellinam/MeiLetter>".to_owned()
        } else if VALLINAM_LETTERS.iter().any(eq_letter) {
            return "<Vallinam/MeiLetter>".to_owned()
        } else if IDAYINAM_LETTERS.iter().any(eq_letter) {
            return "<Idayinam/MeiLetter>".to_owned()
        }
    } else if UYIRMEI_LETTERS.iter().any(eq_letter) {
        return "<UyirMeiLetter>".to_owned()
    } else if TAMIL_LETTERS.iter().any(eq_letter) {
        return "<TamilOrGrantham>".to_owned()
    } else if first_letter.is_ascii_alphanumeric() {
        return "<English>".to_owned()
    } else if first_letter.is_ascii_digit() {
        return "<Digit>".to_owned()
    }
    return "<non-TamilLetter>".to_owned();
}
