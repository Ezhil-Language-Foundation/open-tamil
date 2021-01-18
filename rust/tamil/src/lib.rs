/**
 * (C) 2021, Ezhil Language Foundation.
 *  This file is part of Open-Tamil for Rust language.
 */
pub mod tamil;

#[cfg(test)]
mod tests {
    #[test]
    fn test_uyir_mei_skt() {
        use tamil;
        assert_eq!(tamil::UYIR.len(), 12);
        assert_eq!(tamil::SANSKRIT_LETTERS.len(), 6);
    }

    #[test]
    fn test_get_letters() {
        use tamil;
        assert_eq!(tamil::get_letters("அப்பம்").len(), 4);
        assert_eq!(tamil::get_letters("இறை").len(), 2);
        assert_eq!(tamil::get_letters("Irai").len(), 4);
        assert_eq!(tamil::get_letters("Iraiஅப்பம்").len(), 8);
    }

    #[test]
    fn test_all_tamil() {
        use tamil;
        assert_eq!(tamil::tamil247().len(), 247);
        assert_eq!(tamil::TAMIL_LETTERS.to_vec().len(), 345);
        assert_eq!(tamil::TAMIL_SYMBOLS.len(), 11);
    }

    #[test]
    fn test_find_sri() {
        use tamil;
        let mut found_sri: bool = false;
        for sym in tamil::TAMIL_SYMBOLS.iter() {
            if *sym == "ஶ்ரீ" {
                found_sri = true;
                break;
            }
        }
        assert!(found_sri);
    }

    #[test]
    fn test_mei_to_agaram() {
        use tamil;
        assert_eq!(tamil::mei_to_agaram("ழ்".to_string()), "ழ".to_string());
    }

    #[test]
    fn test_is_tamil_unicode() {
        use tamil::is_tamil_unicode_predicate;
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
        use tamil::getidx;
        assert_eq!(getidx("அ".to_string()), 0);
        assert_eq!(getidx("கௌ".to_string()), 68);
    }

    #[test]
    fn test_word_pfx() {
        use tamil::istamil_prefix;
        assert_eq!(istamil_prefix("அப்பம்"), true);
        assert_eq!(istamil_prefix("இறை"), true);
        assert_eq!(istamil_prefix("Irai"), false);
        assert_eq!(istamil_prefix("Iraiஅப்பம்"), false);
    }

    #[test]
    fn test_word_alltamil() {
        use tamil::all_tamil;
        assert_eq!(all_tamil("அப்பம்"), true);
        assert_eq!(all_tamil("இறை"), true);
        assert_eq!(all_tamil("Irai"), false);
        assert_eq!(all_tamil("அப்பம்Irai"), false);
    }

    #[test]
    fn test_word_len() {
        use tamil::get_letters_length;
        assert_eq!(get_letters_length("இறையோன்"), 4);
        assert_eq!(get_letters_length("திருவிடைமருதூர்"), 8);
        assert_eq!(get_letters_length("திருவான்மீயூர்"), 7);
    }

    #[test]
    fn test_has_tamil() {
        use std::collections::HashMap;
        use tamil::has_tamil;

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
        use tamil::reverse_word;
        assert_eq!(reverse_word("கபாலி"), "லிபாக");
    }
    #[test]
    fn test_classify() {
        use tamil::classify_letter;
        assert_eq!("<UyirLetter>",classify_letter("அ"));
        assert_eq!("<TamilLetter>",classify_letter("கொ"));
    }
}
