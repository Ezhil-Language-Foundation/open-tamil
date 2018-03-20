# This Python file uses the following encoding: utf-8
#/usr/bin/python3
#
# Copyright (C) 2018 Nithya Duraisamy <nithyadurai87@gmail.com>
# Tamil sandhi checker - validate and fix list of Sandhi errors in Tamil text

import tamil
import collections
import codecs
import os
import sys



#http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm
BASE_DIRECTORY = os.path.split(__file__)[0]

tamil_path = os.path.join(BASE_DIRECTORY,"all-tamil-nouns.txt")
noun_file = codecs.open(tamil_path,"r","UTF-8")
noun_list = noun_file.read().strip().split()

mei_letters = tamil.utf8.mei_letters
uyir_letters = tamil.utf8.uyir_letters
ayudha_letter = ['ஃ']
kuril_letters = tamil.utf8.kuril_letters
nedil_letters = tamil.utf8.nedil_letters
agaram_letters = tamil.utf8.agaram_letters
uyirmei_letters = tamil.utf8.uyirmei_letters
vallinam_letters = tamil.utf8.vallinam_letters
mellinam_letters = tamil.utf8.mellinam_letters
tamil_letters = tamil.utf8.tamil_letters
sanskrit_letters = tamil.utf8.sanskrit_letters 
sanskrit_mei_letters = tamil.utf8.sanskrit_mei_letters 
special_chars=['.','\'',';',',',':','?','(',')','_','-','"','%','±','#','@','!','!','$','%','^','&','*','+','/','–','\\','>','<','|','}','{',']','[']
one_letter_words=['கை','தீ','தை','பூ','மை']
numbers=['0','1','2','3','4','5','6','7','8','9','½']
granda = [u"ஜ்",u"ஷ்", u"ஸ்",u"ஹ்"
,u"ஶ", 	u"ஶா", 	u"ஶி", 	u"ஶீ", u"ஶு", u"ஶூ", u"ஶெ", u"ஶே", u"ஶை", u"ஶொ", u"ஶோ", u"ஶௌ"
,u"ஜ"  ,u"ஜா"  ,u"ஜி"  ,u"ஜீ"  ,u"ஜு"  ,u"ஜூ"  ,u"ஜெ"  ,u"ஜே"  ,u"ஜை"  ,u"ஜொ"  ,u"ஜோ"  ,u"ஜௌ"
,u"ஷ"  ,u"ஷா"  ,u"ஷி"  ,u"ஷீ"  ,u"ஷு"  ,u"ஷூ"  ,u"ஷெ"  ,u"ஷே"  ,u"ஷை"  ,u"ஷொ"  ,u"ஷோ"  ,u"ஷௌ"
,u"ஸ"  ,u"ஸா"  ,u"ஸி"  ,u"ஸீ"  ,u"ஸு"  ,u"ஸூ"  ,u"ஸெ"  ,u"ஸே"  ,u"ஸை"  ,u"ஸொ"  ,u"ஸோ"  ,u"ஸௌ"
,u"ஹ"  ,u"ஹா"  ,u"ஹி"  ,u"ஹீ"  ,u"ஹு"  ,u"ஹூ"  ,u"ஹெ"  ,u"ஹே"  ,u"ஹை"  ,u"ஹொ"  ,u"ஹோ"  ,u"ஹௌ"
,u"க்ஷ" ,u"க்ஷா" ,u"க்ஷி" ,u"க்ஷீ" ,u"க்ஷு" ,u"க்ஷூ" ,u"க்ஷெ" ,u"க்ஷே" ,u"க்ஷை" ,u"க்ஷொ" ,u"க்ஷோ" ,u"க்ஷௌ" ]
english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
suttu_vina=[u'அ',u'இ',u'எ',u'யா',u'அந்த',u'இந்த',u'எந்த',u'அங்கு',u'இங்கு',u'எங்கு',u'ஆங்கு',u'ஈங்கு',u'யாங்கு',u'அப்படி',u'இப்படி',u'எப்படி',u'ஆண்டு',u'ஈண்டு',u'யாண்டு',u'அவ்வகை',u'இவ்வகை',u'எவ்வகை',u'அத்துணை',u'இத்துணை']
specific_words=[u'அது',u'இது',u'எது',u'யாது',u'அவை',u'இவை',u'எவை',u'அன்று',u'இன்று',u'என்று',u'அத்தனை',u'இத்தனை',u'எத்தனை',u'அவ்வளவு',u'இவ்வளவு',u'எவ்வளவு',u'அவ்வாறு',u'இவ்வாறு',u'எவ்வாறு',u'ஒன்று',u'இரண்டு',u'மூன்று',u'நான்கு',u'ஐந்து',u'ஆறு',u'நூறு',u'ஏழு',u'ஒன்பது',u'ஒரு',u'இரு',u'அறு',u'எழு',u'கற்க',u'நில்',u'கவனி',u'செல்',u'செல்க',u'மன்னிய',u'வெல்க',u'செப்பும்',u'வினாவும்',u'வாழ்க',u'ஓம்பல்',u'அஞ்சாமை',u'வாழி',u'வீழ்க',u'ஒழிக',u'வருக',u'உண்க',u'அருள்க',u'கருணைபுரிக',u'வருக',u'வாழிய',u'வாழியர்',u'வாரற்க',u'கூறற்க',u'செல்லற்க',u'வாரல்',u'செல்லல்',u'பகரேல்',u'கல', 'பல',u'சில',u'வா',u'எழு',u'போ',u'பார்']

def safe_splitMeiUyir(arg):
    try:
        # when uyir letters are passed to splitMeiUyir function it will throw an IndexError
        rval = safe_splitMeiUyir(arg)
        if len(rval) == 1:
            return (rval,u'')
        return rval
    except IndexError as idxerr:
        pass
    except ValueError as valerr:
        # non tamil letters cannot be split - e.g. '26வது'
        pass
    return (u'',u'')

class Results:
    # class contains results of 'check_sandhi' method
    ErrorLog = collections.namedtuple('ErrorLog',['rule','description','word']) #description of error
    def __init__(self):
        self.errors = [] #list of ErrorLog object

    def add(self,word,rule,descr):
        elog = Results.ErrorLog( rule, descr, word )
        self.errors.append(elog)

    @property
    def counter(self):
        return len(self.errors)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        summary_list = [u"%s -> (%s, %s),\n"%(err.word,err.rule,err.description) for err in self.errors]
        return u"".join(summary_list)


def check_sandhi(words):
    if not isinstance(words,list):
        words = tamil.utf8.get_words(words)

    result = Results()
    fixed_list=[]
    prev_word_stack = [u'']

    for counter,word in enumerate(words):
        prev_word = prev_word_stack.pop()
        prev_word_stack.append(word)
        next_word = (counter+1) < len(words) and words[counter+1] or u' '
        
        letters = tamil.utf8.get_letters(word)

        # வல்லினம் மிகா - கடைசி வார்த்தை
        if counter == len(words)-1:
            print(u"மிகா - Rule1 - " + word)
            fixed_list.append(word)
            result.add(word,u'விதி 1',u'மிகா') 
            break
        # வல்லினம் மிகா - வடமொழி ஆங்கில எழுத்துக்கள் மற்றும் எண்கள்
        if (any(i in letters for i in (granda + english + numbers))) == True:
            fixed_list.append(word)
            print(u"மிகா - Rule2 - " + word)
            result.add(word,u'விதி 2',u'மிகா')
            continue

        # வல்லினம் மிகா இடங்கள்           
        if (tamil.utf8.get_letters(word)[-1]) in (special_chars + mei_letters):
            fixed_list.append(word)
            print(u"மிகா - Rule3 - " + word)
            result.add(word,u'விதி 3',u'மிகா')
            continue

        # வல்லினம் மிகா சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் - எத்தனை பழங்கள்? ; எண்ணுப்பெயர்கள் - ஐந்து சிறுவர்கள்  
        # வியங்கோள் வினைமுற்று - வருக புலவரே ; பல, சில, ஏவல் வினை - வா கலையரசி
        if word in specific_words:
            fixed_list.append(word)
            print(u"மிகா - Rule4 - " + word)
            result.add(word,u'விதி 4',u'மிகா')
            continue

        # வல்லினம் மிகா வந்த, கண்ட, சொன்ன, வரும் என்பன  போன்ற பெயரெச்சங்களோடு படி, ஆறு என்னும் சொற்கள்- கண்டவாறு சொன்னான்  
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.get_letters(word)[0]) in [u'வ',u'க',u'சொ']:
                if (tamil.utf8.get_letters(word)[-1]) in [u'டி',u'று']:
                    fixed_list.append(word)
                    print(u"மிகா - Rule5 - " + word)
                    result.add(word,u'விதி 5',u'மிகா')
                    continue

        # 6.1.2 - ஓர் எழுத்துச் சொற்கள் முன் வல்லினம்  மிகல் - கை  குழந்தை
        if len(tamil.utf8.get_letters(word)) == 1:
            if  word in one_letter_words:
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                    
                        fixed_list.append(word + mei_of_first_char_of_next_word)
                        print(u"மிகும் - Rule1 - " + word + mei_of_first_char_of_next_word)
                        result.add(word,u'விதி 1',u'மிகும்')
                        continue    

        # வல்லினம் மிகா ஒடு & ஓடு என உயிர் ஈறு கொண்டவை - கத்தியோடு நின்றான் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in [u'ஒ',u'ஓ']:
                    if (tamil.utf8.get_letters(word)[-1]) == u'டு':
                        fixed_list.append(word)
                        print(u"மிகா - Rule6 - " + word)
                        result.add(word,u'விதி 6',u'மிகா')
                        continue

        # வல்லினம் மிகா ‘கொண்டு’ என்னும் சொல்லுருபு -கத்திகொண்டு குத்தினான்
        if ''.join(tamil.utf8.get_letters(word)[-3:]) ==  u'கொண்டு':
            fixed_list.append(word)
            print(u"மிகா - Rule7 - " + word)
            result.add(word,u'விதி 7',u'மிகா')
            continue

        # வல்லினம் மிகா இல் என்பதோடு இருந்து என்னும்  சொல்லுருபு - வீட்டிலிருந்து சென்றான்  
        if ''.join(tamil.utf8.get_letters(word)[-4:]) == u'லிருந்து':
            fixed_list.append(word)
            print(u"மிகா - Rule8 - " + word)
            result.add(word,u'விதி 8',u'மிகா')
            continue

        # வல்லினம் மிகா இன் என்பதோடு நின்று என்னும் சொல்லுருபு - வீட்டினின்று வெளியேறினான் 
        if ''.join(tamil.utf8.get_letters(word)[-3:]) == u'னின்று':
            fixed_list.append(word)
            print(u"மிகா - Rule9 - " + word)
            result.add(word,u'விதி 9',u'மிகா')
            continue

        # வல்லினம் மிகா ஆறாம் வேற்றுமைக்கு உரிய அது - எனது புத்தகம்
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'அ':
                    if (tamil.utf8.get_letters(word)[-1]) == u'து':
                        fixed_list.append(word)
                        print(u"மிகா - Rule10 - " + word)
                        result.add(word,u'விதி 10',u'மிகா')
                        continue

        # வல்லினம் மிகா ‘உடைய’ என்னும் சொல்லுருபு- என்னுடைய புத்தகம்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) == u'டைய':  
            if ''.join(tamil.utf8.get_letters(word)[-3]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == u'உ':
                    fixed_list.append(word)
                    print(u"மிகா - Rule11 - " + word)
                    result.add(word,u'விதி 11',u'மிகா')
                    continue

        # வல்லினம் மிகா மென்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ண்டு, ந்து, ன்று என முடியும் -கண்டு பேசினார்
        # இடைத்தொடர்க் குற்றியலுகர  வினையெச்சங்கள் - ய்து என முடியும் - செய்து தந்தான்
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in [u'ண்டு',u'ந்து',u'ன்று',u'ய்து',u'ன்கு']:            
            fixed_list.append(word)
            print(u"மிகா - Rule12 - " + word)
            result.add(word,u'விதி 12',u'மிகா')
            continue

        # வல்லினம் மிகா மற்ற பெயரெச்சங்கள் - இன்றி, ஆத, இய, ஐய,ற்ற,ல்ல, ட்ட ன்ற, ந்த, த்து உம் ஆகிய  விகுதிகள் பெற்று முடியும்  
        # அழியாத கல்வி 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == u'த':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'ஆ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule13 - " + word)
                        result.add(word,u'விதி 13',u'மிகா')
                        continue

        # பெரிய பெண் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == u'ய':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):           
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'இ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule14 - " + word)
                        result.add(word,u'விதி 14',u'மிகா')
                        continue

        # இன்றைய செய்தி 
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == u'ய':   
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):          
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'ஐ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule15 - " + word)
                        result.add(word,u'விதி 15',u'மிகா')
                        continue

        # கேட்கும் பாட்டு
        if len(tamil.utf8.get_letters(word)) > 1:
            if ''.join(tamil.utf8.get_letters(word)[-1]) == u'ம்':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):         
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'உ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule16 - " + word)
                        result.add(word,u'விதி 16',u'மிகா')
                        continue

        if ''.join(tamil.utf8.get_letters(word)[-2:]) == u'ன்றி':  
            if ''.join(tamil.utf8.get_letters(word)[-3]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):            
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-3])[1]) == u'இ':
                    fixed_list.append(word)
                    print(u"மிகா - Rule17 - " + word)
                    result.add(word,u'விதி 17',u'மிகா')
                    continue

        # கற்ற சிறுவன் 
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in [u'ற்ற',u'ல்ல',u'ட்ட',u'ன்ற',u'ந்த',u'த்து',u'இனி']:            
            fixed_list.append(word)
            print(u"மிகா - Rule18 - " + word)
            result.add(word,u'விதி 18',u'மிகா')
            continue

        # வல்லினம் மிகா மற்ற வினையெச்சங்கள் - ஆக, அன, யுற,றகு,க்கு ஆகிய  விகுதிகள் பெற்று முடியும்  
        # அழியாத கல்வி 
        if len(tamil.utf8.get_letters(word)) > 1:  
            if ''.join(tamil.utf8.get_letters(word)[-1:]) == u'க': 
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):             
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'ஆ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule19 - " + word)
                        result.add(word,u'விதி 19',u'மிகா')
                        continue
        if len(tamil.utf8.get_letters(word)) > 1:  
            if ''.join(tamil.utf8.get_letters(word)[-1]) == u'ன':  
                if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):               
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) == u'அ':
                        fixed_list.append(word)
                        print(u"மிகா - Rule20 - " + word)
                        result.add(word,u'விதி 20',u'மிகா')
                        continue

        if ''.join(tamil.utf8.get_letters(word)[-2:]) in [u'யுற',u'றகு',u'ற்கு',u'க்கு',u'போது']:            
                fixed_list.append(word)
                print(u"மிகா - Rule21 - " + word)
                result.add(word,u'விதி 21',u'மிகா')
                continue
      

        # வல்லினம் மிகா இரட்டைக் கிளவி, அடுக்குத்தொடர்கள் - கல கல
        if word == words[counter + 1]:
            fixed_list.append(word)
            print(u"மிகா - Rule22 - " + word)
            result.add(word,u'விதி 22',u'மிகா')
            continue

        # வல்லினம் மிகா கள், தல் விகுதிகள் - வாக்குகள்  வித்தியாசம் 
        if ''.join(tamil.utf8.get_letters(word)[-2:]) in [u'கள்',u'தல்']:
            fixed_list.append(word)
            print(u"மிகா - Rule23 - " + word)
            result.add(word,u'விதி 23',u'மிகா')
            continue

        # வல்லினம் மிகா பொதுப்பெயர்கள் - மகளிர் கல்லூரி 
        if word in noun_list :   
            fixed_list.append(word)
            print(u"மிகா - Rule24 - " + word)
            result.add(word,u'விதி 24',u'மிகா')
            continue

        # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல் - அந்த பையன்          
        if (tamil.utf8.get_letters(word)) in suttu_vina:
            if (tamil.utf8.get_letters(word)[-1]) not in mei_letters:
                if ''.join(tamil.utf8.get_letters(word)[1:3]) == u'வ்வா':
                    fixed_list.append(word)
                    print(u"மிகா - Rule25 - " + word)
                    result.add(word,u'விதி 25',u'மிகா')
                    continue  
                if ''.join(tamil.utf8.get_letters(word)[-2:]) != u'டைய':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:
                            fixed_list.append(word + mei_of_first_char_of_next_word)
                            print(u"மிகும் - Rule2 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 2',u'மிகும்')
                            continue  

        # 6.1.3 - 1 வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - கற்று கொடுத்தான் 
        if len(tamil.utf8.get_letters(word)) > 1:        
            if (tamil.utf8.get_letters(word)[-2]) in vallinam_letters:
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == u'உ':                
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                    
                            fixed_list.append(word + mei_of_first_char_of_next_word)   
                            print(u"மிகும் - Rule3 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 3',u'மிகும்')
                            continue

        # 6.1.3 - 2 மென்தொடர்க் குற்றியலுகரம் முன்  வல்லினம் மிகல் - குரங்கு குட்டி 
        if len(tamil.utf8.get_letters(word)) > 1:     
            if (tamil.utf8.get_letters(word)[-2]) in mellinam_letters:
                uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                if uyir_of_last_char == u'உ':
                    if ''.join(tamil.utf8.get_letters(word)[-3:]) != u'கொண்டு':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:
                                fixed_list.append(word + mei_of_first_char_of_next_word)            
                                print(u"மிகும் - Rule4 - " + word + mei_of_first_char_of_next_word)
                                result.add(word,u'விதி 4',u'மிகும்')
                                continue

        # 6.1.4 முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல் - 1 - தனிக் குறில் அடுத்து வரும் உகரம்  - பொது பணி   
        if len(tamil.utf8.get_letters(word)) == 2:
            if tamil.utf8.get_letters(word)[-2] not in uyir_letters:
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1]) in kuril_letters:                
                    uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                    if uyir_of_last_char == u'உ':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:                            
                                fixed_list.append(word + mei_of_first_char_of_next_word)              
                                print(u"மிகும் - Rule5 - " + word + mei_of_first_char_of_next_word)
                                result.add(word,u'விதி 5',u'மிகும்')
                                continue

        # 6.1.3 - 3   உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் - விறகு கடை
        if len(tamil.utf8.get_letters(word)) > 1:  
            if tamil.utf8.get_letters(word)[-2] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
                    if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                        uyir_of_last_char = tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]
                        if uyir_of_last_char == u'உ':
                            first_char_of_next_word = (words[counter + 1][0])
                            if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                                mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                                if mei_of_first_char_of_next_word in vallinam_letters:                        
                                    fixed_list.append(word + mei_of_first_char_of_next_word)              
                                    print(u"மிகும் - Rule6 - " + word + mei_of_first_char_of_next_word)
                                    result.add(word,u'விதி 6',u'மிகும்')
                                    continue

        # 6.1.4 - 1 - வல்லினமெய் அல்லாத பிற மெய்களின் மேல் ஏறி வருகின்ற உகரம் - தேர்வு கட்டணம்      
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[0]) not in [u'க்',u'ச்',u'ட்',u'த்',u'ப்',u'ற்']:
                if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                    if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'உ':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:                    
                                fixed_list.append(word + mei_of_first_char_of_next_word)              
                                print(u"மிகும் - Rule7 - " + word + mei_of_first_char_of_next_word)
                                result.add(word,u'விதி 7',u'மிகும்')
                                continue

        # 6.1.5 - 1 - இரண்டாம் வேற்றுமை விரி - கனியை  தின்றான்    
        if len(tamil.utf8.get_letters(word)) > 1: 
            if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஐ':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                
                            fixed_list.append(word + mei_of_first_char_of_next_word)              
                            print(u"மிகும் - Rule8 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 8',u'மிகும்')
                            continue

        # 6.1.5 - 2 -  நான்காம் வேற்றுமை விரி - எனக்கு  கொடு
        if len(tamil.utf8.get_letters(word)) > 1:     
            if tamil.utf8.get_letters(word)[-1] == u'கு':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print(u"மிகும் - Rule9 - " + word + mei_of_first_char_of_next_word)
                        result.add(word,u'விதி 9',u'மிகும்')
                        continue

        # 6.1.6 - 1 - அ இ ய் ர் - அகர, இகர, யகர மெய் ஈற்று வினையெச்சம்; ஈறுகெட்ட எதிர்மறைப் பெயரெச்சம் ்
        # வர சொன்னான் குறிஞ்சி தலைவன்  தேங்காய் சட்னி  தயிர் குடம் தீரா சிக்கல் 
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'அ':
                    if ''.join(tamil.utf8.get_letters(word)[-2:]) != u'டைய':
                        first_char_of_next_word = (words[counter + 1][0])
                        if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                            mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                            if mei_of_first_char_of_next_word in vallinam_letters:                    
                                fixed_list.append(word + mei_of_first_char_of_next_word)              
                                print(u"மிகும் - Rule10 - " + word + mei_of_first_char_of_next_word)
                                result.add(word,u'விதி 10',u'மிகும்')
                                continue
        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'இ':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                
                            fixed_list.append(word + mei_of_first_char_of_next_word)              
                            print(u"மிகும் - Rule11 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 11',u'மிகும்')
                            continue        
    
        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ய்':
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if mei_of_first_char_of_next_word in vallinam_letters:                
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print(u"மிகும் - Rule12 - " + word + mei_of_first_char_of_next_word)
                        result.add(word,u'விதி 12',u'மிகும்')
                        continue

        if len(tamil.utf8.get_letters(word)) > 1:
            if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ர்':            
                first_char_of_next_word = (words[counter + 1][0])
                if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                    mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                    if first_char_of_next_word in special_chars:
                        fixed_list.append(word)
                        print(u"மிகா - Rule13 - " + word)
                        result.add(word,u'விதி 13',u'மிகும்')
                        continue
                    if mei_of_first_char_of_next_word in vallinam_letters:                    
                        fixed_list.append(word + mei_of_first_char_of_next_word)              
                        print(u"மிகும் - Rule14 - " + word + mei_of_first_char_of_next_word)
                        result.add(word,u'விதி 14',u'மிகும்')
                        continue 

        if len(tamil.utf8.get_letters(word)) > 1:
            if tamil.utf8.get_letters(word)[-1] not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english + english):    
                if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])[1]) == u'ஆ':
                    first_char_of_next_word = (words[counter + 1][0])
                    if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
                        mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
                        if mei_of_first_char_of_next_word in vallinam_letters:                
                            fixed_list.append(word + mei_of_first_char_of_next_word)              
                            print(u"மிகும் - Rule15 - " + word + mei_of_first_char_of_next_word)
                            result.add(word,u'விதி 15',u'மிகும்')
                            continue  

        # 6.1.7 - மகர இறுதி கெட்டு உயிர் ஈறாய் நிற்கும் சொற்கள் - மரம் கிளை
        # But this logic tot working for - உலகப்படம்  பார்த்து,  எடுப்பதெல்லாம் பெரிய
        # if len(tamil.utf8.get_letters(word)) > 1:
            # if (tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-1])) == u'ம்':
            #     if ''.join(tamil.utf8.get_letters(word)[-2]) not in (uyir_letters + numbers + ayudha_letter + granda + special_chars + english):
            #         if tamil.utf8.splitMeiUyir(tamil.utf8.get_letters(word)[-2])[1] in uyir_letters:
            #             first_char_of_next_word = (words[counter + 1][0])
            #             if first_char_of_next_word not in (uyir_letters + numbers + ayudha_letter + granda):
            #                 if first_char_of_next_word not in ayudha_letter:
            #                     mei_of_first_char_of_next_word = tamil.utf8.splitMeiUyir(first_char_of_next_word)[0]
            #                     if mei_of_first_char_of_next_word in vallinam_letters:                    
            #                         fixed_list.append(word[:-2] + mei_of_first_char_of_next_word)            
            #                         print(u"மிகும் - Rule16 - " + word[:-2] + mei_of_first_char_of_next_word)
            #                         result.add(word,u'விதி 16',u'மிகும்')
            #                         continue   
            
        fixed_list.append(word)
        #print(u"விதி " + word)
    return fixed_list,result  

def run_sandhi_checker_command_line():
    if len(sys.argv) == 1:
        try:
            in_path = os.path.join(BASE_DIRECTORY,'Input_text.txt') #default
        except Exception as ioe:
            print(u"Usage: sandhi_checker.py <filename>")
            print(u"Output will also be sent to file 'Output_text.txt'")
            sys.exit(-1)
    else:
        in_path = sys.argv[1]
    file_inp = codecs.open(in_path,'r','UTF-8')
    a = file_inp.read()
    file_inp.close()

    new_path = os.path.join(BASE_DIRECTORY,'Output_text.txt')
    file_opt = codecs.open(new_path,'w','UTF-8')

    words=tamil.utf8.get_words(a)
    fixed_list,result = check_sandhi(words)
    print(u' '.join(fixed_list))
    print(u"%s"%result)

if __name__ == u"__main__":
    run_sandhi_checker_command_line()


    
