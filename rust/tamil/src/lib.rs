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
        assert_eq!(tamil::UYIR.len(),12);
        assert_eq!(tamil::SANSKRIT_LETTERS.len(), 6);
    }

    #[test]
    fn test_get_letters() {
        use tamil;
        assert_eq!(tamil::get_letters("அப்பம்").len(),4);
        assert_eq!(tamil::get_letters("இறை").len(), 2);
    }

    #[test]
    fn test_all_tamil() {
        use tamil;
        assert_eq!(tamil::tamil247().len(),247);
        assert_eq!(tamil::TAMIL_LETTERS.to_vec().len(),345);
        assert_eq!(tamil::TAMIL_SYMBOLS.len(),11);
    }

    #[test]
    fn test_find_sri() {
        use tamil;
        let mut found_sri : bool = false;
        for sym in tamil::TAMIL_SYMBOLS.iter() {
            if  *sym == "ஶ்ரீ" {
                found_sri = true;
                break;
            }
        }
        assert!(found_sri);
    }
}
