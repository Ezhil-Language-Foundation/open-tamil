/**
 * (C) 2021, Ezhil Language Foundation.
 *  This file is part of Open-Tamil for Rust language.
 */
pub mod tamil;

#[cfg(test)]
mod tests {
    use tamil::*;
    #[test]
    fn test_uyir_mei_skt() {
        assert_eq!(UYIR.len(), 12);
        assert_eq!(SANSKRIT_LETTERS.len(), 6);
    }

    #[test]
    fn test_get_letters() {
        assert_eq!(get_letters("அப்பம்").len(), 4);
        assert_eq!(get_letters("இறை").len(), 2);
        assert_eq!(get_letters("Irai").len(), 4);
        assert_eq!(get_letters("Iraiஅப்பம்").len(), 8);
    }

    #[test]
    fn test_all_tamil() {
        assert_eq!(tamil247().len(), 247);
        assert_eq!(TAMIL_LETTERS.to_vec().len(), 345);
        assert_eq!(TAMIL_SYMBOLS.len(), 11);
    }

    #[test]
    fn test_find_sri() {
        let mut found_sri: bool = false;
        for sym in TAMIL_SYMBOLS.iter() {
            if *sym == "ஶ்ரீ" {
                found_sri = true;
                break;
            }
        }
        assert!(found_sri);
    }

    #[test]
    fn test_mei_to_agaram() {
        assert_eq!(mei_to_agaram("ழ்".to_string()), "ழ".to_string());
    }

    #[test]
    fn test_is_tamil_unicode() {
        assert_eq!(
            is_tamil_unicode_predicate('அ'),
            is_tamil_unicode_predicate('ஔ')
        );
        assert_eq!(
            is_tamil_unicode_predicate('a'),
            is_tamil_unicode_predicate('√')
        );
        assert_eq!(is_tamil_unicode_predicate('ஆ'), true);
        assert_eq!(is_tamil_unicode_predicate('z'), false);
    }

    #[test]
    fn test_is_tamil_index() {
        assert_eq!(getidx("அ".to_string()), 0);
        assert_eq!(getidx("கௌ".to_string()), 68);
    }

    #[test]
    fn test_word_pfx() {
        assert_eq!(istamil_prefix("அப்பம்"), true);
        assert_eq!(istamil_prefix("இறை"), true);
        assert_eq!(istamil_prefix("Irai"), false);
        assert_eq!(istamil_prefix("Iraiஅப்பம்"), false);
    }

    #[test]
    fn test_word_alltamil() {
        assert_eq!(all_tamil("அப்பம்"), true);
        assert_eq!(all_tamil("இறை"), true);
        assert_eq!(all_tamil("Irai"), false);
        assert_eq!(all_tamil("அப்பம்Irai"), false);
    }

    #[test]
    fn test_word_len() {
        assert_eq!(get_letters_length("இறையோன்"), 4);
        assert_eq!(get_letters_length("திருவிடைமருதூர்"), 8);
        assert_eq!(get_letters_length("திருவான்மீயூர்"), 7);
    }

    #[test]
    fn test_has_tamil() {
        use std::collections::HashMap;
        assert_eq!(has_tamil("அப்பம்"), true);
        assert_eq!(has_tamil("இறை"), true);
        assert_eq!(has_tamil("Irai"), false);
        assert_eq!(has_tamil("அப்பம்Irai"), true);

        let timber_resources: HashMap<&str, bool> =
            [("Norway", false), ("Denmark", false), ("Iceland", false)]
                .iter()
                .cloned()
                .collect();
        for (key, value) in timber_resources.iter() {
            assert_eq!(has_tamil(key), *value);
            let mut keytam = key.to_string();
            keytam.push('க');
            assert_eq!(has_tamil(&keytam), true);
        }
    }

    #[test]
    fn test_uyirmei_construct() {
        use tamil::uyirmei_constructed;
        assert_eq!(uyirmei_constructed(5, 3), "றீ");
        assert_eq!(uyirmei_constructed(0, 10), "கோ");
        assert_eq!(uyirmei_constructed(0, 0), "க");
    }

    #[test]
    fn test_reverse() {
        assert_eq!(reverse_word("கபாலி"), "லிபாக");
    }
    #[test]
    fn test_classify() {
        assert_eq!("<Kuril/UyirLetter>", classify_letter("அ"));
        assert_eq!("<UyirMeiLetter>", classify_letter("கொ"));
        assert_eq!("<Vallinam/MeiLetter>", classify_letter("க்"));
    }
    #[test]
    fn test_mei_uyir() {
        assert_eq!(join_mei_uyir("ன்", "ஊ"), "னூ");
        assert_eq!(join_mei_uyir("க்", "ஒ"), "கொ");
    }
    #[test]
    fn test_join_elementary() {
        let expected = String::from("காரைவீடு");
        let mut input: Vec<String> = Vec::<String>::new();
        for s in vec!["க்", "ஆ", "ர்", "ஐ", "வ்", "ஈ", "ட்", "உ"].iter() {
            input.push(s.to_string());
        }
        let actual = join_letters_elementary(&input);
        assert_eq!(actual.len(), expected.len());
        assert_eq!(&actual, &expected);
    }

    #[test]
    fn test_split_mei_uyir() {
        let ab = split_mei_uyir("போ");
        assert_eq!(&ab[0], "ப்");
        assert_eq!(&ab[1], "ஓ");
        assert_eq!(ab.len(), 2);

        let bc = split_mei_uyir("டா");
        assert_eq!(&bc[0], "ட்");
        assert_eq!(&bc[1], "ஆ");
        assert_eq!(bc.len(), 2);
    }

    #[test]
    fn test_split_mei_uyir2() {
        let bc = split_mei_uyir("ற");
        assert_eq!(&bc[0], "ற்");
        assert_eq!(&bc[1], "அ");
        assert_eq!(bc.len(), 2);
    }

    #[test]
    fn test_get_letters_elementary() {
        let parts = get_letters_elementary("கொற்றவை");
        let expected = vec!["க்", "ஒ", "ற்", "", "ற்", "அ", "வ்", "ஐ"];
        println!("{:?}", parts);
        assert_eq!(parts, expected);
    }
}
