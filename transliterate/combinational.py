# -*- coding: utf-8 -*-
# (C) 2013 Muthiah Annamalai
#
# Implementation of combinational transliterate rules - தமிழ் எழுத்துக்கள்
# according to uyir+mei combination using their respective phonetic sounds.
#
# like how,  க் +  ஊ -> கூ , using the following table we can write in english,
# k -> க், uu -> ஊ   ==>  kuu -> கூ
#
# அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ
# vowels = [u"a", u"aa", u"i", u"ii", u"u", u"uu", u"e", u"ee", u"ai", u"o", u"oo", u"au"]
#
# க ச ட த ப ற ஞ ங ண ந ம ன ய ர ல வ ழ ள ஜ ஷ ஸ ஹ
# க, ச, ட, த, ப, ற, ஞ, ங, ண, ந, ம, ன, ய, ர, ல, வ, ழ, ள, ஜ, ஷ, ஸ, ஹ
# consonant_mei = [u"k", u"s", u"d", u"th",u"p",u"R",u"nj", u"ng",u"N", u"n-", u"m",u"n",
#                  u"y", u"r",u"l",u"v", u"zh", u"L", u"j", u"S", u"sh", u"ha"]
#
# Key Map Table  : Acknowledgements to concept used at Kandupidi.com
#
# For maintenance, use the function '__built_table__()' to build the phonetic->Unicode mapping


class Transliteration:
    """
    Implementation of combinational transliterate rules - தமிழ் எழுத்துக்கள்
    according to uyir+mei combination using their respective phonetic sounds.
    """

    table = {}

    table[u"1"] = u"௧"
    table[u"10"] = u"௰"
    table[u"1000"] = u"௲"
    table[u"2"] = u"௨"
    table[u"3"] = u"௩"
    table[u"4"] = u"௪"
    table[u"5"] = u"௫"
    table[u"6"] = u"௬"
    table[u"7"] = u"௭"
    table[u"8"] = u"௮"
    table[u"9"] = u"௯"
    table[u"L"] = u"ள்"
    table[u"La"] = u"ள"
    table[u"Laa"] = u"ளா"
    table[u"Lai"] = u"ளை"
    table[u"Lau"] = u"ளௌ"
    table[u"Le"] = u"ளெ"
    table[u"Lee"] = u"ளே"
    table[u"Li"] = u"ளி"
    table[u"Lii"] = u"ளீ"
    table[u"Lo"] = u"ளொ"
    table[u"Loo"] = u"ளோ"
    table[u"Lu"] = u"ளு"
    table[u"Luu"] = u"ளூ"
    table[u"N"] = u"ண்"
    table[u"Na"] = u"ண"
    table[u"Naa"] = u"ணா"
    table[u"Nai"] = u"ணை"
    table[u"Nau"] = u"ணௌ"
    table[u"Ne"] = u"ணெ"
    table[u"Nee"] = u"ணே"
    table[u"Ni"] = u"ணி"
    table[u"Nii"] = u"ணீ"
    table[u"No"] = u"ணொ"
    table[u"Noo"] = u"ணோ"
    table[u"Nu"] = u"ணு"
    table[u"Nuu"] = u"ணூ"
    table[u"R"] = u"ற்"
    table[u"Ra"] = u"ற"
    table[u"Raa"] = u"றா"
    table[u"Rai"] = u"றை"
    table[u"Rau"] = u"றௌ"
    table[u"Re"] = u"றெ"
    table[u"Ree"] = u"றே"
    table[u"Ri"] = u"றி"
    table[u"Rii"] = u"றீ"
    table[u"Ro"] = u"றொ"
    table[u"Roo"] = u"றோ"
    table[u"Ru"] = u"று"
    table[u"Ruu"] = u"றூ"
    table[u"S"] = u"ஷ்"
    table[u"Sa"] = u"ஷ"
    table[u"Saa"] = u"ஷா"
    table[u"Sai"] = u"ஷை"
    table[u"Sau"] = u"ஷௌ"
    table[u"Se"] = u"ஷெ"
    table[u"See"] = u"ஷே"
    table[u"Si"] = u"ஷி"
    table[u"Sii"] = u"ஷீ"
    table[u"So"] = u"ஷொ"
    table[u"Soo"] = u"ஷோ"
    table[u"Su"] = u"ஷு"
    table[u"Suu"] = u"ஷூ"
    table[u"Z"] = u"ஃஜ்"
    table[u"Za"] = u"ஃஜ"
    table[u"Zaa"] = u"ஃஜா"
    table[u"Zae"] = u"ஃஜே"
    table[u"Zai"] = u"ஃஜை"
    table[u"Ze"] = u"ஃஜெ"
    table[u"Zi"] = u"ஃஜி"
    table[u"Zii"] = u"ஃஜீ"
    table[u"Zo"] = u"ஃஜொ"
    table[u"Zoa"] = u"ஃஜோ"
    table[u"Zow"] = u"ஃஜௌ"
    table[u"Zu"] = u"ஃஜு"
    table[u"Zuu"] = u"ஃஜூ"
    table[u"d"] = u"ட்"
    table[u"da"] = u"ட"
    table[u"daa"] = u"டா"
    table[u"dai"] = u"டை"
    table[u"dau"] = u"டௌ"
    table[u"de"] = u"டெ"
    table[u"dee"] = u"டே"
    table[u"di"] = u"டி"
    table[u"dii"] = u"டீ"
    table[u"do"] = u"டொ"
    table[u"doo"] = u"டோ"
    table[u"du"] = u"டு"
    table[u"duu"] = u"டூ"
    table[u"f"] = u"ஃப்"
    table[u"fa"] = u"ஃப"
    table[u"faa"] = u"ஃபா"
    table[u"fae"] = u"ஃபே"
    table[u"fai"] = u"ஃபை"
    table[u"fe"] = u"ஃபெ"
    table[u"fi"] = u"ஃபி"
    table[u"fii"] = u"ஃபீ"
    table[u"fo"] = u"ஃபொ"
    table[u"foa"] = u"ஃபோ"
    table[u"fow"] = u"ஃபௌ"
    table[u"fu"] = u"ஃபு"
    table[u"fuu"] = u"ஃபூ"
    table[u"ha"] = u"ஹ்"
    table[u"haa"] = u"ஹ"
    table[u"haaa"] = u"ஹா"
    table[u"haai"] = u"ஹை"
    table[u"haau"] = u"ஹௌ"
    table[u"hae"] = u"ஹெ"
    table[u"haee"] = u"ஹே"
    table[u"hai"] = u"ஹி"
    table[u"haii"] = u"ஹீ"
    table[u"hao"] = u"ஹொ"
    table[u"haoo"] = u"ஹோ"
    table[u"hau"] = u"ஹு"
    table[u"hauu"] = u"ஹூ"
    table[u"j"] = u"ஜ்"
    table[u"ja"] = u"ஜ"
    table[u"jaa"] = u"ஜா"
    table[u"jai"] = u"ஜை"
    table[u"jau"] = u"ஜௌ"
    table[u"je"] = u"ஜெ"
    table[u"jee"] = u"ஜே"
    table[u"ji"] = u"ஜி"
    table[u"jii"] = u"ஜீ"
    table[u"jo"] = u"ஜொ"
    table[u"joo"] = u"ஜோ"
    table[u"ju"] = u"ஜு"
    table[u"juu"] = u"ஜூ"
    table[u"k"] = u"க்"
    table[u"ka"] = u"க"
    table[u"kaa"] = u"கா"
    table[u"kai"] = u"கை"
    table[u"kau"] = u"கௌ"
    table[u"ke"] = u"கெ"
    table[u"kee"] = u"கே"
    table[u"ki"] = u"கி"
    table[u"kii"] = u"கீ"
    table[u"ko"] = u"கொ"
    table[u"koo"] = u"கோ"
    table[u"ksh"] = u"க்ஷ்"
    table[u"ksha"] = u"க்ஷ"
    table[u"kshaa"] = u"க்ஷா"
    table[u"kshae"] = u"க்ஷே"
    table[u"kshai"] = u"க்ஷை"
    table[u"kshe"] = u"க்ஷெ"
    table[u"kshi"] = u"க்ஷி"
    table[u"kshii"] = u"க்ஷீ"
    table[u"ksho"] = u"க்ஷொ"
    table[u"kshoa"] = u"க்ஷோ"
    table[u"kshow"] = u"க்ஷௌ"
    table[u"kshu"] = u"க்ஷு"
    table[u"kshuu"] = u"க்ஷூ"
    table[u"ku"] = u"கு"
    table[u"kuu"] = u"கூ"
    table[u"l"] = u"ல்"
    table[u"la"] = u"ல"
    table[u"laa"] = u"லா"
    table[u"lai"] = u"லை"
    table[u"lau"] = u"லௌ"
    table[u"le"] = u"லெ"
    table[u"lee"] = u"லே"
    table[u"li"] = u"லி"
    table[u"lii"] = u"லீ"
    table[u"lo"] = u"லொ"
    table[u"loo"] = u"லோ"
    table[u"lu"] = u"லு"
    table[u"luu"] = u"லூ"
    table[u"m"] = u"ம்"
    table[u"ma"] = u"ம"
    table[u"maa"] = u"மா"
    table[u"mai"] = u"மை"
    table[u"mau"] = u"மௌ"
    table[u"me"] = u"மெ"
    table[u"mee"] = u"மே"
    table[u"mi"] = u"மி"
    table[u"mii"] = u"மீ"
    table[u"mo"] = u"மொ"
    table[u"moo"] = u"மோ"
    table[u"mu"] = u"மு"
    table[u"muu"] = u"மூ"
    table[u"n"] = u"ன்"
    table[u"n-"] = u"ந்"
    table[u"n-a"] = u"ந"
    table[u"n-aa"] = u"நா"
    table[u"n-ai"] = u"நை"
    table[u"n-au"] = u"நௌ"
    table[u"n-e"] = u"நெ"
    table[u"n-ee"] = u"நே"
    table[u"n-i"] = u"நி"
    table[u"n-ii"] = u"நீ"
    table[u"n-o"] = u"நொ"
    table[u"n-oo"] = u"நோ"
    table[u"n-u"] = u"நு"
    table[u"n-uu"] = u"நூ"
    table[u"na"] = u"ன"
    table[u"naa"] = u"னா"
    table[u"nai"] = u"னை"
    table[u"nau"] = u"னௌ"
    table[u"ne"] = u"னெ"
    table[u"nee"] = u"னே"
    table[u"ng"] = u"ங்"
    table[u"nga"] = u"ங"
    table[u"ngaa"] = u"ஙா"
    table[u"ngai"] = u"ஙை"
    table[u"ngau"] = u"ஙௌ"
    table[u"nge"] = u"ஙெ"
    table[u"ngee"] = u"ஙே"
    table[u"ngi"] = u"ஙி"
    table[u"ngii"] = u"ஙீ"
    table[u"ngo"] = u"ஙொ"
    table[u"ngoo"] = u"ஙோ"
    table[u"ngu"] = u"ஙு"
    table[u"nguu"] = u"ஙூ"
    table[u"ni"] = u"னி"
    table[u"nii"] = u"னீ"
    table[u"nj"] = u"ஞ்"
    table[u"nja"] = u"ஞ"
    table[u"njaa"] = u"ஞா"
    table[u"njai"] = u"ஞை"
    table[u"njau"] = u"ஞௌ"
    table[u"nje"] = u"ஞெ"
    table[u"njee"] = u"ஞே"
    table[u"nji"] = u"ஞி"
    table[u"njii"] = u"ஞீ"
    table[u"njo"] = u"ஞொ"
    table[u"njoo"] = u"ஞோ"
    table[u"nju"] = u"ஞு"
    table[u"njuu"] = u"ஞூ"
    table[u"no"] = u"னொ"
    table[u"noo"] = u"னோ"
    table[u"nu"] = u"னு"
    table[u"nuu"] = u"னூ"
    table[u"p"] = u"ப்"
    table[u"pa"] = u"ப"
    table[u"paa"] = u"பா"
    table[u"pai"] = u"பை"
    table[u"pau"] = u"பௌ"
    table[u"pe"] = u"பெ"
    table[u"pee"] = u"பே"
    table[u"pi"] = u"பி"
    table[u"pii"] = u"பீ"
    table[u"po"] = u"பொ"
    table[u"poo"] = u"போ"
    table[u"pu"] = u"பு"
    table[u"puu"] = u"பூ"
    table[u"r"] = u"ர்"
    table[u"ra"] = u"ர"
    table[u"raa"] = u"ரா"
    table[u"rai"] = u"ரை"
    table[u"rau"] = u"ரௌ"
    table[u"re"] = u"ரெ"
    table[u"ree"] = u"ரே"
    table[u"ri"] = u"ரி"
    table[u"rii"] = u"ரீ"
    table[u"ro"] = u"ரொ"
    table[u"roo"] = u"ரோ"
    table[u"ru"] = u"ரு"
    table[u"ruu"] = u"ரூ"
    table[u"s"] = u"ச்"
    table[u"sa"] = u"ச"
    table[u"saa"] = u"சா"
    table[u"sai"] = u"சை"
    table[u"sau"] = u"சௌ"
    table[u"se"] = u"செ"
    table[u"see"] = u"சே"
    table[u"sh"] = u"ஸ்"
    table[u"sha"] = u"ஸ"
    table[u"shaa"] = u"ஸா"
    table[u"shai"] = u"ஸை"
    table[u"shau"] = u"ஸௌ"
    table[u"she"] = u"ஸெ"
    table[u"shee"] = u"ஸே"
    table[u"shi"] = u"ஸி"
    table[u"shii"] = u"ஸீ"
    table[u"sho"] = u"ஸொ"
    table[u"shoo"] = u"ஸோ"
    table[u"shree"] = u"ஸ்ரீ"
    table[u"shri"] = u"ஸ்ரீ"
    table[u"shu"] = u"ஸு"
    table[u"shuu"] = u"ஸூ"
    table[u"si"] = u"சி"
    table[u"sii"] = u"சீ"
    table[u"so"] = u"சொ"
    table[u"soo"] = u"சோ"
    table[u"sree"] = u"ஸ்ரீ"
    table[u"sri"] = u"ஸ்ரீ"
    table[u"su"] = u"சு"
    table[u"suu"] = u"சூ"
    table[u"th"] = u"த்"
    table[u"tha"] = u"த"
    table[u"thaa"] = u"தா"
    table[u"thai"] = u"தை"
    table[u"thau"] = u"தௌ"
    table[u"the"] = u"தெ"
    table[u"thee"] = u"தே"
    table[u"thi"] = u"தி"
    table[u"thii"] = u"தீ"
    table[u"tho"] = u"தொ"
    table[u"thoo"] = u"தோ"
    table[u"thu"] = u"து"
    table[u"thuu"] = u"தூ"
    table[u"v"] = u"வ்"
    table[u"va"] = u"வ"
    table[u"vaa"] = u"வா"
    table[u"vai"] = u"வை"
    table[u"vau"] = u"வௌ"
    table[u"ve"] = u"வெ"
    table[u"vee"] = u"வே"
    table[u"vi"] = u"வி"
    table[u"vii"] = u"வீ"
    table[u"vo"] = u"வொ"
    table[u"voo"] = u"வோ"
    table[u"vu"] = u"வு"
    table[u"vuu"] = u"வூ"
    table[u"x"] = u"ஃஸ்"
    table[u"xa"] = u"ஃஸ"
    table[u"xaa"] = u"ஃஸா"
    table[u"xae"] = u"ஃஸே"
    table[u"xai"] = u"ஃஸை"
    table[u"xe"] = u"ஃஸெ"
    table[u"xi"] = u"ஃஸி"
    table[u"xo"] = u"ஃஸொ"
    table[u"xoa"] = u"ஃஸோ"
    table[u"xow"] = u"ஃஸௌ"
    table[u"xu"] = u"ஃஸு"
    table[u"xuu"] = u"ஃஸூ"
    table[u"y"] = u"ய்"
    table[u"ya"] = u"ய"
    table[u"yaa"] = u"யா"
    table[u"yai"] = u"யை"
    table[u"yau"] = u"யௌ"
    table[u"ye"] = u"யெ"
    table[u"yee"] = u"யே"
    table[u"yi"] = u"யி"
    table[u"yii"] = u"யீ"
    table[u"yo"] = u"யொ"
    table[u"yoo"] = u"யோ"
    table[u"yu"] = u"யு"
    table[u"yuu"] = u"யூ"
    table[u"zh"] = u"ழ்"
    table[u"zha"] = u"ழ"
    table[u"zhaa"] = u"ழா"
    table[u"zhai"] = u"ழை"
    table[u"zhau"] = u"ழௌ"
    table[u"zhe"] = u"ழெ"
    table[u"zhee"] = u"ழே"
    table[u"zhi"] = u"ழி"
    table[u"zhii"] = u"ழீ"
    table[u"zho"] = u"ழொ"
    table[u"zhoo"] = u"ழோ"
    table[u"zhu"] = u"ழு"
    table[u"zhuu"] = u"ழூ"

    vowels = [
        u"a",
        u"aa",
        u"i",
        u"ii",
        u"u",
        u"uu",
        u"e",
        u"ee",
        u"ai",
        u"o",
        u"oo",
        u"au",
    ]
    uyir_letters = "அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ".split(" ")
    aytham_letter = u"ஃ"
    for uyir, uyir_utf8 in zip(vowels, uyir_letters):
        table[uyir] = uyir_utf8
    table["ak"] = aytham_letter


def __built_table__():
    """ this class is for maintenance purposes only """
    from tamil import utf8

    table = {}

    # அ ஆ இ ஈ உ ஊ எ ஏ ஐ ஒ ஓ ஔ
    vowels = [
        u"a",
        u"aa",
        u"i",
        u"ii",
        u"u",
        u"uu",
        u"e",
        u"ee",
        u"ai",
        u"o",
        u"oo",
        u"au",
    ]
    for uyir, uyir_utf8 in zip(vowels, utf8.uyir_letters):
        table[uyir] = uyir_utf8
    table["ak"] = utf8.aytham_letter
    print(u" ".join(utf8.agaram_letters + utf8.sanskrit_letters))
    #
    # க ச ட த ப ற ஞ ங ண ந ம ன ய ர ல வ ழ ள ஜ ஷ ஸ ஹ
    # க, ச, ட, த, ப, ற, ஞ, ங, ண, ந, ம, ன, ய, ர, ல, வ, ழ, ள, ஜ, ஷ, ஸ, ஹ
    #
    consonant_mei = [
        u"k",
        u"s",
        u"d",
        u"th",
        u"p",
        u"R",
        u"nj",
        u"ng",
        u"N",
        u"n-",
        u"m",
        u"n",
        u"y",
        u"r",
        u"l",
        u"v",
        u"zh",
        u"L",
        u"j",
        u"S",
        u"sh",
        u"ha",
    ]

    # initialize mei phonetic map
    for mei, mei_utf8 in zip(
        consonant_mei, utf8.mei_letters + utf8.sanskrit_mei_letters
    ):
        table[mei] = mei_utf8

    # build the combination table for
    # uyirmei phonetic map
    for mei, mei_agaram in zip(
        consonant_mei, utf8.agaram_letters + utf8.sanskrit_letters
    ):
        for uyir, uyir_accent in zip(vowels, utf8.accent_symbols):
            table[mei + uyir] = mei_agaram + uyir_accent
            print(u"uyirmei->phonetic | %s => %s " % (table[mei + uyir], mei + uyir))

    # special grantha characters
    table["ksha"] = u"க்ஷ"
    table["kshaa"] = u"க்ஷா"
    table["kshi"] = u"க்ஷி"
    table["kshii"] = u"க்ஷீ"
    table["kshu"] = u"க்ஷு"
    table["kshuu"] = u"க்ஷூ"
    table["kshe"] = u"க்ஷெ"
    table["kshae"] = u"க்ஷே"
    table["kshai"] = u"க்ஷை"
    table["ksho"] = u"க்ஷொ"
    table["kshoa"] = u"க்ஷோ"
    table["kshow"] = u"க்ஷௌ"
    table["ksh"] = u"க்ஷ்"
    table["sri"] = u"ஸ்ரீ"
    table["sree"] = u"ஸ்ரீ"
    table["shree"] = u"ஸ்ரீ"
    table["shri"] = u"ஸ்ரீ"
    table["fa"] = u"ஃப"
    table["faa"] = u"ஃபா"
    table["fi"] = u"ஃபி"
    table["fii"] = u"ஃபீ"
    table["fu"] = u"ஃபு"
    table["fuu"] = u"ஃபூ"
    table["fe"] = u"ஃபெ"
    table["fae"] = u"ஃபே"
    table["fai"] = u"ஃபை"
    table["fo"] = u"ஃபொ"
    table["foa"] = u"ஃபோ"
    table["fow"] = u"ஃபௌ"
    table["f"] = u"ஃப்"
    table["Za"] = u"ஃஜ"
    table["Zaa"] = u"ஃஜா"
    table["Zi"] = u"ஃஜி"
    table["Zii"] = u"ஃஜீ"
    table["Zu"] = u"ஃஜு"
    table["Zuu"] = u"ஃஜூ"
    table["Ze"] = u"ஃஜெ"
    table["Zae"] = u"ஃஜே"
    table["Zai"] = u"ஃஜை"
    table["Zo"] = u"ஃஜொ"
    table["Zoa"] = u"ஃஜோ"
    table["Zow"] = u"ஃஜௌ"
    table["Z"] = u"ஃஜ்"
    table["xa"] = u"ஃஸ"
    table["xaa"] = u"ஃஸா"
    table["xi"] = u"ஃஸி"
    table["xu"] = u"ஃஸு"
    table["xuu"] = u"ஃஸூ"
    table["xe"] = u"ஃஸெ"
    table["xae"] = u"ஃஸே"
    table["xai"] = u"ஃஸை"
    table["xo"] = u"ஃஸொ"
    table["xoa"] = u"ஃஸோ"
    table["xow"] = u"ஃஸௌ"
    table["x"] = u"ஃஸ்"

    # special numerials/ symbols
    table["1"] = u"௧"
    table["2"] = u"௨"
    table["3"] = u"௩"
    table["4"] = u"௪"
    table["5"] = u"௫"
    table["6"] = u"௬"
    table["7"] = u"௭"
    table["8"] = u"௮"
    table["9"] = u"௯"
    table["10"] = u"௰"
    table["1000"] = u"௲"

    kk = table.keys()
    kk.sort()
    for k in kk:
        v = table[k]
        print(u'\ttable[u"%s"] = u"%s"' % (k, v))


#  Key Map Table  : Acknowledgements to Kandupidi.com
#
# 		a	aa	i	ii	u	uu	e	ee	ai	o	oo	au
# 		அ	ஆ	இ	ஈ	உ	ஊ	எ	ஏ	ஐ	ஒ	ஓ	ஔ
# k	க்	க	கா	கி	கீ	கு	கூ	கெ	கே	கை	கொ	கோ	கௌ
# ng	ங்	ங	ஙா	ஙி	ஙீ	ஙு	ஙூ	ஙெ	ஙே	ஙை	ஙொ	ஙோ	ஙௌ
# s	ச்	ச	சா	சி	சீ	சு	சூ	செ	சே	சை	சொ	சோ	சௌ
# nj	ஞ்	ஞ	ஞா	ஞி	ஞீ	ஞு	ஞூ	ஞெ	ஞே	ஞை	ஞொ	ஞோ	ஞௌ
# d	ட்	ட	டா	டி	டீ	டு	டூ	டெ	டே	டை	டொ	டோ	டௌ
# N	ண்	ண	ணா	ணி	ணீ	ணு	ணூ	ணெ	ணே	ணை	ணொ	ணோ	ணௌ
# th	த்	த	தா	தி	தீ	து	தூ	தெ	தே	தை	தொ	தோ	தௌ
# n-	ந்	ந	நா	நி	நீ	நு	நூ	நெ	நே	நை	நொ	நோ	நை
# p	ப்	ப	பா	பி	பீ	பு	பூ	பெ	பே	பை	பொ	போ	பௌ
# m	ம்	ம	மா	மி	மீ	மு	மூ	மெ	மே	மை	மொ	மோ	மௌ
# y	ய்	ய	யா	யி	யீ	யு	யூ	யெ	யே	யை	யொ	யோ	யௌ
# r	ர்	ர	ரா	ரி	ரீ	ரு	ரூ	ரெ	ரே	ரை	ரொ	ரோ	ரௌ
# l	ல்	ல	லா	லி	லீ	லு	லூ	லெ	லே	லை	லொ	லோ	லௌ
# v	வ்	வ	வா	வி	வீ	வு	வூ	வெ	வே	வை	வொ	வோ	வௌ
# zh	ழ்	ழ	ழா	ழி	ழீ	ழு	ழூ	ழெ	ழே	ழை	ழொ	ழோ	ழௌ
# L	ள்	ள	ளா	ளி	ளீ	ளு	ளூ	ளெ	ளே	ளை	ளொ	ளோ	ளௌ
# R	ற்	ற	றா	றி	றீ	று	றூ	றெ	றே	றை	றொ	றோ	றௌ
# n	ன்	ன	னா	னி	னீ	னு	னூ	னெ	னே	னை	னொ	னோ	னௌ
# j	ஜ்	ஜ	ஜா	ஜி	ஜீ	ஜு	ஜூ	ஜெ	ஜே	ஜை	ஜொ	ஜோ	ஜௌ
# S	ஸ்	ஸ	ஸா	ஸி	ஸீ	ஸு	ஸூ	ஸெ	ஸே	ஸை	ஸொ	ஸோ	ஸௌ
# sh	ஷ்	ஷ	ஷா	ஷி	ஷீ	ஷு	ஷூ	ஷெ	ஷே	ஷை	ஷொ	ஷோ	ஷௌ
# h	ஹ்	ஹ	ஹா	ஹி	ஹீ	ஹு	ஹூ	ஹெ	ஹே	ஹை	ஹொ	ஹோ	ஹௌ
