#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tamil.utf8 import splitMeiUyir, joinMeiUyir, get_letters, uyir_letters, mei_letters

# http://www.tamilvu.org/library/lA432/html/lA432cn1.htm
# 1. முதல் சொல்லின் இறுதி எழுத்து அ
# http://www.tamilvu.org/slet/lA100/lA100pd3.jsp?bookid=169&pno=77
all_rules = {
    u"அ": {
        # todo : need to fine tune this solo words
        "first_solo_words": (
            u"என்ன",
            u"நல்ல",
            u"இன்ன",
            u"இன்றைய",
            u"படித்த",
            u"எழுதாத",
        ),
        "secondword_first_chars": (u"க்", u"ச்", u"த்", u"ப்"),
        "diff_jn_words": (((u"சின்ன"), (u"சிறு", u"சிறிய"), u"ஞ்"),),
        "special_secondword_first_chars": (uyir_letters, u"வ்"),
        "same_words": ((u"பல", u"சில"), u"ற்"),
        "same_word_disappear_lastchar": (u"அ"),
        "firstword_double_special_secondword": ((u"என்று", u"என"), u"வ்"),
    },
}


def joinWords(word_a, word_b):
    word_a = word_a.strip()
    word_b = word_b.strip()

    if word_b == "கள்": return word_a + word_b

    # get readable letters of first word
    first_word_letters = get_letters(word_a)

    if first_word_letters[-1] in mei_letters:
        # first word last char is mei letter. so just return as it is.
        # todo : apply special conditions also
        rval = word_a + " " + word_b
        return rval
    # end of if first_word_last_chars[-1] in mei_letters:

    # get mei & uyir characters of first word's last char
    first_word_last_chars = splitMeiUyir(first_word_letters[-1])
    if len(first_word_last_chars) == 2:
        first_word_last_mei_char, first_word_last_uyir_char = first_word_last_chars
    else:
        first_word_last_mei_char, first_word_last_uyir_char = (
            first_word_last_chars[0],
            first_word_last_chars[0],
        )

    # get rule sub dictionary from all dictionary by passing
    rule = all_rules.get(first_word_last_uyir_char, None)

    if word_a == word_b:
        # both input words are same
        same_word_rule = rule.get("same_words", [])
        if word_a in same_word_rule[0]:
            # get conjuction char
            jn = same_word_rule[1]
            # insert conjuction char between input words
            rval = first_word_letters[0] + jn + word_b
            return rval
        elif len(first_word_letters) == 3:
            # both words are same but length is 3.
            disappear_lastchar = rule.get("same_word_disappear_lastchar", [])
            if disappear_lastchar:
                disappear_lastchar = disappear_lastchar[0]
                if first_word_last_uyir_char == disappear_lastchar:
                    first_word_first_char = first_word_letters[0]
                    # get uyir char of second word's first char
                    first_word_first_uyir_char = splitMeiUyir(first_word_first_char)[-1]
                    # get conjuction char by joining first word's last mei char and second word's first uyir char
                    jn = joinMeiUyir(
                        first_word_last_mei_char, first_word_first_uyir_char
                    )
                    # get first word till pre-last char
                    first_word = u"".join(first_word_letters[:-1])
                    # get second word from second char till end
                    second_word = u"".join(first_word_letters[1:])
                    # join all first, conjuction, second word
                    rval = first_word + jn + second_word
                    return rval
            # end of if disappear_lastchar:
        # end of if word_a in same_word_rule[0]:
    # end of if word_a == word_b:

    if rule:
        if word_a in rule.get("first_solo_words", []):
            # todo : need to find tune this first solo word check like using startswith, endswith, etc
            rval = word_a + " " + word_b
            return rval
        # end of if word_a in rule.get('first_solo_words', []):

        for diff_jn in rule.get("diff_jn_words", []):
            if word_a in diff_jn[0]:
                for last in diff_jn[1]:
                    if word_b.startswith(last):
                        # apply different conjuction char rule
                        rval = word_a + diff_jn[2] + word_b
                        return rval
    # end of for diff_jn in  rule.get('diff_jn_words', []):

    # get readable letters of second word
    second_word_letters = get_letters(word_b)
    # get second word's from second char to till end
    second_word_after_first_char = u"".join(second_word_letters[1:])
    # get mei & uyir characters of second word's first char
    second_word_first_chars = splitMeiUyir(second_word_letters[0])
    if len(second_word_first_chars) == 2:
        (
            second_word_first_mei_char,
            second_word_first_uyir_char,
        ) = second_word_first_chars
    else:
        second_word_first_mei_char, second_word_first_uyir_char = (
            second_word_first_chars[0],
            second_word_first_chars[0],
        )

    if rule:
        if second_word_first_mei_char in rule.get("secondword_first_chars", []):
            # apply major conjuction rule
            return word_a + second_word_first_mei_char + " " + word_b
            # end of if second_word_first_mei_char in rule.get('secondword_first_chars', []):

        firstword_double_special_secondword = rule.get(
            "firstword_double_special_secondword", None
        )
        if firstword_double_special_secondword:
            if len(first_word_letters) == 4:
                # check either first word has repeated two times
                if (
                        first_word_letters[:2] == first_word_letters[2:]
                ):  # first word repeat two times within it
                    # get root second word by removing prefix
                    sec_word = (
                            second_word_first_uyir_char + second_word_after_first_char
                    )
                    if sec_word in firstword_double_special_secondword[0]:
                        # get conjuction char by joining  special conjuction and  second root word
                        jn = joinMeiUyir(
                            firstword_double_special_secondword[1],
                            second_word_first_uyir_char,
                        )
                        # join all
                        return word_a + jn + second_word_after_first_char
        # end of if firstword_double_special_secondword:

        special_secondword_first_chars = rule.get(
            "special_secondword_first_chars", None
        )
        if special_secondword_first_chars:
            if second_word_first_uyir_char in special_secondword_first_chars[0]:
                # get special conjuction char
                jn = special_secondword_first_chars[1]
                # join special conjuction char with second word's first uyir char
                second_word_first_schar = joinMeiUyir(jn, second_word_first_uyir_char)
                # complete second word with prefix of conjuction
                second_word = second_word_first_schar + second_word_after_first_char
                # join all
                return word_a + second_word
            # end of if second_word_first_uyir_char in special_secondword_first_chars[0]:
        # end of if special_secondword_first_chars:

    # if all above rules not applicable, then just return as it is !
    return word_a + " " + word_b

# end of def joinWords(word_a, word_b):
