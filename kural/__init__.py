# This Python file uses the following encoding: utf-8

# This file is now part of Open-Tamil; originally published as
# libkural in 2013, to access programatically the ancient
# Tamil ethics/moral canon 'Thirukkural'.
# Original PIP package: https://pypi.org/project/libkural/#files

##Copyright (c) 2013, Muthiah Annamalai
##All rights reserved.
##
##Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
##
##    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
##    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
##
##THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.Code and source is licensed under terms of BSD 2 open source license

from xml.sax.saxutils import unescape


class Kural:
    def __init__(self):
        self.no = -1;
        self.pal = '';
        self.adhikaram = '';
        self.ta = '';
        self.en = '';
        self.commentary = '';

    def __str__(self):
        q = """<kural id="%04d" pal="%s" adhikaram="%s">
<ta-content>%s</ta-content>
<en-content>%s</en-content>
<en-commentary>%s</en-commentary>
</kural>""" % (self.no, (self.pal), (self.adhikaram), (self.ta), (self.en), (self.commentary));
        return q

    @staticmethod
    def factory(no, pal, adhikaram, ta, en, commentary):
        k = Kural();

        # sapient
        if (isinstance(no, str) or isinstance(no, str)):
            no = int(no);
        assert (no > 0 and no < 1331);
        k.no = no;
        k.adhikaram = adhikaram;
        k.pal = unescape(pal);
        D = {'&#9;': ' ', '&#10;': '\n', '&quot;': '\''};
        k.ta = unescape(ta, D);
        k.en = unescape(en, D);
        k.commentary = unescape(commentary, D);
        return k

    @staticmethod
    def load_data_base():
        k = list(range(0, 1330));
        k[0] = Kural.factory(1, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''அகர முதல எழுத்தெல்லாம் ஆதி
  பகவன் முதற்றே உலகு.''', '''A, as its first of letters, every speech maintains;
The \'Primal Deity\' is first through all the world\'s domains.''',
                             '''As all letters have the letter A for their first, so the world has the eternal God for its first.''');
        k[1] = Kural.factory(2, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''கற்றதனால் ஆய பயனென்கொல் வாலறிவன்
  நற்றாள் தொழாஅர் எனின்.''', '''No fruit have men of all their studied lore,
Save they the \'Purely Wise One\'s\' feet adore.''',
                             '''What Profit have those derived from learning, who worship not the good feet of Him who is possessed of pure knowledge ?''');
        k[2] = Kural.factory(3, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''மலர்மிசை ஏகினான் மாணடி சேர்ந்தார்
  நிலமிசை நீடுவாழ் வார்.''', '''His feet, \'Who o\'er the full-blown flower hath past,\' who gain
In bliss long time shall dwell above this earthly plain.''',
                             '''They who are united to the glorious feet of Him who occupies swiftly the flower of the mind, shall flourish in the highest of worlds (heaven).''');
        k[3] = Kural.factory(4, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''வேண்டுதல் வேண்டாமை இலானடி சேர்ந்தார்க்கு
  யாண்டும் இடும்பை இல.''', '''His foot, \'Whom want affects not, irks not grief,\' who gain
Shall not, through every time, of any woes complain.''',
                             '''To those who meditate the feet of Him who is void of desire or aversion, evil shall never come.''');
        k[4] = Kural.factory(5, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''இருள்சேர் இருவினையும் சேரா இறைவன்
  பொருள்சேர் புகழ்புரிந்தார் மாட்டு.''', '''The men, who on the \'King\'s\' true praised delight to dwell,
Affects not them the fruit of deeds done ill or well.''',
                             '''The two-fold deeds that spring from darkness shall not adhere to those who delight in the true praise of God.''');
        k[5] = Kural.factory(6, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''பொறிவாயில் ஐந்தவித்தான் பொய்தீர் ஒழுக்க
  நெறிநின்றார் நீடுவாழ் வார்.''', '''Long live they blest, who \'ve stood in path from falsehood freed;
His, \'Who quenched lusts that from the sense-gates five proceed\'.''',
                             '''Those shall long proposer who abide in the faultless way of Him who has destroyed the five desires of the senses.''');
        k[6] = Kural.factory(7, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''தனக்குவமை இல்லாதான் தாள்சேர்ந்தார்க் கல்லால்
  மனக்கவலை மாற்றல் அரிது.''', '''Unless His foot, \'to Whom none can compare,\' men gain,
\'Tis hard for mind to find relief from anxious pain.''',
                             '''Anxiety of mind cannot be removed, except from those who are united to the feet of Him who is incomparable.''');
        k[7] = Kural.factory(8, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''அறவாழி அந்தணன் தாள்சேர்ந்தார்க் கல்லால்
  பிறவாழி நீந்தல் அரிது.''', '''Unless His feet \'the Sea of Good, the Fair and Bountiful,\' men gain,
\'Tis hard the further bank of being\'s changeful sea to attain.''',
                             '''None can swim the sea of vice, but those who are united to the feet of that gracious Being who is a sea of virtue.''');
        k[8] = Kural.factory(9, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''கோளில் பொறியின் குணமிலவே எண்குணத்தான்
  தாளை வணங்காத் தலை.''', '''Before His foot, \'the Eight-fold Excellence,\' with unbent head,
Who stands, like palsied sense, is to all living functions dead.''',
                             '''The head that worships not the feet of Him who is possessed of eight attributes, is as useless as a sense without the power of sensation.''');
        k[9] = Kural.factory(10, '''அறத்துப்பால்''', '''கடவுள் வாழ்த்து''', '''பிறவிப் பெருங்கடல் நீந்துவர் நீந்தார்
  இறைவன் அடிசேரா தார்.''', '''They swim the sea of births, the \'Monarch\'s\' foot who gain;
None others reach the shore of being\'s mighty main.''',
                             '''None can swim the great sea of births but those who are united to the feet of God.''');
        k[10] = Kural.factory(11, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''வான்நின்று உலகம் வழங்கி வருதலால்
  தான்அமிழ்தம் என்றுணரற் பாற்று.''', '''The world its course maintains through life that rain unfailing gives;
Thus rain is known the true ambrosial food of all that lives.''',
                              '''By the continuance of rain the world is preserved in existence; it is therefore worthy to be called ambrosia.''');
        k[11] = Kural.factory(12, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''துப்பார்க்குத் துப்பாய துப்பாக்கித் துப்பார்க்குத்
  துப்பாய தூஉம் மழை.''', '''The rain makes pleasant food for eaters rise;
As food itself, thirst-quenching draught supplies.''', '''Rain produces good food, and is itself food.''');
        k[12] = Kural.factory(13, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''விண்இன்று பொய்ப்பின் விரிநீர் வியனுலகத்து
  உள்நின்று உடற்றும் பசி.''', '''If clouds, that promised rain, deceive, and in the sky remain,
Famine, sore torment, stalks o\'er earth\'s vast ocean-girdled plain.''',
                              '''If the cloud, withholding rain, deceive (our hopes) hunger will long distress the sea-girt spacious world.''');
        k[13] = Kural.factory(14, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''ஏரின் உழாஅர் உழவர் புயல்என்னும்
  வாரி வளங்குன்றிக் கால்.''', '''If clouds their wealth of waters fail on earth to pour,
The ploughers plough with oxen\'s sturdy team no more.''',
                              '''If the abundance of wealth imparting rain diminish, the labour of the plough must cease.''');
        k[14] = Kural.factory(15, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''கெடுப்பதூஉம் கெட்டார்க்குச் சார்வாய்மற் றாங்கே
  எடுப்பதூஉம் எல்லாம் மழை.''', '''\'Tis rain works all: it ruin spreads, then timely aid supplies;
As, in the happy days before, it bids the ruined rise.''',
                              '''Rain by its absence ruins men; and by its existence restores them to fortune.''');
        k[15] = Kural.factory(16, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''விசும்பின் துளிவீழின் அல்லால்மற் றாங்கே
  பசும்புல் தலைகாண்பு அரிது.''', '''If from the clouds no drops of rain are shed.
\'Tis rare to see green herb lift up its head.''',
                              '''If no drop falls from the clouds, not even the green blade of grass will be seen.''');
        k[16] = Kural.factory(17, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''நெடுங்கடலும் தன்நீர்மை குன்றும் தடிந்தெழிலி
  தான்நல்கா தாகி விடின்.''', '''If clouds restrain their gifts and grant no rain,
The treasures fail in ocean\'s wide domain.''',
                              '''Even the wealth of the wide sea will be diminished, if the cloud that has drawn (its waters) up gives them not back again (in rain).''');
        k[17] = Kural.factory(18, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''சிறப்பொடு பூசனை செல்லாது வானம்
  வறக்குமேல் வானோர்க்கும் ஈண்டு.''', '''If heaven grow dry, with feast and offering never more,
Will men on earth the heavenly ones adore.''',
                              '''If the heaven dry up, neither yearly festivals, nor daily worship will be offered in this world, to the celestials.''');
        k[18] = Kural.factory(19, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''தானம் தவம்இரண்டும் தங்கா வியன்உலகம்
  வானம் வழங்கா தெனின்.''', '''If heaven its watery treasures ceases to dispense,
Through the wide world cease gifts, and deeds of \'penitence\'.''',
                              '''If rain fall not, penance and alms-deeds will not dwell within this spacious world.''');
        k[19] = Kural.factory(20, '''அறத்துப்பால்''', '''வான்சிறப்பு''', '''நீர்இன்று அமையாது உலகெனின் யார்யார்க்கும்
  வான்இன்று அமையாது ஒழுக்கு.''', '''When water fails, functions of nature cease, you say;
Thus when rain fails, no men can walk in \'duty\'s ordered way\'.''',
                              '''If it be said that the duties of life cannot be discharged by any person without water, so without rain there cannot be the flowing of water.''');
        k[20] = Kural.factory(21, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''ஒழுக்கத்து நீத்தார் பெருமை விழுப்பத்து
  வேண்டும் பனுவல் துணிவு.''', '''The settled rule of every code requires, as highest good,
Their greatness who, renouncing all, true to their rule have stood.''',
                              '''The end and aim of all treatise is to extol beyond all other excellence, the greatness of those who, while abiding in the rule of conduct peculiar to their state, have abandoned all desire.''');
        k[21] = Kural.factory(22, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''துறந்தார் பெருமை துணைக்கூறின் வையத்து
  இறந்தாரை எண்ணிக்கொண் டற்று.''', '''As counting those that from the earth have passed away,
\'Tis vain attempt the might of holy men to say.''',
                              '''To describe the measure of the greatness of those who have forsaken the two-fold desires, is like counting the dead.''');
        k[22] = Kural.factory(23, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''இருமை வகைதெரிந்து ஈண்டுஅறம் பூண்டார்
  பெருமை பிறங்கிற்று உலகு.''', '''Their greatness earth transcends, who, way of both worlds weighed,
In this world take their stand, in virtue\'s robe arrayed.''',
                              '''The greatness of those who have discovered the properties of both states of being, and renounced the world, shines forth on earth (beyond all others).''');
        k[23] = Kural.factory(24, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''உரனென்னும் தோட்டியான் ஓரைந்தும் காப்பான்
  வரனென்னும் வைப்பிற்கோர் வித்தது.''', '''He, who with firmness, curb the five restrains,
Is seed for soil of yonder happy plains.''',
                              '''He who guides his five senses by the hook of wisdom will be a seed in the world of heaven.''');
        k[24] = Kural.factory(25, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''ஐந்தவித்தான் ஆற்றல் அகல்விசும்பு ளார்கோமான்
  இந்திரனே சாலுங் கரி.''', '''Their might who have destroyed \'the five\', shall soothly tell
Indra, the lord of those in heaven\'s wide realms that dwell.''',
                              '''Indra, the king of the inhabitants of the spacious heaven, is himself, a sufficient proof of the strength of him who has subdued his five senses.''');
        k[25] = Kural.factory(26, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''செயற்கரிய செய்வார் பெரியர் சிறியர்
  செயற்கரிய செய்கலா தார்.''', '''Things hard in the doing will great men do;
Things hard in the doing the mean eschew.''',
                              '''The great will do those things which is difficult to be done; but the mean cannot do them.''');
        k[26] = Kural.factory(27, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''சுவைஒளி ஊறுஓசை நாற்றமென ஐந்தின்
  வகைதெரிவான் கட்டே உலகு.''', '''Taste, light, touch, sound, and smell: who knows the way
Of all the five,- the world submissive owns his sway.''',
                              '''The world is within the knowledge of him who knows the properties of taste, sight, touch, hearing and smell.''');
        k[27] = Kural.factory(28, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''நிறைமொழி மாந்தர் பெருமை நிலத்து
  மறைமொழி காட்டி விடும்.''', '''The might of men whose word is never vain,
The \'secret word\' shall to the earth proclaim.''',
                              '''The hidden words of the men whose words are full of effect, will shew their greatness to the world.''');
        k[28] = Kural.factory(29, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''குணமென்னும் குன்றேறி நின்றார் வெகுளி
  கணமேயும் காத்தல் அரிது.''', '''The wrath \'tis hard e\'en for an instant to endure,
Of those who virtue\'s hill have scaled, and stand secure.''',
                              '''The anger of those who have ascended the mountain of goodness, though it continue but for a moment, cannot be resisted.''');
        k[29] = Kural.factory(30, '''அறத்துப்பால்''', '''நீத்தார் பெருமை''', '''அந்தணர் என்போர் அறவோர்மற் றெவ்வுயிர்க்கும்
  செந்தண்மை பூண்டொழுக லான்.''', '''Towards all that breathe, with seemly graciousness adorned they live;
And thus to virtue\'s sons the name of \'Anthanar\' men give,''',
                              '''The virtuous are truly called Anthanar; because in their conduct towards all creatures they are clothed in kindness.''');
        k[30] = Kural.factory(31, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''சிறப்புஈனும் செல்வமும் ஈனும் அறத்தினூஉங்கு
  ஆக்கம் எவனோ உயிர்க்கு.''', '''It yields distinction, yields prosperity; what gain
Greater than virtue can a living man obtain?''',
                              '''Virtue will confer heaven and wealth; what greater source of happiness can man possess ?''');
        k[31] = Kural.factory(32, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''அறத்தினூஉங்கு ஆக்கமும் இல்லை அதனை
  மறத்தலின் ஊங்கில்லை கேடு.''', '''No greater gain than virtue aught can cause;
No greater loss than life oblivious of her laws.''',
                              '''There can be no greater source of good than (the practice of) virtue; there can be no greater source of evil than the forgetfulness of it.''');
        k[32] = Kural.factory(33, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''ஒல்லும் வகையான் அறவினை ஓவாதே
  செல்லும்வாய் எல்லாஞ் செயல்.''', '''To finish virtue\'s work with ceaseless effort strive,
What way thou may\'st, where\'er thou see\'st the work may thrive.''',
                              '''As much as possible, in every way, incessantly practise virtue.''');
        k[33] = Kural.factory(34, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''மனத்துக்கண் மாசிலன் ஆதல் அனைத்தறன்
  ஆகுல நீர பிற.''', '''Spotless be thou in mind! This only merits virtue\'s name;
All else, mere pomp of idle sound, no real worth can claim.''',
                              '''Let him who does virtuous deeds be of spotless mind; to that extent is virtue; all else is vain show.''');
        k[34] = Kural.factory(35, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''அழுக்காறு அவாவெகுளி இன்னாச்சொல் நான்கும்
  இழுக்கா இயன்றது அறம்.''', '''\'Tis virtue when, his footsteps sliding not through envy, wrath,
Lust, evil speech-these four, man onwards moves in ordered path.''',
                              '''That conduct is virtue which is free from these four things, viz, malice, desire, anger and bitter speech.''');
        k[35] = Kural.factory(36, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''அன்றறிவாம் என்னாது அறஞ்செய்க மற்றது
  பொன்றுங்கால் பொன்றாத் துணை.''', '''Do deeds of virtue now. Say not, \'To-morrow we\'ll be wise\';
Thus, when thou diest, shalt thou find a help that never dies.''',
                              '''Defer not virtue to another day; receive her now; and at the dying hour she will be your undying friend.''');
        k[36] = Kural.factory(37, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''அறத்தாறு இதுவென வேண்டா சிவிகை
  பொறுத்தானோடு ஊர்ந்தான் இடை.''', '''Needs not in words to dwell on virtue\'s fruits: compare
The man in litter borne with them that toiling bear!''',
                              '''The fruit of virtue need not be described in books; it may be inferred from seeing the bearer of a palanquin and the rider therein.''');
        k[37] = Kural.factory(38, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''வீழ்நாள் படாஅமை நன்றாற்றின் அஃதொருவன்
  வாழ்நாள் வழியடைக்கும் கல்.''', '''If no day passing idly, good to do each day you toil,
A stone it will be to block the way of future days of moil.''',
                              '''If one allows no day to pass without some good being done, his conduct will be a stone to block up the passage to other births.''');
        k[38] = Kural.factory(39, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''அறத்தான் வருவதே இன்பம் மற்றெல்லாம்
  புறத்த புகழும் இல.''', '''What from virtue floweth, yieldeth dear delight;
All else extern, is void of glory\'s light.''',
                              '''Only that pleasure which flows from domestic virtue is pleasure; all else is not pleasure, and it is without praise.''');
        k[39] = Kural.factory(40, '''அறத்துப்பால்''', '''அறன்வலியுறுத்தல்''', '''செயற்பால தோரும் அறனே ஒருவற்கு
  உயற்பால தோரும் பழி.''', '''\'Virtue\' sums the things that should be done;
\'Vice\' sums the things that man should shun.''',
                              '''That is virtue which each ought to do, and that is vice which each should shun.''');
        k[40] = Kural.factory(41, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''இல்வாழ்வான் என்பான் இயல்புடைய மூவர்க்கும்
  நல்லாற்றின் நின்ற துணை.''', '''The men of household virtue, firm in way of good, sustain
The other orders three that rule professed maintain.''',
                              '''He will be called a (true) householder, who is a firm support to the virtuous of the three orders in their good path.''');
        k[41] = Kural.factory(42, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''துறந்தார்க்கும் துவ்வாதவர்க்கும் இறந்தார்க்கும் இல்வாழ்வான்
  என்பான் துணை.''', '''To anchorites, to indigent, to those who\'ve passed away,
The man for household virtue famed is needful held and stay.''',
                              '''He will be said to flourish in domestic virtue who aids the forsaken, the poor, and the dead.''');
        k[42] = Kural.factory(43, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''தென்புலத்தார் தெய்வம் விருந்தொக்கல் தானென்றாங்கு
  ஐம்புலத்தாறு ஓம்பல் தலை.''', '''The manes, God, guests kindred, self, in due degree,
These five to cherish well is chiefest charity.''',
                              '''The chief (duty of the householder) is to preserve the five-fold rule (of conduct) towards the manes, the Gods, his guests, his relations and himself.''');
        k[43] = Kural.factory(44, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''பழியஞ்சிப் பாத்தூண் உடைத்தாயின் வாழ்க்கை
  வழியெஞ்சல் எஞ்ஞான்றும் இல்.''', '''Who shares his meal with other, while all guilt he shuns,
His virtuous line unbroken though the ages runs.''',
                              '''His descendants shall never fail who, living in the domestic state, fears vice (in the acquisition of property) and shares his food (with others).''');
        k[44] = Kural.factory(45, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''அன்பும் அறனும் உடைத்தாயின் இல்வாழ்க்கை
  பண்பும் பயனும் அது.''', '''If love and virtue in the household reign,
This is of life the perfect grace and gain.''',
                              '''If the married life possess love and virtue, these will be both its duty and reward.''');
        k[45] = Kural.factory(46, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''அறத்தாற்றின் இல்வாழ்க்கை ஆற்றின் புறத்தாற்றில்
  போஒய்ப் பெறுவ எவன்.''', '''If man in active household life a virtuous soul retain,
What fruit from other modes of virtue can he gain?''',
                              '''What will he who lives virtuously in the domestic state gain by going into the other, (ascetic) state ?''');
        k[46] = Kural.factory(47, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''இயல்பினான் இல்வாழ்க்கை வாழ்பவன் என்பான்
  முயல்வாருள் எல்லாம் தலை.''', '''In nature\'s way who spends his calm domestic days,
\'Mid all that strive for virtue\'s crown hath foremost place.''',
                              '''Among all those who labour (for future happiness) he is greatest who lives well in the household state.''');
        k[47] = Kural.factory(48, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''ஆற்றின் ஒழுக்கி அறனிழுக்கா இல்வாழ்க்கை
  நோற்பாரின் நோன்மை உடைத்து.''', '''Others it sets upon their way, itself from virtue ne\'er declines;
Than stern ascetics\' pains such life domestic brighter shines.''',
                              '''The householder who, not swerving from virtue, helps the ascetic in his way, endures more than those who endure penance.''');
        k[48] = Kural.factory(49, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''அறனென்ப் பட்டதே இல்வாழ்க்கை அஃதும்
  பிறன்பழிப்ப தில்லாயின் நன்று.''', '''The life domestic rightly bears true virtue\'s name;
That other too, if blameless found, due praise may claim.''',
                              '''The marriage state is truly called virtue. The other state is also good, if others do not reproach it.''');
        k[49] = Kural.factory(50, '''அறத்துப்பால்''', '''இல்வாழ்க்கை''', '''வையத்துள் வாழ்வாங்கு வாழ்பவன் வான்உநற்யும்
  தெய்வத்துள் வைக்கப் படும்.''', '''Who shares domestic life, by household virtues graced,
Shall, mid the Gods, in heaven who dwell, be placed.''',
                              '''He who on earth has lived in the conjugal state as he should live, will be placed among the Gods who dwell in heaven.''');
        k[50] = Kural.factory(51, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''மனைக்தக்க மாண்புடையள் ஆகித்தற் கொண்டான்
  வளத்தக்காள் வாழ்க்கைத் துணை.''', '''As doth the house beseem, she shows her wifely dignity;
As doth her husband\'s wealth befit, she spends: help - meet is she.''',
                              '''She who has the excellence of home virtues, and can expend within the means of her husband, is a help in the domestic state.''');
        k[51] = Kural.factory(52, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''மனைமாட்சி இல்லாள்கண் இல்லாயின் வாழ்க்கை
  எனைமாட்சித் தாயினும் இல்.''', '''If household excellence be wanting in the wife,
Howe\'er with splendour lived, all worthless is the life.''',
                              '''If the wife be devoid of domestic excellence, whatever (other) greatness be possessed, the conjugal state, is nothing.''');
        k[52] = Kural.factory(53, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''இல்லதென் இல்லவள் மாண்பானால் உள்ளதென்
  இல்லவள் மாணாக் கடை.''', '''There is no lack within the house, where wife in worth excels,
There is no luck within the house, where wife dishonoured dwells.''',
                              '''If his wife be eminent (in virtue), what does (that man) not possess ? If she be without excellence, what does (he) possess ?''');
        k[53] = Kural.factory(54, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''பெண்ணின் பெருந்தக்க யாவுள கற்பென்னும்
  திண்மைஉண் டாகப் பெறின்.''', '''If woman might of chastity retain,
What choicer treasure doth the world contain?''',
                              '''What is more excellent than a wife, if she possess the stability of chastity ?''');
        k[54] = Kural.factory(55, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''தெய்வம் தொழாஅள் கொழுநன் தொழுதெழுவாள்
  பெய்யெனப் பெய்யும் மழை.''', '''No God adoring, low she bends before her lord;
Then rising, serves: the rain falls instant at her word!''',
                              '''If she, who does not worship God, but who rising worships her husband, say, "let it rain," it will rain.''');
        k[55] = Kural.factory(56, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''தற்காத்துத் தற்கொண்டாற் பேணித் தகைசான்ற
  சொற்காத்துச் சோர்விலாள் பெண்.''', '''Who guards herself, for husband\'s comfort cares, her household\'s fame,
In perfect wise with sleepless soul preserves, -give her a woman\'s name.''',
                              '''She is a wife who unweariedly guards herself, takes care of her husband, and preserves an unsullied fame.''');
        k[56] = Kural.factory(57, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''சிறைகாக்கும் காப்பெவன் செய்யும் மகளிர்
  நிறைகாக்கும் காப்பே தலை.''', '''Of what avail is watch and ward?
Honour\'s woman\'s safest guard.''',
                              '''What avails the guard of a prison ? The chief guard of a woman is her chastity.''');
        k[57] = Kural.factory(58, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''பெற்றாற் பெறின்பெறுவர் பெண்டிர் பெருஞ்சிறப்புப்
  புத்தேளிர் வாழும் உலகு.''', '''If wife be wholly true to him who gained her as his bride,
Great glory gains she in the world where gods bliss abide.''',
                              '''If women shew reverence to their husbands, they will obtain great excellence in the world where the gods flourish.''');
        k[58] = Kural.factory(59, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''புகழ்புரிந்த இல்லிலோர்க்கு இல்லை இகழ்வார்முன்
  ஏறுபோல் பீடு நடை.''', '''Who have not spouses that in virtue\'s praise delight,
They lion-like can never walk in scorner\'s sight.''',
                              '''The man whose wife seeks not the praise (of chastity) cannot walk with lion-like stately step, before those who revile them.''');
        k[59] = Kural.factory(60, '''அறத்துப்பால்''', '''வாழ்க்கைத் துணைநலம்''', '''மங்கலம் என்ப மனைமாட்சி மற்றுஅதன்
  நன்கலம் நன்மக்கட் பேறு.''', '''The house\'s \'blessing\', men pronounce the house-wife excellent;
The gain of blessed children is its goodly ornament.''',
                              '''The excellence of a wife is the good of her husband; and good children are the jewels of that goodness.''');
        k[60] = Kural.factory(61, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''பெறுமவற்றுள் யாமறிவது இல்லை அறிவறிந்த
  மக்கட்பேறு அல்ல பிற.''', '''Of all that men acquire, we know not any greater gain,
Than that which by the birth of learned children men obtain.''',
                              '''Among all the benefits that may be acquired, we know no greater benefit than the acquisition of intelligent children.''');
        k[61] = Kural.factory(62, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''எழுபிறப்பும் தீயவை தீண்டா பழிபிறங்காப்
  பண்புடை மக்கட் பெறின்.''', '''Who children gain, that none reproach, of virtuous worth,
No evils touch them, through the sev\'n-fold maze of birth.''',
                              '''The evils of the seven births shall not touch those who abtain children of a good disposition, free from vice.''');
        k[62] = Kural.factory(63, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''தம்பொருள் என்பதம் மக்கள் அவர்பொருள்
  தம்தம் வினையான் வரும்.''', '''\'Man\'s children are his fortune,\' say the wise;
From each one\'s deeds his varied fortunes rise.''',
                              '''Men will call their sons their wealth, because it flows to them through the deeds which they (sons) perform on their behalf.''');
        k[63] = Kural.factory(64, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''அமிழ்தினும் ஆற்ற இனிதேதம் மக்கள்
  சிறுகை அளாவிய கூழ்.''', '''Than God\'s ambrosia sweeter far the food before men laid,
In which the little hands of children of their own have play\'d.''',
                              '''The rice in which the little hand of their children has dabbled will be far sweeter (to the parent) than ambrosia.''');
        k[64] = Kural.factory(65, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''மக்கள்மெய் தீண்டல் உடற்கின்பம் மற்றுஅவர்
  சொற்கேட்டல் இன்பம் செவிக்கு.''', '''To patent sweet the touch of children dear;
Their voice is sweetest music to his ear.''',
                              '''The touch of children gives pleasure to the body, and the hearing of their words, pleasure to the ear.''');
        k[65] = Kural.factory(66, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''குழல்இனிது யாழ்இனிது என்பதம் மக்கள்
  மழலைச்சொல் கேளா தவர்.''', '''\'The pipe is sweet,\' \'the lute is sweet,\' by them\'t will be averred,
Who music of their infants\' lisping lips have never heard.''',
                              '''"The pipe is sweet, the lute is sweet," say those who have not heard the prattle of their own children.''');
        k[66] = Kural.factory(67, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''தந்தை மகற்காற்று நன்றி அவையத்து
  முந்தி இருப்பச் செயல்.''', '''Sire greatest boon on son confers, who makes him meet,
In councils of the wise to fill the highest seat.''',
                              '''The benefit which a father should confer on his son is to give him precedence in the assembly of the learned.''');
        k[67] = Kural.factory(68, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''தம்மின்தம் மக்கள் அறிவுடைமை மாநிலத்து
  மன்னுயிர்க் கெல்லாம் இனிது.''', '''Their children\'s wisdom greater than their own confessed,
Through the wide world is sweet to every human breast.''',
                              '''That their children should possess knowledge is more pleasing to all men of this great earth than to themselves.''');
        k[68] = Kural.factory(69, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''ஈன்ற பொழுதின் பெரிதுவக்கும் தன்மகனைச்
  சான்றோன் எனக்கேட்ட தாய்.''', '''When mother hears him named \'fulfill\'d of wisdom\'s lore,\'
Far greater joy she feels, than when her son she bore.''',
                              '''The mother who hears her son called "a wise man" will rejoice more than she did at his birth.''');
        k[69] = Kural.factory(70, '''அறத்துப்பால்''', '''புதல்வரைப் பெறுதல்''', '''மகன்தந்தைக்கு ஆற்றும் உதவி இவன்தந்தை
  என்நோற்றான் கொல்எனும் சொல்.''', '''To sire, what best requital can by grateful child be done?
To make men say, \'What merit gained the father such a son?\'''',
                              '''(So to act) that it may be said "by what great penance did his father beget him," is the benefit which a son should render to his father.''');
        k[70] = Kural.factory(71, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்பிற்கும் உண்டோ அடைக்குந்தாழ் ஆர்வலர்
  புன்கணீர் பூசல் தரும்.''', '''And is there bar that can even love restrain?
The tiny tear shall make the lover\'s secret plain.''',
                              '''Is there any fastening that can shut in love ? Tears of the affectionate will publish the love that is within.''');
        k[71] = Kural.factory(72, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்பிலார் எல்லாம் தமக்குரியர் அன்புடையார்
  என்பும் உரியர் பிறர்க்கு.''', '''The loveless to themselves belong alone;
The loving men are others\' to the very bone.''',
                              '''Those who are destitute of love appropriate all they have to themselves; but those who possess love consider even their bones to belong to others.''');
        k[72] = Kural.factory(73, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்போடு இயைந்த வழக்கென்ப ஆருயிர்க்கு
  என்போடு இயைந்த தொடர்பு.''', '''Of precious soul with body\'s flesh and bone,
The union yields one fruit, the life of love alone.''',
                              '''They say that the union of soul and body in man is the fruit of the union of love and virtue (in a former birth).''');
        k[73] = Kural.factory(74, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்புஈனும் ஆர்வம் உடைமை அதுஈனும்
  நண்பு என்னும் நாடாச் சிறப்பு.''', '''From love fond yearning springs for union sweet of minds;
And that the bond of rare excelling friendship binds.''',
                              '''Love begets desire: and that (desire) begets the immeasureable excellence of friendship.''');
        k[74] = Kural.factory(75, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்புற்று அமர்ந்த வழக்கென்ப வையகத்து
  இன்புற்றார் எய்தும் சிறப்பு.''', '''Sweetness on earth and rarest bliss above,
These are the fruits of tranquil life of love.''',
                              '''They say that the felicity which those who, after enjoying the pleasure (of the conjugal state) in this world, obtain in heaven is the result of their domestic state imbued with love.''');
        k[75] = Kural.factory(76, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அறத்திற்கே அன்புசார் பென்ப அறியார்
  மறத்திற்கும் அஃதே துணை.''', '''The unwise deem love virtue only can sustain,
It also helps the man who evil would restrain.''',
                              '''The ignorant say that love is an ally to virtue only, but it is also a help to get out of vice.''');
        k[76] = Kural.factory(77, '''அறத்துப்பால்''', '''அன்புடைமை''', '''என்பி லதனை வெயில்போலக் காயுமே
  அன்பி லதனை அறம்.''', '''As sun\'s fierce ray dries up the boneless things,
So loveless beings virtue\'s power to nothing brings.''',
                              '''Virtue will burn up the soul which is without love, even as the sun burns up the creature which is without bone, i.e. worms.''');
        k[77] = Kural.factory(78, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்பகத் தில்லா உயிர்வாழ்க்கை வன்பாற்கண்
  வற்றல் மரந்தளிர்த் தற்று.''', '''The loveless soul, the very joys of life may know,
When flowers, in barren soil, on sapless trees, shall blow.''',
                              '''The domestic state of that man whose mind is without love is like the flourishing of a withered tree upon the parched desert.''');
        k[78] = Kural.factory(79, '''அறத்துப்பால்''', '''அன்புடைமை''', '''புறத்துறுப் பெல்லாம் எவன்செய்யும் யாக்கை
  அகத்துறுப்பு அன்பி லவர்க்கு.''', '''Though every outward part complete, the body\'s fitly framed;
What good, when soul within, of love devoid, lies halt and maimed?''',
                              '''Of what avail are all the external members (of the body) to those who are destitute of love, the internal member.''');
        k[79] = Kural.factory(80, '''அறத்துப்பால்''', '''அன்புடைமை''', '''அன்பின் வழியது உயிர்நிலை அஃதிலார்க்கு
  என்புதோல் போர்த்த உடம்பு.''', '''Bodies of loveless men are bony framework clad with skin;
Then is the body seat of life, when love resides within.''',
                              '''That body alone which is inspired with love contains a living soul: if void of it, (the body) is bone overlaid with skin.''');
        k[80] = Kural.factory(81, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''இருந்தோம்பி இல்வாழ்வ தெல்லாம் விருந்தோம்பி
  வேளாண்மை செய்தற் பொருட்டு.''', '''All household cares and course of daily life have this in view.
Guests to receive with courtesy, and kindly acts to do.''',
                              '''The whole design of living in the domestic state and laying up (property) is (to be able) to exercise the benevolence of hospitality.''');
        k[81] = Kural.factory(82, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''விருந்து புறத்ததாத் தானுண்டல் சாவா
  மருந்தெனினும் வேண்டற்பாற் றன்று.''', '''Though food of immortality should crown the board,
Feasting alone, the guests without unfed, is thing abhorred.''',
                              '''It is not fit that one should wish his guests to be outside (his house) even though he were eating the food of immortality.''');
        k[82] = Kural.factory(83, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''வருவிருந்து வைகலும் ஓம்புவான் வாழ்க்கை
  பருவந்து பாழ்படுதல் இன்று.''', '''Each day he tends the coming guest with kindly care;
Painless, unfailing plenty shall his household share.''',
                              '''The domestic life of the man that daily entertains the guests who come to him shall not be laid waste by poverty.''');
        k[83] = Kural.factory(84, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''அகனமர்ந்து செய்யாள் உறையும் முகனமர்ந்து
  நல்விருந்து ஓம்புவான் இல்.''', '''With smiling face he entertains each virtuous guest,
\'Fortune\' with gladsome mind shall in his dwelling rest.''',
                              '''Lakshmi with joyous mind shall dwell in the house of that man who, with cheerful countenance, entertains the good as guests.''');
        k[84] = Kural.factory(85, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''வித்தும் இடல்வேண்டும் கொல்லோ விருந்தோம்பி
  மிச்சில் மிசைவான் புலம்.''', '''Who first regales his guest, and then himself supplies,
O\'er all his fields, unsown, shall plenteous harvests rise.''',
                              '''Is it necessary to sow the field of the man who, having feasted his guests, eats what may remain ?''');
        k[85] = Kural.factory(86, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''செல்விருந்து ஓம்பி வருவிருந்து பார்த்திருப்பான்
  நல்வருந்து வானத் தவர்க்கு.''', '''The guest arrived he tends, the coming guest expects to see;
To those in heavenly homes that dwell a welcome guest is he.''',
                              '''He who, having entertained the guests that have come, looks out for others who may yet come, will be a welcome guest to the inhabitants of heaven.''');
        k[86] = Kural.factory(87, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''இனைத்துணைத் தென்பதொன் றில்லை விருந்தின்
  துணைத்துணை வேள்விப் பயன்.''', '''To reckon up the fruit of kindly deeds were all in vain;
Their worth is as the worth of guests you entertain.''',
                              '''The advantages of benevolence cannot be measured; the measure (of the virtue) of the guests (entertained) is the only measure.''');
        k[87] = Kural.factory(88, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''பரிந்தோம்பிப் பற்றற்றேம் என்பர் விருந்தோம்பி
  வேள்வி தலைப்படா தார்.''', '''With pain they guard their stores, yet \'All forlorn are we,\' they\'ll cry,
Who cherish not their guests, nor kindly help supply.''',
                              '''Those who have taken no part in the benevolence of hospitality shall (at length lament) saying, "we have laboured and laid up wealth and are now without support."''');
        k[88] = Kural.factory(89, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''உடைமையுள் இன்மை விருந்தோம்பல் ஓம்பா
  மடமை மடவார்கண் உண்டு.''', '''To turn from guests is penury, though worldly goods abound;
\'Tis senseless folly, only with the senseless found.''',
                              '''That stupidity which excercises no hospitality is poverty in the midst of wealth. It is the property of the stupid.''');
        k[89] = Kural.factory(90, '''அறத்துப்பால்''', '''விருந்தோம்பல்''', '''மோப்பக் குழையும் அனிச்சம் முகந்திரிந்து
  நோக்கக் குநழ்யும் விருந்து.''', '''The flower of \'Anicha\' withers away, If you do but its fragrance inhale;
If the face of the host cold welcome convey, The guest\'s heart within him will fail.''',
                              '''As the Anicham flower fades in smelling, so fades the guest when the face is turned away.''');
        k[90] = Kural.factory(91, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''இன்சொலால் ஈரம் அளைஇப் படிறுஇலவாம்
  செம்பொருள் கண்டார்வாய்ச் சொல்.''', '''Pleasant words are words with all pervading love that burn;
Words from his guileless mouth who can the very truth discern.''',
                              '''Sweet words are those which imbued with love and free from deceit flow from the mouth of the virtuous.''');
        k[91] = Kural.factory(92, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''அகன்அமர்ந்து ஈதலின் நன்றே முகனமர்ந்து
  இன்சொலன் ஆகப் பெறின்.''', '''A pleasant word with beaming smile,s preferred,
Even to gifts with liberal heart conferred.''',
                              '''Sweet speech, with a cheerful countenance is better than a gift made with a joyous mind.''');
        k[92] = Kural.factory(93, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''முகத்தான் அமர்ந்து இனிதுநோக்கி அகத்தானாம்
  இன்சொ லினதே அறம்.''', '''With brightly beaming smile, and kindly light of loving eye,
And heart sincere, to utter pleasant words is charity.''',
                              '''Sweet speech, flowing from the heart (uttered) with a cheerful countenance and a sweet look, is true virtue.''');
        k[93] = Kural.factory(94, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''துன்புறூஉம் துவ்வாமை இல்லாகும் யார்மாட்டும்
  இன்புறூஉம் இன்சொ லவர்க்கு.''', '''The men of pleasant speech that gladness breathe around,
Through indigence shall never sorrow\'s prey be found.''',
                              '''Sorrow-increasing poverty shall not come upon those who use towards all, pleasure-increasing sweetness of speech.''');
        k[94] = Kural.factory(95, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''பணிவுடையன் இன்சொலன் ஆதல் ஒருவற்கு
  அணியல்ல மற்றுப் பிற.''', '''Humility with pleasant speech to man on earth,
Is choice adornment; all besides is nothing worth.''',
                              '''Humility and sweetness of speech are the ornaments of man; all others are not (ornaments).''');
        k[95] = Kural.factory(96, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''அல்லவை தேய அறம்பெருகும் நல்லவை
  நாடி இனிய சொலின்''', '''Who seeks out good, words from his lips of sweetness flow;
In him the power of vice declines, and virtues grow.''',
                              '''If a man, while seeking to speak usefully, speaks also sweetly, his sins will diminish and his virtue increase.''');
        k[96] = Kural.factory(97, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''நயன்ஈன்று நன்றி பயக்கும் பயன்ஈன்று
  பண்பின் தலைப்பிரியாச் சொல்.''', '''The words of sterling sense, to rule of right that strict adhere,
To virtuous action prompting, blessings yield in every sphere.''',
                              '''That speech which, while imparting benefits ceases not to please, will yield righteousness (for this world) and merit (for the next world).''');
        k[97] = Kural.factory(98, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''சிறுமையுவு நீங்கிய இன்சொல் மறுமையும்
  இம்மையும் இன்பம் தரும்.''', '''Sweet kindly words, from meanness free, delight of heart,
In world to come and in this world impart.''',
                              '''Sweet speech, free from harm to others, will give pleasure both in this world and in the next.''');
        k[98] = Kural.factory(99, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''இன்சொல் இனிதீன்றல் காண்பான் எவன்கொலோ
  வன்சொல் வழங்கு வது.''', '''Who sees the pleasure kindly speech affords,
Why makes he use of harsh, repellant words?''',
                              '''Why does he use harsh words, who sees the pleasure which sweet speech yields ?''');
        k[99] = Kural.factory(100, '''அறத்துப்பால்''', '''இனியவைகூறல்''', '''இனிய உளவாக இன்னாத கூறல்
  கனிஇருப்பக் காய்கவர்ந் தற்று.''', '''When pleasant words are easy, bitter words to use,
Is, leaving sweet ripe fruit, the sour unripe to choose.''',
                              '''To say disagreeable things when agreeable are at hand is like eating unripe fruit when there is ripe.''');
        k[100] = Kural.factory(101, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''செய்யாமல் செய்த உதவிக்கு வையகமும்
  வானகமும் ஆற்றல் அரிது.''', '''Assistance given by those who ne\'er received our aid,
Is debt by gift of heaven and earth but poorly paid.''',
                               '''(The gift of) heaven and earth is not an equivalent for a benefit which is conferred where none had been received.''');
        k[101] = Kural.factory(102, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''காலத்தி னாற்செய்த நன்றி சிறிதெனினும்
  ஞாலத்தின் மாணப் பெரிது.''', '''A timely benefit, -though thing of little worth,
The gift itself, -in excellence transcends the earth.''',
                               '''A favour conferred in the time of need, though it be small (in itself), is (in value) much larger than the world.''');
        k[102] = Kural.factory(103, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''பயன்தூக்கார் செய்த உதவி நயன்தூக்கின்
  நன்மை கடலின் பெரிது.''', '''Kindness shown by those who weigh not what the return may be:
When you ponder right its merit, \'Tis vaster than the sea.''',
                               '''If we weigh the excellence of a benefit which is conferred without weighing the return, it is larger than the sea.''');
        k[103] = Kural.factory(104, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''தினைத்துணை நன்றி செயினும் பனைத்துணையாக்
  கொள்வர் பயன்தெரி வார்.''', '''Each benefit to those of actions\' fruit who rightly deem,
Though small as millet-seed, as palm-tree vast will seem.''',
                               '''Though the benefit conferred be as small as a millet seed, those who know its advantage will consider it as large as a palmyra fruit.''');
        k[104] = Kural.factory(105, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''உதவி வரைத்தன்று உதவி உதவி
  செயப்பட்டார் சால்பின் வரைத்து.''', '''The kindly aid\'s extent is of its worth no measure true;
Its worth is as the worth of him to whom the act you do.''',
                               '''The benefit itself is not the measure of the benefit; the worth of those who have received it is its measure.''');
        k[105] = Kural.factory(106, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''மறவற்க மாசற்றார் கேண்மை துறவற்க
  துன்பத்துள் துப்பாயார் நட்பு.''', '''Kindness of men of stainless soul remember evermore!
Forsake thou never friends who were thy stay in sorrow sore!''',
                               '''Forsake not the friendship of those who have been your staff in adversity. Forget not be benevolence of the blameless.''');
        k[106] = Kural.factory(107, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''எழுமை எழுபிறப்பும் உள்ளுவர் தங்கண்
  விழுமந் துடைத்தவர் நட்பு.''', '''Through all seven worlds, in seven-fold birth, Remains in mem\'ry of the wise.
Friendship of those who wiped on earth, The tears of sorrow from their eyes.''',
                               '''(The wise) will remember throughout their seven-fold births the love of those who have wiped away their affliction.''');
        k[107] = Kural.factory(108, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''நன்றி மறப்பது நன்றன்று நன்றல்லது
  அன்றே மறப்பது நன்று.''', '''\'Tis never good to let the thought of good things done thee pass away;
Of things not good, \'tis good to rid thy memory that very day.''',
                               '''It is not good to forget a benefit; it is good to forget an injury even in the very moment (in which it is inflicted).''');
        k[108] = Kural.factory(109, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''கொன்றன்ன இன்னா செயினும் அவர்செய்த
  ஒன்றுநன்று உள்ளக் கெடும்.''', '''Effaced straightway is deadliest injury,
By thought of one kind act in days gone by.''',
                               '''Though one inflict an injury great as murder, it will perish before the thought of one benefit (formerly) conferred.''');
        k[109] = Kural.factory(110, '''அறத்துப்பால்''', '''செய்ந்நன்றி அறிதல்''', '''எந்நன்றி கொன்றார்க்கும் உய்வுண்டாம் உய்வில்லை
  செய்ந்நன்றி கொன்ற மகற்கு.''', '''Who every good have killed, may yet destruction flee;
Who \'benefit\' has killed, that man shall ne\'er \'scape free!''',
                               '''He who has killed every virtue may yet escape; there is no escape for him who has killed a benefit.''');
        k[110] = Kural.factory(111, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''தகுதி எனவொன்று நன்றே பகுதியால்
  பாற்பட்டு ஒழுகப் பெறின்.''', '''If justice, failing not, its quality maintain,
Giving to each his due, -\'tis man\'s one highest gain.''',
                               '''That equity which consists in acting with equal regard to each of (the three) divisions of men [enemies, strangers and friends] is a pre-eminent virtue.''');
        k[111] = Kural.factory(112, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''செப்பம் உடையவன் ஆக்கஞ் சிதைவின்றி
  எச்சத்திற் கேமாப்பு உடைத்து.''', '''The just man\'s wealth unwasting shall endure,
And to his race a lasting joy ensure.''',
                               '''The wealth of the man of rectitude will not perish, but will bring happiness also to his posterity.''');
        k[112] = Kural.factory(113, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''நன்றே தரினும் நடுவிகந்தாம் ஆக்கத்தை
  அன்றே யொழிய விடல்.''', '''Though only good it seem to give, yet gain
By wrong acquired, not e\'en one day retain!''',
                               '''Forsake in the very moment (of acquisition) that gain which, though it should bring advantage, is without equity.''');
        k[113] = Kural.factory(114, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''தக்கார் தகவிலர் என்பது அவரவர்
  எச்சத்தாற் காணப்ப படும்.''', '''Who just or unjust lived shall soon appear:
By each one\'s offspring shall the truth be clear.''',
                               '''The worthy and unworthy may be known by the existence or otherwise of good offsprings.''');
        k[114] = Kural.factory(115, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''கேடும் பெருக்கமும் இல்லல்ல நெஞ்சத்துக்
  கோடாமை சான்றோர்க் கணி.''', '''The gain and loss in life are not mere accident;
Just mind inflexible is sages\' ornament.''',
                               '''Loss and gain come not without cause; it is the ornament of the wise to preserve evenness of mind (under both).''');
        k[115] = Kural.factory(116, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''கெடுவல்யான் என்பது அறிகதன் நெஞ்சம்
  நடுவொரீஇ அல்ல செயின்.''', '''If, right deserting, heart to evil turn,
Let man impending ruin\'s sign discern!''',
                               '''Let him whose mind departing from equity commits sin well consider thus within himself, "I shall perish."''');
        k[116] = Kural.factory(117, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''கெடுவாக வையாது உலகம் நடுவாக
  நன்றிக்கண் தங்கியான் தாழ்வு.''', '''The man who justly lives, tenacious of the right,
In low estate is never low to wise man\'s sight.''',
                               '''The great will not regard as poverty the low estate of that man who dwells in the virtue of equity.''');
        k[117] = Kural.factory(118, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''சமன்செய்து சீர்தூக்குங் கோல்போல் அமைந்தொருபால்
  கோடாமை சான்றோர்க் கணி.''', '''To stand, like balance-rod that level hangs and rightly weighs,
With calm unbiassed equity of soul, is sages\' praise.''',
                               '''To incline to neither side, but to rest impartial as the even-fixed scale is the ornament of the wise.''');
        k[118] = Kural.factory(119, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''சொற்கோட்டம் இல்லது செப்பம் ஒருதலையா
  உட்கோட்டம் இன்மை பெறின்.''', '''Inflexibility in word is righteousness,
If men inflexibility of soul possess.''',
                               '''Freedom from obliquity of speech is rectitude, if there be (corresponding) freedom from bias of mind.''');
        k[119] = Kural.factory(120, '''அறத்துப்பால்''', '''நடுவு நிலைமை''', '''வாணிகம் செய்வார்க்கு வாணிகம் பேணிப்
  பிறவும் தமபோல் செயின்.''', '''As thriving trader is the trader known,
Who guards another\'s interests as his own.''',
                               '''The true merchandize of merchants is to guard and do by the things of others as they do by their own.''');
        k[120] = Kural.factory(121, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''அடக்கம் அமரருள் உய்க்கும் அடங்காமை
  ஆரிருள் உய்த்து விடும்.''', '''Control of self does man conduct to bliss th\' immortals share;
Indulgence leads to deepest night, and leaves him there.''',
                               '''Self-control will place (a man) among the Gods; the want of it will drive (him) into the thickest darkness (of hell).''');
        k[121] = Kural.factory(122, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''காக்க பொருளா அடக்கத்தை ஆக்கம்
  அதனினூஉங் கில்லை உயிர்க்கு.''', '''Guard thou as wealth the power of self-control;
Than this no greater gain to living soul!''',
                               '''Let self-control be guarded as a treasure; there is no greater source of good for man than that.''');
        k[122] = Kural.factory(123, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''செறிவறிந்து சீர்மை பயக்கும் அறிவறிந்து
  ஆற்றின் அடங்கப் பெறின்.''', '''If versed in wisdom\'s lore by virtue\'s law you self restrain.
Your self-repression known will yield you glory\'s gain.''',
                               '''Knowing that self-control is knowledge, if a man should control himself, in the prescribed course, such self-control will bring him distinction among the wise.''');
        k[123] = Kural.factory(124, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''நிலையின் திரியாது அடங்கியான் தோற்றம்
  மலையினும் மாணப் பெரிது.''', '''In his station, all unswerving, if man self subdue,
Greater he than mountain proudly rising to the view.''',
                               '''More lofty than a mountain will be the greatness of that man who without swerving from his domestic state, controls himself.''');
        k[124] = Kural.factory(125, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''எல்லார்க்கும் நன்றாம் பணிதல் அவருள்ளும்
  செல்வர்க்கே செல்வம் தகைத்து.''', '''To all humility is goodly grace; but chief to them
With fortune blessed, -\'tis fortune\'s diadem.''',
                               '''Humility is good in all; but especially in the rich it is (the excellence of) higher riches.''');
        k[125] = Kural.factory(126, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''ஒருநம்யுள் ஆமைபோல் ஐந்தடக்கல் ஆற்றின்
  எழுநம்யும் ஏமாப் புடைத்து.''', '''Like tortoise, who the five restrains
In one, through seven world bliss obtains.''',
                               '''Should one throughout a single birth, like a tortoise keep in his five senses, the fruit of it will prove a safe-guard to him throughout the seven-fold births.''');
        k[126] = Kural.factory(127, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''யாகாவா ராயினும் நாகாக்க காவாக்கால்
  சோகாப்பர் சொல்லிழுக்குப் பட்டு.''', '''Whate\'er they fail to guard, o\'er lips men guard should keep;
If not, through fault of tongue, they bitter tears shall weep.''',
                               '''Whatever besides you leave unguarded, guard your tongue; otherwise errors of speech and the consequent misery will ensue.''');
        k[127] = Kural.factory(128, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''ஒன்றானுந் தீச்சொல் பொருட்பயன் உண்டாயின்
  நன்றாகா தாகி விடும்.''', '''Though some small gain of good it seem to bring,
The evil word is parent still of evil thing.''',
                               '''If a man\'s speech be productive of a single evil, all the good by him will be turned into evil.''');
        k[128] = Kural.factory(129, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''தீயினாற் சுட்டபுண் உள்ளாறும் ஆறாதே
  நாவினாற் சுட்ட வடு.''', '''In flesh by fire inflamed, nature may thoroughly heal the sore;
In soul by tongue inflamed, the ulcer healeth never more.''',
                               '''The wound which has been burnt in by fire may heal, but a wound burnt in by the tongue will never heal.''');
        k[129] = Kural.factory(130, '''அறத்துப்பால்''', '''அடக்கமுடைமை''', '''கதங்காத்துக் கற்றடங்கல் ஆற்றுவான் செவ்வி
  அறம்பார்க்கும் ஆற்றின் நுழைந்து.''', '''Who learns restraint, and guards his soul from wrath,
Virtue, a timely aid, attends his path.''',
                               '''Virtue, seeking for an opportunity, will come into the path of that man who, possessed of learning and self-control, guards himself against anger.''');
        k[130] = Kural.factory(131, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''ஒழுக்கம் விழுப்பந் தரலான் ஒழுக்கம்
  உயிரினும் ஓம்பப் படும்.''', '''\'Decorum\' gives especial excellence; with greater care
\'Decorum\' should men guard than life, which all men share.''',
                               '''Propriety of conduct leads to eminence, it should therefore be preserved more carefully than life.''');
        k[131] = Kural.factory(132, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''பரிந்தோம்பிக் காக்க ஒழுக்கம் தெரிந்தோம்பித்
  தேரினும் அஃதே துணை.''', '''Searching, duly watching, learning, \'decorum\' still we find;
Man\'s only aid; toiling, guard thou this with watchful mind.''',
                               '''Let propriety of conduct be laboriously preserved and guarded; though one know and practise and excel in many virtues, that will be an eminent aid.''');
        k[132] = Kural.factory(133, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''ஒழுக்கம் உடைமை குடிமை இழுக்கம்
  இழிந்த பிறப்பாய் விடும்.''', '''\'Decorum\'s\' true nobility on earth;
\'Indecorum\'s\' issue is ignoble birth.''',
                               '''Propriety of conduct is true greatness of birth, and impropriety will sink into a mean birth.''');
        k[133] = Kural.factory(134, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''மறப்பினும் ஓத்துக் கொளலாகும் பார்ப்பான்
  பிறப்பொழுக்கங் குன்றக் கெடும்.''', '''Though he forget, the Brahman may regain his Vedic lore;
Failing in \'decorum due,\' birthright\'s gone for evermore.''',
                               '''A Brahman though he should forget the Vedas may recover it by reading; but, if he fail in propriety of conduct even his high birth will be destroyed.''');
        k[134] = Kural.factory(135, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''அழுக்கா றுடையான்கண் ஆக்கம்போன்று இல்லை
  ஒழுக்க மிலான்கண் உயர்வு.''', '''The envious soul in life no rich increase of blessing gains,
So man of \'due decorum\' void no dignity obtains.''',
                               '''Just as the envious man will be without wealth, so will the man of destitute of propriety of conduct be without greatness.''');
        k[135] = Kural.factory(136, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''ஒழுக்கத்தின் ஒல்கார் உரவோர் இழுக்கத்தின்
  ஏதம் படுபாக் கறிந்து.''', '''The strong of soul no jot abate of \'strict decorum\'s\' laws,
Knowing that \'due decorum\'s\' breach foulest disgrace will cause.''',
                               '''Those firm in mind will not slacken in their observance of the proprieties of life, knowing, as they do, the misery that flows from the transgression from them.''');
        k[136] = Kural.factory(137, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''ஒழுக்கத்தின் எய்துவர் மேன்மை இழுக்கத்தின்
  எய்துவர் எய்தாப் பழி.''', '''\'Tis source of dignity when \'true decorum\' is preserved;
Who break \'decorum\'s\' rules endure e\'en censures undeserved.''',
                               '''From propriety of conduct men obtain greatness; from impropriety comes insufferable disgrace.''');
        k[137] = Kural.factory(138, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''நன்றிக்கு வித்தாகும் நல்லொழுக்கம் தீயொழுக்கம்
  என்றும் இடும்பை தரும்.''', '''\'Decorum true\' observed a seed of good will be;
\'Decorum\'s breach\' will sorrow yield eternally.''',
                               '''Propriety of conduct is the seed of virtue; impropriety will ever cause sorrow.''');
        k[138] = Kural.factory(139, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''ஒழுக்க முடையவர்க்கு ஒல்லாவே தீய
  வழுக்கியும் வாயாற் சொலல்.''', '''It cannot be that they who \'strict decorum\'s\' law fulfil,
E\'en in forgetful mood, should utter words of ill.''',
                               '''Those who study propriety of conduct will not speak evil, even forgetfully.''');
        k[139] = Kural.factory(140, '''அறத்துப்பால்''', '''ஒழுக்கமுடைமை''', '''உலகத்தோடு ஒட்ட ஒழுகல் பலகற்றும்
  கல்லார் அறிவிலா தார்''', '''Who know not with the world in harmony to dwell,
May many things have learned, but nothing well.''',
                               '''Those who know not how to act agreeably to the world, though they have learnt many things, are still ignorant.''');
        k[140] = Kural.factory(141, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''பிறன்பொருளாள் பெட்டொழுகும் பேதைமை ஞாலத்து
  அறம்பொருள் கண்டார்கண் இல்.''', '''Who laws of virtue and possession\'s rights have known,
Indulge no foolish love of her by right another\'s own.''',
                               '''The folly of desiring her who is the property of another will not be found in those who know (the attributes of) virtue and (the rights of) property.''');
        k[141] = Kural.factory(142, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''அறன்கடை நின்றாருள் எல்லாம் பிறன்கடை
  நின்றாரின் பேதையார் இல்.''', '''No fools, of all that stand from virtue\'s pale shut out,
Like those who longing lurk their neighbour\'s gate without.''',
                               '''Among all those who stand on the outside of virtue, there are no greater fools than those who stand outside their neighbour\'s door.''');
        k[142] = Kural.factory(143, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''விளிந்தாரின் வேறல்லர் மன்ற தெளிந்தாரில்
  தீமை புரிந்துதொழுகு வார்.''', '''They\'re numbered with the dead, e\'en while they live, -how otherwise?
With wife of sure confiding friend who evil things devise.''',
                               '''Certainly they are no better than dead men who desire evil towards the wife of those who undoubtingly confide in them.''');
        k[143] = Kural.factory(144, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''எனைத்துணையர் ஆயினும் என்னாம் தினைத்துணையும்
  தேரான் பிறனில் புகல்.''', '''How great soe\'er they be, what gain have they of life,
Who, not a whit reflecting, seek a neighbour\'s wife.''',
                               '''However great one may be, what does it avail if, without at all considering his guilt, he goes unto the wife of another ?''');
        k[144] = Kural.factory(145, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''எளிதென இல்லிறப்பான் எய்துமெஞ் ஞான்றும்
  விளியாது நிற்கும் பழி.''', '''\'Mere triflel\' saying thus, invades the home, so he ensures.
A gain of guilt that deathless aye endures.''',
                               '''He who thinks lightly of going into the wife of another acquires guilt that will abide with him imperishably and for ever.''');
        k[145] = Kural.factory(146, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''பகைபாவம் அச்சம் பழியென நான்கும்
  இகவாவாம் இல்லிறப்பான் கண்.''', '''Who home ivades, from him pass nevermore,
Hatred and sin, fear, foul disgrace; these four.''',
                               '''Hatred, sin, fear, disgrace; these four will never leave him who goes in to his neighbour\'s wife.''');
        k[146] = Kural.factory(147, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''அறனியலான் இல்வாழ்வான் என்பான் பிறனியலாள்
  பெண்மை நயவா தவன்.''', '''Who sees the wife, another\'s own, with no desiring eye
In sure domestic bliss he dwelleth ever virtuously.''',
                               '''He who desires not the womanhood of her who should walk according to the will of another will be praised as a virtuous house-holder.''');
        k[147] = Kural.factory(148, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''பிறன்மனை நோக்காத பேராண்மை சான்றோர்க்கு
  அறனொன்றோ ஆன்ற வொழுக்கு.''', '''Manly excellence, that looks not on another\'s wife,
Is not virtue merely, \'tis full \'propriety\' of life.''',
                               '''That noble manliness which looks not at the wife of another is the virtue and dignity of the great.''');
        k[148] = Kural.factory(149, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''நலக்குரியார் யாரெனின் நாமநீர் வைப்பின்
  பிறர்க்குரியாள் தோள்தோயா தார்.''', '''Who \'re good indeed, on earth begirt by ocean\'s gruesome tide?
The men who touch not her that is another\'s bride.''',
                               '''Is it asked, "who are those who shall obtain good in this world surrounded by the terror-producing sea ?" Those who touch not the shoulder of her who belongs to another.''');
        k[149] = Kural.factory(150, '''அறத்துப்பால்''', '''பிறனில் விழையாமை''', '''அறன்வரையான் அல்ல செயினும் பிறன்வரையாள்
  பெண்மை நயவாமை நன்று.''', '''Though virtue\'s bounds he pass, and evil deeds hath wrought;
At least, \'tis good if neighbour\'s wife he covet not.''',
                               '''Though a man perform no virtuous deeds and commit (every) vice, it will be well if he desire not the womanhood of her who is within the limit (of the house) of another.''');
        k[150] = Kural.factory(151, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''அகழ்வாரைத் தாங்கும் நிலம்போலத் தம்மை
  இகழ்வார்ப் பொறுத்தல் தலை.''', '''As earth bears up the men who delve into her breast,
To bear with scornful men of virtues is the best.''',
                               '''To bear with those who revile us, just as the earth bears up those who dig it, is the first of virtues.''');
        k[151] = Kural.factory(152, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''பொறுத்தல் இறப்பினை என்றும் அதனை
  மறத்தல் அதனினும் நன்று.''', '''Forgiving trespasses is good always;
Forgetting them hath even higher praise;''',
                               '''Bear with reproach even when you can retaliate; but to forget it will be still better than that.''');
        k[152] = Kural.factory(153, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''இன்நம்யுள் இன்மை விருந்தொரால் வன்மையுள்
  வன்மை மடவார்ப் பொறை.''', '''The sorest poverty is bidding guest unfed depart;
The mightiest might to bear with men of foolish heart.''',
                               '''To neglect hospitality is poverty of poverty. To bear with the ignorant is might of might.''');
        k[153] = Kural.factory(154, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''நிறையுடைமை நீங்காமை வேண்டின் பொற்யுடைமை
  போற்றி யொழுகப் படும்.''', '''Seek\'st thou honour never tarnished to retain;
So must thou patience, guarding evermore, maintain.''',
                               '''If you desire that greatness should never leave, you preserve in your conduct the exercise of patience.''');
        k[154] = Kural.factory(155, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''ஒறுத்தாரை ஒன்றாக வையாரே வைப்பர்
  பொறுத்தாரைப் பொன்போற் பொதிந்து.''', '''Who wreak their wrath as worthless are despised;
Who patiently forbear as gold are prized.''',
                               '''(The wise) will not at all esteem the resentful. They will esteem the patient just as the gold which they lay up with care.''');
        k[155] = Kural.factory(156, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''ஒறுத்தார்க்கு ஒருநாளை இன்பம் பொறுத்தார்க்குப்
  பொன்றுந் துணையும் புகழ்.''', '''Who wreak their wrath have pleasure for a day;
Who bear have praise till earth shall pass away.''',
                               '''The pleasure of the resentful continues for a day. The praise of the patient will continue until (the final destruction of) the world.''');
        k[156] = Kural.factory(157, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''திறனல்ல தற்பிறர் செய்யினும் நோநொந்து
  அறனல்ல செய்யாமை நன்று.''', '''Though others work thee ill, thus shalt thou blessing reap;
Grieve for their sin, thyself from vicious action keep!''',
                               '''Though others inflict injuries on you, yet compassionating the evil (that will come upon them) it will be well not to do them anything contrary to virtue.''');
        k[157] = Kural.factory(158, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''மிகுதியான் மிக்கவை செய்தாரைத் தாந்தம்
  தகுதியான் வென்று விடல்.''', '''With overweening pride when men with injuries assail,
By thine own righteous dealing shalt thou mightily prevail.''',
                               '''Let a man by patience overcome those who through pride commit excesses.''');
        k[158] = Kural.factory(159, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''துறந்தாரின் தூய்மை உடையர் இறந்தார்வாய்
  இன்னாச்சொல் நோற்கிற் பவர்.''', '''They who transgressors\' evil words endure
With patience, are as stern ascetics pure.''',
                               '''Those who bear with the uncourteous speech of the insolent are as pure as the ascetics.''');
        k[159] = Kural.factory(160, '''அறத்துப்பால்''', '''பொறையுடைமை''', '''உண்ணாது நோற்பார் பெரியர் பிறர்சொல்லும்
  இன்னாச்சொல் நோற்பாரின் பின்.''', '''Though \'great\' we deem the men that fast and suffer pain,
Who others\' bitter words endure, the foremost place obtain.''',
                               '''Those who endure abstinence from food are great, next to those who endure the uncourteous speech of others.''');
        k[160] = Kural.factory(161, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''ஒழுக்காறாக் கொள்க ஒருவன்தன் நெஞ்சத்து
  அழுக்காறு இலாத இயல்பு.''', '''As \'strict decorum\'s\' laws, that all men bind,
Let each regard unenvying grace of mind.''',
                               '''Let a man esteem that disposition which is free from envy in the same manner as propriety of conduct.''');
        k[161] = Kural.factory(162, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''விழுப்பேற்றின் அஃதொப்பது இல்லையார் மாட்டும்
  அழுக்காற்றின் அன்மை பெறின்.''', '''If man can learn to envy none on earth,
\'Tis richest gift, -beyond compare its worth.''',
                               '''Amongst all attainable excellences there is none equal to that of being free from envy towords others.''');
        k[162] = Kural.factory(163, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அறன்ஆக்கம் வேண்டாதான் என்பான் பிறனாக்கம்
  பேணாது அழுக்கறுப் பான்.''', '''Nor wealth nor virtue does that man desire \'tis plain,
Whom others\' wealth delights not, feeling envious pain.''',
                               '''Of him who instead of rejoicing in the wealth of others, envies it, it will be said "he neither desires virtue not wealth."''');
        k[163] = Kural.factory(164, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அழுக்காற்றின் அல்லவை செய்யார் இழுக்காற்றின்
  ஏதம் படுபாக்கு அறிந்து.''', '''The wise through envy break not virtue\'s laws,
Knowing ill-deeds of foul disgrace the cause.''',
                               '''(The wise) knowing the misery that comes from transgression will not through envy commit unrighteous deeds.''');
        k[164] = Kural.factory(165, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அழுக்காறு உடையார்க்கு அதுசாலும் ஒன்னார்
  வழுக்காயும் கேடீன் பது.''', '''Envy they have within! Enough to seat their fate!
Though foemen fail, envy can ruin consummate.''',
                               '''To those who cherish envy that is enough. Though free from enemies that (envy) will bring destruction.''');
        k[165] = Kural.factory(166, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''கொடுப்பது அழுக்கறுப்பான் சுற்றம் உடுப்பதூஉம்
  உண்பதூஉம் இன்றிக் கெடும்.''', '''Who scans good gifts to others given with envious eye,
His kin, with none to clothe or feed them, surely die.''',
                               '''He who is envious at a gift (made to another) will with his relations utterly perish destitute of food and rainment.''');
        k[166] = Kural.factory(167, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அவ்வித்து அழுக்காறு உடையானைச் செய்யவள்
  தவ்வையைக் காட்டி விடும்.''', '''From envious man good fortune\'s goddess turns away,
Grudging him good, and points him out misfortune\'s prey.''',
                               '''Lakshmi envying (the prosperity) of the envious man will depart and introduce him to her sister.''');
        k[167] = Kural.factory(168, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அழுக்காறு எனஒரு பாவி திருச்செற்றுத்
  தீயுழி உய்த்து விடும்.''', '''Envy, embodied ill, incomparable bane,
Good fortune slays, and soul consigns to fiery pain.''',
                               '''Envy will destroy (a man\'s) wealth (in his world) and drive him into the pit of fire (in the world to come.)''');
        k[168] = Kural.factory(169, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அவ்விய நெஞ்சத்தான் ஆக்கமும் செவ்வியான்
  கேடும் நினைக்கப் படும்.''', '''To men of envious heart, when comes increase of joy,
Or loss to blameless men, the \'why\' will thoughtful hearts employ.''',
                               '''The wealth of a man of envious mind and the poverty of the righteous will be pondered.''');
        k[169] = Kural.factory(170, '''அறத்துப்பால்''', '''அழுக்காறாமை''', '''அழுக்கற்று அகன்றாரும் இல்லை அஃதுஇல்லார்
  பெருக்கத்தில் தீர்ந்தாரும் இல்.''', '''No envious men to large and full felicity attain;
No men from envy free have failed a sure increase to gain.''',
                               '''Never have the envious become great; never have those who are free from envy been without greatness.''');
        k[170] = Kural.factory(171, '''அறத்துப்பால்''', '''வெஃகாமை''', '''நடுவின்றி நன்பொருள் வெஃகின் குடிபொன்றிக்
  குற்றமும் ஆங்கே தரும்.''', '''With soul unjust to covet others\' well-earned store,
Brings ruin to the home, to evil opes the door.''',
                               '''If a man departing from equity covet the property (of others), at that very time will his family be destroyed and guilt be incurred.''');
        k[171] = Kural.factory(172, '''அறத்துப்பால்''', '''வெஃகாமை''', '''படுபயன் வெஃகிப் பழிப்படுவ செய்யார்
  நடுவன்மை நாணு பவர்.''', '''Through lust of gain, no deeds that retribution bring,
Do they, who shrink with shame from every unjust thing.''',
                               '''Those who blush at the want of equity will not commit disgraceful acts through desire of the profit that may be gained.''');
        k[172] = Kural.factory(173, '''அறத்துப்பால்''', '''வெஃகாமை''', '''சிற்றின்பம் வெஃகி அறனல்ல செய்யாரே
  மற்றின்பம் வேண்டு பவர்.''', '''No deeds of ill, misled by base desire,
Do they, whose souls to other joys aspire.''',
                               '''Those who desire the higher pleasures (of heaven) will not act unjustly through desire of the trifling joy. (in this life.)''');
        k[173] = Kural.factory(174, '''அறத்துப்பால்''', '''வெஃகாமை''', '''இலமென்று வெஃகுதல் செய்யார் புலம்வென்ற
  புன்மையில் காட்சி யவர்.''', '''Men who have conquered sense, with sight from sordid vision freed,
Desire not other\'s goods, e\'en in the hour of sorest need.''',
                               '''The wise who have conquered their senses and are free from crime, will not covet (the things of others), with the thought "we are destitute."''');
        k[174] = Kural.factory(175, '''அறத்துப்பால்''', '''வெஃகாமை''', '''அஃகி அகன்ற அறிவென்னாம் யார்மாட்டும்
  வெஃகி வெறிய செயின்.''', '''What gain, though lore refined of amplest reach he learn,
His acts towards all mankind if covetous desire to folly turn?''',
                               '''What is the advantage of extensive and accurate knowledge if a man through covetousness act senselessly towards all ?''');
        k[175] = Kural.factory(176, '''அறத்துப்பால்''', '''வெஃகாமை''', '''அருள்வெஃகி ஆற்றின்கண் நின்றான் பொருள்வெஃகிப்
  பொல்லாத சூழக் கெடும்.''', '''Though, grace desiring, he in virtue\'s way stand strong,
He\'s lost who wealth desires, and ponders deeds of wrong.''',
                               '''If he, who through desire of the virtue of kindness abides in the domestic state i.e., the path in which it may be obtained, covet (the property of others) and think of evil methods (to obtain it), he will perish.''');
        k[176] = Kural.factory(177, '''அறத்துப்பால்''', '''வெஃகாமை''', '''வேண்டற்க வெஃகியாம் ஆக்கம் விளைவயின்
  மாண்டற் கரிதாம் பயன்.''', '''Seek not increase by greed of gain acquired;
That fruit matured yields never good desired.''',
                               '''Desire not the gain of covetousness. In the enjoyment of its fruits there is no glory.''');
        k[177] = Kural.factory(178, '''அறத்துப்பால்''', '''வெஃகாமை''', '''அஃகாமை செல்வத்திற்கு யாதெனின் வெஃகாமை
  வேண்டும் பிறன்கைப் பொருள்.''', '''What saves prosperity from swift decline?
Absence of lust to make another\'s cherished riches thine!''',
                               '''If it is weighed, "what is the indestructibility of wealth," it is freedom from covetousness.''');
        k[178] = Kural.factory(179, '''அறத்துப்பால்''', '''வெஃகாமை''', '''அறனறிந்து வெஃகா அறிவுடையார்ச் சேரும்
  திறன்அறிந் தாங்கே திரு.''', '''Good fortune draws anigh in helpful time of need,
To him who, schooled in virtue, guards his soul from greed.''',
                               '''Lakshmi, knowing the manner (in which she may approach) will immediately come to those wise men who, knowing that it is virtue, covet not the property of others.''');
        k[179] = Kural.factory(180, '''அறத்துப்பால்''', '''வெஃகாமை''', '''இறலீனும் எண்ணாது வெஃகின் விறல்ஈனும்
  வேண்டாமை என்னுஞ் செருக்கு.''', '''From thoughtless lust of other\'s goods springs fatal ill,
Greatness of soul that covets not shall triumph still.''',
                               '''To covet (the wealth of another) regardless of consequences will bring destruction. That greatness (of mind) which covets not will give victory.''');
        k[180] = Kural.factory(181, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''அறங்கூறான் அல்ல செயினும் ஒருவன்
  புறங்கூறான் என்றல் இனிது.''', '''Though virtuous words his lips speak not, and all his deeds are ill.
If neighbour he defame not, there\'s good within him still.''',
                               '''Though one do not even speak of virtue and live in sin, it will be well if it be said of him "he does not backbite."''');
        k[181] = Kural.factory(182, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''அறனழீஇ அல்லவை செய்தலின் தீதே
  புறனழீஇப் பொய்த்து நகை.''', '''Than he who virtue scorns, and evil deeds performs, more vile,
Is he that slanders friend, then meets him with false smile.''',
                               '''To smile deceitfully (in another\'s presence) after having reviled him to his destruction (behind his back) is a greater evil than the commission of (every other) sin and the destruction of (every) virtue.''');
        k[182] = Kural.factory(183, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''புறங்கூறிப் பொய்த்துயிர் வாழ்தலின் சாதல்
  அறங்கூற்றும் ஆக்கத் தரும்.''', '''\'Tis greater gain of virtuous good for man to die,
Than live to slander absent friend, and falsely praise when nigh.''',
                               '''Death rather than life will confer upon the deceitful backbiter the profit which (the treatises on) virtue point out.''');
        k[183] = Kural.factory(184, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''கண்ணின்று கண்ணறச் சொல்லினும் சொல்லற்க
  முன்னின்று பின்நோக்காச் சொல்.''', '''In presence though unkindly words you speak, say not
In absence words whose ill result exceeds your thought.''',
                               '''Though you speak without kindness before another\'s face speak not in his absence words which regard not the evil subsequently resulting from it.''');
        k[184] = Kural.factory(185, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''அறஞ்சொல்லும் நெஞ்சத்தான் அன்மை புறஞ்சொல்லும்
  புன்மையாற் காணப் படும்.''', '''The slanderous meanness that an absent friend defames,
\'This man in words owns virtue, not in heart,\' proclaims.''',
                               '''The emptiness of that man\'s mind who (merely) praises virtue will be seen from the meanness of reviling another behind his back.''');
        k[185] = Kural.factory(186, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''பிறன்பழி கூறுவான் தன்பழி யுள்ளும்
  திறன்தெரிந்து கூறப் படும்.''', '''Who on his neighbours\' sins delights to dwell,
The story of his sins, culled out with care, the world will tell.''',
                               '''The character of the faults of that man who publishes abroad the faults of others will be sought out and published.''');
        k[186] = Kural.factory(187, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''பகச்சொல்லிக் கேளிர்ப் பிரிப்பர் நகச்சொல்லி
  நட்பாடல் தேற்றா தவர்.''', '''With friendly art who know not pleasant words to say,
Speak words that sever hearts, and drive choice friends away.''',
                               '''Those who know not to live in friendship with amusing conversation will by back-biting estrange even their relatives.''');
        k[187] = Kural.factory(188, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''துன்னியார் குற்றமும் தூற்றும் மரபினார்
  என்னைகொல் ஏதிலார் மாட்டு.''', '''Whose nature bids them faults of closest friends proclaim
What mercy will they show to other men\'s good name?''',
                               '''What will those not do to strangers whose nature leads them to publish abroad the faults of their intimate friends ?''');
        k[188] = Kural.factory(189, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''அறன்நோக்கி ஆற்றுங்கொல் வையம் புறன்நோக்கிப்
  புன்சொல் உரைப்பான் பொறை.''', '''\'Tis charity, I ween, that makes the earth sustain their load.
Who, neighbours\' absence watching, tales or slander tell abroad.''',
                               '''The world through charity supports the weight of those who reproach others observing their absence.''');
        k[189] = Kural.factory(190, '''அறத்துப்பால்''', '''புறங்கூறாமை''', '''ஏதிலார் குற்றம்போல் தங்குற்றங் காண்கிற்பின்
  தீதுண்டோ மன்னும் உயிர்க்கு.''', '''If each his own, as neighbours\' faults would scan,
Could any evil hap to living man?''',
                               '''If they observed their own faults as they observe the faults of others, would any evil happen to men ?''');
        k[190] = Kural.factory(191, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''பல்லார் முனியப் பயனில சொல்லுவான்
  எல்லாரும் எள்ளப் படும்.''', '''Words without sense, while chafe the wise,
Who babbles, him will all despise.''',
                               '''He who to the disgust of many speaks useless things will be despised by all.''');
        k[191] = Kural.factory(192, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''பயனில பல்லார்முன் சொல்லல் நயனில
  நட்டார்கண் செய்தலிற் றீது.''', '''Words without sense, where many wise men hear, to pour
Than deeds to friends ungracious done offendeth more.''',
                               '''To speak useless things in the presence of many is a greater evil than to do unkind things towards friends.''');
        k[192] = Kural.factory(193, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''நயனிலன் என்பது சொல்லும் பயனில
  பாரித் துரைக்கும் உரை.''', '''Diffusive speech of useless words proclaims
A man who never righteous wisdom gains.''',
                               '''That conversation in which a man utters forth useless things will say of him "he is without virtue."''');
        k[193] = Kural.factory(194, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''நயன்சாரா நன்மையின் நீக்கும் பயன்சாராப்
  பண்பில்சொல் பல்லா ரகத்து.''', '''Unmeaning, worthless words, said to the multitude,
To none delight afford, and sever men from good.''',
                               '''The words devoid of profit or pleasure which a man speaks will, being inconsistent with virtue, remove him from goodness.''');
        k[194] = Kural.factory(195, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''சீர்மை சிறப்பொடு நீங்கும் பயனில
  நீர்மை யுடையார் சொலின்.''', '''Gone are both fame and boasted excellence,
When men of worth speak of words devoid of sense.''',
                               '''If the good speak vain words their eminence and excellence will leave them.''');
        k[195] = Kural.factory(196, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''பயனில்சொல் பராட்டு வானை மகன்எனல்
  மக்கட் பதடி யெனல்.''', '''Who makes display of idle words\' inanity,
Call him not man, -chaff of humanity!''',
                               '''Call not him a man who parades forth his empty words. Call him the chaff of men.''');
        k[196] = Kural.factory(197, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''நயனில சொல்லினுஞ் சொல்லுக சான்றோர்
  பயனில சொல்லாமை நன்று.''', '''Let those who list speak things that no delight afford,
\'Tis good for men of worth to speak no idle word.''',
                               '''Let the wise if they will, speak things without excellence; it will be well for them not to speak useless things.''');
        k[197] = Kural.factory(198, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''அரும்பயன் ஆயும் அறிவினார் சொல்லார்
  பெரும்பயன் இல்லாத சொல்.''', '''The wise who weigh the worth of every utterance,
Speak none but words of deep significance.''',
                               '''The wise who seek after rare pleasures will not speak words that have not much weight in them.''');
        k[198] = Kural.factory(199, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''பொருள்தீர்ந்த பொச்சாந்துஞ் சொல்லார் மருள்தீர்ந்த
  மாசறு காட்சி யவர்.''', '''The men of vision pure, from wildering folly free,
Not e\'en in thoughtless hour, speak words of vanity.''',
                               '''Those wise men who are without faults and are freed from ignorance will not even forgetfully speak things that profit not.''');
        k[199] = Kural.factory(200, '''அறத்துப்பால்''', '''பயனில சொல்லாமை''', '''சொல்லுக சொல்லிற் பயனுடைய சொல்லற்க
  சொல்லிற் பயனிலாச் சொல்.''', '''If speak you will, speak words that fruit afford,
If speak you will, speak never fruitless word.''', '''Speak what is useful, and speak not useless words.''');
        k[200] = Kural.factory(201, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''தீவினையார் அஞ்சார் விழுமியார் அஞ்சுவர்
  தீவினை என்னும் செருக்கு.''', '''With sinful act men cease to feel the dread of ill within,
The excellent will dread the wanton pride of cherished sin.''',
                               '''Those who have experience of evil deeds will not fear, but the excellent will fear the pride of sin.''');
        k[201] = Kural.factory(202, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''தீயவை தீய பயத்தலால் தீயவை
  தீயினும் அஞ்சப் படும்.''', '''Since evils new from evils ever grow,
Evil than fire works out more dreaded woe.''',
                               '''Because evil produces evil, therefore should evil be feared more than fire.''');
        k[202] = Kural.factory(203, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''அறிவினுள் எல்லாந் தலையென்ப தீய
  செறுவார்க்கும் செய்யா விடல்.''', '''Even to those that hate make no return of ill;
So shalt thou wisdom\'s highest law, \'tis said, fulfil.''',
                               '''To do no evil to enemies will be called the chief of all virtues.''');
        k[203] = Kural.factory(204, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''மறந்தும் பிறன்கேடு சூழற்க சூழின்
  அறஞ்சூழம் சூழ்ந்தவன் கேடு.''', '''Though good thy soul forget, plot not thy neighbour\'s fall,
Thy plans shall \'virtue\'s Power\' by ruin to thyself forestall.''',
                               '''Even though forgetfulness meditate not the ruin of another. Virtue will meditate the ruin of him who thus meditates.''');
        k[204] = Kural.factory(205, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''இலன்என்று தீயவை செய்யற்க செய்யின்
  இலனாகும் மற்றும் பெயர்த்து.''', '''Make not thy poverty a plea for ill;
Thy evil deeds will make thee poorer still.''',
                               '''Commit not evil, saying, "I am poor": if you do, you will become poorer still.''');
        k[205] = Kural.factory(206, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''தீப்பால தான்பிறர்கண் செய்யற்க நோய்ப்பால
  தன்னை அடல்வேண்டா தான்.''', '''What ranks as evil spare to do, if thou would\'st shun
Affliction sore through ill to thee by others done.''',
                               '''Let him not do evil to others who desires not that sorrows should pursue him.''');
        k[206] = Kural.factory(207, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''எனைப்பகை யுற்றாரும் உய்வர் வினைப்பகை
  வீயாது பின்சென்று அடும்.''', '''From every enmity incurred there is to \'scape, a way;
The wrath of evil deeds will dog men\'s steps, and slay.''',
                               '''However great be the enmity men have incurred they may still live. The enmity of sin will incessantly pursue and kill.''');
        k[207] = Kural.factory(208, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''தீயவை செய்தார் கெடுதல் நிழல்தன்னை
  வீயாது அஇஉறைந் தற்று.''', '''Man\'s shadow dogs his steps where\'er he wends;
Destruction thus on sinful deeds attends.''',
                               '''Destruction will dwell at the heels of those who commit evil even as their shadow that leaves them not.''');
        k[208] = Kural.factory(209, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''தன்னைத்தான் காதல னாயின் எனைத்தொன்றும்
  துன்னற்க தீவினைப் பால்.''', '''Beware, if to thyself thyself is dear,
Lest thou to aught that ranks as ill draw near!''',
                               '''If a man love himself, let him not commit any sin however small.''');
        k[209] = Kural.factory(210, '''அறத்துப்பால்''', '''தீவினையச்சம்''', '''அருங்கேடன் என்பது அறிக மருங்கோடித்
  தீவினை செய்யான் எனின்.''', '''The man, to devious way of sin that never turned aside,
From ruin rests secure, whatever ills betide.''',
                               '''Know ye that he is freed from destruction who commits no evil, going to neither side of the right path.''');
        k[210] = Kural.factory(211, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''கைம்மாறு வேண்டா கடப்பாடு மாரிமாட்டு
  என்ஆற்றுங் கொல்லோ உலகு.''', '''Duty demands no recompense; to clouds of heaven,
By men on earth, what answering gift is given?''',
                               '''Benevolence seeks not a return. What does the world give back to the clouds ?''');
        k[211] = Kural.factory(212, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''தாளாற்றித் தந்த பொருளெல்லாம் தக்கார்க்கு
  வேளாண்மை செய்தற் பொருட்டு.''', '''The worthy say, when wealth rewards their toil-spent hours,
For uses of beneficence alone \'tis ours.''',
                               '''All the wealth acquired with perseverance by the worthy is for the exercise of benevolence.''');
        k[212] = Kural.factory(213, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''புத்தே ளுலகத்தும் ஈண்டும் பெறலரிதே
  ஒப்புரவின் நல்ல பிற.''', '''To \'due beneficence\' no equal good we know,
Amid the happy gods, or in this world below.''',
                               '''It is difficult to obtain another good equal to benevolence either in this world or in that of the gods.''');
        k[213] = Kural.factory(214, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''ஒத்த தறவோன் உயிர்வாழ்வான் மற்றையான்
  செத்தாருள் வைக்கப் படும்.''', '''Who knows what\'s human life\'s befitting grace,
He lives; the rest \'mongst dead men have their place.''',
                               '''He truly lives who knows (and discharges) the proper duties (of benevolence). He who knows them not will be reckoned among the dead.''');
        k[214] = Kural.factory(215, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''ஊருணி நீர்நிறைந் தற்றே உலகவாம்
  பேரறி வாளன் திரு.''', '''The wealth of men who love the \'fitting way,\' the truly wise,
Is as when water fills the lake that village needs supplies.''',
                               '''The wealth of that man of eminent knowledge who desires to exercise the benevolence approved of by the world, is like the full waters of a city-tank.''');
        k[215] = Kural.factory(216, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''பயன்மரம் உள்ளூர்ப் பழுத்தற்றால் செல்வம்
  நயனுடை யான்கண் படின்.''', '''A tree that fruits in th\' hamlet\'s central mart,
Is wealth that falls to men of liberal heart.''',
                               '''The wealth of a man (possessed of the virtue) of benevolence is like the ripening of a fruitful tree in the midst of a town.''');
        k[216] = Kural.factory(217, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''மருந்தாகித் தப்பா மரத்தற்றால் செல்வம்
  பெருந்தகை யான்கண் படின்.''', '''Unfailing tree that healing balm distils from every part,
Is ample wealth that falls to him of large and noble heart.''',
                               '''If wealth be in the possession of a man who has the great excellence (of benevolence), it is like a tree which as a medicine is an infallible cure for disease.''');
        k[217] = Kural.factory(218, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''இடனில் பருவத்தும் ஒப்புரவிற்கு ஒல்கார்
  கடனறி காட்சி யவர்.''', '''E\'en when resources fall, they weary not of \'kindness due,\'-
They to whom Duty\'s self appears in vision true.''',
                               '''The wise who know what is duty will not scant their benevolence even when they are without wealth.''');
        k[218] = Kural.factory(219, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''நயனுடையான் நல்கூர்ந்தா னாதல் செயும்நீர
  செய்யாது அமைகலா வாறு.''', '''The kindly-hearted man is poor in this alone,
When power of doing deeds of goodness he finds none.''',
                               '''The poverty of a benevolent man, is nothing but his inability to exercise the same.''');
        k[219] = Kural.factory(220, '''அறத்துப்பால்''', '''ஒப்புரவறிதல்''', '''ஒப்புரவி னால்வரும் கேடெனின் அஃதொருவன்
  விற்றுக்கோள் தக்க துடைத்து.''', '''Though by \'beneficence,\' the loss of all should come,
\'Twere meet man sold himself, and bought it with the sum.''',
                               '''If it be said that loss will result from benevolence, such loss is worth being procured even by the sale of one\'s self.''');
        k[220] = Kural.factory(221, '''அறத்துப்பால்''', '''ஈகை''', '''வறியார்க்கொன்று ஈவதே ஈகைமற் றெல்லாம்
  குறியெதிர்ப்பை நீர துடைத்து.''', '''Call that a gift to needy men thou dost dispense,
All else is void of good, seeking for recompense.''',
                               '''To give to the destitute is true charity. All other gifts have the nature of (what is done for) a measured return.''');
        k[221] = Kural.factory(222, '''அறத்துப்பால்''', '''ஈகை''', '''நல்லாறு எனினும் கொளல்தீது மேலுலகம்
  இல்லெனினும் ஈதலே நன்று.''', '''Though men declare it heavenward path, yet to receive is ill;
Though upper heaven were not, to give is virtue still.''',
                               '''To beg is evil, even though it were said that it is a good path (to heaven). To give is good, even though it were said that those who do so cannot obtain heaven.''');
        k[222] = Kural.factory(223, '''அறத்துப்பால்''', '''ஈகை''', '''இலனென்னும் எவ்வம் உரையாமை ஈதல்
  குலனுடையான் கண்ணே யுள.''', '''\'I\'ve nought\' is ne\'er the high-born man\'s reply;
He gives to those who raise themselves that cry.''',
                               '''(Even in a low state) not to adopt the mean expedient of saying "I have nothing," but to give, is the characteristic of the mad of noble birth.''');
        k[223] = Kural.factory(224, '''அறத்துப்பால்''', '''ஈகை''', '''இன்னாது இரக்கப் படுதல் இரந்தவர்
  இன்முகங் காணும் அளவு.''', '''The suppliants\' cry for aid yields scant delight,
Until you see his face with grateful gladness bright.''',
                               '''To see men begging from us in disagreeable, until we see their pleasant countenance.''');
        k[224] = Kural.factory(225, '''அறத்துப்பால்''', '''ஈகை''', '''ஆற்றுவார் ஆற்றல் பசிஆற்றல் அப்பசியை
  மாற்றுவார் ஆற்றலின் பின்.''', '''\'Mid devotees they\'re great who hunger\'s pangs sustain,
Who hunger\'s pangs relieve a higher merit gain.''',
                               '''The power of those who perform penance is the power of enduring hunger. It is inferior to the power of those who remove the hunger (of others).''');
        k[225] = Kural.factory(226, '''அறத்துப்பால்''', '''ஈகை''', '''அற்றார் அழிபசி தீர்த்தல் அஃதொருவன்
  பெற்றான் பொருள்வைப் புழி.''', '''Let man relieve the wasting hunger men endure;
For treasure gained thus finds he treasure-house secure.''',
                               '''The removal of the killing hunger of the poor is the place for one to lay up his wealth.''');
        k[226] = Kural.factory(227, '''அறத்துப்பால்''', '''ஈகை''', '''பாத்தூண் மரீஇ யவனைப் பசியென்னும்
  தீப்பிணி தீண்டல் அரிது.''', '''Whose soul delights with hungry men to share his meal,
The hand of hunger\'s sickness sore shall never feel.''',
                               '''The fiery disease of hunger shall never touch him who habitually distributes his food to others.''');
        k[227] = Kural.factory(228, '''அறத்துப்பால்''', '''ஈகை''', '''ஈத்துவக்கும் இன்பம் அறியார்கொல் தாமுடைமை
  வைத்திழக்கும் வன்க ணவர்.''', '''Delight of glad\'ning human hearts with gifts do they not know.
Men of unpitying eye, who hoard their wealth and lose it so?''',
                               '''Do the hard-eyed who lay up and lose their possessions not know the happiness which springs from the pleasure of giving ?''');
        k[228] = Kural.factory(229, '''அறத்துப்பால்''', '''ஈகை''', '''இரத்தலின் இன்னாது மன்ற நிரப்பிய
  தாமே தமியர் உணல்.''', '''They keep their garners full, for self alone the board they spread;-
\'Tis greater pain, be sure, than begging daily bread!''',
                               '''Solitary and unshared eating for the sake of filling up one\'s own riches is certainly much more unpleasant than begging.''');
        k[229] = Kural.factory(230, '''அறத்துப்பால்''', '''ஈகை''', '''சாதலின் இன்னாத தில்லை இனிததூஉம்
  ஈதல் இயையாக் கடை.''', '''\'Tis bitter pain to die, \'Tis worse to live.
For him who nothing finds to give!''',
                               '''Nothing is more unpleasant than death: yet even that is pleasant where charity cannot be exercised.''');
        k[230] = Kural.factory(231, '''அறத்துப்பால்''', '''புகழ்''', '''ஈதல் இசைபட வாழ்தல் அதுவல்லது
  ஊதியம் இல்லை உயிர்க்கு.''', '''See that thy life the praise of generous gifts obtain;
Save this for living man exists no real gain.''',
                               '''Give to the poor and live with praise. There is no greater profit to man than that.''');
        k[231] = Kural.factory(232, '''அறத்துப்பால்''', '''புகழ்''', '''உரைப்பார் உரைப்பவை எல்லாம் இரப்பார்க்கொன்று
  ஈவார்மேல் நிற்கும் புகழ்.''', '''The speech of all that speak agrees to crown
The men that give to those that ask, with fair renown.''',
                               '''Whatsoever is spoken in the world will abide as praise upon that man who gives alms to the poor.''');
        k[232] = Kural.factory(233, '''அறத்துப்பால்''', '''புகழ்''', '''ஒன்றா உலகத்து உயர்ந்த புகழல்லால்
  பொன்றாது நிற்பதொன் றில்.''', '''Save praise alone that soars on high,
Nought lives on earth that shall not die.''',
                               '''There is nothing that stands forth in the world imperishable, except fame, exalted in solitary greatness.''');
        k[233] = Kural.factory(234, '''அறத்துப்பால்''', '''புகழ்''', '''நிலவரை நீள்புகழ் ஆற்றின் புலவரைப்
  போற்றாது புத்தேள் உலகு.''', '''If men do virtuous deeds by world-wide ample glory crowned,
The heavens will cease to laud the sage for other gifts renowned.''',
                               '''If one has acquired extensive fame within the limits of this earth, the world of the Gods will no longer praise those sages who have attained that world.''');
        k[234] = Kural.factory(235, '''அறத்துப்பால்''', '''புகழ்''', '''நத்தம்போல் கேடும் உளதாகும் சாக்காடும்
  வித்தகர்க் கல்லால் அரிது.''', '''Loss that is gain, and death of life\'s true bliss fulfilled,
Are fruits which only wisdom rare can yield.''',
                               '''Prosperity to the body of fame, resulting in poverty to the body of flesh and the stability to the former arising from the death of the latter, are achievable only by the wise.''');
        k[235] = Kural.factory(236, '''அறத்துப்பால்''', '''புகழ்''', '''தோன்றின் புகழொடு தோன்றுக அஃதிலார்
  தோன்றலின் தோன்றாமை நன்று.''', '''If man you walk the stage, appear adorned with glory\'s grace;
Save glorious you can shine, \'twere better hide your face.''',
                               '''If you are born (in this world), be born with qualities conductive to fame. From those who are destitute of them it will be better not to be born.''');
        k[236] = Kural.factory(237, '''அறத்துப்பால்''', '''புகழ்''', '''புகழ்பட வாழாதார் தந்நோவார் தம்மை
  இகழ்வாரை நோவது எவன்.''', '''If you your days will spend devoid of goodly fame,
When men despise, why blame them? You\'ve yourself to blame.''',
                               '''Why do those who cannot live with praise, grieve those who despise them, instead of grieving themselves for their own inability.''');
        k[237] = Kural.factory(238, '''அறத்துப்பால்''', '''புகழ்''', '''வசையென்ப வையத்தார்க் கெல்லாம் இசையென்னும்
  எச்சம் பெறாஅ விடின்.''', '''Fame is virtue\'s child, they say; if, then,
You childless live, you live the scorn of men.''',
                               '''Not to beget fame will be esteemed a disgrace by the wise in this world.''');
        k[238] = Kural.factory(239, '''அறத்துப்பால்''', '''புகழ்''', '''வசையிலா வண்பயன் குன்றும் இசையிலா
  யாக்கை பொறுத்த நிலம்.''', '''The blameless fruits of fields\' increase will dwindle down,
If earth the burthen bear of men without renown.''',
                               '''The ground which supports a body without fame will diminish in its rich produce.''');
        k[239] = Kural.factory(240, '''அறத்துப்பால்''', '''புகழ்''', '''வசையொழிய வாழ்வாரே வாழ்வார் இசையொழிய
  வாழ்வாரே வாழா தவர்.''', '''Who live without reproach, them living men we deem;
Who live without renown, live not, though living men they seem.''',
                               '''Those live who live without disgrace. Those who live without fame live not.''');
        k[240] = Kural.factory(241, '''அறத்துப்பால்''', '''அருளுடைமை''', '''அருட்செல்வம் செல்வத்துள் செல்வம் பொருட்செல்வம்
  பூரியார் கண்ணும் உள.''', '''Wealth \'mid wealth is wealth \'kindliness\';
Wealth of goods the vilest too possess.''',
                               '''The wealth of kindness is wealth of wealth, in as much as the wealth of property is possessed by the basest of men.''');
        k[241] = Kural.factory(242, '''அறத்துப்பால்''', '''அருளுடைமை''', '''நல்லாற்றாள் நாடி அருளாள்க பல்லாற்றால்
  தேரினும் அஃதே துணை.''', '''The law of \'grace\' fulfil, by methods good due trial made,
Though many systems you explore, this is your only aid.''',
                               '''(Stand) in the good path, consider, and be kind. Even considering according to the conflicting tenets of the different sects, kindness will be your best aid, (in the acquisition of heavenly bliss.)''');
        k[242] = Kural.factory(243, '''அறத்துப்பால்''', '''அருளுடைமை''', '''அருள்சேர்ந்த நெஞ்சினார்க் கில்லை இருள்சேர்ந்த
  இன்னா உலகம் புகல்.''', '''They in whose breast a \'gracious kindliness\' resides,
See not the gruesome world, where darkness drear abides.''',
                               '''They will never enter the world of darkness and wretchedness whose minds are the abode of kindness.''');
        k[243] = Kural.factory(244, '''அறத்துப்பால்''', '''அருளுடைமை''', '''மன்னுயிர் ஓம்பி அருளாள்வார்க்கு இல்லென்ப
  தன்னுயிர் அஞ்சும் வினை.''', '''Who for undying souls of men provides with gracious zeal,
In his own soul the dreaded guilt of sin shall never feel.''',
                               '''(The wise) say that the evils, which his soul would dread, will never come upon the man who exercises kindness and protects the life (of other creatures)''');
        k[244] = Kural.factory(245, '''அறத்துப்பால்''', '''அருளுடைமை''', '''அல்லல் அருளாள்வார்க்கு இல்லை வளிவழங்கும்
  மல்லன்மா ஞாலங் கரி.''', '''The teeming earth\'s vast realm, round which the wild winds blow,
Is witness, men of \'grace\' no woeful want shall know.''',
                               '''This great rich earth over which the wind blows, is a witness that sorrow never comes upon the kind-hearted.''');
        k[245] = Kural.factory(246, '''அறத்துப்பால்''', '''அருளுடைமை''', '''பொருள்நீங்கிப் பொச்சாந்தார் என்பர் அருள்நீங்கி
  அல்லவை செய்தொழுகு வார்.''', '''Gain of true wealth oblivious they eschew,
Who \'grace\' forsake, and graceless actions do.''',
                               '''(The wise) say that those who neglect kindness and practise cruelties, neglected virtue (in their former birth), and forgot (the sorrows which they must suffer.)''');
        k[246] = Kural.factory(247, '''அறத்துப்பால்''', '''அருளுடைமை''', '''அருளில்லார்க்கு அவ்வுலகம் இல்லை பொருளில்லார்க்கு
  இவ்வுலகம் இல்லாகி யாங்கு.''', '''As to impoverished men this present world is not;
The \'graceless\' in you world have neither part nor lot.''',
                               '''As this world is not for those who are without wealth, so that world is not for those who are without kindness.''');
        k[247] = Kural.factory(248, '''அறத்துப்பால்''', '''அருளுடைமை''', '''பொருளற்றார் பூப்பர் ஒருகால் அருளற்றார்
  அற்றார்மற் றாதல் அரிது.''', '''Who lose the flower of wealth, when seasons change, again may bloom;
Who lose \'benevolence\', lose all; nothing can change their doom.''',
                               '''Those who are without wealth may, at some future time, become prosperous; those who are destitute of kindness are utterly destitute; for them there is no change.''');
        k[248] = Kural.factory(249, '''அறத்துப்பால்''', '''அருளுடைமை''', '''தெருளாதான் மெய்ப்பொருள் கண்டற்றால் தேரின்
  அருளாதான் செய்யும் அறம்.''', '''When souls unwise true wisdom\'s mystic vision see,
The \'graceless\' man may work true works of charity.''',
                               '''If you consider, the virtue of him who is without kindness is like the perception of the true being by him who is without wisdom.''');
        k[249] = Kural.factory(250, '''அறத்துப்பால்''', '''அருளுடைமை''', '''வலியார்முன் தன்னை நினைக்கதான் தன்னின்
  மெலியார்மேல் செல்லு மிடத்து.''', '''When weaker men you front with threat\'ning brow,
Think how you felt in presence of some stronger foe.''',
                               '''When a man is about to rush upon those who are weaker than himself, let him remember how he has stood (trembling) before those who are stronger than himself.''');
        k[250] = Kural.factory(251, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''தன்னூன் பெருக்கற்குத் தான்பிறிது ஊனுண்பான்
  எங்ஙனம் ஆளும் அருள்.''', '''How can the wont of \'kindly grace\' to him be known,
Who other creatures\' flesh consumes to feed his own?''',
                               '''How can he be possessed of kindness, who to increase his own flesh, eats the flesh of other creatures.''');
        k[251] = Kural.factory(252, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''பொருளாட்சி போற்றாதார்க்கு இல்லை அருளாட்சி
  ஆங்கில்லை ஊன்தின் பவர்க்கு.''', '''No use of wealth have they who guard not their estate;
No use of grace have they with flesh who hunger sate.''',
                               '''As those possess no property who do not take care of it, so those possess no kindness who feed on flesh.''');
        k[252] = Kural.factory(253, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''படைகொண்டார் நெஞ்சம்போல் நன்னூக்காது ஒன்றன்
  உடல்சுவை உண்டார் மனம்.''', '''Like heart of them that murderous weapons bear, his mind,
Who eats of savoury meat, no joy in good can find.''',
                               '''Like the (murderous) mind of him who carries a weapon (in his hand), the mind of him who feasts with pleasure on the body of another (creature), has no regard for goodness.''');
        k[253] = Kural.factory(254, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''ருளல்லது யாதெனின் கொல்லாமை கோறல்
  பொருளல்லது அவ்வூன் தினல்.''', '''\'What\'s grace, or lack of grace\'? \'To kill\' is this, that \'not to kill\';
To eat dead flesh can never worthy end fulfil.''',
                               '''If it be asked what is kindness and what its opposite, the answer would be preservation and destruction of life; and therefore it is not right to feed on the flesh (obtained by taking away life).''');
        k[254] = Kural.factory(255, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''உண்ணாமை உள்ளது உயிர்நிலை ஊனுண்ண
  அண்ணாத்தல் செய்யாது அளறு.''', '''If flesh you eat not, life\'s abodes unharmed remain;
Who eats, hell swallows him, and renders not again.''',
                               '''Not to eat flesh contributes to the continuance of life; therefore if a man eat flesh, hell will not open its mouth (to let him escape out, after he has once fallen in).''');
        k[255] = Kural.factory(256, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''தினற்பொருட்டால் கொல்லாது உலகெனின் யாரும்
  விலைப்பொருட்டால் ஊன்றருவா ரில்.''', '''\'We eat the slain,\' you say, by us no living creatures die;
Who\'d kill and sell, I pray, if none came there the flesh to buy?''',
                               '''If the world does not destroy life for the purpose of eating, then no one would sell flesh for the sake of money.''');
        k[256] = Kural.factory(257, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''உண்ணாமை வேண்டும் புலாஅல் பிறிதொன்றன்
  புண்ணது உணர்வார்ப் பெறின்.''', '''With other beings\' ulcerous wounds their hunger they appease;
If this they felt, desire to eat must surely cease.''',
                               '''If men should come to know that flesh is nothing but the unclean ulcer of a body, let them abstain from eating it.''');
        k[257] = Kural.factory(258, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''செயிரின் தலைப்பிரிந்த காட்சியார் உண்ணார்
  உயிரின் தலைப்பிரிந்த ஊன்.''', '''Whose souls the vision pure and passionless perceive,
Eat not the bodies men of life bereave.''',
                               '''The wise, who have freed themselves from mental delusion, will not eat the flesh which has been severed from an animal.''');
        k[258] = Kural.factory(259, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''அவிசொரிந் தாயிரம் வேட்டலின் ஒன்றன்
  உயிர்செகுத் துண்ணாமை நன்று.''', '''Than thousand rich oblations, with libations rare,
Better the flesh of slaughtered beings not to share.''',
                               '''Not to kill and eat (the flesh of) an animal, is better than the pouring forth of ghee etc., in a thousand sacrifices.''');
        k[259] = Kural.factory(260, '''அறத்துப்பால்''', '''புலான்மறுத்தல்''', '''கொல்லான் புலாலை மறுத்தானைக் கைகூப்பி
  எல்லா உயிருந் தொழும்.''', '''Who slays nought,- flesh rejects- his feet before
All living things with clasped hands adore.''',
                               '''All creatures will join their hands together, and worship him who has never taken away life, nor eaten flesh.''');
        k[260] = Kural.factory(261, '''அறத்துப்பால்''', '''தவம்''', '''உற்றநோய் நோன்றல் உயிர்க்குறுகண் செய்யாமை
  அற்றே தவத்திற் குரு.''', '''To bear due penitential pains, while no offence
He causes others, is the type of \'penitence\'.''',
                               '''The nature of religious discipline consists, in the endurance (by the ascetic) of the sufferings which it brings on himself, and in abstaining from giving pain to others.''');
        k[261] = Kural.factory(262, '''அறத்துப்பால்''', '''தவம்''', '''தவமும் தவமுடையார்க்கு ஆகும் அதனை
  அஃதிலார் மேற்கொள் வது.''', '''To \'penitents\' sincere avails their \'penitence\';
Where that is not, \'tis but a vain pretence.''',
                               '''Austerities can only be borne, and their benefits enjoyed, by those who have practised them (in a former birth); it will be useless for those who have not done so, to attempt to practise them (now).''');
        k[262] = Kural.factory(263, '''அறத்துப்பால்''', '''தவம்''', '''துறந்தார்க்குத் துப்புரவு வேண்டி மறந்தார்கொல்
  மற்றை யவர்கள் தவம்.''', '''Have other men forgotten \'penitence\' who strive
To earn for penitents the things by which they live?''',
                               '''It is to provide food etc, for the ascetics who have abandoned (the desire of earthly possessions) that other persons have forgotten (to practise) austerity ?''');
        k[263] = Kural.factory(264, '''அறத்துப்பால்''', '''தவம்''', '''ஒன்னார்த் தெறலும் உவந்தாரை ஆக்கலும்
  எண்ணின் தவத்தான் வரும்.''', '''Destruction to his foes, to friends increase of joy.
The \'penitent\' can cause, if this his thoughts employ.''',
                               '''If (the ascetic) desire the destruction of his enemies, or the aggrandizement of his friends, it will be effected by (the power of) his austerities.''');
        k[264] = Kural.factory(265, '''அறத்துப்பால்''', '''தவம்''', '''வேண்டிய வேண்டியாங் கெய்தலால் செய்தவம்
  ஈண்டு முயலப் படும்.''', '''That what they wish may, as they wish, be won,
By men on earth are works of painful \'penance\' done.''',
                               '''Religious dislipline is practised in this world, because it secures the attainment of whatever one may wish to enjoy (in the world to come).''');
        k[265] = Kural.factory(266, '''அறத்துப்பால்''', '''தவம்''', '''தவஞ்செய்வார் தங்கருமஞ் செய்வார்மற் றல்லார்
  அவஞ்செய்வார் ஆசையுட் பட்டு.''', '''Who works of \'penance\' do, their end attain,
Others in passion\'s net enshared, toil but in vain.''',
                               '''Those discharge their duty who perform austerities; all others accomplish their own destruction, through the entanglement of the desire (of riches and sensual pleasure).''');
        k[266] = Kural.factory(267, '''அறத்துப்பால்''', '''தவம்''', '''சுடச்சுடரும் பொன்போல் ஒளிவிடும் துன்பஞ்
  சுடச்சுட நோற்கிற் பவர்க்கு.''', '''The hotter glows the fining fire, the gold the brighter shines;
The pain of penitence, like fire, the soul of man refines.''',
                               '''Just as gold is purified as heated in the fire, will those shine, who have endured the burning of pain (in frequent austerities).''');
        k[267] = Kural.factory(268, '''அறத்துப்பால்''', '''தவம்''', '''தன்னுயிர் தான்அறப் பெற்றானை ஏனைய
  மன்னுயி ரெல்லாந் தொழும்.''', '''Who gains himself in utter self-control,
Him worships every other living soul.''',
                               '''All other creatures will worship him who has attained the control of his own soul.''');
        k[268] = Kural.factory(269, '''அறத்துப்பால்''', '''தவம்''', '''கூற்றம் குதித்தலும் கைகூடும் நோற்றலின்
  ஆற்றல் தலைப்பட் டவர்க்குல்.''', '''E\'en over death the victory he may gain,
If power by penance won his soul obtain.''',
                               '''Those who have attained the power which religious discipline confers, will be able also to pass the limit of Yama, (the God of death).''');
        k[269] = Kural.factory(270, '''அறத்துப்பால்''', '''தவம்''', '''இலர்பல ராகிய காரணம் நோற்பார்
  சிலர்பலர் நோலா தவர்.''', '''The many all things lack! The cause is plain,
The \'penitents\' are few. The many shun such pain.''',
                               '''Because there are few who practise austerity and many who do not, there are many destitute and few rich in this world.''');
        k[270] = Kural.factory(271, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''வஞ்ச மனத்தான் படிற்றொழுக்கம் பூதங்கள்
  ஐந்தும் அகத்தே நகும்.''', '''Who with deceitful mind in false way walks of covert sin,
The five-fold elements his frame compose, decide within.''',
                               '''The five elements (of his body) will laugh within him at the feigned conduct of the deceitful minded man.''');
        k[271] = Kural.factory(272, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''வானுயர் தோற்றம் எவன்செய்யும் தன்னெஞ்சம்
  தான்அறி குற்றப் படின்.''', '''What gain, though virtue\'s semblance high as heaven his fame exalt,
If heart dies down through sense of self-detected fault?''',
                               '''What avails an appearance (of sanctity) high as heaven, if his mind suffers (the indulgence) of conscious sin.''');
        k[272] = Kural.factory(273, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''வலியில் நிலைமையான் வல்லுருவம் பெற்றம்
  புலியின்தோல் போர்த்துமேய்ந் தற்று.''', '''As if a steer should graze wrapped round with tiger\'s skin,
Is show of virtuous might when weakness lurks within.''',
                               '''The assumed appearance of power, by a man who has no power (to restrain his senses and perform austerity), is like a cow feeding on grass covered with a tiger\'s skin.''');
        k[273] = Kural.factory(274, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''தவமறைந்து அல்லவை செய்தல் புதல்மறைந்து
  வேட்டுவன் புள்சிமிழ்த் தற்று.''', '''\'Tis as a fowler, silly birds to snare, in thicket lurks.
When, clad in stern ascetic garb, one secret evil works.''',
                               '''He who hides himself under the mask of an ascetic and commits sins, like a sportsman who conceals himself in the thicket to catch birds.''');
        k[274] = Kural.factory(275, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''பற்றற்றேம் என்பார் படிற்றொழுக்கம் எற்றெற்றென்று
  ஏதம் பலவுந் தரும்.''', '''\'Our souls are free,\' who say, yet practise evil secretly,
\'What folly have we wrought!\' by many shames o\'er-whelmed, shall cry.''',
                               '''The false conduct of those who say they have renounced all desire will one day bring them sorrows that will make them cry out, "Oh! what have we done, what have we done."''');
        k[275] = Kural.factory(276, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''நெஞ்சின் துறவார் துறந்தார்போல் வஞ்சித்து
  வாழ்வாரின் வன்கணார் இல்.''', '''In mind renouncing nought, in speech renouncing every tie,
Who guileful live,- no men are found than these of \'harder eye\'.''',
                               '''Amongst living men there are none so hard-hearted as those who without to saking (desire) in their heart, falsely take the appearance of those who have forsaken (it).''');
        k[276] = Kural.factory(277, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''புறங்குன்றி கண்டனைய ரேனும் அகங்குன்றி
  முக்கிற் கரியார் உடைத்து.''', '''Outward, they shine as \'kunri\' berry\'s scarlet bright;
Inward, like tip of \'kunri\' bead, as black as night.''',
                               '''(The world) contains persons whose outside appears (as fair) as the (red) berry of the Abrus, but whose inside is as black as the nose of that berry.''');
        k[277] = Kural.factory(278, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''மனத்தது மாசாக மாண்டார் நீராடி
  மறைந்தொழுகு மாந்தர் பலர்.''', '''Many wash in hollowed waters, living lives of hidden shame;
Foul in heart, yet high upraised of men in virtuous fame.''',
                               '''There are many men of masked conduct, who perform their ablutions, and (make a show) of greatness, while their mind is defiled (with guilt).''');
        k[278] = Kural.factory(279, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''கணைகொடிது யாழ்கோடு செவ்விதுஆங் கன்ன
  வினைபடு பாலால் கொளல்.''', '''Cruel is the arrow straight, the crooked lute is sweet,
Judge by their deeds the many forms of men you meet.''',
                               '''As, in its use, the arrow is crooked, and the curved lute is straight, so by their deeds, (and not by their appearance) let (the uprightness or crookedness of) men be estimated.''');
        k[279] = Kural.factory(280, '''அறத்துப்பால்''', '''கூடாவொழுக்கம்''', '''மழித்தலும் நீட்டலும் வேண்டா உலகம்
  பழித்தது ஒழித்து விடின்.''', '''What\'s the worth of shaven head or tresses long,
If you shun what all the world condemns as wrong?''',
                               '''There is no need of a shaven crown, nor of tangled hair, if a man abstain from those deeds which the wise have condemned.''');
        k[280] = Kural.factory(281, '''அறத்துப்பால்''', '''கள்ளாமை''', '''எள்ளாமை வேண்டுவான் என்பான் எனைத்தொன்றும்
  கள்ளாமை காக்கதன் நெஞ்சு.''', '''Who seeks heaven\'s joys, from impious levity secure,
Let him from every fraud preserve his spirit pure.''',
                               '''Let him, who desires not to be despised, keep his mind from (the desire of) defrauding another of the smallest thing.''');
        k[281] = Kural.factory(282, '''அறத்துப்பால்''', '''கள்ளாமை''', '''உள்ளத்தால் உள்ளலும் தீதே பிறன்பொருளைக்
  கள்ளத்தால் கள்வேம் எனல்.''', '''\'Tis sin if in the mind man but thought conceive;
\'By fraud I will my neighbour of his wealth bereave.\'''',
                               '''Even the thought (of sin) is sin; think not then of crafiily stealing the property of another.''');
        k[282] = Kural.factory(283, '''அறத்துப்பால்''', '''கள்ளாமை''', '''களவினால் ஆகிய ஆக்கம் அளவிறந்து
  ஆவது போலக் கெடும்.''', '''The gain that comes by fraud, although it seems to grow
With limitless increase, to ruin swift shall go.''',
                               '''The property, which is acquired by fraud, will entirely perish, even while it seems to increase.''');
        k[283] = Kural.factory(284, '''அறத்துப்பால்''', '''கள்ளாமை''', '''களவின்கண் கன்றிய காதல் விளைவின்கண்
  வீயா விழுமம் தரும்.''', '''The lust inveterate of fraudful gain,
Yields as its fruit undying pain.''',
                               '''The eager desire of defrauding others will, when it brings forth its fruit, produce undying sorrow.''');
        k[284] = Kural.factory(285, '''அறத்துப்பால்''', '''கள்ளாமை''', '''அருள்கருதி அன்புடைய ராதல் பொருள்கருதிப்
  பொச்சாப்புப் பார்ப்பார்கண் இல்.''', '''\'Grace\' is not in their thoughts, nor know they kind affection\'s power,
Who neighbour\'s goods desire, and watch for his unguarded hour.''',
                               '''The study of kindness and the exercise of benevolence is not with those who watch for another\'s forgetfulness, though desire of his property.''');
        k[285] = Kural.factory(286, '''அறத்துப்பால்''', '''கள்ளாமை''', '''அளவின்கண் நின்றொழுகல் ஆற்றார் களவின்கண்
  கன்றிய காத லவர்.''', '''They cannot walk restrained in wisdom\'s measured bound,
In whom inveterate lust of fraudful gain is found.''',
                               '''They cannot walk steadfastly, according to rule, who eagerly desire to defraud others.''');
        k[286] = Kural.factory(287, '''அறத்துப்பால்''', '''கள்ளாமை''', '''களவென்னும் காரறி வாண்மை அளவென்னும்
  ஆற்றல் புரிந்தார்கண்ட இல்.''', '''Practice of fraud\'s dark cunning arts they shun,
Who long for power by \'measured wisdom\' won.''',
                               '''That black-knowledge which is called fraud, is not in those who desire that greatness which is called rectitude.''');
        k[287] = Kural.factory(288, '''அறத்துப்பால்''', '''கள்ளாமை''', '''அளவற஧ந்தார் நெஞ்சத் தறம்போல நிற்கும்
  களவறிந்தார் நெஞ்சில் கரவு.''', '''As virtue dwells in heart that \'measured wisdom\' gains;
Deceit in hearts of fraudful men established reigns.''',
                               '''Deceit dwells in the mind of those who are conversant with fraud, even as virtue in the minds of those who are conversant with rectitude.''');
        k[288] = Kural.factory(289, '''அறத்துப்பால்''', '''கள்ளாமை''', '''அளவல்ல செய்தாங்கே வீவர் களவல்ல
  மற்றைய தேற்றா தவர்.''', '''Who have no lore save that which fraudful arts supply,
Acts of unmeasured vice committing straightway die.''',
                               '''Those, who are acquainted with nothing but fraud, will perish in the very commission of transgression.''');
        k[289] = Kural.factory(290, '''அறத்துப்பால்''', '''கள்ளாமை''', '''கள்வார்க்குத் தள்ளும் உயிர்நிலை கள்வார்க்குத்
  தள்ளாது புத்தே ளுளகு.''', '''The fraudful forfeit life and being here below;
Who fraud eschew the bliss of heavenly beings know.''',
                               '''Even their body will fail the fraudulent; but even the world of the gods will not fail those who are free from fraud.''');
        k[290] = Kural.factory(291, '''அறத்துப்பால்''', '''வாய்மை''', '''வாய்மை எனப்படுவது யாதெனின் யாதொன்றும்
  தீமை இலாத சொலல்.''', '''You ask, in lips of men what \'truth\' may be;
\'Tis speech from every taint of evil free.''',
                               '''Truth is the speaking of such words as are free from the least degree of evil (to others).''');
        k[291] = Kural.factory(292, '''அறத்துப்பால்''', '''வாய்மை''', '''பொய்மையும் வாய்மை யிடத்த புரைதீர்ந்த
  நன்மை பயக்கும் எனின்.''', '''Falsehood may take the place of truthful word,
If blessing, free from fault, it can afford.''',
                               '''Even falsehood has the nature of truth, if it confer a benefit that is free from fault.''');
        k[292] = Kural.factory(293, '''அறத்துப்பால்''', '''வாய்மை''', '''தன்நெஞ் சறிவது பொய்யற்க பொய்த்தபின்
  தன்நெஞ்சே தன்னைச் சுடும்.''', '''Speak not a word which false thy own heart knows
Self-kindled fire within the false one\'s spirit glows.''',
                               '''Let not a man knowingly tell a lie; for after he has told the lie, his mind will burn him (with the memory of his guilt).''');
        k[293] = Kural.factory(294, '''அறத்துப்பால்''', '''வாய்மை''', '''உள்ளத்தாற் பொய்யா தொழுகின் உலகத்தார்
  உள்ளத்து ளெல்லாம் உளன்.''', '''True to his inmost soul who lives,- enshrined
He lives in souls of all mankind.''',
                               '''He who, in his conduct, preserves a mind free from deceit, will dwell in the minds of all men.''');
        k[294] = Kural.factory(295, '''அறத்துப்பால்''', '''வாய்மை''', '''மனத்தொடு வாய்மை மொழியின் தவத்தொடு
  தானஞ்செய் வாரின் தலை.''', '''Greater is he who speaks the truth with full consenting mind.
Than men whose lives have penitence and charity combined.''',
                               '''He, who speaks truth with all his heart, is superior to those who make gifts and practise austerities.''');
        k[295] = Kural.factory(296, '''அறத்துப்பால்''', '''வாய்மை''', '''பொய்யாமை அன்ன புகழில்லை எய்யாமை
  எல்லா அறமுந் தரும்.''', '''No praise like that of words from falsehood free;
This every virtue yields spontaneously.''',
                               '''There is no praise like the praise of never uttering a falsehood: without causing any suffering, it will lead to every virtue.''');
        k[296] = Kural.factory(297, '''அறத்துப்பால்''', '''வாய்மை''', '''பொய்யாமை பொய்யாமை ஆற்றின் அறம்பிற
  செய்யாமை செய்யாமை நன்று.''', '''If all your life be utter truth, the truth alone,
\'Tis well, though other virtuous acts be left undone.''',
                               '''If a man has the power to abstain from falsehood, it will be well with him, even though he practise no other virtue.''');
        k[297] = Kural.factory(298, '''அறத்துப்பால்''', '''வாய்மை''', '''புறள்தூய்மை நீரான் அமையும் அகந்தூய்மை
  வாய்மையால் காணப் படும்.''', '''Outward purity the water will bestow;
Inward purity from truth alone will flow.''',
                               '''Purity of body is produced by water and purity of mind by truthfulness.''');
        k[298] = Kural.factory(299, '''அறத்துப்பால்''', '''வாய்மை''', '''எல்லா விளக்கும் விளக்கல்ல சான்றோர்க்குப்
  பொய்யா விளக்கே விளக்கு.''', '''Every lamp is not a lamp in wise men\'s sight;
That\'s the lamp with truth\'s pure radiance bright.''',
                               '''All lamps of nature are not lamps; the lamp of truth is the lamp of the wise.''');
        k[299] = Kural.factory(300, '''அறத்துப்பால்''', '''வாய்மை''', '''யாமெய்யாக் கண்டவற்றுள் இல்லை எனைத்தொன்றும்
  வாய்மையின் நல்ல பிற.''', '''Of all good things we\'ve scanned with studious care,
There\'s nought that can with truthfulness compare.''',
                               '''Amidst all that we have seen (described) as real (excellence), there is nothing so good as truthfulness.''');
        k[300] = Kural.factory(301, '''அறத்துப்பால்''', '''வெகுளாமை''', '''செல்லிடத்துக் காப்பான் சினங்காப்பான் அல்லிடத்துக்
  காக்கின்என் காவாக்கா''', '''Where thou hast power thy angry will to work, thy wrath restrain;
Where power is none, what matter if thou check or give it rein?''',
                               '''He restrains his anger who restrains it when it can injure; when it cannot injure, what does it matter whether he restrain it, or not ?''');
        k[301] = Kural.factory(302, '''அறத்துப்பால்''', '''வெகுளாமை''', '''செல்லா இடத்துச் சினந்தீது செல்லிடத்தும்
  இல்அதனின் தீய பிற.''', '''Where power is none to wreak thy wrath, wrath importent is ill;
Where thou hast power thy will to work, \'tis greater, evil still.''',
                               '''Anger is bad, even when it cannot injure; when it can injure; there is no greater evil.''');
        k[302] = Kural.factory(303, '''அறத்துப்பால்''', '''வெகுளாமை''', '''மறத்தல் வெகுளியை யார்மாட்டும் தீய
  பிறத்தல் அதனான் வரும்.''', '''If any rouse thy wrath, the trespass straight forget;
For wrath an endless train of evils will beget.''',
                               '''Forget anger towards every one, as fountains of evil spring from it.''');
        k[303] = Kural.factory(304, '''அறத்துப்பால்''', '''வெகுளாமை''', '''நகையும் உவகையும் கொல்லும் சினத்தின்
  பகையும் உளவோ பிற.''', '''Wrath robs the face of smiles, the heart of joy,
What other foe to man works such annoy?''',
                               '''Is there a greater enemy than anger, which kills both laughter and joy ?''');
        k[304] = Kural.factory(305, '''அறத்துப்பால்''', '''வெகுளாமை''', '''தன்னைத்தான் காக்கின் சினங்காக்க காவாக்கால்
  தன்னையே கொல்லுஞ் சினம்.''', '''If thou would\'st guard thyself, guard against wrath alway;
\'Gainst wrath who guards not, him his wrath shall slay.''',
                               '''If a man would guard himself, let him guard against anger; if he do not guard it, anger will kill him.''');
        k[305] = Kural.factory(306, '''அறத்துப்பால்''', '''வெகுளாமை''', '''சினமென்னும் சேர்ந்தாரைக் கொல்லி இனமென்னும்
  ஏமப் புணையைச் சுடும்.''', '''Wrath, the fire that slayeth whose draweth near,
Will burn the helpful \'raft\' of kindred dear.''',
                               '''The fire of anger will burn up even the pleasant raft of friendship.''');
        k[306] = Kural.factory(307, '''அறத்துப்பால்''', '''வெகுளாமை''', '''சினத்தைப் பொருளென்று கொண்டவன் கேடு
  நிலத்தறைந்தான் கைபிழையா தற்று.''', '''The hand that smites the earth unfailing feels the sting;
So perish they who nurse their wrath as noble thing.''',
                               '''Destruction will come upon him who ragards anger as a good thing, as surely as the hand of him who strikes the ground will not fail.''');
        k[307] = Kural.factory(308, '''அறத்துப்பால்''', '''வெகுளாமை''', '''இணர்எரி தோய்வன்ன இன்னா செயினும்
  புணரின் வெகுளாமை நன்று.''', '''Though men should work thee woe, like touch of tongues of fire.
\'Tis well if thou canst save thy soul from burning ire.''',
                               '''Though one commit things against you as painful (to bear) as if a bundle of fire had been thrust upon you, it will be well, to refrain, if possible, from anger.''');
        k[308] = Kural.factory(309, '''அறத்துப்பால்''', '''வெகுளாமை''', '''உள்ளிய தெல்லாம் உடனெய்தும் உள்ளத்தால்
  உள்ளான் வெகுளி எனின்.''', '''If man his soul preserve from wrathful fires,
He gains with that whate\'er his soul desires.''',
                               '''If a man never indulges anger in his heart, he will at once obtain whatever he has thought of.''');
        k[309] = Kural.factory(310, '''அறத்துப்பால்''', '''வெகுளாமை''', '''இறந்தார் இறந்தார் அனையர் சினத்தைத்
  துறந்தார் துறந்தார் துணை.''', '''Men of surpassing wrath are like the men who\'ve passed away;
Who wrath renounce, equals of all-renouncing sages they.''',
                               '''Those, who give way to excessive anger, are no better than dead men; but those, who are freed from it, are equal to those who are freed (from death).''');
        k[310] = Kural.factory(311, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''சிறப்பீனும் செல்வம் பெறினும் பிறர்க்குஇன்னா
  செய்யாமை மாசற்றார் கோள்.''', '''Though ill to neighbour wrought should glorious pride of wealth secure,
No ill to do is fixed decree of men in spirit pure.''',
                               '''It is the determination of the spotless not to cause sorrow to others, although they could (by so causing) obtain the wealth which confers greatness.''');
        k[311] = Kural.factory(312, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''கறுத்துஇன்னா செய்தவக் கண்ணும் மறுத்தின்னா
  செய்யாமை மாசற்றார் கோள்.''', '''Though malice work its worst, planning no ill return, to endure,
And work no ill, is fixed decree of men in spirit pure.''',
                               '''It is the determination of the spotless not to do evil, even in return, to those who have cherished enmity and done them evil.''');
        k[312] = Kural.factory(313, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''செய்யாமல் செற்றார்க்கும் இன்னாத செய்தபின்
  உய்யா விழுமந் தரும்.''', '''Though unprovoked thy soul malicious foes should sting,
Retaliation wrought inevitable woes will bring.''',
                               '''In an ascetic inflict suffering even on those who hate him, when he has not done them any evil, it will afterwards give him irretrievable sorrow.''');
        k[313] = Kural.factory(314, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''இன்னாசெய் தாரை ஒறுத்தல் அவர்நாண
  நன்னயஞ் செய்து விடல்.''', '''To punish wrong, with kindly benefits the doers ply;
Thus shame their souls; but pass the ill unheeded by.''',
                               '''The (proper) punishment to those who have done evil (to you), is to put them to shame by showing them kindness, in return and to forget both the evil and the good done on both sides.''');
        k[314] = Kural.factory(315, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''அறிவினான் ஆகுவ துண்டோ பிறிதின்நோய்
  தந்நோய்போல் போற்றாக் கடை.''', '''From wisdom\'s vaunted lore what doth the learner gain,
If as his own he guard not others\' souls from pain?''',
                               '''What benefit has he derived from his knowledge, who does not endeavour to keep off pain from another as much as from himself ?''');
        k[315] = Kural.factory(316, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''இன்னா எனத்தான் உணர்ந்தவை துன்னாமை
  வேண்டும் பிறன்கண் செயல்.''', '''What his own soul has felt as bitter pain,
From making others feel should man abstain.''',
                               '''Let not a man consent to do those things to another which, he knows, will cause sorrow.''');
        k[316] = Kural.factory(317, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''எனைத்தானும் எஞ்ஞான்றும் யார்க்கும் மனத்தானாம்
  மாணாசெய் யாமை தலை.''', '''To work no wilful woe, in any wise, through all the days,
To any living soul, is virtue\'s highest praise.''',
                               '''It is the chief of all virtues not knowingly to do any person evil, even in the lowest degree, and at any time.''');
        k[317] = Kural.factory(318, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''தன்னுயிர்ககு ஏன்னாமை தானறிவான் என்கொலோ
  மன்னுயிர்க்கு இன்னா செயல்.''', '''Whose soul has felt the bitter smart of wrong, how can
He wrongs inflict on ever-living soul of man?''',
                               '''Why does a man inflict upon other creatures those sufferings, which he has found by experience are sufferings to himself ?''');
        k[318] = Kural.factory(319, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''பிறர்க்கின்னா முற்பகல் செய்யின் தமக்குஇன்னா
  பிற்பகல் தாமே வரும்.''', '''If, ere the noontide, you to others evil do,
Before the eventide will evil visit you.''',
                               '''If a man inflict sorrow upon others in the morning, it will come upon him unsought in the very evening.''');
        k[319] = Kural.factory(320, '''அறத்துப்பால்''', '''இன்னாசெய்யாமை''', '''நோயெல்லாம் நோய்செய்தார் மேலவாம் நோய்செய்யார்
  நோயின்மை வேண்டு பவர்.''', '''O\'er every evil-doer evil broodeth still;
He evil shuns who freedom seeks from ill.''',
                               '''Sorrow will come upon those who cause pain to others; therfore those, who desire to be free from sorrow, give no pain to others.''');
        k[320] = Kural.factory(321, '''அறத்துப்பால்''', '''கொல்லாமை''', '''அறவினை யாதெனின் கொல்லாமை கோறல்
  பிறவினை எல்லாந் தரும்.''', '''What is the work of virtue? \'Not to kill\';
For \'killing\' leads to every work of ill.''',
                               '''Never to destroy life is the sum of all virtuous conduct. The destruction of life leads to every evil.''');
        k[321] = Kural.factory(322, '''அறத்துப்பால்''', '''கொல்லாமை''', '''பகுத்துண்டு பல்லுயிர் ஓம்புதல் நூலோர்
  தொகுத்தவற்றுள் எல்லாந் தலை.''', '''Let those that need partake your meal; guard every-thing that lives;
This the chief and sum of lore that hoarded wisdom gives.''',
                               '''The chief of all (the virtues) which authors have summed up, is the partaking of food that has been shared with others, and the preservation of the mainfold life of other creatures.''');
        k[322] = Kural.factory(323, '''அறத்துப்பால்''', '''கொல்லாமை''', '''ஒன்றாக நல்லது கொல்லாமை மற்றதன்
  பின்சாரப் பொய்யாமை நன்று.''', '''Alone, first of goods things, is \'not to slay\';
The second is, no untrue word to say.''',
                               '''Not to destroy life is an incomparably (great) good next to it in goodness ranks freedom from falsehood.''');
        k[323] = Kural.factory(324, '''அறத்துப்பால்''', '''கொல்லாமை''', '''நல்லாறு எனப்படுவது யாதெனின் யாதொன்றும்
  கொல்லாமை சூழும் நெறி.''', '''You ask, What is the good and perfect way?
\'Tis path of him who studies nought to slay.''',
                               '''Good path is that which considers how it may avoid killing any creature.''');
        k[324] = Kural.factory(325, '''அறத்துப்பால்''', '''கொல்லாமை''', '''நிலைஅஞ்சி நீத்தாருள் எல்லாம் கொலைஅஞ்சிக்
  கொல்லாமை சூழ்வான் தலை.''', '''Of those who \'being\' dread, and all renounce, the chief are they,
Who dreading crime of slaughter, study nought to slay.''',
                               '''Of all those who, fearing the permanence of earthly births, have abandoned desire, he is the chief who, fearing (the guilt of) murder, considers how he may avoid the destruction of life.''');
        k[325] = Kural.factory(326, '''அறத்துப்பால்''', '''கொல்லாமை''', '''கொல்லாமை மேற்கொண் டொழுகுவான் வாழ்நாள்மேல்
  செல்லாது உயிருண்ணுங் கூற்று.''', '''Ev\'n death that life devours, their happy days shall spare,
Who law, \'Thou shall not kill\', uphold with reverent care.''',
                               '''Yama, the destroyer of life, will not attack the life of him, who acts under the determination of never destroying life.''');
        k[326] = Kural.factory(327, '''அறத்துப்பால்''', '''கொல்லாமை''', '''தன்னுயிர் நீப்பினும் செய்யற்க தான்பிறிது
  இன்னுயிர் நீக்கும் வினை.''', '''Though thine own life for that spared life the price must pay,
Take not from aught that lives gift of sweet life away.''',
                               '''Let no one do that which would destroy the life of another, although he should by so doing, lose his own life.''');
        k[327] = Kural.factory(328, '''அறத்துப்பால்''', '''கொல்லாமை''', '''நன்றாகும் ஆக்கம் பெரிதெனினும் சான்றோர்க்குக்
  கொன்றாகும் ஆக்கங் கடை.''', '''Though great the gain of good should seem, the wise
Will any gain by staughter won despise.''',
                               '''The advantage which might flow from destroying life in sacrifice, is dishonourable to the wise (who renounced the world), even although it should be said to be productive of great good.''');
        k[328] = Kural.factory(329, '''அறத்துப்பால்''', '''கொல்லாமை''', '''கொலைவினைய ராகிய மாக்கள் புலைவினையர்
  புன்மை தெரிவா ரகத்து.''', '''Whose trade is \'killing\', always vile they show,
To minds of them who what is vileness know.''',
                               '''Men who destroy life are base men, in the estimation of those who know the nature of meanness.''');
        k[329] = Kural.factory(330, '''அறத்துப்பால்''', '''கொல்லாமை''', '''உயிர் உடம்பின் நீக்கியார் என்ப
  செயிர் உடம்பின் செல்லாத்தீ வாழ்க்கை
  யவர்.''', '''Who lead a loathed life in bodies sorely pained,
Are men, the wise declare, by guilt of slaughter stained.''',
                               '''(The wise) will say that men of diseased bodies, who live in degradation and in poverty, are those who separated the life from the body of animals (in a former birth).''');
        k[330] = Kural.factory(331, '''அறத்துப்பால்''', '''நிலையாமை''', '''நில்லாத வற்றை நிலையின என்றுணரும்
  புல்லறி வாண்மை கடை.''', '''Lowest and meanest lore, that bids men trust secure,
In things that pass away, as things that shall endure!''',
                               '''That ignorance which considers those things to be stable which are not so, is dishonourable (to the wise).''');
        k[331] = Kural.factory(332, '''அறத்துப்பால்''', '''நிலையாமை''', '''கூத்தாட்டு அவைக்குழாத் தற்றே பெருஞ்செல்வம்
  போக்கும் அதுவிளிந் தற்று.''', '''As crowds round dancers fill the hall, is wealth\'s increase;
Its loss, as throngs dispersing, when the dances cease.''',
                               '''The acquisition of wealth is like the gathering together of an assembly for a theatre; its expenditure is like the breaking up of that assembly.''');
        k[332] = Kural.factory(333, '''அறத்துப்பால்''', '''நிலையாமை''', '''அற்கா இயல்பிற்றுச் செல்வம் அதுபெற்றால்
  அற்குப ஆங்கே செயல்.''', '''Unenduring is all wealth; if you wealth enjoy,
Enduring works in working wealth straightway employ.''',
                               '''Wealth is perishable; let those who obtain it immediately practise those (virtues) which are imperishable.''');
        k[333] = Kural.factory(334, '''அறத்துப்பால்''', '''நிலையாமை''', '''நாளென ஒன்றுபோற் காட்டி உயிர்ஈரும்
  வாளது உணர்வார்ப் பெறின்.''', '''As \'day\' it vaunts itself; well understood, \'tis knife\',
That daily cuts away a portion from thy life.''',
                               '''Time, which shows itself (to the ignorant) as if it were something (real) is in the estimation of the wise (only) a saw which cuts down life.''');
        k[334] = Kural.factory(335, '''அறத்துப்பால்''', '''நிலையாமை''', '''நாச்செற்று விக்குள்மேல் வாராமுன் நல்வினை
  மேற்சென்று செய்யப் படும்''', '''Before the tongue lie powerless, \'mid the gasp of gurgling breath,
Arouse thyself, and do good deeds beyond the power of death.''',
                               '''Let virtuous deeds be done quickly, before the biccup comes making the tongue silent.''');
        k[335] = Kural.factory(336, '''அறத்துப்பால்''', '''நிலையாமை''', '''நெருநல் உளனொருவன் இன்றில்லை என்னும்
  பெருமை உடைத்துஇவ் வுலகு.''', '''Existing yesterday, today to nothing hurled!-
Such greatness owns this transitory world.''',
                               '''This world possesses the greatness that one who yesterday was is not today.''');
        k[336] = Kural.factory(337, '''அறத்துப்பால்''', '''நிலையாமை''', '''ஒருபொழுதும் வாழ்வது அறியார் கருதுப
  கோடியும் அல்ல பல.''', '''Who know not if their happy lives shall last the day,
In fancies infinite beguile the hours away!''',
                               '''Innumerable are the thoughts which occupy the mind of (the unwise), who know not that they shall live another moment.''');
        k[337] = Kural.factory(338, '''அறத்துப்பால்''', '''நிலையாமை''', '''குடம்பை தனித்துஒழியப் புள்பறந் தற்றே
  உடம்பொடு உயிரிடை நட்பு.''', '''Birds fly away, and leave the nest deserted bare;
Such is the short-lived friendship soul and body share.''',
                               '''The love of the soul to the body is like (the love of) a bird to its egg which it flies away from and leaves empty.''');
        k[338] = Kural.factory(339, '''அறத்துப்பால்''', '''நிலையாமை''', '''உறங்கு வதுபோலுஞ் சாக்காடு உறங்கி
  விழிப்பது போலும் பிறப்பு.''', '''Death is sinking into slumbers deep;
Birth again is waking out of sleep.''', '''Death is like sleep; birth is like awaking from it.''');
        k[339] = Kural.factory(340, '''அறத்துப்பால்''', '''நிலையாமை''', '''புக்கில் அமைந்தின்று கொல்லோ உடம்பினுள்
  துச்சில் இருந்த உயிர்க்கு.''', '''The soul in fragile shed as lodger courts repose:-
Is it because no home\'s conclusive rest it knows?''',
                               '''It seems as if the soul, which takes a temporary shelter in a body, had not attained a home.''');
        k[340] = Kural.factory(341, '''அறத்துப்பால்''', '''துறவு''', '''யாதனின் யாதனின் நீங்கியான் நோதல்
  அதனின் அதனின் இலன்.''', '''From whatever, aye, whatever, man gets free,
From what, aye, from that, no more of pain hath he!''',
                               '''Whatever thing, a man has renounced, by that thing; he cannot suffer pain.''');
        k[341] = Kural.factory(342, '''அறத்துப்பால்''', '''துறவு''', '''வேண்டின்உண் டாகத் துறக்க துறந்தபின்
  ஈண்டுஇயற் பால பல.''', '''\'Renunciation\' made- ev\'n here true pleasures men acquire;
\'Renounce\' while time is yet, if to those pleasures you aspire.''',
                               '''After a man has renounced (all things), there will still be many things in this world (which he may enjoy); if he should desire them, let him, while it is time abandon. (the world).''');
        k[342] = Kural.factory(343, '''அறத்துப்பால்''', '''துறவு''', '''அடல்வேண்டும் ஐந்தன் புலத்தை விடல்வேண்டும்
  வேண்டிய வெல்லாம் ஒருங்கு.''', '''\'Perceptions of the five\' must all expire;-
Relinquished in its order each desire''',
                               '''Let the five senses be destroyed; and at the same time, let everything be abandoned that (the ascetic) has (formerly) desired.''');
        k[343] = Kural.factory(344, '''அறத்துப்பால்''', '''துறவு''', '''இயல்பாகும் நோன்பிற்கொன்று இன்மை உடைமை
  மயலாகும் மற்றும் பெயர்த்து.''', '''\'Privation absolute\' is penance true;
\'Possession\' brings bewilderment anew.''',
                               '''To be altogether destitute is the proper condition of those who perform austerities; if they possess anything, it will change (their resolution) and bring them back to their confused state.''');
        k[344] = Kural.factory(345, '''அறத்துப்பால்''', '''துறவு''', '''மற்றும் தொடர்ப்பாடு எவன்கொல் பிறப்பறுக்கல்
  உற்றார்க்கு உடம்பும் மிகை.''', '''To those who sev\'rance seek from being\'s varied strife,
Flesh is burthen sore; what then other bonds of life?''',
                               '''What means the addition of other things those who are attempting to cut off (future) births, when even their body is too much (for them).''');
        k[345] = Kural.factory(346, '''அறத்துப்பால்''', '''துறவு''', '''யான் எனது என்னும் செருக்கு
  அறுப்பான் வானோர்க்கு உயர்ந்த உலகம்
  புகும்.''', '''Who kills conceit that utters \'I\' and \'mine\',
Shall enter realms above the powers divine.''',
                               '''He who destroys the pride which says "I", "mine" will enter a world which is difficult even to the Gods to attain.''');
        k[346] = Kural.factory(347, '''அறத்துப்பால்''', '''துறவு''', '''பற்றி விடாஅ இடும்பைகள் பற்றினைப்
  பற்றி விடாஅ தவர்க்கு.''', '''Who cling to things that cling and eager clasp,
Griefs cling to them with unrelaxing grasp.''',
                               '''Sorrows will never let go their hold of those who give not up their hold of desire.''');
        k[347] = Kural.factory(348, '''அறத்துப்பால்''', '''துறவு''', '''தலைப்பட்டார் தீரத் துறந்தார் மயங்கி
  வலைப்பட்டார் மற்றை யவர்.''', '''Who thoroughly \'renounce\' on highest height are set;
The rest bewildered, lie entangled in the net.''',
                               '''Those who have entirely renounced (all things and all desire) have obtained (absorption into God); all others wander in confusion, entangled in the net of (many) births.''');
        k[348] = Kural.factory(349, '''அறத்துப்பால்''', '''துறவு''', '''பற்றற்ற கண்ணே பிறப்பறுக்கும் மற்று
  நிலையாமை காணப் படும்.''', '''When that which clings falls off, severed is being\'s tie;
All else will then be seen as instability.''',
                               '''At the moment in which desire has been abandoned, (other) births will be cut off; when that has not been done, instability will be seen.''');
        k[349] = Kural.factory(350, '''அறத்துப்பால்''', '''துறவு''', '''பற்றுக பற்றற்றான் பற்றினை அப்பற்றைப்
  பற்றுக பற்று விடற்கு.''', '''Cling thou to that which He, to Whom nought clings, hath bid thee cling,
Cling to that bond, to get thee free from every clinging thing.''',
                               '''Desire the desire of Him who is without desire; in order to renounce desire, desire that desire.''');
        k[350] = Kural.factory(351, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''பொருளல்ல வற்றைப் பொருளென்று உணரும்
  மருளானாம் மாணாப் பிறப்பு.''', '''Of things devoid of truth as real things men deem;-
Cause of degraded birth the fond delusive dream!''',
                               '''Inglorious births are produced by the confusion (of mind) which considers those things to be real which are not real.''');
        k[351] = Kural.factory(352, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''இருள்நீங்கி இன்பம் பயக்கும் மருள்நீங்கி
  மாசறு காட்சி யவர்க்கு.''', '''Darkness departs, and rapture springs to men who see,
The mystic vision pure, from all delusion free.''',
                               '''A clear, undimmed vision of things will deliver its possessors from the darkness of future births, and confer the felicity (of heaven).''');
        k[352] = Kural.factory(353, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''ஐயத்தின் நீங்கித் தெளிந்தார்க்கு வையத்தின்
  வானம் நணிய துடைத்து.''', '''When doubts disperse, and mists of error roll
Away, nearer is heav\'n than earth to sage\'s soul.''',
                               '''Heaven is nearer than earth to those men of purified minds who are freed from from doubt.''');
        k[353] = Kural.factory(354, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''ஐயுணர்வு எய்தியக் கண்ணும் பயமின்றே
  மெய்யுணர்வு இல்லா தவர்க்கு.''', '''Five-fold perception gained, what benefits accrue
To them whose spirits lack perception of the true?''',
                               '''Even those who have all the knowledge which can be attained by the five senses, will derive no benefit from it, if they are without a knowledge of the true nature of things.''');
        k[354] = Kural.factory(355, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''எப்பொருள் எத்தன்மைத் தாயினும் அப்பொருள்
  மெய்ப்பொருள் காண்பது அறிவு.''', '''Whatever thing, of whatsoever kind it be,
\'Tis wisdom\'s part in each the very thing to see.''',
                               '''(True) knowledge is the perception concerning every thing of whatever kind, that that thing is the true thing.''');
        k[355] = Kural.factory(356, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''கற்றீண்டு மெய்ப்பொருள் கண்டார் தலைப்படுவர்
  மற்றீண்டு வாரா நெறி.''', '''Who learn, and here the knowledge of the true obtain,
Shall find the path that hither cometh not again.''',
                               '''They, who in this birth have learned to know the True Being, enter the road which returns not into this world.''');
        k[356] = Kural.factory(357, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''ஓர்த்துள்ளம் உள்ளது உணரின் ஒருதலையாப்
  பேர்த்துள்ள வேண்டா பிறப்பு.''', '''The mind that knows with certitude what is, and ponders well,
Its thoughts on birth again to other life need not to dwell.''',
                               '''Let it not be thought that there is another birth for him whose mind having thoroughly considered (all it has been taught) has known the True Being.''');
        k[357] = Kural.factory(358, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''பிறப்பென்னும் பேதைமை நீங்கச் சிறப்பென்னும்
  செம்பொருள் காண்பது அறிவு.''', '''When folly, cause of births, departs; and soul can view
The truth of things, man\'s dignity- \'tis wisdom true.''',
                               '''True knowledge consists in the removal of ignorance; which is (the cause of) births, and the perception of the True Being who is (the bestower of) heaven.''');
        k[358] = Kural.factory(359, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''சார்புணர்ந்து சார்பு கெடஒழுகின் மற்றழித்துச்
  சார்தரா சார்தரு நோய்.''', '''The true \'support\' who knows- rejects \'supports\' he sought before-
Sorrow that clings all destroys, shall cling to him no more.''',
                               '''He who so lives as to know Him who is the support of all things and abandon all desire, will be freed from the evils which would otherwise cleave to him and destroy (his efforts after absorption).''');
        k[359] = Kural.factory(360, '''அறத்துப்பால்''', '''மெய்யுணர்தல்''', '''காமம் வெகுளி மயக்கம் இவ்முன்றன்
  நாமம் கெடக்கெடும் நோய்.''', '''When lust and wrath and error\'s triple tyranny is o\'er,
Their very names for aye extinct, then pain shall be no more.''',
                               '''If the very names of these three things, desire, anger, and confusion of mind, be destroyed, then will also perish the evils (which flow from them).''');
        k[360] = Kural.factory(361, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''அவாஎன்ப எல்லா உயிர்க்கும் எஞ்ஞான்றும்
  தவாஅப் பிறப்பீனும் வித்து.''', '''The wise declare, through all the days, to every living thing.
That ceaseless round of birth from seed of strong desire doth spring.''',
                               '''(The wise) say that the seed, which produces unceasing births, at all times, to all creatures, is desire.''');
        k[361] = Kural.factory(362, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''வேண்டுங்கால் வேண்டும் பிறவாமை மற்றது
  வேண்டாமை வேண்ட வரும்.''', '''If desire you feel, freedom from changing birth require!
\'I\' will come, if you desire to \'scape, set free from all desire.''',
                               '''If anything be desired, freedom from births should be desired; that (freedom from births) will be attained by desiring to be without desire.''');
        k[362] = Kural.factory(363, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''வேண்டாமை அன்ன விழுச்செல்வம் ஈண்டில்லை
  ஆண்டும் அஃதொப்பது இல்.''', '''No glorious wealth is here like freedom from desire;
To bliss like this not even there can soul aspire.''',
                               '''There is in this world no excellence equal to freedom from desire; and even in that world, there is nothing like it.''');
        k[363] = Kural.factory(364, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''தூஉய்மை என்பது அவாவின்மை மற்றது
  வாஅய்மை வேண்ட வரும்.''', '''Desire\'s decease as purity men know;
That, too, from yearning search for truth will grow.''',
                               '''Purity (of mind) consists in freedom from desire; and that (freedom from desire) is the fruit of the love of truth.''');
        k[364] = Kural.factory(365, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''அற்றவர் என்பார் அவாஅற்றார் மற்றையார்
  அற்றாக அற்றது இலர்.''', '''Men freed from bonds of strong desire are free;
None other share such perfect liberty.''',
                               '''They are said to be free (from future birth) who are freed from desire; all others (who, whatever else they may be free from, are not freed from desire) are not thus free.''');
        k[365] = Kural.factory(366, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''அஞ்சுவ தோரும் அறனே ஒருவனை
  வஞ்சிப்ப தோரும் அவா.''', '''Desire each soul beguiles;
True virtue dreads its wiles.''',
                               '''It is the chief duty of (an ascetic) to watch against desire with (jealous) fear; for it has power to deceive (and destroy) him.''');
        k[366] = Kural.factory(367, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''அவாவினை ஆற்ற அறுப்பின் தவாவினை
  தான்வேண்டு மாற்றான் வரும்.''', '''Who thoroughly rids his life of passion-prompted deed,
Deeds of unfailing worth shall do, which, as he plans, succeed.''',
                               '''If a man thoroughly cut off all desire, the deeds, which confer immortality, will come to him, in the path in which he seeks them.''');
        k[367] = Kural.factory(368, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''அவாஇல்லார்க் கில்லாகுந் துன்பம் அஃதுண்டேல்
  தவாஅது மேன்மேல் வரும்.''', '''Affliction is not known where no desires abide;
Where these are, endless rises sorrow\'s tide.''',
                               '''There is no sorrow to those who are without desire; but where that is, (sorrow) will incessantly come, more and more.''');
        k[368] = Kural.factory(369, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''இன்பம் இடையறா தீண்டும் அவாவென்னும்
  துன்பத்துள் துன்பங் கெடின்.''', '''When dies away desire, that woe of woes
Ev\'n here the soul unceasing rapture knows.''',
                               '''Even while in this body, joy will never depart (from the mind, in which) desire, that sorrow of sorrows, has been destroyed.''');
        k[369] = Kural.factory(370, '''அறத்துப்பால்''', '''அவாவறுத்தல்''', '''ஆரா இயற்கை அவாநீப்பின் அந்நிலையே
  பேரா இயற்கை தரும்.''', '''Drive from thy soul desire insatiate;
Straight\'way is gained the moveless blissful state.''',
                               '''The removal of desire, whose nature it is never to be satisfied, will immediately confer a nature that can never be changed.''');
        k[370] = Kural.factory(371, '''அறத்துப்பால்''', '''ஊழ்''', '''ஆகூழால் தோன்றும் அசைவின்மை கைப்பொருள்
  போகூழால் தோன்றும் மடி.''', '''Wealth-giving fate power of unflinching effort brings;
From fate that takes away idle remissness springs.''',
                               '''Perseverance comes from a prosperous fate, and idleness from an adverse fate.''');
        k[371] = Kural.factory(372, '''அறத்துப்பால்''', '''ஊழ்''', '''பேதைப் படுக்கும் இழவூழ் அறிவகற்றும்
  ஆகலூழ் உற்றக் கடை.''', '''The fate that loss ordains makes wise men\'s wisdom foolishness;
The fate that gain bestows with ampler powers will wisdom bless.''',
                               '''An adverse fate produces folly, and a prosperous fate produces enlarged knowledge.''');
        k[372] = Kural.factory(373, '''அறத்துப்பால்''', '''ஊழ்''', '''நுண்ணிய நூல்பல கற்பினும் மற்றுந்தன்
  உண்மை யறிவே மிகும்.''', '''In subtle learning manifold though versed man be,
\'The wisdom, truly his, will gain supremacy.''',
                               '''Although (a man) may study the most polished treatises, the knowledge which fate has decreed to him will still prevail.''');
        k[373] = Kural.factory(374, '''அறத்துப்பால்''', '''ஊழ்''', '''இருவேறு உலகத்து இயற்கை திருவேறு
  தெள்ளிய ராதலும் வேறு.''', '''Two fold the fashion of the world: some live in fortune\'s light;
While other some have souls in wisdom\'s radiance bright.''',
                               '''There are (through fate) two different natures in the world, hence the difference (observable in men) in (their acquisition of) wealth, and in their attainment of knowledge.''');
        k[374] = Kural.factory(375, '''அறத்துப்பால்''', '''ஊழ்''', '''நல்லவை எல்லாஅந் தீயவாம் தீயவும்
  நல்லவாம் செல்வம் செயற்கு.''', '''All things that good appear will oft have ill success;
All evil things prove good for gain of happiness.''',
                               '''In the acquisition of property, every thing favourable becomes unfavourable, and (on the other hand) everything unfavourable becomes favourable, (through the power of fate).''');
        k[375] = Kural.factory(376, '''அறத்துப்பால்''', '''ஊழ்''', '''பரியினும் ஆகாவாம் பாலல்ல உய்த்துச்
  சொரியினும் போகா தம.''', '''Things not your own will yield no good, howe\'er you guard with pain;
Your own, howe\'er you scatter them abroad, will yours remain.''',
                               '''Whatever is not conferred by fate cannot be preserved although it be guarded with most painful care; and that, which fate has made his, cannot be lost, although one should even take it and throw it away.''');
        k[376] = Kural.factory(377, '''அறத்துப்பால்''', '''ஊழ்''', '''வகுத்தான் வகுத்த வகையல்லால் கோடி
  தொகுத்தார்க்கு துய்த்தல் அரிது.''', '''Save as the \'sharer\' shares to each in due degree,
To those who millions store enjoyment scarce can be.''',
                               '''Even those who gather together millions will only enjoy them, as it has been determined by the disposer (of all things).''');
        k[377] = Kural.factory(378, '''அறத்துப்பால்''', '''ஊழ்''', '''துறப்பார்மன் துப்புர வில்லார் உறற்பால
  ஊட்டா கழியு மெனின்.''', '''The destitute with ascetics merit share,
If fate to visit with predestined ills would spare.''',
                               '''The destitute will renounce desire (and become ascetics), if (fate) do not make them suffer the hindrances to which they are liable, and they pass away.''');
        k[378] = Kural.factory(379, '''அறத்துப்பால்''', '''ஊழ்''', '''நன்றாங்கால் நல்லவாக் காண்பவர் அன்றாங்கால்
  அல்லற் படுவ தெவன்.''', '''When good things come, men view them all as gain;
When evils come, why then should they complain?''',
                               '''How is it that those, who are pleased with good fortune, trouble themselves when evil comes, (since both are equally the decree of fate) ?''');
        k[379] = Kural.factory(380, '''அறத்துப்பால்''', '''ஊழ்''', '''ஊழிற் பெருவலி யாவுள மற்றொன்று
  சூழினுந் தான்முந் துறும்.''', '''What powers so great as those of Destiny? Man\'s skill
Some other thing contrives; but fate\'s beforehand still.''',
                               '''What is stronger than fate ? If we think of an expedient (to avert it), it will itself be with us before (the thought).''');
        k[380] = Kural.factory(381, '''பொருட்பால்''', '''இறைமாட்சி''', '''படைகுடி கூழ்அமைச்சு நட்பரண் ஆறும்
  உடையான் அரசருள் ஏறு.''', '''An army, people, wealth, a minister, friends, fort: six things-
Who owns them all, a lion lives amid the kings.''',
                               '''He who possesses these six things, an army, a people, wealth, ministers, friends and a fortress, is a lion among kings.''');
        k[381] = Kural.factory(382, '''பொருட்பால்''', '''இறைமாட்சி''', '''அஞ்சாமை ஈகை அறிவூக்கம் இந்நான்கும்
  எஞ்சாமை வேந்தர்க் கியல்பு.''', '''Courage, a liberal hand, wisdom, and energy: these four
Are qualities a king adorn for evermore.''',
                               '''Never to fail in these four things, fearlessness, liberality, wisdom, and energy, is the kingly character.''');
        k[382] = Kural.factory(383, '''பொருட்பால்''', '''இறைமாட்சி''', '''தூங்காமை கல்வி துணிவுடைமை இம்மூன்றும்
  நீங்கா நிலனான் பவர்க்கு.''', '''A sleepless promptitude, knowledge, decision strong:
These three for aye to rulers of the land belong.''',
                               '''These three things, viz., vigilance, learning, and bravery, should never be wanting in the ruler of a country.''');
        k[383] = Kural.factory(384, '''பொருட்பால்''', '''இறைமாட்சி''', '''அறனிழுக்கா தல்லவை நீக்கி மறனிழுக்கா
  மானம் உடைய தரசு.''', '''Kingship, in virtue failing not, all vice restrains,
In courage failing not, it honour\'s grace maintains.''',
                               '''He is a king who, with manly modesty, swerves not from virtue, and refrains from vice.''');
        k[384] = Kural.factory(385, '''பொருட்பால்''', '''இறைமாட்சி''', '''இயற்றலும் ஈட்டலுங் காத்தலும் காத்த
  வகுத்தலும் வல்ல தரசு.''', '''A king is he who treasure gains, stores up, defends,
And duly for his kingdom\'s weal expends.''',
                               '''He is a king who is able to acquire (wealth), to lay it up, to guard, and to distribute it.''');
        k[385] = Kural.factory(386, '''பொருட்பால்''', '''இறைமாட்சி''', '''காட்சிக் கெளியன் கடுஞ்சொல்லன் அல்லனேல்
  மீக்கூறும் மன்னன் நிலம்''', '''Where king is easy of access, where no harsh word repels,
That land\'s high praises every subject swells.''',
                               '''The whole world will exalt the country of the king who is easy of access, and who is free from harsh language.''');
        k[386] = Kural.factory(387, '''பொருட்பால்''', '''இறைமாட்சி''', '''இன்சொலால் ஈத்தளிக்க வல்லார்க்குத் தன்சொலால்
  தான்கண் டனைத்திவ் வுலகு.''', '''With pleasant speech, who gives and guards with powerful liberal hand,
He sees the world obedient all to his command.''',
                               '''The world will praise and submit itself to the mind of the king who is able to give with affability, and to protect all who come to him.''');
        k[387] = Kural.factory(388, '''பொருட்பால்''', '''இறைமாட்சி''', '''முறைசெய்து காப்பாற்றும் மன்னவன் மக்கட்கு
  இறையென்று வைக்கப் படும்.''', '''Who guards the realm and justice strict maintains,
That king as god o\'er subject people reigns.''',
                               '''That king, will be esteemed a God among men, who performs his own duties, and protects (his subjects).''');
        k[388] = Kural.factory(389, '''பொருட்பால்''', '''இறைமாட்சி''', '''செவிகைப்பச் சொற்பொறுக்கும் பண்புடை வேந்தன்
  கவிகைக்கீழ்த் தங்கும் உலகு.''', '''The king of worth, who can words bitter to his ear endure,
Beneath the shadow of his power the world abides secure.''',
                               '''The whole world will dwell under the umbrella of the king, who can bear words that embitter the ear.''');
        k[389] = Kural.factory(390, '''பொருட்பால்''', '''இறைமாட்சி''', '''கொடையளி செங்கோல் குடியோம்பல் நான்கும்
  உடையானாம் வேந்தர்க் கொளி.''', '''Gifts, grace, right sceptre, care of people\'s weal;
These four a light of dreaded kings reveal.''',
                               '''He is the light of kings who has there four things, beneficence, benevolence, rectitude, and care for his people.''');
        k[390] = Kural.factory(391, '''பொருட்பால்''', '''கல்வி''', '''கற்க கசடறக் கற்பவை கற்றபின்
  நிற்க அதற்குத் தக.''', '''So learn that you may full and faultless learning gain,
Then in obedience meet to lessons learnt remain.''',
                               '''Let a man learn thoroughly whatever he may learn, and let his conduct be worthy of his learning.''');
        k[391] = Kural.factory(392, '''பொருட்பால்''', '''கல்வி''', '''எண்ணென்ப ஏனை எழுத்தென்ப இவ்விரண்டும்
  கண்ணென்ப வாழும் உயிர்க்கு.''', '''The twain that lore of numbers and of letters give
Are eyes, the wise declare, to all on earth that live.''', '''Letters and numbers are the two eyes of man.''');
        k[392] = Kural.factory(393, '''பொருட்பால்''', '''கல்வி''', '''கண்ணுடையர் என்பவர் கற்றோர் முகத்திரண்டு
  புண்ணுடையர் கல்லா தவர்.''', '''Men who learning gain have eyes, men say;
Blockheads\' faces pairs of sores display.''',
                               '''The learned are said to have eyes, but the unlearned have (merely) two sores in their face.''');
        k[393] = Kural.factory(394, '''பொருட்பால்''', '''கல்வி''', '''உவப்பத் தலைக்கூடி உள்ளப் பிரிதல்
  அனைத்தே புலவர் தொழில்.''', '''You meet with joy, with pleasant thought you part;
Such is the learned scholar\'s wonderous art!''',
                               '''It is the part of the learned to give joy to those whom they meet, and on leaving, to make them think (Oh! when shall we meet them again.)''');
        k[394] = Kural.factory(395, '''பொருட்பால்''', '''கல்வி''', '''உடையார்முன் இல்லார்போல் ஏக்கற்றுங் கற்றார்
  கடையரே கல்லா தவர்.''', '''With soul submiss they stand, as paupers front a rich man\'s face;
Yet learned men are first; th\'unlearned stand in lowest place.''',
                               '''The unlearned are inferior to the learned, before whom they stand begging, as the destitute before the wealthy.''');
        k[395] = Kural.factory(396, '''பொருட்பால்''', '''கல்வி''', '''தொட்டனைத் தூறும் மணற்கேணி மாந்தர்க்குக்
  கற்றனைத் தூறும் அறிவு.''', '''In sandy soil, when deep you delve, you reach the springs below;
The more you learn, the freer streams of wisdom flow.''',
                               '''Water will flow from a well in the sand in proportion to the depth to which it is dug, and knowledge will flow from a man in proportion to his learning.''');
        k[396] = Kural.factory(397, '''பொருட்பால்''', '''கல்வி''', '''யாதானும் நாடாமால் ஊராமால் என்னொருவன்
  சாந்துணையுங் கல்லாத வாறு.''', '''The learned make each land their own, in every city find a home;
Who, till they die; learn nought, along what weary ways they roam!''',
                               '''How is it that any one can remain without learning, even to his death, when (to the learned man) every country is his own (country), and every town his own (town) ?''');
        k[397] = Kural.factory(398, '''பொருட்பால்''', '''கல்வி''', '''ஒருமைக்கண் தான்கற்ற கல்வி ஒருவற்கு
  எழுமையும் ஏமாப் புடைத்து.''', '''The man who store of learning gains,
In one, through seven worlds, bliss attains.''',
                               '''The learning, which a man has acquired in one birth, will yield him pleasure during seven births.''');
        k[398] = Kural.factory(399, '''பொருட்பால்''', '''கல்வி''', '''தாமின் புறுவது உலகின் புறக்கண்டு
  காமுறுவர் கற்றறிந் தார்.''', '''Their joy is joy of all the world, they see; thus more
The learners learn to love their cherished lore.''',
                               '''The learned will long (for more learning), when they see that while it gives pleasure to themselves, the world also derives pleasure from it.''');
        k[399] = Kural.factory(400, '''பொருட்பால்''', '''கல்வி''', '''கேடில் விழுச்செல்வம் கல்வி யொருவற்கு
  மாடல்ல மற்றை யவை.''', '''Learning is excellence of wealth that none destroy;
To man nought else affords reality of joy.''',
                               '''Learning is the true imperishable riches; all other things are not riches.''');
        k[400] = Kural.factory(401, '''பொருட்பால்''', '''கல்லாமை''', '''அரங்கின்றி வட்டாடி யற்றே நிரம்பிய
  நூலின்றிக் கோட்டி கொளல்.''', '''Like those at draughts would play without the chequered square,
Men void of ample lore would counsels of the learned share.''',
                               '''To speak in an assembly (of the learned) without fullness of knowledge, is like playing at chess (on a board) without squares.''');
        k[401] = Kural.factory(402, '''பொருட்பால்''', '''கல்லாமை''', '''கல்லாதான் சொற்கா முறுதல் முலையிரண்டும்
  இல்லாதாள் பெண்காமுற் றற்று.''', '''Like those who doat on hoyden\'s undeveloped charms are they,
Of learning void, who eagerly their power of words display.''',
                               '''The desire of the unlearned to speak (in an assembly), is like a woman without breasts desiring (the enjoyment of ) woman-hood.''');
        k[402] = Kural.factory(403, '''பொருட்பால்''', '''கல்லாமை''', '''கல்லா தவரும் நனிநல்லர் கற்றார்முன்
  சொல்லா திருக்கப் பெறின்.''', '''The blockheads, too, may men of worth appear,
If they can keep from speaking where the learned hear!''',
                               '''The unlearned also are very excellent men, if they know how to keep silence before the learned.''');
        k[403] = Kural.factory(404, '''பொருட்பால்''', '''கல்லாமை''', '''கல்லாதான் ஒட்பம் கழியநன் றாயினும்
  கொள்ளார் அறிவுடை யார்.''', '''From blockheads\' lips, when words of wisdom glibly flow,
The wise receive them not, though good they seem to show.''',
                               '''Although the natural knowledge of an unlearned man may be very good, the wise will not accept for true knowledge.''');
        k[404] = Kural.factory(405, '''பொருட்பால்''', '''கல்லாமை''', '''கல்லா ஒருவன் தகைமை தலைப்பெய்து
  சொல்லாடச் சோர்வு படும்.''', '''As worthless shows the worth of man unlearned,
When council meets, by words he speaks discerned.''',
                               '''The self-conceit of an unlearned man will fade away, as soon as he speaks in an assembly (of the learned).''');
        k[405] = Kural.factory(406, '''பொருட்பால்''', '''கல்லாமை''', '''உளரென்னும் மாத்திரையர் அல்லால் பயவாக்
  களரனையர் கல்லா தவர்.''', '''\'They are\': so much is true of men untaught;
But, like a barren field, they yield us nought!''',
                               '''The unlearned are like worthless barren land: all that can be said of them is, that they exist.''');
        k[406] = Kural.factory(407, '''பொருட்பால்''', '''கல்லாமை''', '''நுண்மாண் நுழைபுலம் இல்லான் எழில்நலம்
  மண்மாண் புனைபாவை யற்று.''', '''Who lack the power of subtle, large, and penetrating sense,
Like puppet, decked with ornaments of clay, their beauty\'s vain pretence.''',
                               '''The beauty and goodness of one who is destitute of knowledge by the study of great and exquisite works, is like (the beauty and goodness) of a painted earthen doll.''');
        k[407] = Kural.factory(408, '''பொருட்பால்''', '''கல்லாமை''', '''நல்லார்கண் பட்ட வறுமையின் இன்னாதே
  கல்லார்கண் பட்ட திரு.''', '''To men unlearned, from fortune\'s favour greater-evil springs
Than poverty to men of goodly wisdom brings.''',
                               '''Wealth, gained by the unlearned, will give more sorrow than the poverty which may come upon the learned.''');
        k[408] = Kural.factory(409, '''பொருட்பால்''', '''கல்லாமை''', '''மேற்பிறந்தா ராயினும் கல்லாதார் கீழ்ப்பிறந்தும்
  கற்றார் அனைத்திலர் பாடு.''', '''Lower are men unlearned, though noble be their race,
Than low-born men adorned with learning\'s grace.''',
                               '''The unlearned, though born in a high caste, are not equal in dignity to the learned; though they may have been born in a low caste.''');
        k[409] = Kural.factory(410, '''பொருட்பால்''', '''கல்லாமை''', '''விலங்கொடு மக்கள் அனையர் இலங்குநூல்
  கற்றாரோடு ஏனை யவர்.''', '''Learning\'s irradiating grace who gain,
Others excel, as men the bestial train.''',
                               '''As beasts by the side of men, so are other men by the side of those who are learned in celebrated works.''');
        k[410] = Kural.factory(411, '''பொருட்பால்''', '''கேள்வி''', '''செல்வத்துட் செல்வஞ் செவிச்செல்வம் அச்செல்வம்
  செல்வத்து ளெல்லாந் தலை.''', '''Wealth of wealth is wealth acquired be ear attent;
Wealth mid all wealth supremely excellent.''',
                               '''Wealth (gained) by the ear is wealth of wealth; that wealth is the chief of all wealth.''');
        k[411] = Kural.factory(412, '''பொருட்பால்''', '''கேள்வி''', '''செவுக்குண வில்லாத போழ்து சிறிது
  வயிற்றுக்கும் ஈயப் படும்.''', '''When \'tis no longer time the listening ear to feed
With trifling dole of food supply the body\'s need.''',
                               '''When there is no food for the ear, give a little also to the stomach.''');
        k[412] = Kural.factory(413, '''பொருட்பால்''', '''கேள்வி''', '''செவியுணவிற் கேள்வி யுடையார் அவியுணவின்
  ஆன்றாரோ டொப்பர் நிலத்து.''', '''Who feed their ear with learned teachings rare,
Are like the happy gods oblations rich who share.''',
                               '''Those who in this world enjoy instruction which is the food of the ear, are equal to the Gods, who enjoy the food of the sacrifices.''');
        k[413] = Kural.factory(414, '''பொருட்பால்''', '''கேள்வி''', '''கற்றில னாயினுங் கேட்க அஃதொருவற்கு
  ஒற்கத்தின் ஊற்றாந் துணை.''', '''Though learning none hath he, yet let him hear alway:
In weakness this shall prove a staff and stay.''',
                               '''Although a man be without learning, let him listen (to the teaching of the learned); that will be to him a staff in adversity.''');
        k[414] = Kural.factory(415, '''பொருட்பால்''', '''கேள்வி''', '''இழுக்கல் உடையுழி ஊற்றுக்கோல் அற்றே
  ஒழுக்க முடையார்வாய்ச் சொல்.''', '''Like staff in hand of him in slippery ground who strays
Are words from mouth of those who walk in righteous ways.''',
                               '''The words of the good are like a staff in a slippery place.''');
        k[415] = Kural.factory(416, '''பொருட்பால்''', '''கேள்வி''', '''எனைத்தானும் நல்லவை கேட்க அனைத்தானும்
  ஆன்ற பெருமை தரும்.''', '''Let each man good things learn, for e\'en as he
Shall learn, he gains increase of perfect dignity.''',
                               '''Let a man listen, never so little, to good (instruction), even that will bring him great dignity.''');
        k[416] = Kural.factory(417, '''பொருட்பால்''', '''கேள்வி''', '''பிழைத்துணர்ந்தும் பேதைமை சொல்லா ரிழைத்துணர்ந்
  தீண்டிய கேள்வி யவர்.''', '''Not e\'en through inadvertence speak they foolish word,
With clear discerning mind who\'ve learning\'s ample lessons heard.''',
                               '''Not even when they have imperfectly understood (a matter), will those men speak foolishly, who have profoundly studied and diligently listened (to instruction).''');
        k[417] = Kural.factory(418, '''பொருட்பால்''', '''கேள்வி''', '''கேட்பினுங் கேளாத் தகையவே கேள்வியால்
  தோட்கப் படாத செவி.''', '''Where teaching hath not oped the learner\'s ear,
The man may listen, but he scarce can hear.''',
                               '''The ear which has not been bored by instruction, although it hears, is deaf.''');
        k[418] = Kural.factory(419, '''பொருட்பால்''', '''கேள்வி''', '''நுணங்கிய கேள்விய ரல்லார் வணங்கிய
  வாயின ராதல் அரிது.''', '''\'Tis hard for mouth to utter gentle, modest word,
When ears discourse of lore refined have never heard.''',
                               '''It is a rare thing to find modesty, a reverend mouth- with those who have not received choice instruction.''');
        k[419] = Kural.factory(420, '''பொருட்பால்''', '''கேள்வி''', '''செவியிற் சுவையுணரா வாயுணர்வின் மாக்கள்
  அவியினும் வாழினும் என்.''', '''His mouth can taste, but ear no taste of joy can give!
What matter if he die, or prosperous live?''',
                               '''What does it matter whether those men live or die, who can judge of tastes by the mouth, and not by the ear ?''');
        k[420] = Kural.factory(421, '''பொருட்பால்''', '''அறிவுடைமை''', '''அறிவற்றங் காக்குங் கருவி செறுவார்க்கும்
  உள்ளழிக்க லாகா அரண்.''', '''True wisdom wards off woes, A circling fortress high;
Its inner strength man\'s eager foes Unshaken will defy.''',
                               '''Wisdom is a weapon to ward off destruction; it is an inner fortress which enemies cannot destroy.''');
        k[421] = Kural.factory(422, '''பொருட்பால்''', '''அறிவுடைமை''', '''சென்ற இடத்தால் செலவிடா தீதொரீஇ
  நன்றின்பால் உய்ப்ப தறிவு.''', '''Wisdom restrains, nor suffers mind to wander where it would;
From every evil calls it back, and guides in way of good.''',
                               '''Not to permit the mind to go where it lists, to keep it from evil, and to employ it in good, this is wisdom.''');
        k[422] = Kural.factory(423, '''பொருட்பால்''', '''அறிவுடைமை''', '''எப்பொருள் யார்யார்வாய்க் கேட்பினும் அப்பொருள்
  மெய்ப்பொருள் காண்ப தறிவு.''', '''Though things diverse from divers sages\' lips we learn,
\'Tis wisdom\'s part in each the true thing to discern.''',
                               '''To discern the truth in every thing, by whomsoever spoken, is wisdom.''');
        k[423] = Kural.factory(424, '''பொருட்பால்''', '''அறிவுடைமை''', '''எண்பொருள வாகச் செலச்சொல்லித் தான்பிறர்வாய்
  நுண்பொருள் காண்ப தறிவு.''', '''Wisdom hath use of lucid speech, words that acceptance win,
And subtle sense of other men\'s discourse takes in.''',
                               '''To speak so as that the meaning may easily enter the mind of the hearer, and to discern the subtlest thought which may lie hidden in the words of others, this is wisdom.''');
        k[424] = Kural.factory(425, '''பொருட்பால்''', '''அறிவுடைமை''', '''உலகம் தழீஇய தொட்பம் மலர்தலும்
  கூம்பலும் இல்ல தறிவு.''', '''Wisdom embraces frank the world, to no caprice exposed;
Unlike the lotus flower, now opened wide, now petals strictly closed.''',
                               '''To secure the friendship of the great is true wisdom; it is (also) wisdom to keep (that friendship unchanged, and) not opening and closing (like the lotus flower).''');
        k[425] = Kural.factory(426, '''பொருட்பால்''', '''அறிவுடைமை''', '''எவ்வ துறைவது உலகம் உலகத்தோடு
  அவ்வ துறைவ தறிவு.''', '''As dwells the world, so with the world to dwell
In harmony- this is to wisely live and well.''', '''To live as the world lives, is wisdom.''');
        k[426] = Kural.factory(427, '''பொருட்பால்''', '''அறிவுடைமை''', '''அறிவுடையார் ஆவ தறிவார் அறிவிலார்
  அஃதறி கல்லா தவர்.''', '''The wise discern, the foolish fail to see,
And minds prepare for things about to be.''',
                               '''The wise are those who know beforehand what will happen; those who do not know this are the unwise.''');
        k[427] = Kural.factory(428, '''பொருட்பால்''', '''அறிவுடைமை''', '''அஞ்சுவ தஞ்சாமை பேதைமை அஞ்சுவது
  அஞ்சல் அறிவார் தொழில்.''', '''Folly meets fearful ills with fearless heart;
To fear where cause of fear exists is wisdom\'s part.''',
                               '''Not to fear what ought to be feared, is folly; it is the work of the wise to fear what should be feared.''');
        k[428] = Kural.factory(429, '''பொருட்பால்''', '''அறிவுடைமை''', '''எதிரதாக் காக்கும் அறிவினார்க் கில்லை
  அதிர வருவதோர் நோய்.''', '''The wise with watchful soul who coming ills foresee;
From coming evil\'s dreaded shock are free.''',
                               '''No terrifying calamity will happen to the wise, who (foresee) and guard against coming evils.''');
        k[429] = Kural.factory(430, '''பொருட்பால்''', '''அறிவுடைமை''', '''அறிவுடையார் எல்லா முடையார் அறிவிலார்
  என்னுடைய ரேனும் இலர்.''', '''The wise is rich, with ev\'ry blessing blest;
The fool is poor, of everything possessed.''',
                               '''Those who possess wisdom, possess every thing; those who have not wisdom, whatever they may possess, have nothing.''');
        k[430] = Kural.factory(431, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''செருக்குஞ் சினமும் சிறுமையும் இல்லார்
  பெருக்கம் பெருமித நீர்த்து.''', '''Who arrogance, and wrath, and littleness of low desire restrain,
To sure increase of lofty dignity attain.''',
                               '''Truly great is the excellence of those (kings) who are free from pride, anger, and lust.''');
        k[431] = Kural.factory(432, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''இவறலும் மாண்பிறந்த மானமும் மாணா
  உவகையும் ஏதம் இறைக்கு.''', '''A niggard hand, o\'erweening self-regard, and mirth
Unseemly, bring disgrace to men of kingly brith.''',
                               '''Avarice, undignified pride, and low pleasures are faults in a king.''');
        k[432] = Kural.factory(433, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''தினைத்துணையாங் குற்றம் வரினும் பனைத்துணையாக்
  கொள்வர் பழிநாணு வார்.''', '''Though small as millet-seed the fault men deem;
As palm tree vast to those who fear disgrace \'twill seem.''',
                               '''Those who fear guilt, if they commit a fault small as a millet seed, will consider it to be as large as a palmyra tree.''');
        k[433] = Kural.factory(434, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''குற்றமே காக்க பொருளாகக் குற்றமே
  அற்றந் த்ரூஉம் பகை.''', '''Freedom from faults is wealth; watch heedfully
\'Gainst these, for fault is fatal enmity.''',
                               '''Guard against faults as a matter (of great consequence; for) faults are a deadly enemy.''');
        k[434] = Kural.factory(435, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''வருமுன்னர்க் காவாதான் வாழ்க்கை எரிமுன்னர்
  வைத்தூறு போலக் கெடும்.''', '''His joy who guards not \'gainst the coming evil day,
Like straw before the fire shall swift consume away.''',
                               '''The prosperity of him who does not timely guard against faults, will perish like straw before fire.''');
        k[435] = Kural.factory(436, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''தன்குற்றம் நீக்கிப் பிறர்குற்றங் காண்கிற்பின்
  என்குற்ற மாகும் இறைக்கு.''', '''Faultless the king who first his own faults cures, and then
Permits himself to scan faults of other men.''',
                               '''What fault will remain in the king who has put away his own evils, and looks after the evils of others.''');
        k[436] = Kural.factory(437, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''செயற்பால செய்யா திவறியான் செல்வம்
  உயற்பால தன்றிக் கெடும்.''', '''Who leaves undone what should be done, with niggard mind,
His wealth shall perish, leaving not a wrack behind.''',
                               '''The wealth of the avaricious man, who does not expend it for the purposes for which he ought to expend it will waste away and not continue.''');
        k[437] = Kural.factory(438, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''பற்றுள்ளம் என்னும் இவறன்மை எற்றுள்ளும்
  எண்ணப் படுவதொன் றன்று.''', '''The greed of soul that avarice men call,
When faults are summed, is worst of all.''',
                               '''Griping avarice is not to be reckoned as one among other faults; (it stands alone - greater than all).''');
        k[438] = Kural.factory(439, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''வியவற்க எஞ்ஞான்றும் தன்னை நயவற்க
  நன்றி பயவா வினை.''', '''Never indulge in self-complaisant mood,
Nor deed desire that yields no gain of good.''',
                               '''Let no (one) praise himself, at any time; let him not desire to do useless things.''');
        k[439] = Kural.factory(440, '''பொருட்பால்''', '''குற்றங்கடிதல்''', '''காதல காதல் அறியாமை உய்க்கிற்பின்
  ஏதில ஏதிலார் நூல்.''', '''If, to your foes unknown, you cherish what you love,
Counsels of men who wish you harm will harmless prove.''',
                               '''If (a king) enjoys, privately the things which he desires, the designs of his enemies will be useless.''');
        k[440] = Kural.factory(441, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''அறனறிந்து மூத்த அறிவுடையார் கேண்மை
  திறனறிந்து தேர்ந்து கொளல்.''', '''As friends the men who virtue know, and riper wisdom share,
Their worth weighed well, the king should choose with care.''',
                               '''Let (a king) ponder well its value, and secure the friendship of men of virtue and of mature knowledge.''');
        k[441] = Kural.factory(442, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''உற்றநோய் நீக்கி உறாஅமை முற்காக்கும்
  பெற்றியார்ப் பேணிக் கொளல்.''', '''Cherish the all-accomplished men as friends,
Whose skill the present ill removes, from coming ill defends.''',
                               '''Let (a king) procure and kindly care for men who can overcome difficulties when they occur, and guard against them before they happen.''');
        k[442] = Kural.factory(443, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''அரியவற்று ளெல்லாம் அரிதே பெரியாரைப்
  பேணித் தமராக் கொளல்.''', '''To cherish men of mighty soul, and make them all their own,
Of kingly treasures rare, as rarest gift is known.''',
                               '''To cherish great men and make them his own, is the most difficult of all difficult things.''');
        k[443] = Kural.factory(444, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''தம்மிற் பெரியார் தமரா ஒழுகுதல்
  வன்மையு ளெல்லாந் தலை.''', '''To live with men of greatness that their own excels,
As cherished friends, is greatest power that with a monarch dwells.''',
                               '''So to act as to make those men, his own, who are greater than himself is of all powers the highest.''');
        k[444] = Kural.factory(445, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''சூழ்வார்கண் ணாக ஒழுகலான் மன்னவன்
  சூழ்வாரைக் சூழ்ந்து கொளல்.''', '''The king, since counsellors are monarch\'s eyes,
Should counsellors select with counsel wise.''',
                               '''As a king must use his ministers as eyes (in managing his kingdom), let him well examine their character and qualifications before he engages them.''');
        k[445] = Kural.factory(446, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''தக்கா ரினத்தனாய்த் தானொழுக வல்லானைச்
  செற்றார் செயக்கிடந்த தில்.''', '''The king, who knows to live with worthy men allied,
Has nought to fear from any foeman\'s pride.''',
                               '''There will be nothing left for enemies to do, against him who has the power of acting (so as to secure) the fellowship of worthy men.''');
        k[446] = Kural.factory(447, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''இடிக்குந் துணையாரை யாள்வரை யாரே
  கெடுக்குந் தகைமை யவர்.''', '''What power can work his fall, who faithful ministers
Employs, that thunder out reproaches when he errs.''',
                               '''Who are great enough to destroy him who has servants that have power to rebuke him ?''');
        k[447] = Kural.factory(448, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''இடிப்பாரை இல்லாத ஏமரா மன்னன்
  கெடுப்பா ரிலானுங் கெடும்.''', '''The king with none to censure him, bereft of safeguards all,
Though none his ruin work, shall surely ruined fall.''',
                               '''The king, who is without the guard of men who can rebuke him, will perish, even though there be no one to destroy him.''');
        k[448] = Kural.factory(449, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''முதலிலார்க ஊதிய மில்லை மதலையாஞ்
  சார்பிலார்க் கில்லை நிலை.''', '''Who owns no principal, can have no gain of usury;
Who lacks support of friends, knows no stability.''',
                               '''There can be no gain to those who have no capital; and in like manner there can be no permanence to those who are without the support of adherents.''');
        k[449] = Kural.factory(450, '''பொருட்பால்''', '''பெரியாரைத் துணைக்கோடல்''', '''பல்லார் பகைகொளலிற் பத்தடுத்த தீமைத்தே
  நல்லார் தொடர்கை விடல்.''', '''Than hate of many foes incurred, works greater woe
Ten-fold, of worthy men the friendship to forego.''',
                               '''It is tenfold more injurious to abandon the friendship of the good, than to incur the hatred of the many.''');
        k[450] = Kural.factory(451, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''சிற்றினம் அஞ்சும் பெருமை சிறுமைதான்
  சுற்றமாச் சூழ்ந்து விடும்.''', '''The great of soul will mean association fear;
The mean of soul regard mean men as kinsmen dear.''',
                               '''(True) greatness fears the society of the base; it is only the low - minded who will regard them as friends.''');
        k[451] = Kural.factory(452, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''நிலத்தியல்பால் நீர்திரிந் தற்றாகும் மாந்தர்க்கு
  இனத்தியல்ப தாகும் அறிவு.''', '''The waters\' virtues change with soil through which they flow;
As man\'s companionship so will his wisdom show.''',
                               '''As water changes (its nature), from the nature of the soil (in which it flows), so will the character of men resemble that of their associates.''');
        k[452] = Kural.factory(453, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனத்தானாம் மாந்தர்க் குணர்ச்சி இனத்தானாம்
  இன்னான் எனப்படுஞ் சொல்.''', '''Perceptions manifold in men are of the mind alone;
The value of the man by his companionship is known.''',
                               '''The power of knowing is from the mind; (but) his character is from that of his associates.''');
        k[453] = Kural.factory(454, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனத்து ளதுபோலக் காட்டி ஒருவற்கு
  இனத்துள தாகும் அறிவு.''', '''Man\'s wisdom seems the offspring of his mind;
\'Tis outcome of companionship we find.''',
                               '''Wisdom appears to rest in the mind, but it really exists to a man in his companions.''');
        k[454] = Kural.factory(455, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனந்தூய்மை செய்வினை தூய்மை இரண்டும்
  இனந்தூய்மை தூவா வரும்.''', '''Both purity of mind, and purity of action clear,
Leaning no staff of pure companionship, to man draw near.''',
                               '''Chaste company is the staff on which come, these two things, viz, purity of mind and purity of conduct.''');
        k[455] = Kural.factory(456, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனந்தூயார்க் கெச்சம்நன் றாகும் இனந்தூயார்க்கு
  இல்லைநன் றாகா வினை.''', '''From true pure-minded men a virtuous race proceeds;
To men of pure companionship belong no evil deeds.''',
                               '''To the pure-minded there will be a good posterity. By those whose associates are pure, no deeds will be done that are not good.''');
        k[456] = Kural.factory(457, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனநலம் மன்னுயிர்க் காக்கம் இனநலம்
  எல்லாப் புகழும் தரும்.''', '''Goodness of mind to lives of men increaseth gain;
And good companionship doth all of praise obtain.''',
                               '''Goodness of mind will give wealth, and good society will bring with it all praise, to men.''');
        k[457] = Kural.factory(458, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனநலம் நன்குடைய ராயினும் சான்றோர்க்கு
  இனநலம் ஏமாப் புடைத்து.''', '''To perfect men, though minds right good belong,
Yet good companionship is confirmation strong.''',
                               '''Although they may have great (natural) goodness of mind, yet good society will tend to strengthen it.''');
        k[458] = Kural.factory(459, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''மனநலத்தின் ஆகும் மறுமைமற் றஃதும்
  இனநலத்தின் ஏமாப் புடைத்து.''', '''Although to mental goodness joys of other life belong,
Yet good companionship is confirmation strong.''',
                               '''Future bliss is (the result) of goodness of mind; and even this acquires strength from the society of the good.''');
        k[459] = Kural.factory(460, '''பொருட்பால்''', '''சிற்றினஞ்சேராமை''', '''நல்லினத்தி னூங்குந் துணையில்லை தீயினத்தின்
  அல்லற் படுப்பதூஉம் இல்.''', '''Than good companionship no surer help we know;
Than bad companionship nought causes direr woe.''',
                               '''There is no greater help than the company of the good; there is no greater source of sorrow than the company of the wicked.''');
        k[460] = Kural.factory(461, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''அழிவதூஉம் ஆவதூஉம் ஆகி வழிபயக்கும்
  ஊதியமும் சூழ்ந்து செயல்.''', '''Expenditure, return, and profit of the deed
In time to come; weigh these- than to the act proceed.''',
                               '''Let a man reflect on what will be lost, what will be acquired and (from these) what will be his ultimate gain, and (then, let him) act.''');
        k[461] = Kural.factory(462, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''தெரிந்த இனத்தொடு தேர்ந்தெண்ணிச் செய்வார்க்கு
  அரும்பொருள் யாதொன்றும் இல்.''', '''With chosen friends deliberate; next use the private thought;
Then act. By those who thus proceed all works with ease are wrought.''',
                               '''There is nothing too difficult to (be attained by) those who, before they act, reflect well themselves, and thoroughly consider (the matter) with chosen friends.''');
        k[462] = Kural.factory(463, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''ஆக்கம் கருதி முதலிழக்கும் செய்வினை
  ஊக்கார் அறிவுடை யார்.''', '''To risk one\'s all and lose, aiming at added gain,
Is rash affair, from which the wise abstain.''',
                               '''Wise men will not, in the hopes of profit, undertake works that will consume their principal.''');
        k[463] = Kural.factory(464, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''தெளிவி லதனைத் தொடங்கார் இளிவென்னும்
  ஏதப்பாடு அஞ்சு பவர்.''', '''A work of which the issue is not clear,
Begin not they reproachful scorn who fear.''',
                               '''Those who fear reproach will not commence anything which has not been (thoroughly considered) and made clear to them.''');
        k[464] = Kural.factory(465, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''வகையறச் சூழா தெழுதல் பகைவரைப்
  பாத்திப் படுப்பதோ ராறு.''', '''With plans not well matured to rise against your foe,
Is way to plant him out where he is sure to grow!''',
                               '''One way to promote the prosperity of an enemy, is (for a king) to set out (to war) without having thoroughly weighed his ability (to cope with its chances).''');
        k[465] = Kural.factory(466, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''செய்தக்க அல்ல செயக்கெடும் செய்தக்க
  செய்யாமை யானுங் கெடும்.''', '''\'Tis ruin if man do an unbefitting thing;
Fit things to leave undone will equal ruin bring.''',
                               '''He will perish who does not what is not fit to do; and he also will perish who does not do what it is fit to do.''');
        k[466] = Kural.factory(467, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''எண்ணித் துணிக கருமம் துணிந்தபின்
  எண்ணுவம் என்பது இழுக்கு.''', '''Think, and then dare the deed! Who cry,
\'Deed dared, we\'ll think,\' disgraced shall be.''',
                               '''Consider, and then undertake a matter; after having undertaken it, to say "We will consider," is folly.''');
        k[467] = Kural.factory(468, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''ஆற்றின் வருந்தா வருத்தம் பலர்நின்று
  போற்றினும் பொத்துப் படும்.''', '''On no right system if man toil and strive,
Though many men assist, no work can thrive.''',
                               '''The work, which is not done by suitable methods, will fail though many stand to uphold it.''');
        k[468] = Kural.factory(469, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''நன்றாற்ற லுள்ளுந் தவுறுண்டு அவரவர்
  பண்பறிந் தாற்றாக் கடை.''', '''Though well the work be done, yet one mistake is made,
To habitudes of various men when no regard is paid.''',
                               '''There are failures even in acting well, when it is done without knowing the various dispositions of men.''');
        k[469] = Kural.factory(470, '''பொருட்பால்''', '''தெரிந்துசெயல்வகை''', '''எள்ளாத எண்ணிச் செயல்வேண்டும் தம்மோடு
  கொள்ளாத கொள்ளாது உலகு.''', '''Plan and perform no work that others may despise;
What misbeseems a king the world will not approve as wise.''',
                               '''Let a man reflect, and do things which bring no reproach; the world will not approve, with him, of things which do not become of his position to adopt.''');
        k[470] = Kural.factory(471, '''பொருட்பால்''', '''வலியறிதல்''', '''வினைவலியும் தன்வலியும் மாற்றான் வலியும்
  துணைவலியும் தூக்கிச் செயல்.''', '''The force the strife demands, the force he owns, the force of foes,
The force of friends; these should he weigh ere to the war he goes.''',
                               '''Let (one) weigh well the strength of the deed (he purposes to do), his own strength, the strength of his enemy, and the strength of the allies (of both), and then let him act.''');
        k[471] = Kural.factory(472, '''பொருட்பால்''', '''வலியறிதல்''', '''ஒல்வ தறிவது அறிந்ததன் கண்தங்கிச்
  செல்வார்க்குச் செல்லாதது இல்.''', '''Who know what can be wrought, with knowledge of the means, on this,
Their mind firm set, go forth, nought goes with them amiss.''',
                               '''There is nothing which may not be accomplished by those who, before they attack (an enemy), make themselves acquainted with their own ability, and with whatever else is (needful) to be known, and apply themselves wholly to their object.''');
        k[472] = Kural.factory(473, '''பொருட்பால்''', '''வலியறிதல்''', '''உடைத்தம் வலியறியார் ஊக்கத்தின் ஊக்கி
  இடைக்கண் முரிந்தார் பலர்.''', '''Ill-deeming of their proper powers, have many monarchs striven,
And midmost of unequal conflict fallen asunder riven.''',
                               '''There are many who, ignorant of their (want of) power (to meet it), have haughtily set out to war, and broken down in the midst of it.''');
        k[473] = Kural.factory(474, '''பொருட்பால்''', '''வலியறிதல்''', '''அமைந்தாங் கொழுகான் அளவறியான் தன்னை
  வியந்தான் விரைந்து கெடும்.''', '''Who not agrees with those around, no moderation knows,
In self-applause indulging, swift to ruin goes.''',
                               '''He will quickly perish who, ignorant of his own resources flatters himself of his greatness, and does not live in peace with his neighbours.''');
        k[474] = Kural.factory(475, '''பொருட்பால்''', '''வலியறிதல்''', '''பீலிபெய் சாகாடும் அச்சிறும் அப்பண்டஞ்
  சால மிகுத்துப் பெயின்.''', '''With peacock feathers light, you load the wain;
Yet, heaped too high, the axle snaps in twain.''',
                               '''The axle tree of a bandy, loaded only with peacocks\' feathers will break, if it be greatly overloaded.''');
        k[475] = Kural.factory(476, '''பொருட்பால்''', '''வலியறிதல்''', '''நுனிக்கொம்பர் ஏறினார் அஃதிறந் தூக்கின்
  உயிர்க்கிறுதி ஆகி விடும்.''', '''Who daring climbs, and would himself upraise
Beyond the branch\'s tip, with life the forfeit pays.''',
                               '''There will be an end to the life of him who, having climbed out to the end of a branch, ventures to go further.''');
        k[476] = Kural.factory(477, '''பொருட்பால்''', '''வலியறிதல்''', '''ஆற்றின் அறவறிந்து ஈக அதுபொருள்
  போற்றி வழங்கு நெறி.''', '''With knowledge of the measure due, as virtue bids you give!
That is the way to guard your wealth, and seemly live.''',
                               '''Let a man know the measure of his ability (to give), and let him give accordingly; such giving is the way to preserve his property.''');
        k[477] = Kural.factory(478, '''பொருட்பால்''', '''வலியறிதல்''', '''ஆகாறு அளவிட்டி தாயினுங் கேடில்லை
  போகாறு அகலாக் கடை.''', '''Incomings may be scant; but yet, no failure there,
If in expenditure you rightly learn to spare.''',
                               '''Even though the income (of a king) be small, it will not cause his (ruin), if his outgoings be not larger than his income.''');
        k[478] = Kural.factory(479, '''பொருட்பால்''', '''வலியறிதல்''', '''அளவற஧ந்து வாழாதான் வாழ்க்கை உளபோல
  இல்லாகித் தோன்றாக் கெடும்.''', '''Who prosperous lives and of enjoyment knows no bound,
His seeming wealth, departing, nowhere shall be found.''',
                               '''The prosperity of him who lives without knowing the measure (of his property), will perish, even while it seems to continue.''');
        k[479] = Kural.factory(480, '''பொருட்பால்''', '''வலியறிதல்''', '''உளவரை தூக்காத ஒப்புர வாண்மை
  வளவரை வல்லைக் கெடும்.''', '''Beneficence that measures not its bound of means,
Will swiftly bring to nought the wealth on which it leans.''',
                               '''The measure of his wealth will quickly perish, whose liberality weighs not the measure of his property.''');
        k[480] = Kural.factory(481, '''பொருட்பால்''', '''காலமறிதல்''', '''பகல்வெல்லும் கூகையைக் காக்கை இகல்வெல்லும்
  வேந்தர்க்கு வேண்டும் பொழுது.''', '''A crow will conquer owl in broad daylight;
The king that foes would crush, needs fitting time to fight.''',
                               '''A crow will overcome an owl in the day time; so the king who would conquer his enemy must have (a suitable) time.''');
        k[481] = Kural.factory(482, '''பொருட்பால்''', '''காலமறிதல்''', '''பருவத்தோடு ஒட்ட ஒழுகல் திருவினைத்
  தீராமை ஆர்க்குங் கயிறு.''', '''The bond binds fortune fast is ordered effort made,
Strictly observant still of favouring season\'s aid.''',
                               '''Acting at the right season, is a cord that will immoveably bind success (to a king).''');
        k[482] = Kural.factory(483, '''பொருட்பால்''', '''காலமறிதல்''', '''அருவினை யென்ப உளவோ கருவியான்
  காலம் அற஧ந்து செயின்.''', '''Can any work be hard in very fact,
If men use fitting means in timely act?''',
                               '''Is there anything difficult for him to do, who acts, with (the right) instruments at the right time ?''');
        k[483] = Kural.factory(484, '''பொருட்பால்''', '''காலமறிதல்''', '''ஞாலம் கருதினுங் கைகூடுங் காலம்
  கருதி இடத்தாற் செயின்.''', '''The pendant world\'s dominion may be won,
In fitting time and place by action done.''',
                               '''Though (a man) should meditate (the conquest of) the world, he may accomplish it if he acts in the right time, and at the right place.''');
        k[484] = Kural.factory(485, '''பொருட்பால்''', '''காலமறிதல்''', '''காலம் கருதி இருப்பர் கலங்காது
  ஞாலம் கருது பவர்.''', '''Who think the pendant world itself to subjugate,
With mind unruffled for the fitting time must wait.''',
                               '''They who thoughtfully consider and wait for the (right) time (for action), may successfully meditate (the conquest of) the world.''');
        k[485] = Kural.factory(486, '''பொருட்பால்''', '''காலமறிதல்''', '''ஊக்க முடையான் ஒடுக்கம் பொருதகர்
  தாக்கற்குப் பேருந் தகைத்து.''', '''The men of mighty power their hidden energies repress,
As fighting ram recoils to rush on foe with heavier stress.''',
                               '''The self-restraint of the energetic (while waiting for a suitable opportunity), is like the drawing back of a fighting-ram in order to butt.''');
        k[486] = Kural.factory(487, '''பொருட்பால்''', '''காலமறிதல்''', '''பொள்ளென ஆங்கே புறம்வேரார் காலம்பார்த்து
  உள்வேர்ப்பர் ஒள்ளி யவர்.''', '''The glorious once of wrath enkindled make no outward show,
At once; they bide their time, while hidden fires within them glow.''',
                               '''The wise will not immediately and hastily shew out their anger; they will watch their time, and restrain it within.''');
        k[487] = Kural.factory(488, '''பொருட்பால்''', '''காலமறிதல்''', '''செறுநரைக் காணின் சுமக்க இறுவரை
  காணின் கிழக்காம் தலை.''', '''If foes\' detested form they see, with patience let them bear;
When fateful hour at last they spy,- the head lies there.''',
                               '''If one meets his enemy, let him show him all respect, until the time for his destruction is come; when that is come, his head will be easily brought low.''');
        k[488] = Kural.factory(489, '''பொருட்பால்''', '''காலமறிதல்''', '''எய்தற் கரியது இயைந்தக்கால் அந்நிலையே
  செய்தற் கரிய செயல்.''', '''When hardest gain of opportunity at last is won,
With promptitude let hardest deed be done.''',
                               '''If a rare opportunity occurs, while it lasts, let a man do that which is rarely to be accomplished (but for such an opportunity).''');
        k[489] = Kural.factory(490, '''பொருட்பால்''', '''காலமறிதல்''', '''கொக்கொக்க கூம்பும் பருவத்து மற்றதன்
  குத்தொக்க சீர்த்த இடத்து.''', '''As heron stands with folded wing, so wait in waiting hour;
As heron snaps its prey, when fortune smiles, put forth your power.''',
                               '''At the time when one should use self-control, let him restrain himself like a heron; and, let him like it, strike, when there is a favourable opportunity.''');
        k[490] = Kural.factory(491, '''பொருட்பால்''', '''இடனறிதல்''', '''தொடங்கற்க எவ்வினையும் எள்ளற்க முற்றும்
  இடங்கண்ட பின்அல் லது.''', '''Begin no work of war, depise no foe,
Till place where you can wholly circumvent you know.''',
                               '''Let not (a king) despise (an enemy), nor undertake any thing (against him), until he has obtained (a suitable) place for besieging him.''');
        k[491] = Kural.factory(492, '''பொருட்பால்''', '''இடனறிதல்''', '''முரண்சேர்ந்த மொய்ம்பி னவர்க்கும் அரண்சேர்ந்தாம்
  ஆக்கம் பலவுந் தரும்.''', '''Though skill in war combine with courage tried on battle-field,
The added gain of fort doth great advantage yield.''',
                               '''Even to those who are men of power and expedients, an attack in connection with a fortification will yield many advantages.''');
        k[492] = Kural.factory(493, '''பொருட்பால்''', '''இடனறிதல்''', '''ஆற்றாரும் ஆற்றி அடுப இடனறிந்து
  போற்றார்கண் போற்றிச் செயின்.''', '''E\'en weak ones mightily prevail, if place of strong defence,
They find, protect themselves, and work their foes offence.''',
                               '''Even the powerless will become powerful and conquer, if they select a proper field (of action), and guard themselves, while they make war on their enemies.''');
        k[493] = Kural.factory(494, '''பொருட்பால்''', '''இடனறிதல்''', '''எண்ணியார் எண்ணம் இழப்பர் இடனறிந்து
  துன்னியார் துன்னிச் செயின்.''', '''The foes who thought to triumph, find their thoughts were vain,
If hosts advance, seize vantage ground, and thence the fight maintain.''',
                               '''If they who draw near (to fight) choose a suitable place to approach (their enemy), the latter, will have to relinquish the thought which they once entertained, of conquering them.''');
        k[494] = Kural.factory(495, '''பொருட்பால்''', '''இடனறிதல்''', '''நெடும்புனலுள் வெல்லும் முதலை அடும்புனலின்
  நீங்கின் அதனைப் பிற.''', '''The crocodile prevails in its own flow of water wide,
If this it leaves, \'tis slain by anything beside.''',
                               '''In deep water, a crocodile will conquer (all other animals); but if it leave the water, other animals will conquer it.''');
        k[495] = Kural.factory(496, '''பொருட்பால்''', '''இடனறிதல்''', '''கடலோடா கால்வல் நெடுந்தேர் கடலோடும்
  நாவாயும் ஓடா நிலத்து.''', '''The lofty car, with mighty wheel, sails not o\'er watery main,
The boat that skims the sea, runs not on earth\'s hard plain.''',
                               '''Wide chariots, with mighty wheels, will not run on the ocean; neither will ships that the traverse ocean, move on the earth.''');
        k[496] = Kural.factory(497, '''பொருட்பால்''', '''இடனறிதல்''', '''அஞ்சாமை அல்லால் துணைவேண்டா எஞ்சாமை
  எண்ணி இடத்தால் செயின்.''', '''Save their own fearless might they need no other aid,
If in right place they fight, all due provision made.''',
                               '''You will need no other aid than fearlessness, if you thoroughly reflect (on what you are to do), and select (a suitable) place for your operations.''');
        k[497] = Kural.factory(498, '''பொருட்பால்''', '''இடனறிதல்''', '''சிறுபடையான் செல்லிடம் சேரின் உறுபடையான்
  ஊக்கம் அழிந்து விடும்.''', '''If lord of army vast the safe retreat assail
Of him whose host is small, his mightiest efforts fail.''',
                               '''The power of one who has a large army will perish, if he goes into ground where only a small army can act.''');
        k[498] = Kural.factory(499, '''பொருட்பால்''', '''இடனறிதல்''', '''சிறைநலனும் சீரும் இலரெனினும் மாந்தர்
  உறைநிலத்தோடு ஒட்டல் அரிது.''', '''Though fort be none, and store of wealth they lack,
\'Tis hard a people\'s homesteads to attack!''',
                               '''It is a hazardous thing to attack men in their own country, although they may neither have power nor a good fortress.''');
        k[499] = Kural.factory(500, '''பொருட்பால்''', '''இடனறிதல்''', '''காலாழ் களரில் நரியடும் கண்ணஞ்சா
  வேலாள் முகத்த களிறு.''', '''The jackal slays, in miry paths of foot-betraying fen,
The elephant of fearless eye and tusks transfixing armed men.''',
                               '''A fox can kill a fearless, warrior-faced elephant, if it go into mud in which its legs sink down.''');
        k[500] = Kural.factory(501, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''அறம்பொருள் இன்பம் உயிரச்சம் நான்கின்
  திறந்தெரிந்து தேறப் படும்.''', '''How treats he virtue, wealth and pleasure? How, when life\'s at stake,
Comports himself? This four-fold test of man will full assurance make.''',
                               '''Let (a minister) be chosen, after he has been tried by means of these four things, viz,-his virtue, (love of) money, (love of) sexual pleasure, and tear of (losing) life.''');
        k[501] = Kural.factory(502, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''குடிப்பிறந்து குற்றத்தின் நீங்கி வடுப்பரியும்
  நாணுடையான் சுட்டே தெளிவு.''', '''Of noble race, of faultless worth, of generous pride
That shrinks from shame or stain; in him may king confide.''',
                               '''(The king\'s) choice should (fall) on him, who is of good family, who is free from faults, and who has the modesty which fears the wounds (of sin).''');
        k[502] = Kural.factory(503, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''அரியகற்று ஆசற்றார் கண்ணும் தெரியுங்கால்
  இன்மை அரிதே வெளிறு.''', '''Though deeply learned, unflecked by fault, \'tis rare to see,
When closely scanned, a man from all unwisdom free.''',
                               '''When even men, who have studied the most difficult works, and who are free from faults, are (carefully) examined, it is a rare thing to find them without ignorance.''');
        k[503] = Kural.factory(504, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''குணம்நாடிக் குற்றமும் நாடி அவற்றுள்
  மிகைநாடி மிக்க கொளல்.''', '''Weigh well the good of each, his failings closely scan,
As these or those prevail, so estimate the man.''',
                               '''Let (a king) consider (a man\'s) good qualities, as well as his faults, and then judge (of his character) by that which prevails.''');
        k[504] = Kural.factory(505, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''பெருமைக்கும் ஏனைச் சிறுமைக்கும் தத்தம்
  கருமமே கட்டளைக் கல்.''', '''Of greatness and of meanness too,
The deeds of each are touchstone true.''', '''A man\'s deeds are the touchstone of his greatness and littleness.''');
        k[505] = Kural.factory(506, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''அற்றாரைத் தேறுதல் ஓம்புக மற்றவர்
  பற்றிலர் நாணார் பழி.''', '''Beware of trusting men who have no kith of kin;
No bonds restrain such men, no shame deters from sin.''',
                               '''Let (a king) avoid choosing men who have no relations; such men have no attachment, and therefore have no fear of crime.''');
        k[506] = Kural.factory(507, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''காதன்மை கந்தா அறிவறியார்த் தேறுதல்
  பேதைமை எல்லாந் தரும்.''', '''By fond affection led who trusts in men of unwise soul,
Yields all his being up to folly\'s blind control.''',
                               '''To choose ignorant men, through partiality, is the height of folly.''');
        k[507] = Kural.factory(508, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''தேரான் பிறனைத் தெளிந்தான் வழிமுறை
  தீரா இடும்பை தரும்.''', '''Who trusts an untried stranger, brings disgrace,
Remediless, on all his race.''',
                               '''Sorrow that will not leave even his posterity will come upon him chooses a stranger whose character he has not known.''');
        k[508] = Kural.factory(509, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''தேறற்க யாரையும் தேராது தேர்ந்தபின்
  தேறுக தேறும் பொருள்.''', '''Trust no man whom you have not fully tried,
When tested, in his prudence proved confide.''',
                               '''Let (a king) choose no one without previous consideration; after he has made his choice, let him unhesitatingly select for each such duties as are appropriate.''');
        k[509] = Kural.factory(510, '''பொருட்பால்''', '''தெரிந்துதெளிதல்''', '''தேரான் தெளிவும் தெளிந்தான்கண் ஐயுறவும்
  தீரா இடும்பை தரும்.''', '''Trust where you have not tried, doubt of a friend to feel,
Once trusted, wounds inflict that nought can heal.''',
                               '''To make choice of one who has not been examined, and to entertain doubts respecting one who has been chosen, will produce irremediable sorrow.''');
        k[510] = Kural.factory(511, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''நன்மையும் தீமையும் நாடி நலம்புரிந்த
  தன்மையான் ஆளப் படும்.''', '''Who good and evil scanning, ever makes the good his joy;
Such man of virtuous mood should king employ.''',
                               '''He should be employed (by a king), whose nature leads him to choose the good, after having weighed both the evil and the good in any undertaking.''');
        k[511] = Kural.factory(512, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''வாரி பெருக்கி வளம்படுத்து உற்றவை
  ஆராய்வான் செய்க வினை.''', '''Who swells the revenues, spreads plenty o\'er the land,
Seeks out what hinders progress, his the workman\'s hand.''',
                               '''Let him do (the king\'s) work who can enlarge the sources (of revenue), increase wealth and considerately prevent the accidents (which would destroy it).''');
        k[512] = Kural.factory(513, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''அன்பறிவு தேற்றம் அவாவின்மை இந்நான்கும்
  நன்குடையான் கட்டே தெளிவு.''', '''A loyal love with wisdom, clearness, mind from avarice free;
Who hath these four good gifts should ever trusted be.''',
                               '''Let the choice (of a king) fall upon him who largely possesses these four things, love, knowledge, a clear mind and freedom from covetousness.''');
        k[513] = Kural.factory(514, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''எனைவகையான் தேறியக் கண்ணும் வினைவகையான்
  வேறாகும் மாந்தர் பலர்.''', '''Even when tests of every kind are multiplied,
Full many a man proves otherwise, by action tried!''',
                               '''Even when (a king) has tried them in every possible way, there are many men who change, from the nature of the works (in which they may be employed).''');
        k[514] = Kural.factory(515, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''அறிந்தாற்றிச் செய்கிற்பாற்கு அல்லால் வினைதான்
  சிறந்தானென்று ஏவற்பாற் றன்று.''', '''No specious fav\'rite should the king\'s commission bear,
But he that knows, and work performs with patient care.''',
                               '''(A king\'s) work can only be accomplished by a man of wisdom and patient endurance; it is not of a nature to be given to one from mere personal attachment.''');
        k[515] = Kural.factory(516, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''செய்வானை நாடி வினைநாடிக் காலத்தோடு
  எய்த உணர்ந்து செயல்.''', '''Let king first ask, \'Who shall the deed perform?\' and \'What the deed?\'
Of hour befitting both assured, let every work proceed.''',
                               '''Let (a king) act, after having considered the agent (whom he is to employ), the deed (he desires to do), and the time which is suitable to it.''');
        k[516] = Kural.factory(517, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''இதனை இதனால் இவன்முடிக்கும் என்றாய்ந்து
  அதனை அவன்கண் விடல்.''', '''\'This man, this work shall thus work out,\' let thoughtful king command;
Then leave the matter wholly in his servant\'s hand.''',
                               '''After having considered, "this man can accomplish this, by these means", let (the king) leave with him the discharge of that duty.''');
        k[517] = Kural.factory(518, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''வினைக்குரிமை நாடிய பின்றை அவனை
  அதற்குரிய னாகச் செயல்.''', '''As each man\'s special aptitude is known,
Bid each man make that special work his own.''',
                               '''Having considered what work a man is fit for, let (the king) employ him in that work.''');
        k[518] = Kural.factory(519, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''வினைக்கண் வினையுடையான் கேண்மைவே றாக
  நினைப்பானை நீங்கும் திரு.''', '''Fortune deserts the king who ill can bear,
Informal friendly ways of men his tolls who share.''',
                               '''Prosperity will leave (the king) who doubts the friendship of the man who steadily labours in the discharge of his duties.''');
        k[519] = Kural.factory(520, '''பொருட்பால்''', '''தெரிந்துவினையாடல்''', '''நாடோறும் நாடுக மன்னன் வினைசெய்வான்
  கோடாமை கோடா துலகு.''', '''Let king search out his servants\' deeds each day;
When these do right, the world goes rightly on its way.''',
                               '''Let a king daily examine the conduct of his servants; if they do not act crookedly, the world will not act crookedly.''');
        k[520] = Kural.factory(521, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''பற்றற்ற கண்ணும் பழைமைபா ராட்டுதல்
  சுற்றத்தார் கண்ணே உள.''', '''When wealth is fled, old kindness still to show,
Is kindly grace that only kinsmen know.''',
                               '''Even when (a man\'s) property is all gone, relatives will act towards him with their accustomed (kindness).''');
        k[521] = Kural.factory(522, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''விருப்பறாச் சுற்றம் இயையின் அருப்பறா
  ஆக்கம் பலவும் தரும்.''', '''The gift of kin\'s unfailing love bestows
Much gain of good, like flower that fadeless blows.''',
                               '''If (a man\'s) relatives remain attached to him with unchanging love, it will be a source of ever-increasing wealth.''');
        k[522] = Kural.factory(523, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''அளவளா வில்லாதான் வாழ்க்கை குளவளாக்
  கோடின்றி நீர்நிறைந் தற்று.''', '''His joy of life who mingles not with kinsmen gathered round,
Is lake where streams pour in, with no encircling bound.''',
                               '''The wealth of one who does not mingle freely with his relatives, will be like the filling of water in a spacious tank that has no banks.''');
        k[523] = Kural.factory(524, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''சுற்றத்தால் சுற்றப் படஒழுகல் செல்வந்தான்
  பெற்றத்தால் பெற்ற பயன்.''', '''The profit gained by wealth\'s increase,
Is living compassed round by relatives in peace.''',
                               '''To live surrounded by relatives, is the advantage to be derived from the acquisition of wealth.''');
        k[524] = Kural.factory(525, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''கொடுத்தலும் இன்சொலும் ஆற்றின் அடுக்கிய
  சுற்றத்தால் சுற்றப் படும்.''', '''Who knows the use of pleasant words, and liberal gifts can give,
Connections, heaps of them, surrounding him shall live.''',
                               '''He will be surrounded by numerous relatives who manifests generosity and affability.''');
        k[525] = Kural.factory(526, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''பெருங்கொடையான் பேணான் வெகுளி அவனின்
  மருங்குடையார் மாநிலத்து இல்.''', '''Than one who gifts bestows and wrath restrains,
Through the wide world none larger following gains.''',
                               '''No one, in all the world, will have so many relatives (about him), as he who makes large gift, and does not give way to anger.''');
        k[526] = Kural.factory(527, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''காக்கை கரவா கரைந்துண்ணும் ஆக்கமும்
  அன்னநீ ரார்க்கே உள.''', '''The crows conceal not, call their friends to come, then eat;
Increase of good such worthy ones shall meet.''',
                               '''The crows do not conceal (their prey), but will call out for others (to share with them) while they eat it; wealth will be with those who show a similar disposition (towards their relatives).''');
        k[527] = Kural.factory(528, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''பொதுநோக்கான் வேந்தன் வரிசையா நோக்கின்
  அதுநோக்கி வாழ்வார் பலர்.''', '''Where king regards not all alike, but each in his degree,
\'Neath such discerning rule many dwell happily.''',
                               '''Many relatives will live near a king, when they observe that he does not look on all alike, but that he looks on each man according to his merit.''');
        k[528] = Kural.factory(529, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''தமராகிக் தற்றுறந்தார் சுற்றம் அமராமைக்
  காரணம் இன்றி வரும்.''', '''Who once were his, and then forsook him, as before
Will come around, when cause of disagreement is no more.''',
                               '''Those who have been friends and have afterwards forsaken him, will return and join themselves (to him), when the cause of disagreement is not to be found in him.''');
        k[529] = Kural.factory(530, '''பொருட்பால்''', '''சுற்றந்தழால்''', '''உழைப்பிரிந்து காரணத்தின் வந்தானை வேந்தன்
  இழைத்திருந்து எண்ணிக் கொளல்.''', '''Who causeless went away, then to return, for any cause, ask leave;
The king should sift their motives well, consider, and receive!''',
                               '''When one may have left him, and for some cause has returned to him, let the king fulfil the object (for which he has come back) and thoughtfully receive him again.''');
        k[530] = Kural.factory(531, '''பொருட்பால்''', '''பொச்சாவாமை''', '''இறந்த வெகுளியின் தீதே சிறந்த
  உவகை மகிழ்ச்சியிற் சோர்வு.''', '''\'Tis greater ill, it rapture of o\'erweening gladness to the soul
Bring self-forgetfulness than if transcendent wrath control.''',
                               '''More evil than excessive anger, is forgetfulness which springs from the intoxication of great joy.''');
        k[531] = Kural.factory(532, '''பொருட்பால்''', '''பொச்சாவாமை''', '''பொச்சாப்புக் கொல்லும் புகழை அறிவினை
  நிச்ச நிரப்புக்கொன் றாங்கு.''', '''Perpetual, poverty is death to wisdom of the wise;
When man forgets himself his glory dies!''',
                               '''Forgetfulness will destroy fame, even as constant poverty destroys knowledge.''');
        k[532] = Kural.factory(533, '''பொருட்பால்''', '''பொச்சாவாமை''', '''பொச்சாப்பார்க் கில்லை புகழ்மை அதுஉலகத்து
  எப்பால்நூ லோர்க்கும் துணிவு.''', '''\'To self-oblivious men no praise\'; this rule
Decisive wisdom sums of every school.''',
                               '''Thoughtlessness will never acquire fame; and this tenet is upheld by all treatises in the world.''');
        k[533] = Kural.factory(534, '''பொருட்பால்''', '''பொச்சாவாமை''', '''அச்ச முடையார்க்கு அரணில்லை ஆங்கில்லை
  பொச்சாப் புடையார்க்கு நன்கு.''', '''\'To cowards is no fort\'s defence\'; e\'en so
The self-oblivious men no blessing know.''',
                               '''Just as the coward has no defence (by whatever fortifications ha may be surrounded), so the thoughtless has no good (whatever advantages he may possess).''');
        k[534] = Kural.factory(535, '''பொருட்பால்''', '''பொச்சாவாமை''', '''முன்னுறக் காவாது இழுக்கியான் தன்பிழை
  பின்னூறு இரங்கி விடும்.''', '''To him who nought foresees, recks not of anything,
The after woe shall sure repentance bring.''',
                               '''The thoughtless man, who provides not against the calamities that may happen, will afterwards repent for his fault.''');
        k[535] = Kural.factory(536, '''பொருட்பால்''', '''பொச்சாவாமை''', '''இழுக்காமை யார்மாட்டும் என்றும் வழுக்காமை
  வாயின் அதுவொப்பது இல்.''', '''Towards all unswerving, ever watchfulness of soul retain,
Where this is found there is no greater gain.''',
                               '''There is nothing comparable with the possession of unfailing thoughtfulness at all times; and towards all persons.''');
        k[536] = Kural.factory(537, '''பொருட்பால்''', '''பொச்சாவாமை''', '''அரியஎன்று ஆகாத இல்லைபொச் சாவாக்
  கருவியால் போற்றிச் செயின்.''', '''Though things are arduous deemed, there\'s nought may not be won,
When work with mind\'s unslumbering energy and thought is done.''',
                               '''There is nothing too difficult to be accomplished, if a man set about it carefully, with unflinching endeavour.''');
        k[537] = Kural.factory(538, '''பொருட்பால்''', '''பொச்சாவாமை''', '''புகழ்ந்தவை போற்றிச் செயல்வேண்டும் செய்யாது
  இகழ்ந்தார்க்கு எழுமையும் இல்.''', '''Let things that merit praise thy watchful soul employ;
Who these despise attain through sevenfold births no joy.''',
                               '''Let (a man) observe and do these things which have been praised (by the wise); if he neglects and fails to perform them, for him there will be no (happiness) throughout the seven births.''');
        k[538] = Kural.factory(539, '''பொருட்பால்''', '''பொச்சாவாமை''', '''இகழ்ச்சியின் கெட்டாரை உள்ளுக தாந்தம்
  மகிழ்ச்சியின் மைந்துறும் போழ்து.''', '''Think on the men whom scornful mind hath brought to nought,
When exultation overwhelms thy wildered thought.''',
                               '''Let (a king) think of those who have been ruined by neglect, when his mind is elated with joy.''');
        k[539] = Kural.factory(540, '''பொருட்பால்''', '''பொச்சாவாமை''', '''உள்ளியது எய்தல் எளிதுமன் மற்றுந்தான்
  உள்ளியது உள்ளப் பெறின்.''', '''\'Tis easy what thou hast in mind to gain,
If what thou hast in mind thy mind retain.''',
                               '''It is easy for (one) to obtain whatever he may think of, if he can again think of it.''');
        k[540] = Kural.factory(541, '''பொருட்பால்''', '''செங்கோன்மை''', '''ஓர்ந்துகண் ணோடாது இறைபுரிந்து யார்மாட்டும்
  தேர்ந்துசெய் வஃதே முறை.''', '''Search out, to no one favour show; with heart that justice loves
Consult, then act; this is the rule that right approves.''',
                               '''To examine into (the crimes which may be committed), to show no favour (to any one), to desire to act with impartiality towards all, and to inflict (such punishments) as may be wisely resolved on, constitute rectitude.''');
        k[541] = Kural.factory(542, '''பொருட்பால்''', '''செங்கோன்மை''', '''வானோக்கி வாழும் உலகெல்லாம் மன்னவன்
  கோல்நோக்கி வாழுங் குடி.''', '''All earth looks up to heav\'n whence raindrops fall;
All subjects look to king that ruleth all.''',
                               '''When there is rain, the living creation thrives; and so when the king rules justly, his subjects thrive.''');
        k[542] = Kural.factory(543, '''பொருட்பால்''', '''செங்கோன்மை''', '''அந்தணர் நூற்கும் அறத்திற்கும் ஆதியாய்
  நின்றது மன்னவன் கோல்.''', '''Learning and virtue of the sages spring,
From all-controlling sceptre of the king.''',
                               '''The sceptre of the king is the firm support of the Vedas of the Brahmin, and of all virtues therein described.''');
        k[543] = Kural.factory(544, '''பொருட்பால்''', '''செங்கோன்மை''', '''குடிதழீஇக் கோலோச்சும் மாநில மன்னன்
  அடிதழீஇ நிற்கும் உலகு.''', '''Whose heart embraces subjects all, lord over mighty land
Who rules, the world his feet embracing stands.''',
                               '''The world will constantly embrace the feet of the great king who rules over his subjects with love.''');
        k[544] = Kural.factory(545, '''பொருட்பால்''', '''செங்கோன்மை''', '''இயல்புளிக் கோலோச்சும் மன்னவன் நாட்ட
  பெயலும் விளையுளும் தொக்கு.''', '''Where king, who righteous laws regards, the sceptre wields,
There fall the showers, there rich abundance crowns the fields.''',
                               '''Rain and plentiful crops will ever dwell together in the country of the king who sways his sceptre with justice.''');
        k[545] = Kural.factory(546, '''பொருட்பால்''', '''செங்கோன்மை''', '''வேலன்று வென்றி தருவது மன்னவன்
  கோலதூஉங் கோடா தெனின்.''', '''Not lance gives kings the victory,
But sceptre swayed with equity.''',
                               '''It is not the javelin that gives victory, but the king\'s sceptre, if it do no injustice.''');
        k[546] = Kural.factory(547, '''பொருட்பால்''', '''செங்கோன்மை''', '''இறைகாக்கும் வையகம் எல்லாம் அவனை
  முறைகாக்கும் முட்டாச் செயின்.''', '''The king all the whole realm of earth protects;
And justice guards the king who right respects.''',
                               '''The king defends the whole world; and justice, when administered without defect, defends the king.''');
        k[547] = Kural.factory(548, '''பொருட்பால்''', '''செங்கோன்மை''', '''எண்பதத்தான் ஓரா முறைசெய்யா மன்னவன்
  தண்பதத்தான் தானே கெடும்.''', '''Hard of access, nought searching out, with partial hand
The king who rules, shall sink and perish from the land.''',
                               '''The king who gives not facile audience (to those who approach him), and who does not examine and pass judgment (on their complaints), will perish in disgrace.''');
        k[548] = Kural.factory(549, '''பொருட்பால்''', '''செங்கோன்மை''', '''குடிபுறங் காத்தோம்பிக் குற்றம் கடிதல்
  வடுவன்று வேந்தன் தொழில்.''', '''Abroad to guard, at home to punish, brings
No just reproach; \'tis work assigned to kings.''',
                               '''In guarding his subjects (against injury from others), and in preserving them himself; to punish crime is not a fault in a king, but a duty.''');
        k[549] = Kural.factory(550, '''பொருட்பால்''', '''செங்கோன்மை''', '''கொலையிற் கொடியாரை வேந்தொறுத்தல் பைங்கூழ்
  களைகட் டதனொடு நேர்.''', '''By punishment of death the cruel to restrain,
Is as when farmer frees from weeds the tender grain.''',
                               '''For a king to punish criminals with death, is like pulling up the weeds in the green corn.''');
        k[550] = Kural.factory(551, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''கொலைமேற்கொண் டாரிற் கொடிதே அலைமேற்கொண்டு
  அல்லவை செய்தொழுகும் வேந்து.''', '''Than one who plies the murderer\'s trade, more cruel is the king
Who all injustice works, his subjects harassing.''',
                               '''The king who gives himself up to oppression and acts unjustly (towards his subjects) is more cruel than the man who leads the life of a murderer.''');
        k[551] = Kural.factory(552, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''வேலொடு நின்றான் இடுவென் றதுபோலும்
  கோலொடு நின்றான் இரவு.''', '''As \'Give\' the robber cries with lance uplift,
So kings with sceptred hand implore a gift.''',
                               '''The request (for money) of him who holds the sceptre is like the word of a highway robber who stands with a weapon in hand and says "give up your wealth".''');
        k[552] = Kural.factory(553, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''நாடொறும் நாடி முறைசெய்யா மன்னவன்
  நாடொறும் நாடு கெடும்.''', '''Who makes no daily search for wrongs, nor justly rules, that king
Doth day by day his realm to ruin bring.''',
                               '''The country of the king who does not daily examine into the wrongs done and distribute justice, will daily fall to ruin.''');
        k[553] = Kural.factory(554, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''கூழுங் குடியும் ஒருங்கிழக்கும் கோல்கோடிச்
  சூழாது செய்யும் அரசு.''', '''Whose rod from right deflects, who counsel doth refuse,
At once his wealth and people utterly shall lose.''',
                               '''The king, who, without reflecting (on its evil consequences), perverts justice, will lose at once both his wealth and his subjects.''');
        k[554] = Kural.factory(555, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''அல்லற்பட்டு ஆற்றாது அழுதகண் ணீரன்றே
  செல்வத்தைத் தேய்க்கும் படை''', '''His people\'s tears of sorrow past endurance, are not they
Sharp instruments to wear the monarch\'s wealth away?''',
                               '''Will not the tears, shed by a people who cannot endure the oppression which they suffer (from their king), become a saw to waste away his wealth ?''');
        k[555] = Kural.factory(556, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''மன்னர்க்கு மன்னுதல் செங்கோன்மை அஃதின்றேல்
  மன்னாவாம் மன்னர்க் கொளி.''', '''To rulers\' rule stability is sceptre right;
When this is not, quenched is the rulers\' light.''',
                               '''Righteous government gives permanence to (the fame of) kings; without that their fame will have no endurance.''');
        k[556] = Kural.factory(557, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''துளியின்மை ஞாலத்திற்கு எற்றற்றே வேந்தன்
  அளியின்மை வாழும் உயிர்க்கு.''', '''As lack of rain to thirsty lands beneath,
Is lack of grace in kings to all that breathe.''',
                               '''As is the world without rain, so live a people whose king is without kindness.''');
        k[557] = Kural.factory(558, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''இன்மையின் இன்னாது உடைமை முறைசெய்யா
  மன்னவன் கோற்கீழ்ப் படின்.''', '''To poverty it adds a sharper sting,
To live beneath the sway of unjust king.''',
                               '''Property gives more sorrow than poverty, to those who live under the sceptre of a king without justice.''');
        k[558] = Kural.factory(559, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''முறைகோடி மன்னவன் செய்யின் உறைகோடி
  ஒல்லாது வானம் பெயல்.''', '''Where king from right deflecting, makes unrighteous gain,
The seasons change, the clouds pour down no rain.''',
                               '''If the king acts contrary to justice, rain will become unseasonable, and the heavens will withhold their showers.''');
        k[559] = Kural.factory(560, '''பொருட்பால்''', '''கொடுங்கோன்மை''', '''ஆபயன் குன்றும் அறுதொழிலோர் நூல்மறப்பர்
  காவலன் காவான் எனின்.''', '''Where guardian guardeth not, udder of kine grows dry,
And Brahmans\' sacred lore will all forgotten lie.''',
                               '''If the guardian (of the country) neglects to guard it, the produce of the cows will fail, and the men of six duties viz., the Brahmins will forget the vedas.''');
        k[560] = Kural.factory(561, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''தக்காங்கு நாடித் தலைச்செல்லா வண்ணத்தால்
  ஒத்தாங்கு ஒறுப்பது வேந்து.''', '''Who punishes, investigation made in due degree,
So as to stay advance of crime, a king is he.''',
                               '''He is a king who having equitably examined (any injustice which has been brought to his notice), suitably punishes it, so that it may not be again committed.''');
        k[561] = Kural.factory(562, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''கடிதோச்சி மெல்ல எறிக நெடிதாக்கம்
  நீங்காமை வேண்டு பவர்.''', '''For length of days with still increasing joys on Heav\'n who call,
Should raise the rod with brow severe, but let it gently fall.''',
                               '''Let the king, who desires that his prosperity may long remain, commence his preliminary enquires with strictness, and then punish with mildness.''');
        k[562] = Kural.factory(563, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''வெருவந்த செய்தொழுகும் வெங்கோல னாயின்
  ஒருவந்தம் ஒல்லைக் கெடும்.''', '''Where subjects dread of cruel wrongs endure,
Ruin to unjust king is swift and sure.''',
                               '''The cruel-sceptred king, who acts so as to put his subjects in fear, will certainly and quickly come to ruin.''');
        k[563] = Kural.factory(564, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''இறைகடியன் என்றுரைக்கும் இன்னாச்சொல் வேந்தன்
  உறைகடுகி ஒல்லைக் கெடும்.''', '''\'Ah! cruel is our king\', where subjects sadly say,
His age shall dwindle, swift his joy of life decay.''',
                               '''The king who is spoken of as cruel will quickly perish; his life becoming shortened.''');
        k[564] = Kural.factory(565, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''அருஞ்செவ்வி இன்னா முகத்தான் பெருஞ்செல்வம்
  பேஎய்கண் டன்னது உடைத்து.''', '''Whom subjects scarce may see, of harsh forbidding countenance;
His ample wealth shall waste, blasted by demon\'s glance.''',
                               '''The great wealth of him who is difficult of access and possesses a sternness of countenance, is like that which has been obtained by a devil.''');
        k[565] = Kural.factory(566, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''கடுஞ்சொல்லன் கண்ணிலன் ஆயின் நெடுஞ்செல்வம்
  நீடின்றி ஆங்கே கெடும்.''', '''The tyrant, harsh in speach and hard of eye,
His ample joy, swift fading, soon shall die.''',
                               '''The abundant wealth of the king whose words are harsh and whose looks are void of kindness, will instantly perish instead of abiding long, with him.''');
        k[566] = Kural.factory(567, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''கடுமொழியும் கையிகந்த தண்டமும் வேந்தன்
  அடுமுரண் தேய்க்கும் அரம்.''', '''Harsh words and punishments severe beyond the right,
Are file that wears away the monarch\'s conquering might.''',
                               '''Severe words and excessive punishments will be a file to waste away a king\'s power for destroying (his enemies).''');
        k[567] = Kural.factory(568, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''இனத்தாற்றி எண்ணாத வேந்தன் சினத்தாற்றிச்
  சீறிற் சிறுகும் திரு.''', '''Who leaves the work to those around, and thinks of it no more;
If he in wrathful mood reprove, his prosperous days are o\'er!''',
                               '''The prosperity of that king will waste away, who without reflecting (on his affairs himself), commits them to his ministers, and (when a failure occurs) gives way to anger, and rages against them.''');
        k[568] = Kural.factory(569, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''செருவந்த போழ்திற் சிறைசெய்யா வேந்தன்
  வெருவந்து வெய்து கெடும்.''', '''Who builds no fort whence he may foe defy,
In time of war shall fear and swiftly die.''',
                               '''The king who has not provided himself with a place of defence, will in times of war be seized with fear and quickly perish.''');
        k[569] = Kural.factory(570, '''பொருட்பால்''', '''வெருவந்தசெய்யாமை''', '''கல்லார்ப் பிணிக்கும் கடுங்கோல் அதுவல்லது
  இல்லை நிலக்குப் பொறை.''', '''Tyrants with fools their counsels share:
Earth can no heavier burthen bear!''',
                               '''The earth bears up no greater burden than ignorant men whom a cruel sceptre attaches to itself (as the ministers of its evil deeds).''');
        k[570] = Kural.factory(571, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''கண்ணோட்டம் என்னும் கழிபெருங் காரிகை
  உண்மையான் உண்டிவ் வுலகு.''', '''Since true benignity, that grace exceeding great, resides
In kingly souls, world in happy state abides.''',
                               '''The world exists through that greatest ornament (of princes), a gracious demeanour.''');
        k[571] = Kural.factory(572, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''கண்ணோட்டத் துள்ளது உலகியல் அஃதிலார்
  உண்மை நிலக்குப் பொறை.''', '''The world goes on its wonted way, since grace benign is there;
All other men are burthen for the earth to bear.''',
                               '''The prosperity of the world springs from the kindliness, the existence of those who have no (kindliness) is a burden to the earth.''');
        k[572] = Kural.factory(573, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''பண்என்னாம் பாடற்கு இயைபின்றேல் கண்என்னாம்
  கண்ணோட்டம் இல்லாத கண்.''', '''Where not accordant with the song, what use of sounding chords?
What gain of eye that no benignant light affords?''',
                               '''Of what avail is a song if it be inconsistent with harmony ? what is the use of eyes which possess no kindliness.''');
        k[573] = Kural.factory(574, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''உளபோல் முகத்தெவன் செய்யும் அளவினால்
  கண்ணோட்டம் இல்லாத கண்.''', '''The seeming eye of face gives no expressive light,
When not with duly meted kindness bright.''',
                               '''Beyond appearing to be in the face, what good do they do, those eyes in which is no well-regulated kindness ?''');
        k[574] = Kural.factory(575, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''கண்ணிற்கு அணிகலம் கண்ணோட்டம் அஃதின்றேல்
  புண்ணென்று உணரப் படும்''', '''Benignity is eyes\' adorning grace;
Without it eyes are wounds disfiguring face.''',
                               '''Kind looks are the ornaments of the eyes; without these they will be considered (by the wise) to be merely two sores.''');
        k[575] = Kural.factory(576, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''மண்ணோ டியைந்த மரத்தனையர் கண்ணோ
  டியைந்துகண் ணோடா தவர்.''', '''Whose eyes \'neath brow infixed diffuse no ray
Of grace; like tree in earth infixed are they.''',
                               '''They resemble the trees of the earth, who although they have eyes, never look kindly (on others).''');
        k[576] = Kural.factory(577, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''கண்ணோட்டம் இல்லவர் கண்ணிலர் கண்ணுடையார்
  கண்ணோட்டம் இன்மையும் இல்.''', '''Eyeless are they whose eyes with no benignant lustre shine;
Who\'ve eyes can never lack the light of grace benign.''',
                               '''Men without kind looks are men without eyes; those who (really) have eyes are also not devoid of kind looks.''');
        k[577] = Kural.factory(578, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''கருமம் சிதையாமல் கண்ணோட வல்லார்க்கு
  உரிமை உடைத்திவ் வுலகு.''', '''Who can benignant smile, yet leave no work undone;
By them as very own may all the earth be won.''',
                               '''The world is theirs (kings) who are able to show kindness, without injury to their affairs, (administration of justice).''');
        k[578] = Kural.factory(579, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''ஒறுத்தாற்றும் பண்பினார் கண்ணும்கண் ணோடிப்
  பொறுத்தாற்றும் பண்பே தலை.''', '''To smile on those that vex, with kindly face,
Enduring long, is most excelling grace.''',
                               '''Patiently to bear with, and show kindness to those who grieve us, is the most excellent of all dispositions.''');
        k[579] = Kural.factory(580, '''பொருட்பால்''', '''கண்ணோட்டம்''', '''பெயக்கண்டும் நஞ்சுண் டமைவர் நயத்தக்க
  நாகரிகம் வேண்டு பவர்.''', '''They drink with smiling grace, though poison interfused they see,
Who seek the praise of all-esteemed courtesy.''',
                               '''Those who desire (to cultivate that degree of) urbanity which all shall love, even after swallowing the poison served to them by their friends, will be friendly with them.''');
        k[580] = Kural.factory(581, '''பொருட்பால்''', '''ஒற்றாடல்''', '''ஒற்றும் உரைசான்ற நூலும் இவையிரண்டும்
  தெற்றென்க மன்னவன் கண்.''', '''These two: the code renowned and spies,
In these let king confide as eyes.''',
                               '''Let a king consider as his eyes these two things, a spy and a book (of laws) universally esteemed.''');
        k[581] = Kural.factory(582, '''பொருட்பால்''', '''ஒற்றாடல்''', '''எல்லார்க்கும் எல்லாம் நிகழ்பவை எஞ்ஞான்றும்
  வல்லறிதல் வேந்தன் தொழில்.''', '''Each day, of every subject every deed,
\'Tis duty of the king to learn with speed.''',
                               '''It is the duty of a king to know quickly (by a spy) what all happens, daily, amongst all men.''');
        k[582] = Kural.factory(583, '''பொருட்பால்''', '''ஒற்றாடல்''', '''ஒற்றினான் ஒற்றிப் பொருள்தெரியா மன்னவன்
  கொற்றங் கொளக்கிடந்தது இல்.''', '''By spies who spies, not weighing things they bring,
Nothing can victory give to that unwary king.''',
                               '''There is no way for a king to obtain conquests, who knows not the advantage of discoveries made by a spy.''');
        k[583] = Kural.factory(584, '''பொருட்பால்''', '''ஒற்றாடல்''', '''வினைசெய்வார் தம்சுற்றம் வேண்டாதார் என்றாங்கு
  அனைவரையும் ஆராய்வது ஒற்று.''', '''His officers, his friends, his enemies,
All these who watch are trusty spies.''',
                               '''He is a spy who watches all men, to wit, those who are in the king\'s employment, his relatives, and his enemies.''');
        k[584] = Kural.factory(585, '''பொருட்பால்''', '''ஒற்றாடல்''', '''கடாஅ உருவொடு கண்ணஞ்சாது யாண்டும்
  உகாஅமை வல்லதே ஒற்று.''', '''Of unsuspected mien and all-unfearing eyes,
Who let no secret out, are trusty spies.''',
                               '''A spy is one who is able to assume an appearance which may create no suspicion (in the minds of others), who fears no man\'s face, and who never reveals (his purpose).''');
        k[585] = Kural.factory(586, '''பொருட்பால்''', '''ஒற்றாடல்''', '''துறந்தார் படிவத்த ராகி இறந்தாராய்ந்து
  என்செயினும் சோர்விலது ஒற்று.''', '''As monk or devotee, through every hindrance making way,
A spy, whate\'er men do, must watchful mind display.''',
                               '''He is a spy who, assuming the appearance of an ascetic, goes into (whatever place he wishes), examines into (all, that is needful), and never discovers himself, whatever may be done to him.''');
        k[586] = Kural.factory(587, '''பொருட்பால்''', '''ஒற்றாடல்''', '''மறைந்தவை கேட்கவற் றாகி அறிந்தவை
  ஐயப்பாடு இல்லதே ஒற்று.''', '''A spy must search each hidden matter out,
And full report must render, free from doubt.''',
                               '''A spy is one who is able to discover what is hidden and who retains no doubt concerning what he has known.''');
        k[587] = Kural.factory(588, '''பொருட்பால்''', '''ஒற்றாடல்''', '''ஒற்றொற்றித் தந்த பொருளையும் மற்றுமோர்
  ஒற்றினால் ஒற்றிக் கொளல்.''', '''Spying by spies, the things they tell
To test by other spies is well.''',
                               '''Let not a king receive the information which a spy has discovered and made known to him, until he has examined it by another spy.''');
        k[588] = Kural.factory(589, '''பொருட்பால்''', '''ஒற்றாடல்''', '''ஒற்றெற் றுணராமை ஆள்க உடன்மூவர்
  சொற்றொக்க தேறப் படும்.''', '''One spy must not another see: contrive it so;
And things by three confirmed as truth you know.''',
                               '''Let a king employ spies so that one may have no knowledge of the other; and when the information of three agrees together, let him receive it.''');
        k[589] = Kural.factory(590, '''பொருட்பால்''', '''ஒற்றாடல்''', '''சிறப்பறிய ஒற்ற஧ன்கண் செய்யற்க செய்யின்
  புறப்படுத்தான் ஆகும் மறை.''', '''Reward not trusty spy in others\' sight,
Or all the mystery will come to light.''',
                               '''Let not a king publicly confer on a spy any marks of his favour; if he does, he will divulge his own secret.''');
        k[590] = Kural.factory(591, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''உடையர் எனப்படுவது ஊக்கம் அஃதில்லார்
  உடையது உடையரோ மற்று.''', '''\'Tis energy gives men o\'er that they own a true control;
They nothing own who own not energy of soul.''',
                               '''Energy makes out the man of property; as for those who are destitute of it, do they (really) possess what they possess ?''');
        k[591] = Kural.factory(592, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''உள்ளம் உடைமை உடைமை பொருளுடைமை
  நில்லாது நீங்கி விடும்.''', '''The wealth of mind man owns a real worth imparts,
Material wealth man owns endures not, utterly departs.''',
                               '''The possession of (energy of) mind is true property; the possession of wealth passes away and abides not.''');
        k[592] = Kural.factory(593, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''க்கம் இழந்தேமென்று அல்லாவார் ஊக்கம்
  ஒருவந்தம் கைத்துடை யார்.''', '''\'Lost is our wealth,\' they utter not this cry distressed,
The men of firm concentred energy of soul possessed.''',
                               '''They who are possessed of enduring energy will not trouble themselves, saying, "we have lost our property."''');
        k[593] = Kural.factory(594, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''க்கம் அதர்வினாய்ச் செல்லும் அசைவிலா
  ஊக்க முடையா னுழை.''', '''The man of energy of soul inflexible,
Good fortune seeks him out and comes a friend to dwell.''',
                               '''Wealth will find its own way to the man of unfailing energy.''');
        k[594] = Kural.factory(595, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''வெள்ளத் தனைய மலர்நீட்டம் மாந்தர்தம்
  உள்ளத் தனையது உயர்வு.''', '''With rising flood the rising lotus flower its stem unwinds;
The dignity of men is measured by their minds.''',
                               '''The stalks of water-flowers are proportionate to the depth of water; so is men\'s greatness proportionate to their minds.''');
        k[595] = Kural.factory(596, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''உள்ளுவ தெல்லாம் உயர்வுள்ளல் மற்றது
  தள்ளினுந் தள்ளாமை நீர்த்து.''', '''Whate\'er you ponder, let your aim be loftly still,
Fate cannot hinder always, thwart you as it will.''',
                               '''In all that a king thinks of, let him think of his greatness; and if it should be thrust from him (by fate), it will have the nature of not being thrust from him.''');
        k[596] = Kural.factory(597, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''சிதைவிடத்து ஒல்கார் உரவோர் புதையம்பிற்
  பட்டுப்பா டூன்றுங் களிறு.''', '''The men of lofty mind quail not in ruin\'s fateful hour,
The elephant retains his dignity mind arrows\' deadly shower.''',
                               '''The strong minded will not faint, even when all is lost; the elephant stands firm, even when wounded by a shower of arrows.''');
        k[597] = Kural.factory(598, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''உள்ளம் இலாதவர் எய்தார் உலகத்து
  வள்ளியம் என்னுஞ் செருக்கு.''', '''The soulless man can never gain
Th\' ennobling sense of power with men.''',
                               '''Those who have no (greatness of) mind, will not acquire the joy of saying in the world, "we have excercised liaberality".''');
        k[598] = Kural.factory(599, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''பரியது கூர்ங்கோட்டது ஆயினும் யானை
  ஦வ்ருஉம் புலிதாக் குறின்.''', '''Huge bulk of elephant with pointed tusk all armed,
When tiger threatens shrinks away alarmed!''',
                               '''Although the elephant has a large body, and a sharp tusk, yet it fears the attack of the tiger.''');
        k[599] = Kural.factory(600, '''பொருட்பால்''', '''ஊக்கமுடைமை''', '''உரமொருவற்கு உள்ள வெறுக்கைஅஃ தில்லார்
  மரம்மக்க ளாதலே வேறு.''', '''Firmness of soul in man is real excellance;
Others are trees, their human form a mere pretence.''',
                               '''Energy is mental wealth; those men who are destitute of it are only trees in the form of men.''');
        k[600] = Kural.factory(601, '''பொருட்பால்''', '''மடியின்மை''', '''குடியென்னும் குன்றா விளக்கம் மடியென்னும்
  மாசூர மாய்ந்து கெடும்.''', '''Of household dignity the lustre beaming bright,
Flickers and dies when sluggish foulness dims its light.''',
                               '''By the darkness, of idleness, the indestructible lamp of family (rank) will be extinguished.''');
        k[601] = Kural.factory(602, '''பொருட்பால்''', '''மடியின்மை''', '''மடியை மடியா ஒழுகல் குடியைக்
  குடியாக வேண்டு பவர்.''', '''Let indolence, the death of effort, die,
If you\'d uphold your household\'s dignity.''',
                               '''Let those, who desire that their family may be illustrious, put away all idleness from their conduct.''');
        k[602] = Kural.factory(603, '''பொருட்பால்''', '''மடியின்மை''', '''மடிமடிக் கொண்டொழுகும் பேதை பிறந்த
  குடிமடியும் தன்னினும் முந்து.''', '''Who fosters indolence within his breast, the silly elf!
The house from which he springs shall perish ere himself.''',
                               '''The (lustre of the) family of the ignorant man, who acts under the influence of destructive laziness will perish, even before he is dead.''');
        k[603] = Kural.factory(604, '''பொருட்பால்''', '''மடியின்மை''', '''குடிமடிந்து குற்றம் பெருகும் மடிமடிந்து
  மாண்ட உஞற்றி லவர்க்கு.''', '''His family decays, and faults unheeded thrive,
Who, sunk in sloth, for noble objects doth not strive.''',
                               '''Family (greatness) will be destroyed, and faults will increase, in those men who give way to laziness, and put forth no dignified exertions.''');
        k[604] = Kural.factory(605, '''பொருட்பால்''', '''மடியின்மை''', '''நெடுநீர் மறவி மடிதுயில் நான்கும்
  கெடுநீரார் காமக் கலன்.''', '''Delay, oblivion, sloth, and sleep: these four
Are pleasure-boat to bear the doomed to ruin\'s shore.''',
                               '''Procrastination, forgetfulness, idleness, and sleep, these four things, form the vessel which is desired by those destined to destruction.''');
        k[605] = Kural.factory(606, '''பொருட்பால்''', '''மடியின்மை''', '''படியுடையார் பற்றமைந்தக் கண்ணும் மடியுடையார்
  மாண்பயன் எய்தல் அரிது.''', '''Though lords of earth unearned possessions gain,
The slothful ones no yield of good obtain.''',
                               '''It is a rare thing for the idle, even when possessed of the riches of kings who ruled over the whole earth, to derive any great benefit from it.''');
        k[606] = Kural.factory(607, '''பொருட்பால்''', '''மடியின்மை''', '''இடிபுரிந்து எள்ளுஞ்சொல் கேட்பர் மடிபுரிந்து
  மாண்ட உஞற்றி லவர்.''', '''Who hug their sloth, nor noble works attempt,
Shall bear reproofs and words of just contempt.''',
                               '''Those who through idleness, and do not engage themselves in dignified exertion, will subject themselves to rebukes and reproaches.''');
        k[607] = Kural.factory(608, '''பொருட்பால்''', '''மடியின்மை''', '''மடிமை குடிமைக்கண் தங்கின்தன் ஒன்னார்க்கு
  அடிமை புகுத்தி விடும்.''', '''If sloth a dwelling find mid noble family,
Bondsmen to them that hate them shall they be.''',
                               '''If idleness take up its abode in a king of high birth, it will make him a slave of his enemies.''');
        k[608] = Kural.factory(609, '''பொருட்பால்''', '''மடியின்மை''', '''குடியாண்மை யுள்வந்த குற்றம் ஒருவன்
  மடியாண்மை மாற்றக் கெடும்.''', '''Who changes slothful habits saves
Himself from all that household rule depraves.''',
                               '''When a man puts away idleness, the reproach which has come upon himself and his family will disappear.''');
        k[609] = Kural.factory(610, '''பொருட்பால்''', '''மடியின்மை''', '''மடியிலா மன்னவன் எய்தும் அடியளந்தான்
  தாஅய தெல்லாம் ஒருங்கு.''', '''The king whose life from sluggishness is rid,
Shall rule o\'er all by foot of mighty god bestrid.''',
                               '''The king who never gives way to idleness will obtain entire possession of (the whole earth) passed over by him who measured (the worlds) with His foot.''');
        k[610] = Kural.factory(611, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''அருமை உடைத்தென்று அசாவாமை வேண்டும்
  பெருமை முயற்சி தரும்.''', '''Say not, \'Tis hard\', in weak, desponding hour,
For strenuous effort gives prevailing power.''',
                               '''Yield not to the feebleness which says, "this is too difficult to be done"; labour will give the greatness (of mind) which is necessary (to do it).''');
        k[611] = Kural.factory(612, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''வினைக்கண் வினைகெடல் ஓம்பல் வினைக்குறை
  தீர்ந்தாரின் தீர்ந்தன்று உலகு.''', '''In action be thou, \'ware of act\'s defeat;
The world leaves those who work leave incomplete!''',
                               '''Take care not to give up exertion in the midst of a work; the world will abandon those who abandon their unfinished work.''');
        k[612] = Kural.factory(613, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''தாளாண்மை என்னும் தகைமைக்கண் தங்கிற்றே
  வேளாண்மை என்னுஞ் செருக்கு.''', '''In strenuous effort doth reside
The power of helping others: noble pride!''',
                               '''The lustre of munificence will dwell only with the dignity of laboriousness or efforts.''');
        k[613] = Kural.factory(614, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''தாளாண்மை இல்லாதான் வேளாண்மை பேடிகை
  வாளாண்மை போலக் கெடும்.''', '''Beneficent intent in men by whom no strenuous work is wrought,
Like battle-axe in sexless being\'s hand availeth nought.''',
                               '''The liberality of him, who does not labour, will fail, like the manliness of a hermaphrodite, who has a sword in its hand.''');
        k[614] = Kural.factory(615, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''இன்பம் விழையான் வினைவிழைவான் தன்கேளிர்
  துன்பம் துடைத்தூன்றும் தூண்.''', '''Whose heart delighteth not in pleasure, but in action finds delight,
He wipes away his kinsmen\'s grief and stands the pillar of their might.''',
                               '''He who desires not pleasure, but desires labour, will be a pillar to sustain his relations, wiping away their sorrows.''');
        k[615] = Kural.factory(616, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''முயற்சி திருவினை ஆக்கும் முயற்றின்மை
  இன்மை புகுத்தி விடும்.''', '''Effort brings fortune\'s sure increase,
Its absence brings to nothingness.''', '''Labour will produce wealth; idleness will bring poverty.''');
        k[616] = Kural.factory(617, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''மடியுளாள் மாமுகடி என்ப மடியிலான்
  தாளுளான் தாமரையி னாள்.''', '''In sluggishness is seen misfortune\'s lurid form, the wise declare;
Where man unslothful toils, she of the lotus flower is there!''',
                               '''They say that the black Mudevi (the goddess of adversity) dwells with laziness, and the Latchmi (the goddess of prosperity) dwells with the labour of the industrious.''');
        k[617] = Kural.factory(618, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''பொறியின்மை யார்க்கும் பழியன்று அறிவறிந்து
  ஆள்வினை இன்மை பழி.''', '''\'Tis no reproach unpropitious fate should ban;
But not to do man\'s work is foul disgrace to man!''',
                               '''Adverse fate is no disgrace to any one; to be without exertion and without knowing what should be known, is disgrace.''');
        k[618] = Kural.factory(619, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''தெய்வத்தான் ஆகா தெனினும் முயற்சிதன்
  மெய்வருத்தக் கூலி தரும்.''', '''Though fate-divine should make your labour vain;
Effort its labour\'s sure reward will gain.''',
                               '''Although it be said that, through fate, it cannot be attained, yet labour, with bodily exertion, will yield its reward.''');
        k[619] = Kural.factory(620, '''பொருட்பால்''', '''ஆள்வினையுடைமை''', '''ஊழையும் உப்பக்கம் காண்பர் உலைவின்றித்
  தாழாது உஞற்று பவர்.''', '''Who strive with undismayed, unfaltering mind,
At length shall leave opposing fate behind.''',
                               '''They who labour on, without fear and without fainting will see even fate (put) behind their back.''');
        k[620] = Kural.factory(621, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இடுக்கண் வருங்கால் நகுக அதனை
  அடுத்தூர்வது அஃதொப்ப தில்.''', '''Smile, with patient, hopeful heart, in troublous hour;
Meet and so vanquish grief; nothing hath equal power.''',
                               '''If troubles come, laugh; there is nothing like that, to press upon and drive away sorrow.''');
        k[621] = Kural.factory(622, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''வெள்ளத் தனைய இடும்பை அறிவுடையான்
  உள்ளத்தின் உள்ளக் கெடும்.''', '''Though sorrow, like a flood, comes rolling on,
When wise men\'s mind regards it,- it is gone.''',
                               '''A flood of troubles will be overcome by the (courageous) thought which the minds of the wise will entertain, even in sorrow.''');
        k[622] = Kural.factory(623, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இடும்பைக்கு இடும்பை படுப்பர் இடும்பைக்கு
  இடும்பை படாஅ தவர்.''', '''Who griefs confront with meek, ungrieving heart,
From them griefs, put to grief, depart.''', '''They give sorrow to sorrow, who in sorrow do not suffer sorrow.''');
        k[623] = Kural.factory(624, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''மடுத்தவா யெல்லாம் பகடன்னான் உற்ற
  இடுக்கண் இடர்ப்பாடு உடைத்து.''', '''Like bullock struggle on through each obstructed way;
From such an one will troubles, troubled, roll away.''',
                               '''Troubles will vanish (i.e., will be troubled) before the man who (struggles against difficulties) as a buffalo (drawing a cart) through deep mire.''');
        k[624] = Kural.factory(625, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''அடுக்கி வரினும் அழிவிலான் உற்ற
  இடுக்கண் இடுக்கட் படும்.''', '''When griefs press on, but fail to crush the patient heart,
Then griefs defeated, put to grief, depart.''',
                               '''The troubles of that man will be troubled (and disappear) who, however thickly they may come upon him, does not abandon (his purpose).''');
        k[625] = Kural.factory(626, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''அற்றேமென்று அல்லற் படுபவோ பெற்றேமென்று
  ஓம்புதல் தேற்றா தவர்.''', '''Who boasted not of wealth, nor gave it all their heart,
Will not bemoan the loss, when prosperous days depart.''',
                               '''Will those men ever cry out in sorrow, "we are destitute" who, (in their prosperity), give not way to (undue desire) to keep their wealth.''');
        k[626] = Kural.factory(627, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இலக்கம் உடம்பிடும்பைக் கென்று கலக்கத்தைக்
  கையாறாக் கொள்ளாதாம் மேல்.''', '''\'Man\'s frame is sorrow\'s target\', the noble mind reflects,
Nor meets with troubled mind the sorrows it expects.''',
                               '''The great will not regard trouble as trouble, knowing that the body is the butt of trouble.''');
        k[627] = Kural.factory(628, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இன்பம் விழையான் இடும்பை இயல்பென்பான்
  துன்பம் உறுதல் இலன்.''', '''He seeks not joy, to sorrow man is born, he knows;
Such man will walk unharmed by touch of human woes.''',
                               '''That man never experiences sorrow, who does not seek for pleasure, and who considers distress to be natural (to man).''');
        k[628] = Kural.factory(629, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இன்பத்துள் இன்பம் விழையாதான் துன்பத்துள்
  துன்பம் உறுதல் இலன்.''', '''Mid joys he yields not heart to joys\' control.
Mid sorrows, sorrow cannot touch his soul.''',
                               '''He does not suffer sorrow, in sorrow who does not look for pleasure in pleasure.''');
        k[629] = Kural.factory(630, '''பொருட்பால்''', '''இடுக்கணழியாமை''', '''இன்னாமை இன்பம் எனக்கொளின் ஆகுந்தன்
  ஒன்னார் விழையுஞ் சிறப்பு.''', '''Who pain as pleasure takes, he shall acquire
The bliss to which his foes in vain aspire.''',
                               '''The elevation, which even his enemies will esteem, will be gained by him, who regards pain as pleasure.''');
        k[630] = Kural.factory(631, '''பொருட்பால்''', '''அமைச்சு''', '''கருவியும் காலமும் செய்கையும் செய்யும்
  அருவினையும் மாண்டது அமைச்சு.''', '''A minister is he who grasps, with wisdom large,
Means, time, work\'s mode, and functions rare he must discharge.''',
                               '''The minister is one who can make an excellent choice of means, time, manner of execution, and the difficult undertaking (itself).''');
        k[631] = Kural.factory(632, '''பொருட்பால்''', '''அமைச்சு''', '''வன்கண் குடிகாத்தல் கற்றறிதல் ஆள்வினையோடு
  ஐந்துடன் மாண்டது அமைச்சு.''', '''A minister must greatness own of guardian power, determined mind,
Learn\'d wisdom, manly effort with the former five combined.''',
                               '''The minister is one who in addition to the aforesaid five things excels in the possession of firmness, protection of subjects, clearness by learning, and perseverance.''');
        k[632] = Kural.factory(633, '''பொருட்பால்''', '''அமைச்சு''', '''பிரித்தலும் பேணிக் கொளலும் பிரிந்தார்ப்
  பொருத்தலும் வல்ல தமைச்சு.''', '''A minister is he whose power can foes divide,
Attach more firmly friends, of severed ones can heal the breaches wide.''',
                               '''The minister is one who can effect discord (among foes), maintain the good-will of his friends and restore to friendship those who have seceded (from him).''');
        k[633] = Kural.factory(634, '''பொருட்பால்''', '''அமைச்சு''', '''தெரிதலும் தேர்ந்து செயலும் ஒருதலையாச்
  சொல்லலும் வல்லது அமைச்சு.''', '''A minister has power to see the methods help afford,
To ponder long, then utter calm conclusive word.''',
                               '''The minister is one who is able to comprehend (the whole nature of an undertaking), execute it in the best manner possible, and offer assuring advice (in time of necessity).''');
        k[634] = Kural.factory(635, '''பொருட்பால்''', '''அமைச்சு''', '''அறனறிந்து ஆன்றமைந்த சொல்லான்எஞ் ஞான்றுந்
  திறனறிந்தான் தேர்ச்சித் துணை.''', '''The man who virtue knows, has use of wise and pleasant words.
With plans for every season apt, in counsel aid affords.''',
                               '''He is the best helper (of the king) who understanding the duties, of the latter, is by his special learning, able to tender the fullest advice, and at all times conversant with the best method (of performing actions).''');
        k[635] = Kural.factory(636, '''பொருட்பால்''', '''அமைச்சு''', '''மதிநுட்பம் நூலோடு உடையார்க்கு அதிநுட்பம்
  யாவுள முன்நிற் பவை.''', '''When native subtilty combines with sound scholastic lore,
\'Tis subtilty surpassing all, which nothing stands before.''',
                               '''What (contrivances) are there so acute as to resist those who possess natural acuteness in addition to learning ?.''');
        k[636] = Kural.factory(637, '''பொருட்பால்''', '''அமைச்சு''', '''செயற்கை அற஧ந்தக் கடைத்தும் உலகத்து
  இயற்கை அறிந்து செயல்.''', '''Though knowing all that books can teach, \'tis truest tact
To follow common sense of men in act.''',
                               '''Though you are acquainted with the (theoretical) methods (of performing an act), understand the ways of the world and act accordingly.''');
        k[637] = Kural.factory(638, '''பொருட்பால்''', '''அமைச்சு''', '''அறிகொன்று அறியான் எனினும் உறுதி
  உழையிருந்தான் கூறல் கடன்.''', '''\'Tis duty of the man in place aloud to say
The very truth, though unwise king may cast his words away.''',
                               '''Although the king be utterly ignorant, it is the duty of the minister to give (him) sound advice.''');
        k[638] = Kural.factory(639, '''பொருட்பால்''', '''அமைச்சு''', '''பழுதெண்ணும் மந்திரியின் பக்கததுள் தெவ்வோர்
  எழுபது கோடி உறும்.''', '''A minister who by king\'s side plots evil things
Worse woes than countless foemen brings.''',
                               '''Far better are seventy crores of enemies (for a king) than a minister at his side who intends (his) ruin.''');
        k[639] = Kural.factory(640, '''பொருட்பால்''', '''அமைச்சு''', '''முறைப்படச் சூழ்ந்தும் முடிவிலவே செய்வர்
  திறப்பாடு இலாஅ தவர்.''', '''For gain of end desired just counsel nought avails
To minister, when tact in execution fails.''',
                               '''Those ministers who are destitute of (executive) ability will fail to carry out their projects, although they may have contrived aright.''');
        k[640] = Kural.factory(641, '''பொருட்பால்''', '''சொல்வன்மை''', '''நாநலம் என்னும் நலனுடைமை அந்நலம்
  யாநலத்து உள்ளதூஉம் அன்று.''', '''A tongue that rightly speaks the right is greatest gain,
It stands alone midst goodly things that men obtain.''',
                               '''The possession of that goodness which is called the goodness of speech is (even to others) better than any other goodness.''');
        k[641] = Kural.factory(642, '''பொருட்பால்''', '''சொல்வன்மை''', '''ஆக்கமுங் கேடும் அதனால் வருதலால்
  காத்தோம்பல் சொல்லின்கட் சோர்வு.''', '''Since gain and loss in life on speech depend,
From careless slip in speech thyself defend.''',
                               '''Since (both) wealth and evil result from (their) speech, ministers should most carefully guard themselves against faultiness therein.''');
        k[642] = Kural.factory(643, '''பொருட்பால்''', '''சொல்வன்மை''', '''கேட்டார்ப் பிணிக்கும் தகையவாய்க் கேளாரும்
  வேட்ப மொழிவதாம் சொல்.''', '''\'Tis speech that spell-bound holds the listening ear,
While those who have not heard desire to hear.''',
                               '''The (minister\'s) speech is that which seeks (to express) elements as bind his friends (to himself) and is so delivered as to make even his enemies desire (his friendship).''');
        k[643] = Kural.factory(644, '''பொருட்பால்''', '''சொல்வன்மை''', '''திறனறிந்து சொல்லுக சொல்லை அறனும்
  பொருளும் அதனினூஉங்கு இல்.''', '''Speak words adapted well to various hearers\' state;
No higher virtue lives, no gain more surely great.''',
                               '''Understand the qualities (of your hearers) and (then) make your speech; for superior to it, there is neither virtue nor wealth.''');
        k[644] = Kural.factory(645, '''பொருட்பால்''', '''சொல்வன்மை''', '''சொல்லுக சொல்லைப் பிறிதோர்சொல் அச்சொல்லை
  வெல்லுஞ்சொல் இன்மை அறிந்து.''', '''Speak out your speech, when once \'tis past dispute
That none can utter speech that shall your speech refute.''',
                               '''Deliver your speech, after assuring yourself that no counter speech can defeat your own.''');
        k[645] = Kural.factory(646, '''பொருட்பால்''', '''சொல்வன்மை''', '''வேட்பத்தாஞ் சொல்லிப் பிறர்சொல் பயன்கோடல்
  மாட்சியின் மாசற்றார் கோள்.''', '''Charming each hearer\'s ear, of others\' words to seize the sense,
Is method wise of men of spotless excellence.''',
                               '''It is the opinion of those who are free from defects in diplomacy that the minister should speak so as to make his hearers desire (to hear more) and grasp the meaning of what he hears himself.''');
        k[646] = Kural.factory(647, '''பொருட்பால்''', '''சொல்வன்மை''', '''சொலல்வல்லன் சோர்விலன் அஞ்சான் அவனை
  இகல்வெல்லல் யார்க்கும் அரிது.''', '''Mighty in word, of unforgetful mind, of fearless speech,
\'Tis hard for hostile power such man to overreach.''',
                               '''It is impossible for any one to conquer him by intrique who possesses power of speech, and is neither faulty nor timid.''');
        k[647] = Kural.factory(648, '''பொருட்பால்''', '''சொல்வன்மை''', '''விரைந்து தொழில்கேட்கும் ஞாலம் நிரந்தினிது
  சொல்லுதல் வல்லார்ப் பெறின்.''', '''Swiftly the listening world will gather round,
When men of mighty speech the weighty theme propound.''',
                               '''If there be those who can speak on various subjects in their proper order and in a pleasing manner, the world would readily accept them.''');
        k[648] = Kural.factory(649, '''பொருட்பால்''', '''சொல்வன்மை''', '''பலசொல்லக் காமுறுவர் மன்றமா சற்ற
  சிலசொல்லல் தேற்றா தவர்.''', '''Who have not skill ten faultless words to utter plain,
Their tongues will itch with thousand words man\'s ears to pain.''',
                               '''They will desire to utter many words, who do not know how to speak a few faultless ones.''');
        k[649] = Kural.factory(650, '''பொருட்பால்''', '''சொல்வன்மை''', '''இண்ருழ்த்தும் நாறா மலரனையர் கற்றது
  உணர விரித்துரையா தார்.''', '''Like scentless flower in blooming garland bound
Are men who can\'t their lore acquired to other\'s ears expound.''',
                               '''Those who are unable to set forth their acquirements (before others) are like flowers blossoming in a cluster and yet without fragrance.''');
        k[650] = Kural.factory(651, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''துணைநலம் ஆக்கம் த்ருஉம் வினைநலம்
  வேண்டிய எல்லாந் தரும்.''', '''The good external help confers is worldly gain;
By action good men every needed gift obtain.''',
                               '''The efficacy of support will yield (only) wealth; (but) the efficacy of action will yield all that is desired.''');
        k[651] = Kural.factory(652, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''என்றும் ஒருவுதல் வேண்டும் புகழொடு
  நன்றி பயவா வினை.''', '''From action evermore thyself restrain
Of glory and of good that yields no gain.''',
                               '''Ministers should at all times avoid acts which, in addition to fame, yield no benefit (for the future).''');
        k[652] = Kural.factory(653, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''ஒஓதல் வேண்டும் ஒளிமாழ்கும் செய்வினை
  ஆஅதும் என்னு மவர்.''', '''Who tell themselves that nobler things shall yet be won
All deeds that dim the light of glory must they shun.''',
                               '''Those who say, "we will become (better)" should avoid the performance of acts that would destroy (their fame).''');
        k[653] = Kural.factory(654, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''இடுக்கண் படினும் இளிவந்த செய்யார்
  நடுக்கற்ற காட்சி யவர்.''', '''Though troubles press, no shameful deed they do,
Whose eyes the ever-during vision view.''',
                               '''Those who have infallible judgement though threatened with peril will not do acts which have brought disgrace (on former ministers).''');
        k[654] = Kural.factory(655, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''எற்றென்று இரங்குவ செய்யற்க செய்வானேல்
  மற்றன்ன செய்யாமை நன்று.''', '''Do nought that soul repenting must deplore,
If thou hast sinned, \'tis well if thou dost sin no more.''',
                               '''Let a minister never do acts of which he would have to grieve saying, "what is this I have done"; (but) should he do (them), it were good that he grieved not.''');
        k[655] = Kural.factory(656, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''ஈன்றாள் பசிகாண்பான் ஆயினுஞ் செய்யற்க
  சான்றோர் பழிக்கும் வினை.''', '''Though her that bore thee hung\'ring thou behold, no deed
Do thou, that men of perfect soul have crime decreed.''',
                               '''Though a minister may see his mother starve; let him do not act which the wise would (treat with contempt).''');
        k[656] = Kural.factory(657, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''பழிமலைந்து எய்திய ஆக்கத்தின் சான்றோர்
  கழிநல் குரவே தலை.''', '''Than store of wealth guilt-laden souls obtain,
The sorest poverty of perfect soul is richer gain.''',
                               '''Far more excellent is the extreme poverty of the wise than wealth obtained by heaping up of sinful deeds.''');
        k[657] = Kural.factory(658, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''கடிந்த கடிந்தொரார் செய்தார்க்கு அவைதாம்
  முடிந்தாலும் பீழை தரும்.''', '''To those who hate reproof and do forbidden thing.
What prospers now, in after days shall anguish bring.''',
                               '''The actions of those, who have not desisted from doing deeds forbidden (by the great), will, even if they succeed, cause them sorrow.''');
        k[658] = Kural.factory(659, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''அழக்கொண்ட எல்லாம் அழப்போம் இழப்பினும்
  பிற்பயக்கும் நற்பா லவை.''', '''What\'s gained through tears with tears shall go;
From loss good deeds entail harvests of blessings grow.''',
                               '''All that has been obtained with tears (to the victim) will depart with tears (to himself); but what has been by fair means; though with loss at first, will afterwards yield fruit.''');
        k[659] = Kural.factory(660, '''பொருட்பால்''', '''வினைத்தூய்மை''', '''சலத்தால் பொருள்செய்தே மார்த்தல் பசுமண்
  கலத்துள்நீர் பெய்திரீஇ யற்று.''', '''In pot of clay unburnt he water pours and would retain,
Who seeks by wrong the realm in wealth and safety to maintain.''',
                               '''(For a minister) to protect (his king) with wealth obtained by foul means is like preserving a vessel of wet clay by filling it with water.''');
        k[660] = Kural.factory(661, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''வினைத்திட்பம் என்பது ஒருவன் மனத்திட்பம்
  மற்றைய எல்லாம் பிற.''', '''What men call \'power in action\' know for \'power of mind\'
Externe to man all other aids you find.''',
                               '''Firmness in action is (simply) one\'s firmness of mind; all other (abilities) are not of this nature.''');
        k[661] = Kural.factory(662, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''ஊறொரால் உற்றபின் ஒல்காமை இவ்விரண்டின்
  ஆறென்பர் ஆய்ந்தவர் கோள்.''', '''\'Each hindrance shun\', \'unyielding onward press, If obstacle be there,\'
These two define your way, so those that search out truth declare.''',
                               '''Not to perform a ruinous act, and not to be discouraged by the ruinous termination of an act, are the two maxims which, the wise say, from the principles of those who have investigated the subject.''');
        k[662] = Kural.factory(663, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''கடைக்கொட்கச் செய்தக்க தாண்மை இடைக்கொட்கின்
  எற்றா விழுமந் தரும்.''', '''Man\'s fitting work is known but by success achieved;
In midst the plan revealed brings ruin ne\'er to be retrieved.''',
                               '''So to perform an act as to publish it (only) at its termination is (true) manliness; for to announce it beforehand, will cause irremediable sorrow.''');
        k[663] = Kural.factory(664, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''சொல்லுதல் யார்க்கும் எளிய அரியவாம்
  சொல்லிய வண்ணம் செயல்.''', '''Easy to every man the speech that shows the way;
Hard thing to shape one\'s life by words they say!''',
                               '''To say (how an act is to be performed) is (indeed) easy for any one; but far difficult it is to do according to what has been said.''');
        k[664] = Kural.factory(665, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''வீறெய்தி மாண்டார் வினைத்திட்பம் வேந்தன்கண்
  ஊறெய்தி உள்ளப் படும்.''', '''The power in act of men renowned and great,
With king acceptance finds and fame through all the state.''',
                               '''The firmness in action of those who have become great by the excellence (of their counsel) will, by attaining its fulfilment in the person of the king, be esteemed (by all).''');
        k[665] = Kural.factory(666, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''எண்ணிய எண்ணியாங்கு எய்து எண்ணியார்
  திண்ணியர் ஆகப் பெறின்.''', '''Whate\'er men think, ev\'n as they think, may men obtain,
If those who think can steadfastness of will retain.''',
                               '''If those who have planned (an undertaking) possess firmness (in executing it) they will obtain what they have desired even as they have desired it.''');
        k[666] = Kural.factory(667, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''உருவுகண்டு எள்ளாமை வேண்டும் உருள்பெருந்தேர்க்கு
  அச்சாணி அன்னார் உடைத்து.''', '''Despise not men of modest bearing; Look not at form, but what men are:
For some there live, high functions sharing, Like linch-pin of the mighty car!''',
                               '''Let none be despised for (their) size; (for) the world has those who resemble the linch-pin of the big rolling car.''');
        k[667] = Kural.factory(668, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''கலங்காது கண்ட வினைக்கண் துளங்காது
  தூக்கங் கடிந்து செயல்.''', '''What clearly eye discerns as right, with steadfast will,
And mind unslumbering, that should man fulfil.''',
                               '''An act that has been firmly resolved on must be as firmly carried out without delay.''');
        k[668] = Kural.factory(669, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''துன்பம் உறவரினும் செய்க துணிவாற்றி
  இன்பம் பயக்கும் வினை.''', '''Though toil and trouble face thee, firm resolve hold fast,
And do the deeds that pleasure yield at last.''',
                               '''Though it should cause increasing sorrow (at the outset), do with firmness the act that yield bliss (in the end).''');
        k[669] = Kural.factory(670, '''பொருட்பால்''', '''வினைத்திட்பம்''', '''எனைத்திட்பம் எய்தியக் கண்ணும் வினைத்திட்பம்
  வேண்டாரை வேண்டாது உலகு.''', '''The world desires not men of every power possessed,
Who power in act desire not,- crown of all the rest.''',
                               '''The great will not esteem those who esteem not firmness of action, whatever other abilities the latter may possess.''');
        k[670] = Kural.factory(671, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''சூழ்ச்சி முடிவு துணிவெய்தல் அத்துணிவு
  தாழ்ச்சியுள் தங்குதல் தீது.''', '''Resolve is counsel\'s end, If resolutions halt
In weak delays, still unfulfilled, \'tis grievous fault.''',
                               '''Consultation ends in forming a resolution (to act); (but) delay in the execution of that resolve is an evil.''');
        k[671] = Kural.factory(672, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''தூங்குக தூங்கிச் செயற்பால தூங்கற்க
  தூங்காது செய்யும் வினை.''', '''Slumber when sleepy work\'s in hand: beware
Thou slumber not when action calls for sleepless care!''',
                               '''Sleep over such (actions) as may be slept over; (but) never over such as may not be slept over.''');
        k[672] = Kural.factory(673, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''ஙல்லும்வா யெல்லாம் வினைநன்றே ஒல்லாக்கால்
  செல்லும்வாய் நோக்கிச் செயல்.''', '''When way is clear, prompt let your action be;
When not, watch till some open path you see.''',
                               '''Whenever it is possible (to overcome your enemy) the act (of fighting) is certainly good; if not, endeavour to employ some more successful method.''');
        k[673] = Kural.factory(674, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''வினைபகை என்றிரண்டின் எச்சம் நினையுங்கால்
  தீயெச்சம் போலத் தெறும்.''', '''With work or foe, when you neglect some little thing,
If you reflect, like smouldering fire, \'twill ruin bring.''',
                               '''When duly considered, the incomplete execution of an undertaking and hostility will grow and destroy one like the (unextinguished) remnant of a fire.''');
        k[674] = Kural.factory(675, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''பொருள்கருவி காலம் வினையிடனொடு ஐந்தும்
  இருள்தீர எண்ணிச் செயல்.''', '''Treasure and instrument and time and deed and place of act:
These five, till every doubt remove, think o\'er with care exact.''',
                               '''Do an act after a due consideration of the (following) five, viz. money, means, time, execution and place.''');
        k[675] = Kural.factory(676, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''முடிவும் இடையூறும் முற்றியாங்கு எய்தும்
  படுபயனும் பார்த்துச் செயல்.''', '''Accomplishment, the hindrances, large profits won
By effort: these compare,- then let the work be done.''',
                               '''An act is to be performed after considering the exertion required, the obstacles to be encountered, and the great profit to be gained (on its completion).''');
        k[676] = Kural.factory(677, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''செய்வினை செய்வான் செயன்முறை அவ்வினை
  உள்ளறிவான் உள்ளம் கொளல்.''', '''Who would succeed must thus begin: first let him ask
The thoughts of them who thoroughly know the task.''',
                               '''The method of performance for one who has begun an act is to ascertain the mind of him who knows the secret thereof.''');
        k[677] = Kural.factory(678, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''வினையான் வினையாக்கிக் கோடல் நனைகவுள்
  யானையால் யானையாத் தற்று.''', '''By one thing done you reach a second work\'s accomplishment;
So furious elephant to snare its fellow brute is sent.''',
                               '''To make one undertaking the means of accomplishing another (similar to it) is like making one rutting elephant the means of capturing another.''');
        k[678] = Kural.factory(679, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''நட்டார்க்கு நல்ல செயலின் விரைந்ததே
  ஒட்டாரை ஒட்டிக் கொளல்.''', '''Than kindly acts to friends more urgent thing to do,
Is making foes to cling as friends attached to you.''',
                               '''One should rather hasten to secure the alliance of the foes (of one\'s foes) than perform good offices to one\'s friends.''');
        k[679] = Kural.factory(680, '''பொருட்பால்''', '''வினைசெயல்வகை''', '''உறைசிறியார் உள்நடுங்கல் அஞ்சிக் குறைபெறின்
  கொள்வர் பெரியார்ப் பணிந்து.''', '''The men of lesser realm, fearing the people\'s inward dread,
Accepting granted terms, to mightier ruler bow the head.''',
                               '''Ministers of small states, afraid of their people being frightened, will yield to and acknowledge their superior foes, if the latter offer them a chance of reconciliation.''');
        k[680] = Kural.factory(681, '''பொருட்பால்''', '''தூது''', '''அன்புடைமை ஆன்ற குடிப்பிறத்தல் வேந்தவாம்
  பண்புடைமை தூதுரைப்பான் பண்பு.''', '''Benevolence high birth, the courtesy kings love:-
These qualities the envoy of a king approve.''',
                               '''The qualification of an ambassador are affection (for his relations) a fitting birth, and the possession of attributes pleasing to royalty.''');
        k[681] = Kural.factory(682, '''பொருட்பால்''', '''தூது''', '''அன்பறிவு ஆராய்ந்த சொல்வன்மை தூதுரைப்பார்க்கு
  இன்றி யமையாத மூன்று.''', '''Love, knowledge, power of chosen words, three things,
Should he possess who speaks the words of kings.''',
                               '''Love (to his sovereign), knowledge (of his affairs), and a discriminating power of speech (before other sovereigns) are the three sine qua non qualifications of an ambassador.''');
        k[682] = Kural.factory(683, '''பொருட்பால்''', '''தூது''', '''நூலாருள் நூல்வல்லன் ஆகுதல் வேலாருள்
  வென்றி வினையுரைப்பான் பண்பு.''', '''Mighty in lore amongst the learned must he be,
Midst jav\'lin-bearing kings who speaks the words of victory.''',
                               '''To be powerful in politics among those who are learned (in ethics) is the character of him who speaks to lance-bearing kings on matters of triumph (to his own sovereign).''');
        k[683] = Kural.factory(684, '''பொருட்பால்''', '''தூது''', '''அறிவுரு வாராய்ந்த கல்விஇம் மூன்றன்
  செறிவுடையான் செல்க வினைக்கு.''', '''Sense, goodly grace, and knowledge exquisite.
Who hath these three for envoy\'s task is fit.''',
                               '''He may go on a mission (to foreign rulers) who has combined in him all these three. viz., (natural) sense, an attractive bearing and well-tried learning.''');
        k[684] = Kural.factory(685, '''பொருட்பால்''', '''தூது''', '''தொகச்சொல்லித் தூவாத நீக்கி நகச்சொல்லி
  நன்றி பயப்பதாந் தூது.''', '''In terms concise, avoiding wrathful speech, who utters pleasant word,
An envoy he who gains advantage for his lord.''',
                               '''He is an ambassador who (in the presence of foreign rulers) speaks briefly, avoids harshness, talks so as to make them smile, and thus brings good (to his own sovereign).''');
        k[685] = Kural.factory(686, '''பொருட்பால்''', '''தூது''', '''கற்றுக்கண் அஞ்சான் செலச்சொல்லிக் காலத்தால்
  தக்கது அறிவதாம் தூது.''', '''An envoy meet is he, well-learned, of fearless eye
Who speaks right home, prepared for each emergency.''',
                               '''He is an ambassador who having studied (politics) talks impressively, is not afraid of angry looks, and knows (to employ) the art suited to the time.''');
        k[686] = Kural.factory(687, '''பொருட்பால்''', '''தூது''', '''கடனறிந்து காலங் கருதி இடனறிந்து
  எண்ணி உரைப்பான் தலை.''', '''He is the best who knows what\'s due, the time considered well,
The place selects, then ponders long ere he his errand tell.''',
                               '''He is chief (among ambassadors) who understands the proper decorum (before foreign princes), seeks the (proper) occasion, knows the (most suitable) place, and delivers his message after (due) consideration.''');
        k[687] = Kural.factory(688, '''பொருட்பால்''', '''தூது''', '''தூய்மை துணைமை துணிவுடைமை இம்மூன்றின்
  வாய்மை வழியுரைப்பான் பண்பு.''', '''Integrity, resources, soul determined, truthfulness.
Who rightly speaks his message must these marks possess.''',
                               '''The qualifications of him who faithfully delivers his (sovereign\'s) message are purity, the support (of foreign ministers), and boldness, with truthfulness in addition to the (aforesaid) three.''');
        k[688] = Kural.factory(689, '''பொருட்பால்''', '''தூது''', '''விடுமாற்றம் வேந்தர்க்கு உரைப்பான் வடுமாற்றம்
  வாய்சேரா வன்கணவன்.''', '''His faltering lips must utter no unworthy thing,
Who stands, with steady eye, to speak the mandates of his king.''',
                               '''He alone is fit to communicate (his sovereign\'s) reply, who possesses the firmness not to utter even inadvertently what may reflect discredit (on the latter).''');
        k[689] = Kural.factory(690, '''பொருட்பால்''', '''தூது''', '''இறுதி பயப்பினும் எஞ்சாது இறைவற்கு
  உறுதி பயப்பதாம் தூது.''', '''Death to the faithful one his embassy may bring;
To envoy gains assured advantage for his king.''',
                               '''He is the ambassador who fearlessly seeks his sovereign\'s good though it should cost him his life (to deliver his message).''');
        k[690] = Kural.factory(691, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''அகலாது அணுகாது தீக்காய்வார் போல்க
  இகல்வேந்தர்ச் சேர்ந்தொழுகு வார்.''', '''Who warm them at the fire draw not too near, nor keep too much aloof;
Thus let them act who dwell beneath of warlike kings the palace-roof.''',
                               '''Ministers who serve under fickle-minded monarchs should, like those who warm themselves at the fire, be neither (too) far, nor (too) near.''');
        k[691] = Kural.factory(692, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''மன்னர் விழைப விழையாமை மன்னரால்
  மன்னிய ஆக்கந் தரும்.''', '''To those who prize not state that kings are wont to prize,
The king himself abundant wealth supplies.''',
                               '''For ministers not to cover the things desired by their kings will through the kings themselves yield them everlasting wealth.''');
        k[692] = Kural.factory(693, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''போற்றின் அரியவை போற்றல் கடுத்தபின்
  தேற்றுதல் யார்க்கும் அரிது.''', '''Who would walk warily, let him of greater faults beware;
To clear suspicions once aroused is an achievement rare.''',
                               '''Ministers who would save themselves should avoid (the commission of) serious errors for if the king\'s suspicion is once roused, no one can remove it.''');
        k[693] = Kural.factory(694, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''செவிச்சொல்லும் சேர்ந்த நகையும் அவித்தொழுகல்
  ஆன்ற பெரியா ரகத்து.''', '''All whispered words and interchange of smiles repress,
In presence of the men who kingly power possess.''',
                               '''While in the presence of the sovereign, ministers should neither whisper to nor smile at others.''');
        k[694] = Kural.factory(695, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''எப்பொருளும் ஓரார் தொடரார்மற் றப்பொருளை
  விட்டக்கால் கேட்க மறை.''', '''Seek not, ask not, the secret of the king to hear;
But if he lets the matter forth, give ear!''',
                               '''(When the king is engaged) in secret counsel (with others), ministers should neither over-hear anything whatever nor pry into it with inquisitive questions, but (wait to) listen when it is divulged (by the king himself).''');
        k[695] = Kural.factory(696, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''குறிப்பறிந்து காலங் கருதி வெறுப்பில
  வேண்டுப வேட்பச் சொலல்.''', '''Knowing the signs, waiting for fitting time, with courteous care,
Things not displeasing, needful things, declare.''',
                               '''Knowing the (king\'s disposition and seeking the right time, (the minister) should in a pleasing manner suggest things such as are desirable and not disagreeable.''');
        k[696] = Kural.factory(697, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''வேட்பன சொல்லி வினையில எஞ்ஞான்றும்
  கேட்பினும் சொல்லா விடல்.''', '''Speak pleasant things, but never utter idle word;
Not though by monarch\'s ears with pleasure heard.''',
                               '''Ministers should (always) give agreeable advice but on no occasion recommend useless actions, though requested (to do so).''');
        k[697] = Kural.factory(698, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''இளையர் இனமுறையர் என்றிகழார் நின்ற
  ஒளியோடு ஒழுகப் படும்.''', '''Say not, \'He\'s young, my kinsman,\' despising thus your king;
But reverence the glory kingly state doth bring.''',
                               '''Ministers should behave in accordance with the (Divine) light in the person of kings and not despise them saying, "He is our junior (in age) and connected with our family!".''');
        k[698] = Kural.factory(699, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''கொளப்பட்டேம் என்றெண்ணிக் கொள்ளாத செய்யார்
  துளக்கற்ற காட்சி யவர்.''', '''\'We\'ve gained his grace, boots nought what graceless acts we do\',
So deem not sages who the changeless vision view.''',
                               '''Those whose judgement is firm will not do what is disagreeable (to the sovereign) saying (within themselves) "We are esteemed by the king".''');
        k[699] = Kural.factory(700, '''பொருட்பால்''', '''மன்னரைச் சேர்ந்தொழுதல்''', '''பழையம் எனக்கருதிப் பண்பல்ல செய்யும்
  கெழுதகைமை கேடு தரும்.''', '''Who think \'We\'re ancient friends\' and do unseemly things;
To these familiarity sure ruin brings.''',
                               '''The (foolish) claim with which a minister does unbecoming acts because of his (long) familiarity (with the king) will ensure his ruin.''');
        k[700] = Kural.factory(701, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''கூறாமை நோக்க஧க் குறிப்பறிவான் எஞ்ஞான்றும்
  மாறாநீர் வையக் கணி.''', '''Who knows the sign, and reads unuttered thought, the gem is he,
Of earth round traversed by the changeless sea.''',
                               '''The minister who by looking (at the king) understands his mind without being told (of it), will be a perpetual ornament to the world which is surrounded by a never-drying sea.''');
        k[701] = Kural.factory(702, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''ஐயப் படாஅது அகத்தது உணர்வானைத்
  தெய்வத்தோ டொப்பக் கொளல்.''', '''Undoubting, who the minds of men can scan,
As deity regard that gifted man.''',
                               '''He is to be esteemed a god who is able to ascertain without a doubt what is within (one\'s mind).''');
        k[702] = Kural.factory(703, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''குறிப்பிற் குறிப்புணர் வாரை உறுப்பினுள்
  யாது கொடுத்தும் கொளல்.''', '''Who by the sign the signs interprets plain,
Give any member up his aid to gain.''',
                               '''The king should ever give whatever (is asked) of his belongings and secure him who, by the indications (of his own mind) is able to read those of another.''');
        k[703] = Kural.factory(704, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''குறித்தது கூறாமைக் கொள்வாரோ டேனை
  உறுப்போ ரனையரால் வேறு.''', '''Who reads what\'s shown by signs, though words unspoken be,
In form may seem as other men, in function nobler far is he.''',
                               '''Those who understand one\'s thoughts without being informed (thereof) and those who do not, may (indeed) resemble one another bodily; still are they different (mentally).''');
        k[704] = Kural.factory(705, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''குறிப்பிற் குறிப்புணரா வாயின் உறுப்பினுள்
  என்ன பயத்தவோ கண்.''', '''By sign who knows not sings to comprehend, what gain,
\'Mid all his members, from his eyes does he obtain?''',
                               '''Of what use are the eyes amongst one\'s members, if they cannot by their own indications dive those of another ?.''');
        k[705] = Kural.factory(706, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''அடுத்தது காட்டும் பளிங்குபோல் நெஞ்சம்
  கடுத்தது காட்டும் முகம்.''', '''As forms around in crystal mirrored clear we find,
The face will show what\'s throbbing in the mind.''',
                               '''As the mirror reflects what is near so does the face show what is uppermost in the mind.''');
        k[706] = Kural.factory(707, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''முகத்தின் முதுக்குறைந்தது உண்டோ உவப்பினும்
  காயினும் தான்முந் துறும்.''', '''Than speaking countenance hath aught more prescient skill?
Rejoice or burn with rage, \'tis the first herald still!''',
                               '''Is there anything so full of knowledge as the face ? (No.) it precedes the mind, whether (the latter is) pleased or vexed.''');
        k[707] = Kural.factory(708, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''முகம்நோக்கி நிற்க அமையும் அகம்நோக்கி
  உற்ற துணர்வார்ப் பெறின்.''', '''To see the face is quite enough, in presence brought,
When men can look within and know the lurking thought.''',
                               '''If the king gets those who by looking into his mind can understand (and remove) what has occurred (to him) it is enough that he stand looking at their face.''');
        k[708] = Kural.factory(709, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''பகைமையும் கேண்மையும் கண்ணுரைக்கும் கண்ணின்
  வகைமை உணர்வார்ப் பெறின்.''', '''The eye speaks out the hate or friendly soul of man;
To those who know the eye\'s swift varying moods to scan.''',
                               '''If a king gets ministers who can read the movements of the eye, the eyes (of foreign kings) will (themselves) reveal (to him) their hatred or friendship.''');
        k[709] = Kural.factory(710, '''பொருட்பால்''', '''குறிப்பறிதல்''', '''நுண்ணியம் என்பார் அளக்குங்கோல் காணுங்கால்
  கண்ணல்லது இல்லை பிற.''', '''The men of keen discerning soul no other test apply
(When you their secret ask) than man\'s revealing eye.''',
                               '''The measuring-rod of those (ministers) who say "we are acute" will on inquiry be found to be their (own) eyes and nothing else.''');
        k[710] = Kural.factory(711, '''பொருட்பால்''', '''அவையறிதல்''', '''அவையறிநது ஆராய்ந்து சொல்லுக சொல்லின்
  தொகையறிந்த தூய்மை யவர்.''', '''Men pure in heart, who know of words the varied force,
Should to their audience known adapt their well-arranged discourse.''',
                               '''Let the pure who know the arrangement of words speak with deliberation after ascertaining (the nature of) the court (then assembled).''');
        k[711] = Kural.factory(712, '''பொருட்பால்''', '''அவையறிதல்''', '''இடைதெரிந்து நன்குணர்ந்து சொல்லுக சொல்லின்
  நடைதெரிந்த நன்மை யவர்.''', '''Good men to whom the arts of eloquence are known,
Should seek occasion meet, and say what well they\'ve made their own.''',
                               '''Let the good who know the uses of words speak with a clear knowledge after ascertaining the time (suited to the court).''');
        k[712] = Kural.factory(713, '''பொருட்பால்''', '''அவையறிதல்''', '''அவையறியார் சொல்லல்மேற் கொள்பவர் சொல்லின்
  வகையறியார் வல்லதூஉம் இல்.''', '''Unversed in councils, who essays to speak.
Knows not the way of suasive words,- and all is weak.''',
                               '''Those who undertake to speak without knowing the (nature of the) court are ignorant of the quality of words as well as devoid of the power (of learning).''');
        k[713] = Kural.factory(714, '''பொருட்பால்''', '''அவையறிதல்''', '''ஒளியார்முன் ஒள்ளிய ராதல் வெளியார்முன்
  வான்சுதை வண்ணம் கொளல்.''', '''Before the bright ones shine as doth the light!
Before the dull ones be as purest stucco white!''',
                               '''Ministers should be lights in the assembly of the enlightned, but assume the pure whiteness of mortar (ignorance) in that of fools.''');
        k[714] = Kural.factory(715, '''பொருட்பால்''', '''அவையறிதல்''', '''நன்றென்ற வற்றுள்ளும் நன்றே முதுவருள்
  முந்து கிளவாச் செறிவு.''', '''Midst all good things the best is modest grace,
That speaks not first before the elders\' face.''',
                               '''The modesty by which one does not rush forward and speak in (an assembly of) superiors is the best among all (one\'s) good qualities.''');
        k[715] = Kural.factory(716, '''பொருட்பால்''', '''அவையறிதல்''', '''ஆற்றின் நிலைதளர்ந் தற்றே வியன்புலம்
  ஏற்றுணர்வார் முன்னர் இழுக்கு.''', '''As in the way one tottering falls, is slip before
The men whose minds are filled with varied lore.''',
                               '''(For a minister) to blunder in the presence of those who have acquired a vast store of learning and know (the value thereof) is like a good man stumbling (and falling away) from the path (of virtue).''');
        k[716] = Kural.factory(717, '''பொருட்பால்''', '''அவையறிதல்''', '''கற்றறிந்தார் கல்வி விளங்கும் கசடறச்
  சொல்தெரிதல் வல்லார் அகத்து.''', '''The learning of the learned sage shines bright
To those whose faultless skill can value it aright.''',
                               '''The learning of those who have read and understood (much) will shine in the assembly of those who faultlessly examine (the nature of) words.''');
        k[717] = Kural.factory(718, '''பொருட்பால்''', '''அவையறிதல்''', '''உணர்வ துடையார்முன் சொல்லல் வளர்வதன்
  பாத்தியுள் நீர்சொரிந் தற்று.''', '''To speak where understanding hearers you obtain,
Is sprinkling water on the fields of growing grain!''',
                               '''Lecturing to those who have the ability to understand (for themselves) is like watering a bed of plants that are growing (of themselves).''');
        k[718] = Kural.factory(719, '''பொருட்பால்''', '''அவையறிதல்''', '''புல்லவையுள் பொச்சாந்தும் சொல்லற்க நல்லவையுள்
  நன்குசலச் சொல்லு வார்.''', '''In councils of the good, who speak good things with penetrating power,
In councils of the mean, let them say nought, e\'en in oblivious hour.''',
                               '''Those who are able to speak good things impressively in an assembly of the good should not even forgetfully speak them in that of the low.''');
        k[719] = Kural.factory(720, '''பொருட்பால்''', '''அவையறிதல்''', '''அங்கணத்துள் உக்க அமிழ்தற்றால் தங்கணத்தார்
  அல்லார்முன் கோட்டி கொளல்.''', '''Ambrosia in the sewer spilt, is word
Spoken in presence of the alien herd.''',
                               '''To utter (a good word) in the assembly of those who are of inferior rank is like dropping nectar on the ground.''');
        k[720] = Kural.factory(721, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''வகையறிந்து வல்லவை வாய்சோரார் சொல்லின்
  தொகையறிந்த தூய்மை யவர்.''', '''Men, pure in heart, who know of words the varied force,
The mighty council\'s moods discern, nor fail in their discourse.''',
                               '''The pure who know the classification of words having first ascertained the nature (of the court) will not (through fear) falter in their speech before the powerful body.''');
        k[721] = Kural.factory(722, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''கற்றாருள் கற்றார் எனப்படுவர் கற்றார்முன்
  கற்ற செலச்சொல்லு வார்.''', '''Who what they\'ve learned, in penetrating words heve learned to say,
Before the learn\'d among the learn\'d most learn\'d are they.''',
                               '''Those who can agreeably set forth their acquirements before the learned will be regarded as the most learned among the learned.''');
        k[722] = Kural.factory(723, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''பகையகத்துச் சாவார் எளியர் அரியர்
  அவையகத்து அஞ்சா தவர்.''', '''Many encountering death in face of foe will hold their ground;
Who speak undaunted in the council hall are rarely found.''',
                               '''Many indeed may (fearlessly) die in the presence of (their) foes; (but) few are those who are fearless in the assembly (of the learned).''');
        k[723] = Kural.factory(724, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''கற்றார்முன் கற்ற செலச்சொல்லித் தாம்கற்ற
  மிக்காருள் மிக்க கொளல்.''', '''What you have learned, in penetrating words speak out before
The learn\'d; but learn what men more learn\'d can teach you more.''',
                               '''(Ministers) should agreeably set forth their acquirements before the learned and acquire more (knowledge) from their superiors (in learning).''');
        k[724] = Kural.factory(725, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''ஆற்றின் அளவறிந்து கற்க அவையஞ்சா
  மாற்றங் கொடுத்தற் பொருட்டு.''', '''By rule, to dialectic art your mind apply,
That in the council fearless you may make an apt reply.''',
                               '''In order to reply fearlessly before a foreign court, (ministers) should learn logic according to the rules (of grammar).''');
        k[725] = Kural.factory(726, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''வாளொடென் வன்கண்ணர் அல்லார்க்கு நூலொடென்
  நுண்ணவை அஞ்சு பவர்க்கு.''', '''To those who lack the hero\'s eye what can the sword avail?
Or science what, to those before the council keen who quail?''',
                               '''What have they to do with a sword who are not valiant, or they with learning who are afraid of an intelligent assembly ?''');
        k[726] = Kural.factory(727, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''பகையகத்துப் பேடிகை ஒள்வாள் அவையகத்து
  அஞ்சு மவன்கற்ற நூல்.''', '''As shining sword before the foe which \'sexless being\' bears,
Is science learned by him the council\'s face who fears.''',
                               '''The learning of him who is diffident before an assembly is like the shining sword of an hermaphrodite in the presence of his foes.''');
        k[727] = Kural.factory(728, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''பல்லவை கற்றும் பயமிலரே நல்லவையுள்
  நன்கு செலச்சொல்லா தார்.''', '''Though many things they\'ve learned, yet useless are they all,
To man who cannot well and strongly speak in council hall.''',
                               '''Those who cannot agreeably speak good things before a good assembly are indeed unprofitable persons inspite of all their various acquirements.''');
        k[728] = Kural.factory(729, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''கல்லா தவரின் கடையென்ப கற்றறிந்தும்
  நல்லா ரவையஞ்சு வார்.''', '''Who, though they\'ve learned, before the council of the good men quake,
Than men unlearn\'d a lower place must take.''',
                               '''They who, though they have learned and understood, are yet afraid of the assembly of the good, are said to be inferior (even) to the illiterate.''');
        k[729] = Kural.factory(730, '''பொருட்பால்''', '''அவையஞ்சாமை''', '''உளரெனினும் இல்லாரொடு ஒப்பர் களன்அஞ்சிக்
  கற்ற செலச்சொல்லா தார்.''', '''Who what they\'ve learned, in penetrating words know not to say,
The council fearing, though they live, as dead are they.''',
                               '''Those who through fear of the assembly are unable to set forth their learning in an interesting manner, though alive, are yet like the dead.''');
        k[730] = Kural.factory(731, '''பொருட்பால்''', '''நாடு''', '''தள்ளா விளையுளும் தக்காரும் தாழ்விலாச்
  செல்வரும் சேர்வது நாடு.''', '''Where spreads fertility unfailing, where resides a band,
Of virtuous men, and those of ample wealth, call that a \'land\'''',
                               '''A kingdom is that in which (those who carry on) a complete cultivation, virtuous persons, and merchants with inexhaustible wealth, dwell together.''');
        k[731] = Kural.factory(732, '''பொருட்பால்''', '''நாடு''', '''பெரும்பொருளால் பெட்டக்க தாகி அருங்கேட்டால்
  ஆற்ற விளைவது நாடு.''', '''That is a \'land\' which men desire for wealth\'s abundant share,
Yielding rich increase, where calamities are rare.''',
                               '''A kingdom is that which is desire for its immense wealth, and which grows greatly in prosperity, being free from destructive causes.''');
        k[732] = Kural.factory(733, '''பொருட்பால்''', '''நாடு''', '''பொறையொருங்கு மேல்வருங்கால் தாங்கி இறைவற்கு
  இறையொருங்கு நேர்வது நாடு.''', '''When burthens press, it bears; Yet, With unfailing hand
To king due tribute pays: that is the \'land\'''',
                               '''A kingdom is that which can bear any burden that may be pressed on it (from adjoining kingdoms) and (yet) pay the full tribute to its sovereign.''');
        k[733] = Kural.factory(734, '''பொருட்பால்''', '''நாடு''', '''உறுபசியும் ஓவாப் பிணியும் செறுபகையும்
  சேரா தியல்வது நாடு.''', '''That is a \'land\' whose peaceful annals know,
Nor famine fierce, nor wasting plague, nor ravage of the foe.''',
                               '''A kingdom is that which continues to be free from excessive starvation, irremediable epidemics, and destructive foes.''');
        k[734] = Kural.factory(735, '''பொருட்பால்''', '''நாடு''', '''பல்குழுவும் பாழ்செய்யும் உட்பகையும் வேந்தலைக்கும்
  கொல்குறும்பும் இல்லத''', '''From factions free, and desolating civil strife, and band
Of lurking murderers that king afflict, that is the \'land\'.''',
                               '''A kingdom is that which is without various (irregular) associations, destructive internal enemies, and murderous savages who (sometimes) harass the sovereign.''');
        k[735] = Kural.factory(736, '''பொருட்பால்''', '''நாடு''', '''கேடறியாக் கெட்ட இடத்தும் வளங்குன்றா
  நாடென்ப நாட்டின் தலை.''', '''Chief of all lands is that, where nought disturbs its peace;
Or, if invaders come, still yields its rich increase.''',
                               '''The learned say that the best kingdom is that which knows no evil (from its foes), and, if injured (at all), suffers no diminution in its fruitfulness.''');
        k[736] = Kural.factory(737, '''பொருட்பால்''', '''நாடு''', '''இருபுனலும் வாய்ந்த மலையும் வருபுனலும்
  வல்லரணும் நாட்டிற்கு உறுப்பு.''', '''Waters from rains and springs, a mountain near, and waters thence;
These make a land, with fortress\' sure defence.''',
                               '''The constituents of a kingdom are the two waters (from above and below), well situated hills and an undestructible fort.''');
        k[737] = Kural.factory(738, '''பொருட்பால்''', '''நாடு''', '''பிணியின்மை செல்வம் விளைவின்பம் ஏமம்
  அணியென்ப நாட்டிவ் வைந்து.''', '''A country\'s jewels are these five: unfailing health,
Fertility, and joy, a sure defence, and wealth.''',
                               '''Freedom from epidemics, wealth, produce, happiness and protection (to subjects); these five, the learned, say, are the ornaments of a kingdom.''');
        k[738] = Kural.factory(739, '''பொருட்பால்''', '''நாடு''', '''நாடென்ப நாடா வளத்தன நாடல்ல
  நாட வளந்தரு நாடு.''', '''That is a land that yields increase unsought,
That is no land whose gifts with toil are bought.''',
                               '''The learned say that those are kingdom whose wealth is not laboured for, and those not, whose wealth is only obtained through labour.''');
        k[739] = Kural.factory(740, '''பொருட்பால்''', '''நாடு''', '''ஆங்கமை வெய்தியக் கண்ணும் பயமின்றே
  வேந்தமை வில்லாத நாடு.''', '''Though blest with all these varied gifts\' increase,
A land gains nought that is not with its king at peace.''',
                               '''Although in possession of all the above mentioned excellences, these are indeed of no use to a country, in the absence of harmony between the sovereign and the sujects.''');
        k[740] = Kural.factory(741, '''பொருட்பால்''', '''அரண்''', '''ஆற்று பவர்க்கும் அரண்பொருள் அஞ்சித்தற்
  போற்று பவர்க்கும் பொருள்.''', '''A fort is wealth to those who act against their foes;
Is wealth to them who, fearing, guard themselves from woes.''',
                               '''A fort is an object of importance to those who march (against their foes) as well as to those who through fear (of pursuers) would seek it for shelter.''');
        k[741] = Kural.factory(742, '''பொருட்பால்''', '''அரண்''', '''மணிநீரும் மண்ணும் மலையும் அணிநிழற்
  காடும் உடைய தரண்.''', '''A fort is that which owns fount of waters crystal clear,
An open space, a hill, and shade of beauteous forest near.''',
                               '''A fort is that which has everlasting water, plains, mountains and cool shady forests.''');
        k[742] = Kural.factory(743, '''பொருட்பால்''', '''அரண்''', '''உயர்வகலம் திண்மை அருமைஇந் நான்கின்
  அமைவரண் என்றுரைக்கும் நூல்.''', '''Height, breadth, strength, difficult access:
Science declares a fort must these possess.''',
                               '''The learned say that a fortress is an enclosure having these four (qualities) viz., height, breadth, strength and inaccessibility.''');
        k[743] = Kural.factory(744, '''பொருட்பால்''', '''அரண்''', '''சிறுகாப்பிற் பேரிடத்த தாகி உறுபகை
  ஊக்கம் அழிப்ப தரண்.''', '''A fort must need but slight defence, yet ample be,
Defying all the foeman\'s energy.''',
                               '''A fort is that which has an extensive space within, but only small places to be guarded, and such as can destroy the courage of besieging foes.''');
        k[744] = Kural.factory(745, '''பொருட்பால்''', '''அரண்''', '''கொளற்கரிதாய்க் கொண்டகூழ்த் தாகி அகத்தார்
  நிலைக்கெளிதாம் நீரது அரண்.''', '''Impregnable, containing ample stores of food,
A fort for those within, must be a warlike station good.''',
                               '''A fort is that which cannot be captured, which abounds in suitable provisions, and affords a position of easy defence to its inmates.''');
        k[745] = Kural.factory(746, '''பொருட்பால்''', '''அரண்''', '''எல்லாப் பொருளும் உடைத்தாய் இடத்துதவும்
  நல்லாள் உடையது அரண்.''', '''A fort, with all munitions amply stored,
In time of need should good reserves afford.''',
                               '''A fort is that which has all (needful) things, and excellent heroes that can help it against destruction (by foes).''');
        k[746] = Kural.factory(747, '''பொருட்பால்''', '''அரண்''', '''முற்றியும் முற்றா தெறிந்தும் அறைப்படுத்தும்
  பற்றற் கரியது அரண்.''', '''A fort should be impregnable to foes who gird it round,
Or aim there darts from far, or mine beneath the ground.''',
                               '''A fort is that which cannot be captured by blockading, assaulting, or undermining it.''');
        k[747] = Kural.factory(748, '''பொருட்பால்''', '''அரண்''', '''முற்றாற்றி முற்றி யவரையும் பற்றாற்றிப்
  பற்றியார் வெல்வது அரண்.''', '''Howe\'er the circling foe may strive access to win,
A fort should give the victory to those who guard within.''',
                               '''That is a fort whose inmates are able to overcome without losing their ground, even abler men who have besieged it.''');
        k[748] = Kural.factory(749, '''பொருட்பால்''', '''அரண்''', '''முனைமுகத்து மாற்றலர் சாய வினைமுகத்து
  வீறெய்தி மாண்ட தரண்.''', '''At outset of the strife a fort should foes dismay;
And greatness gain by deeds in every glorious day.''',
                               '''A fort is that which derives excellence from the stratagems made (by its inmates) to defeat their enemies in the battlefield.''');
        k[749] = Kural.factory(750, '''பொருட்பால்''', '''அரண்''', '''எனைமாட்சித் தாகியக் கண்ணும் வினைமாட்சி
  இல்லார்கண் இல்லது அரண்.''', '''Howe\'er majestic castled walls may rise,
To craven souls no fortress strength supplies.''',
                               '''Although a fort may possess all (the above-said) excellence, it is, as it were without these, if its inmates possess not the excellence of action.''');
        k[750] = Kural.factory(751, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''பொருளல் லவரைப் பொருளாகச் செய்யும்
  பொருளல்லது இல்லை பொருள்.''', '''Nothing exists save wealth, that can
Change man of nought to worthy man.''',
                               '''Besides wealth there is nothing that can change people of no importance into those of (some) importance.''');
        k[751] = Kural.factory(752, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''இல்லாரை எல்லாரும் எள்ளுவர் செல்வரை
  எல்லாரும் செய்வர் சிறப்பு.''', '''Those who have nought all will despise;
All raise the wealthy to the skies.''', '''All despise the poor; (but) all praise the rich.''');
        k[752] = Kural.factory(753, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''பொருளென்னும் பொய்யா விளக்கம் இருளறுக்கும்
  எண்ணிய தேயத்துச் சென்று.''', '''Wealth, the lamp unfailing, speeds to every land,
Dispersing darkness at its lord\'s command.''',
                               '''The imperishable light of wealth goes into regions desired (by its owner) and destroys the darkness (of enmity therein).''');
        k[753] = Kural.factory(754, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''அறன்ஈனும் இன்பமும் ஈனும் திறனறிந்து
  தீதின்றி வந்த பொருள்.''', '''Their wealth, who blameless means can use aright,
Is source of virtue and of choice delight.''',
                               '''The wealth acquired with a knowledge of the proper means and without foul practices will yield virtue and happiness.''');
        k[754] = Kural.factory(755, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''அருளொடும் அன்பொடும் வாராப் பொருளாக்கம்
  புல்லார் புரள விடல்.''', '''Wealth gained by loss of love and grace,
Let man cast off from his embrace.''',
                               '''(Kings) should rather avoid than seek the accumulation of wealth which does not flow in with mercy and love.''');
        k[755] = Kural.factory(756, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''உறுபொருளும் உல்கு பொருளும்தன் ஒன்னார்த்
  தெறுபொருளும் வேந்தன் பொருள்.''', '''Wealth that falls to him as heir, wealth from the kingdom\'s dues,
The spoils of slaughtered foes; these are the royal revenues.''',
                               '''Unclaimed wealth, wealth acquired by taxes, and wealth (got) by conquest of foes are (all) the wealth of the king.''');
        k[756] = Kural.factory(757, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''அருளென்னும் அன்பீன் குழவி பொருளென்னும்
  செல்வச் செவிலியால் உண்டு.''', '''\'Tis love that kindliness as offspring bears:
And wealth as bounteous nurse the infant rears.''',
                               '''The child mercy which is borne by love grows under the care of the rich nurse of wealth.''');
        k[757] = Kural.factory(758, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''குன்றேறி யானைப்போர் கண்டற்றால் தன்கைத்தொன்று
  உண்டாகச் செய்வான் வினை.''', '''As one to view the strife of elephants who takes his stand,
On hill he\'s climbed, is he who works with money in his hand.''',
                               '''An undertaking of one who has wealth in one\'s hands is like viewing an elephant-fight from a hill-top.''');
        k[758] = Kural.factory(759, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''செய்க பொருளைச் செறுநர் செருக்கறுக்கும்
  எஃகதனிற் கூரிய தில்.''', '''Make money! Foeman\'s insolence o\'ergrown
To lop away no keener steel is known.''',
                               '''Accumulate wealth; it will destroy the arrogance of (your) foes; there is no weapon sharper than it.''');
        k[759] = Kural.factory(760, '''பொருட்பால்''', '''பொருள்செயல்வகை''', '''ஒண்பொருள் காழ்ப்ப இயற்றியார்க்கு எண்பொருள்
  ஏனை இரண்டும் ஒருங்கு.''', '''Who plenteous store of glorious wealth have gained,
By them the other two are easily obtained.''',
                               '''To those who have honestly acquired an abundance of riches, the other two, (virtue and pleasure) are things easy (of acquisition).''');
        k[760] = Kural.factory(761, '''பொருட்பால்''', '''படைமாட்சி''', '''உறுப்பமைந்து ஊறஞ்சா வெல்படை வேந்தன்
  வெறுக்கையுள் எல்லாம் தலை.''', '''A conquering host, complete in all its limbs, that fears no wound,
Mid treasures of the king is chiefest found.''',
                               '''The army which is complete in (its) parts and conquers without fear of wounds is the chief wealth of the king.''');
        k[761] = Kural.factory(762, '''பொருட்பால்''', '''படைமாட்சி''', '''உலைவிடத்து ஊறஞ்சா வன்கண் தொலைவிடத்துத்
  தொல்படைக் கல்லால் அரிது.''', '''In adverse hour, to face undaunted might of conquering foe,
Is bravery that only veteran host can show.''',
                               '''Ancient army can alone have the valour which makes it stand by its king at the time of defeat, fearless of wounds and unmindful of its reduced strength.''');
        k[762] = Kural.factory(763, '''பொருட்பால்''', '''படைமாட்சி''', '''ஒலித்தக்கால் என்னாம் உவரி எலிப்பகை
  நாகம் உயிர்ப்பக் கெடும்.''', '''Though, like the sea, the angry mice send forth their battle cry;
What then? The dragon breathes upon them, and they die!''',
                               '''What if (a host of) hostile rats roar like the sea ? They will perish at the mere breath of the cobra.''');
        k[763] = Kural.factory(764, '''பொருட்பால்''', '''படைமாட்சி''', '''அழிவின்றி அறைபோகா தாகி வழிவந்த
  வன்க ணதுவே படை.''', '''That is a host, by no defeats, by no desertions shamed,
For old hereditary courage famed.''',
                               '''That indeed is an army which has stood firm of old without suffering destruction or deserting (to the enemy).''');
        k[764] = Kural.factory(765, '''பொருட்பால்''', '''படைமாட்சி''', '''கூற்றுடன்று மேல்வரினும் கூடி எதிர்நிற்கும்
  ஆற்ற லதுவே படை.''', '''That is a \'host\' that joins its ranks, and mightily withstands,
Though death with sudden wrath should fall upon its bands.''',
                               '''That indeed is an army which is capable of offering a united resistance, even if Yama advances against it with fury.''');
        k[765] = Kural.factory(766, '''பொருட்பால்''', '''படைமாட்சி''', '''மறமானம் மாண்ட வழிச்செலவு தேற்றம்
  எனநான்கே ஏமம் படைக்கு.''', '''Valour with honour, sure advance in glory\'s path, with confidence;
To warlike host these four are sure defence.''',
                               '''Valour, honour, following in the excellent-footsteps (of its predecessors) and trust-worthiness; these four alone constitute the safeguard of an army.''');
        k[766] = Kural.factory(767, '''பொருட்பால்''', '''படைமாட்சி''', '''தார்தாங்கிச் செல்வது தானை தலைவந்த
  போர்தாங்கும் தன்மை அறிந்து.''', '''A valiant army bears the onslaught, onward goes,
Well taught with marshalled ranks to meet their coming foes.''',
                               '''That is an army which knowing the art of warding off an impending struggle, can bear against the dust-van (of a hostile force).''');
        k[767] = Kural.factory(768, '''பொருட்பால்''', '''படைமாட்சி''', '''அடல்தகையும் ஆற்றலும் இல்லெனினும் தானை
  படைத்தகையால் பாடு பெறும்.''', '''Though not in war offensive or defensive skilled;
An army gains applause when well equipped and drilled.''',
                               '''Though destitute of courage to fight and strength (to endure), an army may yet gain renown by the splendour of its appearance.''');
        k[768] = Kural.factory(769, '''பொருட்பால்''', '''படைமாட்சி''', '''சிறுமையும் செல்லாத் துனியும் வறுமையும்
  இல்லாயின் வெல்லும் படை.''', '''Where weakness, clinging fear and poverty
Are not, the host will gain the victory.''',
                               '''An army can triumph (over its foes) if it is free from diminution; irremediable aversion and poverty.''');
        k[769] = Kural.factory(770, '''பொருட்பால்''', '''படைமாட்சி''', '''நிலைமக்கள் சால உடைத்தெனினும் தானை
  தலைமக்கள் இல்வழி இல்.''', '''Though men abound, all ready for the war,
No army is where no fit leaders are.''',
                               '''Though an army may contain a large number of permanent soldiers, it cannot last if it has no generals.''');
        k[770] = Kural.factory(771, '''பொருட்பால்''', '''படைச்செருக்கு''', '''என்னைமுன் நில்லன்மின் தெவ்விர் பலரென்னை
  முன்நின்று கல்நின் றவர்.''', '''Ye foes! stand not before my lord! for many a one
Who did my lord withstand, now stands in stone!''',
                               '''O my foes, stand not before my leader; (for) many are those who did so but afterwards stood (in the shape of) statues.''');
        k[771] = Kural.factory(772, '''பொருட்பால்''', '''படைச்செருக்கு''', '''கான முயலெய்த அம்பினில் யானை
  பிழைத்தவேல் ஏந்தல் இனிது.''', '''Who aims at elephant, though dart should fail, has greater praise.
Than he who woodland hare with winged arrow slays.''',
                               '''It is more pleasant to hold the dart that has missed an elephant than that which has hit hare in the forest.''');
        k[772] = Kural.factory(773, '''பொருட்பால்''', '''படைச்செருக்கு''', '''பேராண்மை என்ப தறுகண்ஒன் றுற்றக்கால்
  ஊராண்மை மற்றதன் எஃகு.''', '''Fierceness in hour of strife heroic greatness shows;
Its edge is kindness to our suffering foes.''',
                               '''The learned say that fierceness (incontest with a foe) is indeed great valour; but to become a benefactor in case of accident (to a foe) is the extreme (limit) of that valour.''');
        k[773] = Kural.factory(774, '''பொருட்பால்''', '''படைச்செருக்கு''', '''கைவேல் களிற்றொடு போக்கி வருபவன்
  மெய்வேல் பறியா நகும்.''', '''At elephant he hurls the dart in hand; for weapon pressed,
He laughs and plucks the javelin from his wounded breast.''',
                               '''The hero who after casting the lance in his hand on an elephant, comes (in search of another) will pluck the one (that sticks) in his body and laugh (exultingly).''');
        k[774] = Kural.factory(775, '''பொருட்பால்''', '''படைச்செருக்கு''', '''விழித்தகண் வேல்கொண டெறிய அழித்திமைப்பின்
  ஒட்டன்றோ வன்க ணவர்க்கு.''', '''To hero fearless must it not defeat appear,
If he but wink his eye when foemen hurls his spear.''',
                               '''Is it not a defeat to the valiant to wink and destroy their ferocious look when a lance in cast at them (by their foe) ?''');
        k[775] = Kural.factory(776, '''பொருட்பால்''', '''படைச்செருக்கு''', '''விழுப்புண் படாதநாள் எல்லாம் வழுக்கினுள்
  வைக்கும்தன் நாளை எடுத்து.''', '''The heroes, counting up their days, set down as vain
Each day when they no glorious wound sustain.''',
                               '''The hero will reckon among wasted days all those on which he had not received severe wounds.''');
        k[776] = Kural.factory(777, '''பொருட்பால்''', '''படைச்செருக்கு''', '''சுழலும் இசைவேண்டி வேண்டா உயிரார்
  கழல்யாப்புக் காரிகை நீர்த்து.''', '''Who seek for world-wide fame, regardless of their life,
The glorious clasp adorns, sign of heroic strife.''',
                               '''The fastening of ankle-ring by those who disire a world-wide renown and not (the safety of) their lives is like adorning (themselves).''');
        k[777] = Kural.factory(778, '''பொருட்பால்''', '''படைச்செருக்கு''', '''உறின்உயிர் அஞ்சா மறவர் இறைவன்
  செறினும் சீர்குன்றல் இலர்.''', '''Fearless they rush where\'er \'the tide of battle rolls\';
The king\'s reproof damps not the ardour of their eager souls.''',
                               '''The heroes who are not afraid of losing their life in a contest will not cool their ardour, even if the king prohibits (their fighting).''');
        k[778] = Kural.factory(779, '''பொருட்பால்''', '''படைச்செருக்கு''', '''இழைத்தது இகவாமைச் சாவாரை யாரே
  பிழைத்தது ஒறுக்கிற் பவர்.''', '''Who says they err, and visits them scorn,
Who die and faithful guard the vow they\'ve sworn?''',
                               '''Who would reproach with failure those who seal their oath with their death ?''');
        k[779] = Kural.factory(780, '''பொருட்பால்''', '''படைச்செருக்கு''', '''புரந்தார்கண் நீர்மல்கச் சாகிற்பின் சாக்காடு
  இரந்துகோள் தக்கது உடைத்து.''', '''If monarch\'s eyes o\'erflow with tears for hero slain,
Who would not beg such boon of glorious death to gain?''',
                               '''If (heroes) can so die as to fill with tears the eyes of their rulers, such a death deserves to be obtained even by begging.''');
        k[780] = Kural.factory(781, '''பொருட்பால்''', '''நட்பு''', '''செயற்கரிய யாவுள நட்பின் அதுபோல்
  வினைக்கரிய யாவுள காப்பு.''', '''What so hard for men to gain as friendship true?
What so sure defence \'gainst all that foe can do?''',
                               '''What things are there so difficult to acquire as friendship ? What guards are there so difficult to break through by the efforts (of one\'s foes) ?''');
        k[781] = Kural.factory(782, '''பொருட்பால்''', '''நட்பு''', '''நிறைநீர நீரவர் கேண்மை பிறைமதிப்
  பின்னீர பேதையார் நட்பு.''', '''Friendship with men fulfilled of good Waxes like the crescent moon;
Friendship with men of foolish mood, Like the full orb, waneth soon.''',
                               '''The friendship of the wise waxes like the new moon; (but) that of fools wanes like the full moon.''');
        k[782] = Kural.factory(783, '''பொருட்பால்''', '''நட்பு''', '''நவில்தொறும் நூல்நயம் போலும் பயில்தொறும்
  பண்புடை யாளர் தொடர்பு.''', '''Learned scroll the more you ponder, Sweeter grows the mental food;
So the heart by use grows fonder, Bound in friendship with the good.''',
                               '''Like learning, the friendship of the noble, the more it is cultivated, the more delightful does it become.''');
        k[783] = Kural.factory(784, '''பொருட்பால்''', '''நட்பு''', '''நகுதற் பொருட்டன்று நட்டல் மிகுதிக்கண்
  மேற்செனறு இடித்தற் பொருட்டு.''', '''Nor for laughter only friendship all the pleasant day,
But for strokes of sharp reproving, when from right you stray.''',
                               '''Friendship is to be practised not for the purpose of laughing but for that of being beforehand in giving one another sharp rebukes in case of transgression.''');
        k[784] = Kural.factory(785, '''பொருட்பால்''', '''நட்பு''', '''புணர்ச்சி பழகுதல் வேண்டா உணர்ச்சிதான்
  நட்பாங் கிழமை தரும்.''', '''Not association constant, not affection\'s token bind;
\'Tis the unison of feeling friends unites of kindred mind.''',
                               '''Living together and holding frequent intercourse are not necessary (for friendship); (mutual) understanding can alone create a claim for it.''');
        k[785] = Kural.factory(786, '''பொருட்பால்''', '''நட்பு''', '''முகநக நட்பது நட்பன்று நெஞ்சத்து
  அகநக நட்பது நட்பு.''', '''Not the face\'s smile of welcome shows the friend sincere,
But the heart\'s rejoicing gladness when the friend is near.''',
                               '''The love that dwells (merely in the smiles of the face is not friendship; (but) that which dwells deep in the smiles of the heart is true friendship.''');
        k[786] = Kural.factory(787, '''பொருட்பால்''', '''நட்பு''', '''அழிவி னவைநீக்கி ஆறுய்த்து அழிவின்கண்
  அல்லல் உழப்பதாம் நட்பு.''', '''Friendship from ruin saves, in way of virtue keeps;
In troublous time, it weeps with him who weeps.''',
                               '''(True) friendship turns aside from evil (ways) makes (him) walk in the (good) way, and, in case of loss if shares his sorrow (with him).''');
        k[787] = Kural.factory(788, '''பொருட்பால்''', '''நட்பு''', '''உடுக்கை இழந்தவன் கைபோல ஆங்கே
  இடுக்கண் களைவதாம் நட்பு.''', '''As hand of him whose vesture slips away,
Friendship at once the coming grief will stay.''',
                               '''(True) friendship hastens to the rescue of the afflicted (as readily) as the hand of one whose garment is loosened (before an assembly).''');
        k[788] = Kural.factory(789, '''பொருட்பால்''', '''நட்பு''', '''நட்பிற்கு வீற்றிருக்கை யாதெனின் கொட்பின்றி
  ஒல்லும்வாய் ஊன்றும் நிலை.''', '''And where is friendship\'s royal seat? In stable mind,
Where friend in every time of need support may find.''',
                               '''Friendship may be said to be on its throne when it possesses the power of supporting one at all times and under all circumstances, (in the practice or virtue and wealth).''');
        k[789] = Kural.factory(790, '''பொருட்பால்''', '''நட்பு''', '''இனையர் இவரெமக்கு இன்னம்யாம் என்று
  புனையினும் புல்லென்னும் நட்பு.''', '''Mean is the friendship that men blazon forth,
\'He\'s thus to me\' and \'such to him my worth\'.''',
                               '''Though friends may praise one another saying, "He is so intimate with us, and we so much (with him)"; (still) such friendship will appear mean.''');
        k[790] = Kural.factory(791, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''நாடாது நட்டலிற் கேடில்லை நட்டபின்
  வீடில்லை நட்பாள் பவர்க்கு.''', '''To make an untried man your friend is ruin sure;
For friendship formed unbroken must endure.''',
                               '''As those who are of a friendly nature will not forsake (a friend) after once loving (him), there is no evil so great as contracting a friendship without due inquiry.''');
        k[791] = Kural.factory(792, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''ஆய்ந்தாய்ந்து கொள்ளாதான் கேண்மை கடைமுறை
  தான்சாம் துயரம் தரும்.''', '''Alliance with the man you have not proved and proved again,
In length of days will give you mortal pain.''',
                               '''The friendship contracted by him who has not made repeated inquiry will in the end grieve (him) to death.''');
        k[792] = Kural.factory(793, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''குணமும் குடிமையும் குற்றமும் குன்றா
  இனனும் அறிந்தியாக்க நட்பு.''', '''Temper, descent, defects, associations free
From blame: know these, then let the man be friend to thee.''',
                               '''Make friendship (with one) after ascertaining (his) character, birth, defects and the whole of one\'s relations.''');
        k[793] = Kural.factory(794, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''குடிப்பிறந்து தன்கண் பழிநாணு வானைக்
  கொடுத்தும் கொளல்வேண்டும் நட்பு.''', '''Who, born of noble race, from guilt would shrink with shame,
Pay any price so you as friend that man may claim.''',
                               '''The friendship of one who belongs to a (good) family and is afraid of (being charged with) guilt, is worth even purchasing.''');
        k[794] = Kural.factory(795, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''அழச்சொல்லி அல்லது இடித்து வழக்கறிய
  வல்லார்நடபு ஆய்ந்து கொளல்.''', '''Make them your chosen friend whose words repentance move,
With power prescription\'s path to show, while evil they reprove.''',
                               '''You should examine and secure the friendship of those who can speak so as to make you weep over a crime (before its commission) or rebuke you severely (after you have done it) and are able to teach you (the ways of) the world.''');
        k[795] = Kural.factory(796, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''கேட்டினும் உண்டோர் உறுதி கிளைஞரை
  நீட்டி அளப்பதோர் கோல்.''', '''Ruin itself one blessing lends:
\'Tis staff that measures out one\'s friends.''',
                               '''Even in ruin there is some good; (for) it is a rod by which one may measure fully (the affection of one\'s) relations.''');
        k[796] = Kural.factory(797, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''ஊதியம் என்பது ஒருவற்குப் பேதையார்
  கேண்மை ஒரீஇ விடல்.''', '''\'Tis gain to any man, the sages say,
Friendship of fools to put away.''', '''It is indead a gain for one to renounce the friendship of fools.''');
        k[797] = Kural.factory(798, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''உள்ளற்க உள்ளம் சிறுகுவ கொள்ளற்க
  அல்லற்கண் ஆற்றறுப்பார் நட்பு.''', '''Think not the thoughts that dwarf the soul; nor take
For friends the men who friends in time of grief forsake.''',
                               '''Do not think of things that discourage your mind, nor contract friendship with those who would forsake you in adversity.''');
        k[798] = Kural.factory(799, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''கெடுங்காலைக் கைவிடுவார் கேண்மை அடுங்காலை
  உள்ளினும் உள்ளஞ் சுடும்.''', '''Of friends deserting us on ruin\'s brink,
\'Tis torture e\'en in life\'s last hour to think.''',
                               '''The very thought of the friendship of those who have deserted one at the approach of adversity will burn one\'s mind at the time of death.''');
        k[799] = Kural.factory(800, '''பொருட்பால்''', '''நட்பாராய்தல்''', '''மருவுக மாசற்றார் கேண்மைஒன் றீத்தும்
  ஒருவுக ஒப்பிலார் நட்பு.''', '''Cling to the friendship of the spotless one\'s; whate\'er you pay.
Renounce alliance with the men of evil way.''',
                               '''Continue to enjoy the friendship of the pure; (but) renounce even with a gift, the friendship of those who do not agree (with the world).''');
        k[800] = Kural.factory(801, '''பொருட்பால்''', '''பழைமை''', '''பழைமை எனப்படுவது யாதெனின் யாதும்
  கிழமையைக் கீழ்ந்திடா நட்பு.''', '''Familiarity is friendship\'s silent pact,
That puts restraint on no familiar act.''',
                               '''Imtimate friendship is that which cannot in the least be injured by (things done through the) right (of longstanding intimacy).''');
        k[801] = Kural.factory(802, '''பொருட்பால்''', '''பழைமை''', '''நட்பிற் குறுப்புக் கெழுதகைமை மற்றதற்கு
  உப்பாதல் சான்றோர் கடன்.''', '''Familiar freedom friendship\'s very frame supplies;
To be its savour sweet is duty of the wise.''',
                               '''The constituents of friendship are (things done through) the right of intimacy; to be pleased with such a right is the duty of the wise.''');
        k[802] = Kural.factory(803, '''பொருட்பால்''', '''பழைமை''', '''பழகிய நட்பெவன் செய்யுங் கெழுதகைமை
  செய்தாங்கு அமையாக் கடை.''', '''When to familiar acts men kind response refuse,
What fruit from ancient friendship\'s use?''',
                               '''Of what avail is long-standing friendship, if friends do not admit as their own actions done through the right of intimacy ?''');
        k[803] = Kural.factory(804, '''பொருட்பால்''', '''பழைமை''', '''விழைதகையான் வேண்டி இருப்பர் கெழுதகையாற்
  கேளாது நட்டார் செயின்.''', '''When friends unbidden do familiar acts with loving heart,
Friends take the kindly deed in friendly part.''',
                               '''If friends, through the right of friendship, do (anything) without being asked, the wise will be pleased with them on account of its desirability.''');
        k[804] = Kural.factory(805, '''பொருட்பால்''', '''பழைமை''', '''பேதைமை ஒன்றோ பெருங்கிழமை என்றுணர்க
  நோதக்க நட்டார் செயின்.''', '''Not folly merely, but familiar carelessness,
Esteem it, when your friends cause you distress.''',
                               '''If friends should perform what is painful, understand that it is owing not only to ignorance, but also to the strong claims of intimacy.''');
        k[805] = Kural.factory(806, '''பொருட்பால்''', '''பழைமை''', '''எல்லைக்கண் நின்றார் துறவார் தொலைவிடத்தும்
  தொல்லைக்கண் நின்றார் தொடர்பு.''', '''Who stand within the bounds quit not, though loss impends,
Association with the old familiar friends.''',
                               '''Those who stand within the limits (of true friendship) will not even in adversity give up the intimacy of long-standing friends.''');
        k[806] = Kural.factory(807, '''பொருட்பால்''', '''பழைமை''', '''அழிவந்த செய்யினும் அன்பறார் அன்பின்
  வழிவந்த கேண்மை யவர்.''', '''True friends, well versed in loving ways,
Cease not to love, when friend their love betrays.''',
                               '''Those who have (long) stood in the path of affection will not give it up even if their friends cause (them) their ruin.''');
        k[807] = Kural.factory(808, '''பொருட்பால்''', '''பழைமை''', '''கேளிழுக்கம் கேளாக் கெழுதகைமை வல்லார்க்கு
  நாளிழுக்கம் நட்டார் செயின்.''', '''In strength of friendship rare of friend\'s disgrace who will not hear,
The day his friend offends will day of grace to him appear.''',
                               '''To those who understand that by which they should not listen to (tales about) the faults of their friends, that is a (profitable) day on which the latter may commit a fault.''');
        k[808] = Kural.factory(809, '''பொருட்பால்''', '''பழைமை''', '''கெடாஅ வழிவந்த கேண்மையார் கேண்மை
  விடாஅர் விழையும் உலகு.''', '''Friendship of old and faithful friends,
Who ne\'er forsake, the world commends.''',
                               '''They will be loved by the world, who have not forsaken the friendship of those with whom they have kept up an unbroken long-standing intimacy.''');
        k[809] = Kural.factory(810, '''பொருட்பால்''', '''பழைமை''', '''விழையார் விழையப் படுப பழையார்கண்
  பண்பின் தலைப்பிரியா தார்.''', '''Ill-wishers even wish them well, who guard.
For ancient friends, their wonted kind regard.''',
                               '''Even enemies will love those who have never changed in their affection to their long-standing friends.''');
        k[810] = Kural.factory(811, '''பொருட்பால்''', '''தீ நட்பு''', '''பருகுவார் போலினும் பண்பிலார் கேண்மை
  பெருகலிற் குன்றல் இனிது.''', '''Though evil men should all-absorbing friendship show,
Their love had better die away than grow.''',
                               '''The decrease of friendship with those who look as if they would eat you up (through excess of love) while they are really destitute of goodness is far better than its increase.''');
        k[811] = Kural.factory(812, '''பொருட்பால்''', '''தீ நட்பு''', '''உறின்நட்டு அறின்ஙருஉம் ஒப்பிலார் கேண்மை
  பெறினும் இழப்பினும் என்.''', '''What though you gain or lose friendship of men of alien heart,
Who when you thrive are friends, and when you fail depart?''',
                               '''Of what avail is it to get or lose the friendship of those who love when there is gain and leave when there is none ?''');
        k[812] = Kural.factory(813, '''பொருட்பால்''', '''தீ நட்பு''', '''உறுவது சீர்தூக்கும் நட்பும் பெறுவது
  கொள்வாரும் கள்வரும் நேர்.''', '''These are alike: the friends who ponder friendship\'s gain
Those who accept whate\'er you give, and all the plundering train.''',
                               '''Friendship who calculate the profits (of their friendship), prostitutes who are bent on obtaining their gains, and thieves are (all) of the same character.''');
        k[813] = Kural.factory(814, '''பொருட்பால்''', '''தீ நட்பு''', '''அமரகத்து ஆற்றறுக்கும் கல்லாமா அன்னார்
  தமரின் தனிமை தலை.''', '''A steed untrained will leave you in the tug of war;
Than friends like that to dwell alone is better far.''',
                               '''Solitude is more to be desired than the society of those who resemble the untrained horses which throw down (their riders) in the fields of battle.''');
        k[814] = Kural.factory(815, '''பொருட்பால்''', '''தீ நட்பு''', '''செய்தேமஞ் சாராச் சிறியவர் புன்கேண்மை
  எய்தலின் எய்தாமை நன்று.''', '''\'Tis better not to gain than gain the friendship profitless
Of men of little minds, who succour fails when dangers press.''',
                               '''It is far better to avoid that to contract the evil friendship of the base who cannot protect (their friends) even when appointed to do so.''');
        k[815] = Kural.factory(816, '''பொருட்பால்''', '''தீ நட்பு''', '''பேதை பெருங்கெழீஇ நட்பின் அறிவுடையார்
  ஏதின்மை கோடி உறும்.''', '''Better ten million times incur the wise man\'s hate,
Than form with foolish men a friendship intimate.''',
                               '''The hatred of the wise is ten-million times more profitable than the excessive intimacy of the fool.''');
        k[816] = Kural.factory(817, '''பொருட்பால்''', '''தீ நட்பு''', '''நகைவகைய ராகிய நட்பின் பகைவரால்
  பத்தடுத்த கோடி உறும்.''', '''From foes ten million fold a greater good you gain,
Than friendship yields that\'s formed with laughers vain.''',
                               '''What comes from enemies is a hundred million times more profitable than what comes from the friendship of those who cause only laughter.''');
        k[817] = Kural.factory(818, '''பொருட்பால்''', '''தீ நட்பு''', '''ஒல்லும் கருமம் உடற்று பவர்கேண்மை
  சொல்லாடார் சோர விடல்.''', '''Those men who make a grievous toil of what they do
On your behalf, their friendship silently eschew.''',
                               '''Gradually abandon without revealing (beforehand) the friendship of those who pretend inability to carry out what they (really) could do.''');
        k[818] = Kural.factory(819, '''பொருட்பால்''', '''தீ நட்பு''', '''கனவினும் இன்னாது மன்னோ வினைவேறு
  சொல்வேறு பட்டார் தொடர்பு.''', '''E\'en in a dream the intercourse is bitterness
With men whose deeds are other than their words profess.''',
                               '''The friendship of those whose actions do not agree with their words will distress (one) even in (one\'s) dreams.''');
        k[819] = Kural.factory(820, '''பொருட்பால்''', '''தீ நட்பு''', '''எனைத்தும் குறுகுதல் ஓம்பல் மனைக்கெழீஇ
  மன்றில் பழிப்பார் தொடர்பு.''', '''In anywise maintain not intercourse with those,
Who in the house are friends, in hall are slandering foes.''',
                               '''Avoid even the least approach to a contraction of friendship with those who would love you in private but ridicule you in public.''');
        k[820] = Kural.factory(821, '''பொருட்பால்''', '''கூடாநட்பு''', '''சீரிடம் காணின் எறிதற்குப் பட்டடை
  நேரா நிரந்தவர் நட்பு.''', '''Anvil where thou shalt smitten be, when men occasion find,
Is friendship\'s form without consenting mind.''',
                               '''The friendship of those who behave like friends without inward affection is a weapon that may be thrown when a favourable opportunity presents itself.''');
        k[821] = Kural.factory(822, '''பொருட்பால்''', '''கூடாநட்பு''', '''இனம்போன்று இனமல்லார் கேண்மை மகளிர்
  மனம்போல வேறு படும்.''', '''Friendship of those who seem our kin, but are not really kind.
Will change from hour to hour like woman\'s mind.''',
                               '''The friendship of those who seem to be friends while they are not, will change like the love of women.''');
        k[822] = Kural.factory(823, '''பொருட்பால்''', '''கூடாநட்பு''', '''பலநல்ல கற்றக் கடைத்து மனநல்லர்
  ஆகுதல் மாணார்க் கரிது.''', '''To heartfelt goodness men ignoble hardly may attain,
Although abundant stores of goodly lore they gain.''',
                               '''Though (one\'s) enemies may have mastered many good books, it will be impossible for them to become truly loving at heart.''');
        k[823] = Kural.factory(824, '''பொருட்பால்''', '''கூடாநட்பு''', '''முகத்தின் இனிய நகாஅ அகத்தின்னா
  வஞ்சரை அஞ்சப் படும்.''', '''\'Tis fitting you should dread dissemblers\' guile,
Whose hearts are bitter while their faces smile.''',
                               '''One should fear the deceitful who smile sweetly with their face but never love with their heart.''');
        k[824] = Kural.factory(825, '''பொருட்பால்''', '''கூடாநட்பு''', '''மனத்தின் அமையா தவரை எனைத்தொன்றும்
  சொல்லினால் தேறற்பாற்று அன்று.''', '''When minds are not in unison, \'its never; just,
In any words men speak to put your trust.''',
                               '''In nothing whatever is it proper to rely on the words of those who do not love with their heart.''');
        k[825] = Kural.factory(826, '''பொருட்பால்''', '''கூடாநட்பு''', '''நட்டார்போல் நல்லவை சொல்லினும் ஒட்டார்சொல்
  ஒல்லை உணரப் படும்.''', '''Though many goodly words they speak in friendly tone,
The words of foes will speedily be known.''',
                               '''Though (one\'s) foes may utter good things as though they were friends, once will at once understand (their evil, import).''');
        k[826] = Kural.factory(827, '''பொருட்பால்''', '''கூடாநட்பு''', '''சொல்வணக்கம் ஒன்னார்கண் கொள்ளற்க வில்வணக்கம்
  தீங்கு குறித்தமை யான்.''', '''To pliant speech from hostile lips give thou no ear;
\'Tis pliant bow that show the deadly peril near!''',
                               '''Since the bending of the bow bespeaks evil, one should not accept (as good) the humiliating speeches of one\'s foes.''');
        k[827] = Kural.factory(828, '''பொருட்பால்''', '''கூடாநட்பு''', '''தொழுதகை யுள்ளும் படையொடுங்கும் ஒன்னார்
  அழுதகண் ணீரும் அனைத்து.''', '''In hands that worship weapon ten hidden lies;
Such are the tears that fall from foeman\'s eyes.''',
                               '''A weapon may be hid in the very hands with which (one\'s) foes adore (him) (and) the tears they shed are of the same nature.''');
        k[828] = Kural.factory(829, '''பொருட்பால்''', '''கூடாநட்பு''', '''மிகச்செய்து தம்மெள்ளு வாரை நகச்செய்து
  நட்பினுள் சாப்புல்லற் பாற்று.''', '''\'Tis just, when men make much of you, and then despise,
To make them smile, and slap in friendship\'s guise.''',
                               '''It is the duty of kings to affect great love but make it die (inwardly); as regard those foes who shew them great friendship but despise them (in their heart).''');
        k[829] = Kural.factory(830, '''பொருட்பால்''', '''கூடாநட்பு''', '''பகைநட்பாம் காலம் வருங்கால் முகநட்டு
  அகநட்பு ஒரீஇ விடல்.''', '''When time shall come that foes as friends appear,
Then thou, to hide a hostile heart, a smiling face may\'st wear.''',
                               '''When one\'s foes begin to affect friendship, one should love them with one\'s looks, and, cherishing no love in the heart, give up (even the former).''');
        k[830] = Kural.factory(831, '''பொருட்பால்''', '''பேதைமை''', '''பேதைமை என்பதொன்று யாதெனின் ஏதங்கொண்டு
  ஊதியம் போக விடல்.''', '''What one thing merits folly\'s special name.
Letting gain go, loss for one\'s own to claim!''',
                               '''Folly is one (of the chief defects); it is that which (makes one) incur loss and forego gain.''');
        k[831] = Kural.factory(832, '''பொருட்பால்''', '''பேதைமை''', '''பேதைமையுள் எல்லாம் பேதைமை காதன்மை
  கையல்ல தன்கட் செயல்.''', '''\'Mid follies chiefest folly is to fix your love
On deeds which to your station unbefitting prove.''',
                               '''The greatest folly is that which leads one to take delight in doing what is forbidden.''');
        k[832] = Kural.factory(833, '''பொருட்பால்''', '''பேதைமை''', '''நாணாமை நாடாமை நாரின்மை யாதொன்றும்
  பேணாமை பேதை தொழில்''', '''Ashamed of nothing, searching nothing out, of loveless heart,
Nought cherishing, \'tis thus the fool will play his part.''',
                               '''Shamelessness indifference (to what must be sought after), harshness, and aversion for everything (that ought to be desired) are the qualities of the fool.''');
        k[833] = Kural.factory(834, '''பொருட்பால்''', '''பேதைமை''', '''ஓதி உணர்ந்தும் பிறர்க்குரைத்தும் தானடங்காப்
  பேதையின் பேதையார் இல்.''', '''The sacred law he reads and learns, to other men expounds,-
Himself obeys not; where can greater fool be found?''',
                               '''There are no greater fools than he who, though he has read and understood (a great deal) and even taught it to others, does not walk according to his own teaching.''');
        k[834] = Kural.factory(835, '''பொருட்பால்''', '''பேதைமை''', '''ஒருமைச் செயலாற்றும் பேதை எழுமையும்
  தான்புக் கழுந்தும் அளறு.''', '''The fool will merit hell in one brief life on earth,
In which he entering sinks through sevenfold round of birth.''',
                               '''A fool can procure in a single birth a hell into which he may enter and suffer through all the seven births.''');
        k[835] = Kural.factory(836, '''பொருட்பால்''', '''பேதைமை''', '''பொய்படும் ஒன்றோ புனைபூணும் கையறியாப்
  பேதை வினைமேற் கொளின்.''', '''When fool some task attempts with uninstructed pains,
It fails; nor that alone, himself he binds with chains.''',
                               '''If the fool, who knows not how to act undertakes a work, he will (certainly) fail. (But) is it all ? He will even adorn himself with fetters.''');
        k[836] = Kural.factory(837, '''பொருட்பால்''', '''பேதைமை''', '''ஏதிலார் ஆரத் தமர்பசிப்பர் பேதை
  பெருஞ்செல்வம் உற்றக் கடை.''', '''When fools are blessed with fortune\'s bounteous store,
Their foes feed full, their friends are prey to hunger sore.''',
                               '''If a fool happens to get an immense fortune, his neighbours will enjoy it while his relations starve.''');
        k[837] = Kural.factory(838, '''பொருட்பால்''', '''பேதைமை''', '''மையல் ஒருவன் களித்தற்றால் பேதைதன்
  கையொன்று உடைமை பெறின்.''', '''When folly\'s hand grasps wealth\'s increase, \'twill be
As when a mad man raves in drunken glee.''',
                               '''A fool happening to possess something is like the intoxication of one who is (already) giddy.''');
        k[838] = Kural.factory(839, '''பொருட்பால்''', '''பேதைமை''', '''பெரிதினிது பேதையார் கேண்மை பிரிவின்கண்
  பீழை தருவதொன் றில்.''', '''Friendship of fools is very pleasant thing,
Parting with them will leave behind no sting.''',
                               '''The friendship between fools is exceedingly delightful (to each other): for at parting there will be nothing to cause them pain.''');
        k[839] = Kural.factory(840, '''பொருட்பால்''', '''பேதைமை''', '''கழாஅக்கால் பள்ளியுள் வைத்தற்றால் சான்றோர்
  குழாஅத்துப் பேதை புகல்.''', '''Like him who seeks his couch with unwashed feet,
Is fool whose foot intrudes where wise men meet.''',
                               '''The appearance of a fool in an assembly of the learned is like placing (one\'s) unwashed feet on a bed.''');
        k[840] = Kural.factory(841, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''அறிவின்மை இன்மையுள் இன்மை பிறிதின்மை
  இன்மையா வையா துலகு.''', '''Want of knowledge, \'mid all wants the sorest want we deem;
Want of other things the world will not as want esteem.''',
                               '''The want of wisdom is the greatest of all wants; but that of wealth the world will not regard as such.''');
        k[841] = Kural.factory(842, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''அறிவிலான் நெஞ்சுவந்து ஈதல் பிறிதியாதும்
  இல்லை பெறுவான் தவம்.''', '''The gift of foolish man, with willing heart bestowed, is nought,
But blessing by receiver\'s penance bought.''',
                               '''(The cause of) a fool cheerfully giving (something) is nothing else but the receiver\'s merit (in a former birth).''');
        k[842] = Kural.factory(843, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''அறிவிலார் தாந்தம்மைப் பீழிக்கும் பீழை
  செறுவார்க்கும் செய்தல் அரிது.''', '''With keener anguish foolish men their own hearts wring,
Than aught that even malice of their foes can bring.''',
                               '''The suffering that fools inflict upon themselves is hardly possible even to foes.''');
        k[843] = Kural.factory(844, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''வெண்மை எனப்படுவ தியாதெனின் ஒண்மை
  உடையம்யாம் என்னும் செருக்கு.''', '''What is stupidity? The arrogance that cries,
\'Behold, we claim the glory of the wise.\'''',
                               '''What is called want of wisdom is the vanity which says, "We are wise".''');
        k[844] = Kural.factory(845, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''கல்லாத மேற்கொண் டொழுகல் கசடற
  வல்லதூஉம் ஐயம் தரும்.''', '''If men what they have never learned assume to know,
Upon their real learning\'s power a doubt \'twill throw.''',
                               '''Fools pretending to know what has not been read (by them) will rouse suspicion even as to what they have thoroughly mastered.''');
        k[845] = Kural.factory(846, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''அற்றம் மறைத்தலோ புல்லறிவு தம்வயின்
  குற்றம் மறையா வழி.''', '''Fools are they who their nakedness conceal,
And yet their faults unveiled reveal.''',
                               '''Even to cover one\'s nakedness would be folly, if (one\'s) faults were not covered (by forsaking them).''');
        k[846] = Kural.factory(847, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''அருமறை சோரும் அறிவிலான் செய்யும்
  பெருமிறை தானே தனக்கு.''', '''From out his soul who lets the mystic teachings die,
Entails upon himself abiding misery.''',
                               '''The fool who neglects precious counsel does, of his own accord, a great injury to himself.''');
        k[847] = Kural.factory(848, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''ஏவவும் செய்கலான் தான்தேறான் அவ்வுயிர்
  போஒம் அளவுமோர் நோய்.''', '''Advised, he heeds not; of himself knows nothing wise;
This man\'s whole life is all one plague until he dies.''',
                               '''The fool will not perform (his duties) even when advised nor ascertain them himself; such a soul is a burden (to the earth) till it departs (from the body).''');
        k[848] = Kural.factory(849, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''காணாதான் காட்டுவான் தான்காணான் காணாதான்
  கண்டானாம் தான்கண்ட வாறு.''', '''That man is blind to eyes that will not see who knowledge shows;-
The blind man still in his blind fashion knows.''',
                               '''One who would teach a fool will (simply) betray his folly; and the fool would (still) think himself "wise in his own conceit".''');
        k[849] = Kural.factory(850, '''பொருட்பால்''', '''புல்லறிவாண்மை''', '''உலகத்தார் உண்டென்பது இல்லென்பான் வையத்து
  அலகையா வைக்கப் படும்.''', '''Who what the world affirms as false proclaim,
O\'er all the earth receive a demon\'s name.''',
                               '''He who denies the existence of what the world believes in will be regarded as a demon on earth.''');
        k[850] = Kural.factory(851, '''பொருட்பால்''', '''இகல்''', '''இகலென்ப எல்லா உயிர்க்கும் பகலென்னும்
  பண்பின்மை பார஧க்கும் நோய்.''', '''Hostility disunion\'s plague will bring,
That evil quality, to every living thing.''',
                               '''The disease which fosters the evil of disunion among all creatures is termed hatred by the wise.''');
        k[851] = Kural.factory(852, '''பொருட்பால்''', '''இகல்''', '''பகல்கருதிப் பற்றா செயினும் இகல்கருதி
  இன்னாசெய் யாமை தலை.''', '''Though men disunion plan, and do thee much despite
\'Tis best no enmity to plan, nor evil deeds requite.''',
                               '''Though disagreeable things may be done from (a feeling of) disunion, it is far better that nothing painful be done from (that of) hatred.''');
        k[852] = Kural.factory(853, '''பொருட்பால்''', '''இகல்''', '''இகலென்னும் எவ்வநோய் நீக்கின் தவலில்லாத்
  தாவில் விளக்கம் தரும்.''', '''If enmity, that grievous plague, you shun,
Endless undying praises shall be won.''',
                               '''To rid one-self of the distressing dtsease of hatred will bestow (on one) a never-decreasing imperishable fame.''');
        k[853] = Kural.factory(854, '''பொருட்பால்''', '''இகல்''', '''இன்பத்துள் இன்பம் பயக்கும் இகலென்னும்
  துன்பத்துள் துன்பங் கெடின்.''', '''Joy of joys abundant grows,
When malice dies that woe of woes.''',
                               '''If hatred which is the greatest misery is destroyed, it will yield the greatest delight.''');
        k[854] = Kural.factory(855, '''பொருட்பால்''', '''இகல்''', '''இகலெதிர் சாய்ந்தொழுக வல்லாரை யாரே
  மிக்லூக்கும் தன்மை யவர்.''', '''If men from enmity can keep their spirits free,
Who over them shall gain the victory?''',
                               '''Who indeed would think of conquering those who naturally shrink back from hatred ?''');
        k[855] = Kural.factory(856, '''பொருட்பால்''', '''இகல்''', '''இகலின் மிகலினிது என்பவன் வாழ்க்கை
  தவலும் கெடலும் நணித்து.''', '''The life of those who cherished enmity hold dear,
To grievous fault and utter death is near.''',
                               '''Failure and ruin are not far from him who says it is sweet to excel in hatred.''');
        k[856] = Kural.factory(857, '''பொருட்பால்''', '''இகல்''', '''மிகல்மேவல் மெய்ப்பொருள் காணார் இகல்மேவல்
  இன்னா அறிவி னவர்.''', '''The very truth that greatness gives their eyes can never see,
Who only know to work men woe, fulfilled of enmity.''',
                               '''Those whose judgement brings misery through its connection with hatred cannot understand the triumphant nature of truth.''');
        k[857] = Kural.factory(858, '''பொருட்பால்''', '''இகல்''', '''இகலிற்கு எதிர்சாய்தல் ஆக்கம் அதனை
  மிக்லூக்கின் ஊக்குமாம் கேடு.''', '''\'Tis gain to turn the soul from enmity;
Ruin reigns where this hath mastery.''',
                               '''Shrinking back from hatred will yield wealth; indulging in its increase will hasten ruin.''');
        k[858] = Kural.factory(859, '''பொருட்பால்''', '''இகல்''', '''இகல்காணான் ஆக்கம் வருங்கால் அதனை
  மிகல்காணும் கேடு தரற்கு.''', '''Men think not hostile thought in fortune\'s favouring hour,
They cherish enmity when in misfortune\'s power.''',
                               '''At the approach of wealth one will not think of hatred (but) to secure one\'s ruin, one will look to its increase.''');
        k[859] = Kural.factory(860, '''பொருட்பால்''', '''இகல்''', '''இகலானாம் இன்னாத எல்லாம் நகலானாம்
  நன்னயம் என்னும் செருக்கு.''', '''From enmity do all afflictive evils flow;
But friendliness doth wealth of kindly good bestow.''',
                               '''All calamities are caused by hatred; but by the delight (of friendship) is caused the great wealth of good virtues.''');
        k[860] = Kural.factory(861, '''பொருட்பால்''', '''பகைமாட்சி''', '''வலியார்க்கு மாறேற்றல் ஓம்புக ஓம்பா
  மெலியார்மேல் மேக பகை.''', '''With stronger than thyself, turn from the strife away;
With weaker shun not, rather court the fray.''',
                               '''Avoid offering resistance to the strong; (but) never fail to cherish enmity towards the weak.''');
        k[861] = Kural.factory(862, '''பொருட்பால்''', '''பகைமாட்சி''', '''அன்பிலன் ஆன்ற துணையிலன் தான்துவ்வான்
  என்பரியும் ஏதிலான் துப்பு.''', '''No kinsman\'s love, no strength of friends has he;
How can he bear his foeman\'s enmity?''',
                               '''How can he who is unloving, destitute of powerful aids, and himself without strength overcome the might of his foe ?''');
        k[862] = Kural.factory(863, '''பொருட்பால்''', '''பகைமாட்சி''', '''அஞ்சும் அறியான் அமைவிலன் ஈகலான்
  தஞ்சம் எளியன் பகைக்கு.''', '''A craven thing! knows nought, accords with none, gives nought away;
To wrath of any foe he falls an easy prey.''',
                               '''In the estimation of foes miserably weak is he, who is timid, ignorant, unsociable and niggardly.''');
        k[863] = Kural.factory(864, '''பொருட்பால்''', '''பகைமாட்சி''', '''நீங்கான் வெகுளி நிறையிலன் எஞ்ஞான்றும்
  யாங்கணும் யார்க்கும் எளிது.''', '''His wrath still blazes, every secret told; each day
This man\'s in every place to every foe an easy prey.''',
                               '''He who neither refrains from anger nor keeps his secrets will at all times and in all places be easily conquered by all.''');
        k[864] = Kural.factory(865, '''பொருட்பால்''', '''பகைமாட்சி''', '''வழிநோக்கான் வாய்ப்பன செய்யான் பழிநோக்கான்
  பண்பிலன் பற்றார்க்கு இனிது.''', '''No way of right he scans, no precepts bind, no crimes affright,
No grace of good he owns; such man\'s his foes\' delight.''',
                               '''(A) pleasing (object) to his foes is he who reads not moral works, does nothing that is enjoined by them cares not for reproach and is not possessed of good qualities.''');
        k[865] = Kural.factory(866, '''பொருட்பால்''', '''பகைமாட்சி''', '''காணாச் சினத்தான் கழிபெருங் காமத்தான்
  பேணாமை பேணப் படும்.''', '''Blind in his rage, his lustful passions rage and swell;
If such a man mislikes you, like it well.''',
                               '''Highly to be desired is the hatred of him whose anger is blind, and whose lust increases beyond measure.''');
        k[866] = Kural.factory(867, '''பொருட்பால்''', '''பகைமாட்சி''', '''கொடுத்தும் கொளல்வேண்டும் மன்ற அடுத்திருந்து
  மாணாத செய்வான் பகை.''', '''Unseemly are his deeds, yet proffering aid, the man draws nigh:
His hate- \'tis cheap at any price- be sure to buy!''',
                               '''It is indeed necessary to obtain even by purchase the hatred of him who having begun (a work) does what is not conductive (to its accomplishment).''');
        k[867] = Kural.factory(868, '''பொருட்பால்''', '''பகைமாட்சி''', '''குணனிலனாய்க் குற்றம் பலவாயின் மாற்றார்க்கு
  இனனிலனாம் ஏமாப் புடைத்து.''', '''No gracious gifts he owns, faults many cloud his fame;
His foes rejoice, for none with kindred claim.''',
                               '''He will become friendless who is without (any good) qualities. and whose faults are many; (such a character) is a help to (his) foes.''');
        k[868] = Kural.factory(869, '''பொருட்பால்''', '''பகைமாட்சி''', '''செறுவார்க்குச் சேணிகவா இன்பம் அறிவிலா
  அஞ்சும் பகைவர்ப் பெறின்.''', '''The joy of victory is never far removed from those
Who\'ve luck to meet with ignorant and timid foes.''',
                               '''There will be no end of lofty delights to the victorious, if their foes are (both) ignorant and timid.''');
        k[869] = Kural.factory(870, '''பொருட்பால்''', '''பகைமாட்சி''', '''கல்லான் வெகுளும் சிறுபொருள் எஞ்ஞான்றும்
  ஒல்லானை ஒல்லா தொளி.''', '''The task of angry war with men unlearned in virtue\'s lore
Who will not meet, glory shall meet him never more.''',
                               '''The light (of fame) will never be gained by him who gains not the trifling reputation of having fought an unlearned (foe).''');
        k[870] = Kural.factory(871, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''பகைஎன்னும் பண்பி லதனை ஒருவன்
  நகையேயும் வேண்டற்பாற்று அன்று.''', '''For Hate, that ill-conditioned thing not e\'en in jest.
Let any evil longing rule your breast.''',
                               '''The evil of hatred is not of a nature to be desired by one even in sport.''');
        k[871] = Kural.factory(872, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''வில்லேர் உழவர் பகைகொளினும் கொள்ளற்க
  சொல்லேர் உழவர் பகை.''', '''Although you hate incur of those whose ploughs are bows,
Make not the men whose ploughs are words your foes!''',
                               '''Though you may incur the hatred of warriors whose ploughs are bows, incur not that of ministers whose ploughs are words.''');
        k[872] = Kural.factory(873, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''ஏமுற் றவரினும் ஏழை தமியனாய்ப்
  பல்லார் பகைகொள் பவன்.''', '''Than men of mind diseased, a wretch more utterly forlorn,
Is he who stands alone, object of many foeman\'s scorn.''',
                               '''He who being alone, incurs the hatred of many is more infatuated than even mad men.''');
        k[873] = Kural.factory(874, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''பகைநட்பாக் கொண்டொழுகும் பண்புடை யாளன்
  தகைமைக்கண் தங்கிற்று உலகு.''', '''The world secure on his dexterity depends,
Whose worthy rule can change his foes to friends.''',
                               '''The world abides in the greatness of that good-natured man who behaves so as to turn hatred into friendship.''');
        k[874] = Kural.factory(875, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''தன்துணை இன்றால் பகையிரண்டால் தான்ஒருவன்
  இன்துணையாக் கொள்கவற்றின் ஒன்று.''', '''Without ally, who fights with twofold enemy o\'ermatched,
Must render one of these a friend attached.''',
                               '''He who is alone and helpless while his foes are two should secure one of them as an agreeable help (to himself).''');
        k[875] = Kural.factory(876, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''தேற஧னும் தேறா விடினும் அழிவின்கண்
  தேறான் பகாஅன் விடல்.''', '''Whether you trust or not, in time of sore distress,
Questions of diff\'rence or agreement cease to press.''',
                               '''Though (one\'s foe is) aware or not of one\'s misfortune one should act so as neither to join nor separate (from him).''');
        k[876] = Kural.factory(877, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''நோவற்க நொந்தது அறியார்க்கு மேவற்க
  மென்மை பகைவர் அகத்து.''', '''To those who know them not, complain not of your woes;
Nor to your foeman\'s eyes infirmities disclose.''',
                               '''Relate not your suffering even to friends who are ignorant of it, nor refer to your weakness in the presence of your foes.''');
        k[877] = Kural.factory(878, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''வகையறிந்து தற்செய்து தற்காப்ப மாயும்
  பகைவர்கண் பட்ட செருக்கு.''', '''Know thou the way, then do thy part, thyself defend;
Thus shall the pride of those that hate thee have an end.''',
                               '''The joy of one\'s foes will be destroyed if one guards oneself by knowing the way (of acting) and securing assistance.''');
        k[878] = Kural.factory(879, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''இளைதாக முள்மரம் கொல்க களையுநர்
  கைகொல்லும் காழ்த்த இடத்து.''', '''Destroy the thorn, while tender point can work thee no offence;
Matured by time, \'twill pierce the hand that plucks it thence.''',
                               '''A thorny tree should be felled while young, (for) when it is grown it will destroy the hand of the feller.''');
        k[879] = Kural.factory(880, '''பொருட்பால்''', '''பகைத்திறந்தெரிதல்''', '''உயிர்ப்ப உளரல்லர் மன்ற செயிர்ப்பவர்
  செம்மல் சிதைக்கலா தார்.''', '''But breathe upon them, and they surely die,
Who fail to tame the pride of angry enemy.''',
                               '''Those who do not destroy the pride of those who hate (them) will certainly not exist even to breathe.''');
        k[880] = Kural.factory(881, '''பொருட்பால்''', '''உட்பகை''', '''நிழல்நீரும் இன்னாத இன்னா தமர்நீரும்
  இன்னாவாம் இன்னா செயின்.''', '''Water and shade, if they unwholesome prove, will bring you pain.
And qualities of friends who treacherous act, will be your bane.''',
                               '''Shade and water are not pleasant, (if) they cause disease; so are the qualities of (one\'s) relations not agreeable, (if) they cause pain.''');
        k[881] = Kural.factory(882, '''பொருட்பால்''', '''உட்பகை''', '''வாள்போல பகைவரை அஞ்சற்க அஞ்சுக
  கேள்போல் பகைவர் தொடர்பு.''', '''Dread not the foes that as drawn swords appear;
Friendship of foes, who seem like kinsmen, fear!''',
                               '''Fear not foes (who say they would cut) like a sword; (but) fear the friendship of foes (who seemingly act) like relations.''');
        k[882] = Kural.factory(883, '''பொருட்பால்''', '''உட்பகை''', '''உட்பகை அஞ்சித்தற் காக்க உலைவிடத்து
  மட்பகையின் மாணத் தெறும்.''', '''Of hidden hate beware, and guard thy life;
In troublous time \'twill deeper wound than potter\'s knife.''',
                               '''Fear internal enmity and guard yourself; (if not) it will destroy (you) in an evil hour, as surely as the tool which cuts the potter\'s clay.''');
        k[883] = Kural.factory(884, '''பொருட்பால்''', '''உட்பகை''', '''மனமாணா உட்பகை தோன்றின் இனமாணா
  ஏதம் பலவும் தரும்.''', '''If secret enmities arise that minds pervert,
Then even kin unkind will work thee grievous hurt.''',
                               '''The secret enmity of a person whose mind in unreformed will lead to many evils causing disaffection among (one\'s) relations.''');
        k[884] = Kural.factory(885, '''பொருட்பால்''', '''உட்பகை''', '''உறல்முறையான் உட்பகை தோன்றின் இறல்முறையான்
  ஏதம் பலவும் தரும்.''', '''Amid one\'s relatives if hidden hath arise,
\'Twill hurt inflict in deadly wise.''',
                               '''If there appears internal hatred in a (king\'s) family; it will lead to many a fatal crime.''');
        k[885] = Kural.factory(886, '''பொருட்பால்''', '''உட்பகை''', '''ஒன்றாமை ஒன்றியார் கட்படின் எஞ்ஞான்றும்
  பொன்றாமை ஒன்றல் அரிது.''', '''If discord finds a place midst those who dwelt at one before,
\'Tis ever hard to keep destruction from the door.''',
                               '''If hatred arises among (one\'s) own people, it will be hardly possible (for one) to escape death.''');
        k[886] = Kural.factory(887, '''பொருட்பால்''', '''உட்பகை''', '''செப்பின் புணர்ச்சிபோல் கூடினும் கூடாதே
  உட்பகை உற்ற குடி.''', '''As casket with its cover, though in one they live alway,
No union to the house where hate concealed hath sway.''',
                               '''Never indeed will a family subject to internal hatred unite (really) though it may present an apparent union like that of a casket and its lid.''');
        k[887] = Kural.factory(888, '''பொருட்பால்''', '''உட்பகை''', '''அரம்பொருத பொன்போலத் தேயும் உரம்பொருது
  உட்பகை உற்ற குடி.''', '''As gold with which the file contends is worn away,
So strength of house declines where hate concealed hath sway.''',
                               '''A family subject to internal hatred will wear out and lose its strength like iron that has been filed away.''');
        k[888] = Kural.factory(889, '''பொருட்பால்''', '''உட்பகை''', '''எட்பக வன்ன சிறுமைத்தே ஆயினும்
  உட்பகை உள்ளதாங் கேடு.''', '''Though slight as shred of \'seasame\' seed it be,
Destruction lurks in hidden enmity.''',
                               '''Although internal hatred be as small as the fragment of the sesamum (seed), still does destruction dwell in it.''');
        k[889] = Kural.factory(890, '''பொருட்பால்''', '''உட்பகை''', '''உடம்பாடு இலாதவர் வாழ்க்கை குடங்கருள்
  பாம்போடு உடனுறைந் தற்று.''', '''Domestic life with those who don\'t agree,
Is dwelling in a shed with snake for company.''',
                               '''Living with those who do not agree (with one) is like dwelling with a cobra (in the same) hut.''');
        k[890] = Kural.factory(891, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''ஆற்றுவார் ஆற்றல் இகழாமை போற்றுவார்
  போற்றலுள் எல்லாம் தலை.''', '''The chiefest care of those who guard themselves from ill,
Is not to slight the powers of those who work their mighty will.''',
                               '''Not to disregard the power of those who can carry out (their wishes) is more important than all the watchfulness of those who guard (themselves against evil).''');
        k[891] = Kural.factory(892, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''பெரியாரைப் பேணாது ஒழுகிற் பெரியாரால்
  பேரா இடும்பை தரும்.''', '''If men will lead their lives reckless of great men\'s will,
Such life, through great men\'s powers, will bring perpetual ill.''',
                               '''To behave without respect for the great (rulers) will make them do (us) irremediable evils.''');
        k[892] = Kural.factory(893, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''கெடல்வேண்டின் கேளாது செய்க அடல்வேண்டின்
  ஆற்று பவர்கண் இழுக்கு.''', '''Who ruin covet let them shut their ears, and do despite
To those who, where they list to ruin have the might.''',
                               '''If a person desires ruin, let him not listen to the righteous dictates of law, but commit crimes against those who are able to slay (other sovereigns).''');
        k[893] = Kural.factory(894, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''கூற்றத்தைக் கையால் விளித்தற்றால் ஆற்றுவார்க்கு
  ஆற்றாதார் இன்னா செயல்.''', '''When powerless man \'gainst men of power will evil deeds essay,
Tis beck\'ning with the hand for Death to seize them for its prey.''',
                               '''The weak doing evil to the strong is like beckoning Yama to come (and destroy them).''');
        k[894] = Kural.factory(895, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''யாண்டுச்சென்று யாண்டும் உளராகார் வெந்துப்பின்
  வேந்து செறப்பட் டவர்.''', '''Who dare the fiery wrath of monarchs dread,
Where\'er they flee, are numbered with the dead.''',
                               '''Those who have incurred the wrath of a cruel and mighty potentate will not prosper wherever they may go.''');
        k[895] = Kural.factory(896, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''எரியால் சுடப்படினும் உய்வுண்டாம் உய்யார்
  பெரியார்ப் பிழைத்தொழுகு வார்.''', '''Though in the conflagration caught, he may escape from thence:
He \'scapes not who in life to great ones gives offence.''',
                               '''Though burnt by a fire (from a forest), one may perhaps live; (but) never will he live who has shown disrespect to the great (devotees).''');
        k[896] = Kural.factory(897, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''வகைமாண்ட வாழ்க்கையும் வான்பொருளும் என்னாம்
  தகைமாண்ட தக்கார் செறின்.''', '''Though every royal gift, and stores of wealth your life should crown,
What are they, if the worthy men of mighty virtue frown?''',
                               '''If a king incurs the wrath of the righteous great, what will become of his government with its splendid auxiliaries and (all) its untold wealth ?''');
        k[897] = Kural.factory(898, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''குன்றன்னார் குன்ற மதிப்பின் குடியொடு
  நின்றன்னார் மாய்வர் நிலத்து.''', '''If they, whose virtues like a mountain rise, are light esteemed;
They die from earth who, with their households, ever-during seemed.''',
                               '''If (the) hill-like (devotees) resolve on destruction, those who seemed to be everlasting will be destroyed root and branch from the earth.''');
        k[898] = Kural.factory(899, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''ஏந்திய கொள்கையார் சீறின் இடைமுரிந்து
  வேந்தனும் வேந்து கெடும்.''', '''When blazes forth the wrath of men of lofty fame,
Kings even fall from high estate and perish in the flame.''',
                               '''If those of exalted vows burst in a rage, even (Indra) the king will suffer a sudden loss and be entirely ruined.''');
        k[899] = Kural.factory(900, '''பொருட்பால்''', '''பெரியாரைப் பிழையாமை''', '''இறந்தமைந்த சார்புடையர் ஆயினும் உய்யார்
  சிறந்தமைந்த சீரார் செறின்.''', '''Though all-surpassing wealth of aid the boast,
If men in glorious virtue great are wrath, they\'re lost.''',
                               '''Though in possession of numerous auxiliaries, they will perish who are-exposed to the wrath of the noble whose penance is boundless.''');
        k[900] = Kural.factory(901, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''மனைவிழைவார் மாண்பயன் எய்தார் வினைவிழையார்
  வேண்டாப் பொருளும் அது.''', '''Who give their soul to love of wife acquire not nobler gain;
Who give their soul to strenuous deeds such meaner joys disdain.''',
                               '''Those who lust after their wives will not attain the excellence of virtue; and it is just this that is not desired by those who are bent on acquiring wealth.''');
        k[901] = Kural.factory(902, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''பேணாது பெண்விழைவான் ஆக்கம் பெரியதோர்
  நாணாக நாணுத் தரும்.''', '''Who gives himself to love of wife, careless of noble name
His wealth will clothe him with o\'erwhelming shame.''',
                               '''The wealth of him who, regardless (of his manliness), devotes himself to his wife\'s feminine nature will cause great shame (to ali men) and to himself;''');
        k[902] = Kural.factory(903, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''இல்லாள்கண் தாழ்ந்த இயல்பின்மை எஞ்ஞான்றும்
  நல்லாருள் நாணுத் தரும்.''', '''Who to his wife submits, his strange, unmanly mood
Will daily bring him shame among the good.''',
                               '''The frailty that stoops to a wife will always make (her husband) feel ashamed among the good.''');
        k[903] = Kural.factory(904, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''மனையாளை அஞ்சும் மறுமையி லாளன்
  வினையாண்மை வீறெய்த லின்று.''', '''No glory crowns e\'en manly actions wrought
By him who dreads his wife, nor gives the other world a thought.''',
                               '''The undertaking of one, who fears his wife and is therefore destitute of (bliss), will never be applauded.''');
        k[904] = Kural.factory(905, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''இல்லாளை அஞ்சுவான் அஞ்சுமற் றெஞ்ஞான்றும்
  நல்லார்க்கு நல்ல செயல்.''', '''Who quakes before his wife will ever tremble too,
Good deeds to men of good deserts to do.''',
                               '''He that fears his wife will always be afraid of doing good deeds (even) to the good.''');
        k[905] = Kural.factory(906, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''இமையாரின் வாழினும் பாடிலரே இல்லாள்
  அமையார்தோள் அஞ்சு பவர்.''', '''Though, like the demi-gods, in bliss they dwell secure from harm,
Those have no dignity who fear the housewife\'s slender arm.''',
                               '''They that fear the bamboo-like shoulders of their wives will be destitute of manliness though they may flourish like the Gods.''');
        k[906] = Kural.factory(907, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''பெண்ணேவல் செய்தொழுகும் ஆண்மையின் நாணுடைப்
  பெண்ணே பெருமை உடைத்து.''', '''The dignity of modest womanhood excels
His manliness, obedient to a woman\'s law who dwells.''',
                               '''Even shame faced womanhood is more to be esteemed than the shameless manhood that performs the behests of a wife.''');
        k[907] = Kural.factory(908, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''நட்டார் குறைமுடியார் நன்றாற்றார் நன்னுதலாள்
  பெட்டாங்கு ஒழுகு பவர்.''', '''Who to the will of her with beauteous brow their lives conform,
Aid not their friends in need, nor acts of charity perform.''',
                               '''Those who yield to the wishes of their wives will neither relieve the wants of (their) friends nor perform virtuous deeds.''');
        k[908] = Kural.factory(909, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''அறவினையும் ஆன்ற பொருளும் பிறவினையும்
  பெண்ஏவல் செய்வார்கண் இல்.''', '''No virtuous deed, no seemly wealth, no pleasure, rests
With them who live obedient to their wives\' behests.''',
                               '''From those who obey the commands of their wives are to be expected neither deeds of virtue, nor those of wealth nor (even) those of pleasure.''');
        k[909] = Kural.factory(910, '''பொருட்பால்''', '''பெண்வழிச்சேறல்''', '''எண்சேர்ந்த நெஞ்சத் திடனுடையார்க்கு எஞ்ஞான்றும்
  பெண்சேர்ந்தாம் பேதைமை இல்.''', '''Where pleasures of the mind, that dwell in realms of thought, abound,
Folly, that springs from overweening woman\'s love, is never found.''',
                               '''The foolishness that results from devotion to a wife will never be found in those who possess a reflecting mind and a prosperity (flowing) therefrom.''');
        k[910] = Kural.factory(911, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''அன்பின் விழையார் பொருள்விழையும் ஆய்தொடியார்
  இன்சொல் இழுக்குத் தரும்.''', '''Those that choice armlets wear who seek not thee with love,
But seek thy wealth, their pleasant words will ruin prove.''',
                               '''The sweet words of elegant braceleted (prostitutes) who desire (a man) not from affection but from avarice, will cause sorrow.''');
        k[911] = Kural.factory(912, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''பயன்தூக்கிப் பண்புரைக்கும் பண்பின் மகளிர்
  நயன்தூக்கி நள்ளா விடல்.''', '''Who weigh the gain, and utter virtuous words with vicious heart,
Weighing such women\'s worth, from their society depart.''',
                               '''One must ascertain the character of the ill-natured women who after ascertaining the wealth (of a man) speak (as if they were) good natured-ones, and avoid intercourse (with them).''');
        k[912] = Kural.factory(913, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''பொருட்பெண்டிர் பொய்ம்மை முயக்கம் இருட்டறையில்
  ஏத஧ல் பிணந்தழீஇ அற்று.''', '''As one in darkened room, some stranger corpse inarms,
Is he who seeks delight in mercenary women\'s charms!''',
                               '''The false embraces of wealth-loving women are like (hired men) embracing a strange corpse in a dark room.''');
        k[913] = Kural.factory(914, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''பொருட்பொருளார் புன்னலந் தோயார் அருட்பொருள்
  ஆயும் அறிவி னவர்.''', '''Their worthless charms, whose only weal is wealth of gain,
From touch of these the wise, who seek the wealth of grace, abstain.''',
                               '''The wise who seek the wealth of grace will not desire the base favours of those who regard wealth (and not pleasure) as (their) riches.''');
        k[914] = Kural.factory(915, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''பொதுநலத்தார் புன்னலம் தோயார் மதிநலத்தின்
  மாண்ட அறிவி னவர்.''', '''From contact with their worthless charms, whose charms to all are free,
The men with sense of good and lofty wisdom blest will flee;''',
                               '''Those whose knowledge is made excellent by their (natural) sense will not covet the trffling delights of those whose favours are common (to all).''');
        k[915] = Kural.factory(916, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''தந்நலம் பார஧ப்பார் தோயார் தகைசெருக்கிப்
  புன்னலம் பாரிப்பார் தோள்.''', '''From touch of those who worthless charms, with wanton arts, display,
The men who would their own true good maintain will turn away.''',
                               '''Those who would spread (the fame of) their own goodness will not desire the shoulders of those who rejoice in their accomplishments and bestow their despicable favours (on all who pay).''');
        k[916] = Kural.factory(917, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''நிறைநெஞ்சம் இல்லவர் தோய்வார் பிறநெஞ்சிற்
  பேணிப் புணர்பவர் தோள்.''', '''Who cherish alien thoughts while folding in their feigned embrace,
These none approach save those devoid of virtue\'s grace.''',
                               '''Those who are destitute of a perfectly (reformed) mind will covet the shoulders of those who embrace (them) while their hearts covet other things.''');
        k[917] = Kural.factory(918, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''ஆயும் அறிவினர் அல்லார்க்கு அணங்கென்ப
  மாய மகளிர் முயக்கு.''', '''As demoness who lures to ruin woman\'s treacherous love
To men devoid of wisdom\'s searching power will prove.''',
                               '''The wise say that to such as are destitute of discerning sense the embraces of faithless women are (as ruinous as those of) the celestail female.''');
        k[918] = Kural.factory(919, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''வரைவிலா மாணிழையார் மென்தோள் புரையிலாப்
  பூரியர்கள் ஆழும் அளறு.''', '''The wanton\'s tender arm, with gleaming jewels decked,
Is hell, where sink degraded souls of men abject.''',
                               '''The delicate shoulders of prostitutes with excellent jewels are a hell into which are plunged the ignorant base.''');
        k[919] = Kural.factory(920, '''பொருட்பால்''', '''வரைவின்மகளிர்''', '''இருமனப் பெண்டிரும் கள்ளும் கவறும்
  திருநீக்கப் பட்டார் தொடர்பு.''', '''Women of double minds, strong drink, and dice; to these giv\'n o\'er,
Are those on whom the light of Fortune shines no more.''',
                               '''Treacherous women, liquor, and gambling are the associates of such as have forsaken by Fortune.''');
        k[920] = Kural.factory(921, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''உட்கப் படாஅர் ஒளியிழப்பர் எஞ்ஞான்றும்
  கட்காதல் கொண்டொழுகு வார்.''', '''Who love the palm\'s intoxicating juice, each day,
No rev\'rence they command, their glory fades away.''',
                               '''Those who always thirst after drink will neither inspire fear (in others) nor retain the light (of their fame).''');
        k[921] = Kural.factory(922, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''உண்ணற்க கள்ளை உணில்உண்க சான்றோரான்
  எண்ணப் படவேண்டா தார்.''', '''Drink not inebriating draught. Let him count well the cost.
Who drinks, by drinking, all good men\'s esteem is lost.''',
                               '''Let no liquor be drunk; if it is desired, let it be drunk by those who care not for esteem of the great.''');
        k[922] = Kural.factory(923, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''ஈன்றாள் முகத்தேயும் இன்னாதால் என்மற்றுச்
  சான்றோர் முகத்துக் களி.''', '''The drunkard\'s joy is sorrow to his mother\'s eyes;
What must it be in presence of the truly wise?''',
                               '''Intoxication is painful even in the presence of (one\'s) mother; what will it not then be in that of the wise ?''');
        k[923] = Kural.factory(924, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''நாண்என்னும் நல்லாள் புறங்கொடுக்கும் கள்ளென்னும்
  பேணாப் பெருங்குற்றத் தார்க்கு.''', '''Shame, goodly maid, will turn her back for aye on them
Who sin the drunkard\'s grievous sin, that all condemn.''',
                               '''The fair maid of modesty will turn her back on those who are guilty of the great and abominable crime of drunkenness.''');
        k[924] = Kural.factory(925, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''கையறி யாமை உடைத்தே பொருள்கொடுத்து
  மெய்யறி யாமை கொளல்.''', '''With gift of goods who self-oblivion buys,
Is ignorant of all that man should prize.''',
                               '''To give money and purchase unconsciousness is the result of one\'s ignorance of (one\'s own actions).''');
        k[925] = Kural.factory(926, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''துஞ்சினார் செத்தாரின் வேறல்லர் எஞ்ஞான்றும்
  நஞ்சுண்பார் கள்ளுண் பவர்.''', '''Sleepers are as the dead, no otherwise they seem;
Who drink intoxicating draughts, they poison quaff, we deem.''',
                               '''They that sleep resemble the deed; (likewise) they that drink are no other than poison-eaters.''');
        k[926] = Kural.factory(927, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''உள்ளொற்றி உள்ளூர் நகப்படுவர் எஞ்ஞான்றும்
  கள்ளொற்றிக் கண்சாய் பவர்3''', '''Who turn aside to drink, and droop their heavy eye,
Shall be their townsmen\'s jest, when they the fault espy.''',
                               '''Those who always intoxicate themselves by a private (indulgence in) drink; will have their secrets detected and laughed at by their fellow-townsmen.''');
        k[927] = Kural.factory(928, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''களித்தறியேன் என்பது கைவிடுக நெஞ்சத்து
  ஒளித்ததூஉம் ஆங்கே மிகும்.''', '''No more in secret drink, and then deny thy hidden fraud;
What in thy mind lies hid shall soon be known abroad.''',
                               '''Let (the drunkard) give up saying "I have never drunk"; (for) the moment (he drinks) he will simply betray his former attempt to conceal.''');
        k[928] = Kural.factory(929, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''களித்தானைக் காரணம் காட்டுதல் கீழ்நீர்க்
  குளித்தானைத் தீத்துரீஇ அற்று.''', '''Like him who, lamp in hand, would seek one sunk beneath the wave.
Is he who strives to sober drunken man with reasonings grave.''',
                               '''Reasoning with a drunkard is like going under water with a torch in search of a drowned man.''');
        k[929] = Kural.factory(930, '''பொருட்பால்''', '''கள்ளுண்ணாமை''', '''கள்ளுண்ணாப் போழ்திற் களித்தானைக் காணுங்கால்
  உள்ளான்கொல் உண்டதன் சோர்வு.''', '''When one, in sober interval, a drunken man espies,
Does he not think, \'Such is my folly in my revelries\'?''',
                               '''When (a drunkard) who is sober sees one who is not, it looks as if he remembered not the evil effects of his (own) drink.''');
        k[930] = Kural.factory(931, '''பொருட்பால்''', '''சூது''', '''வேண்டற்க வென்றிடினும் சூதினை வென்றதூஉம்
  தூண்டிற்பொன் மீன்விழுங்கி அற்று.''', '''Seek not the gamester\'s play; though you should win,
Your gain is as the baited hook the fish takes in.''',
                               '''Though able to win, let not one desire gambling; (for) even what is won is like a fish swallowing the iron in fish-hook.''');
        k[931] = Kural.factory(932, '''பொருட்பால்''', '''சூது''', '''ஒன்றெய்தி நூறிழக்கும் சூதர்க்கும் உண்டாங்கொல்
  நன்றெய்தி வாழ்வதோர் ஆறு.''', '''Is there for gamblers, too, that gaining one a hundred lose, some way
That they may good obtain, and see a prosperous day?''',
                               '''Is there indeed a means of livelihood that can bestow happiness on gamblers who gain one and lose a hundred ?''');
        k[932] = Kural.factory(933, '''பொருட்பால்''', '''சூது''', '''உருளாயம் ஓவாது கூறின் பொருளாயம்
  போஒய்ப் புறமே படும்.''', '''If prince unceasing speak of nought but play,
Treasure and revenue will pass from him away.''',
                               '''If the king is incessantly addicted to the rolling dice in the hope of gain, his wealth and the resources thereof will take their departure and fall into other\'s hands.''');
        k[933] = Kural.factory(934, '''பொருட்பால்''', '''சூது''', '''சிறுமை பலசெய்து சீரழ஧க்கும் சூதின்
  வறுமை தருவதொன்று இல்.''', '''Gaming brings many woes, and ruins fair renown;
Nothing to want brings men so surely down.''',
                               '''There is nothing else that brings (us) poverty like gambling which causes many a misery and destroys (one\'s) reputation.''');
        k[934] = Kural.factory(935, '''பொருட்பால்''', '''சூது''', '''கவறும் கழகமும் கையும் தருக்கி
  இவறியார் இல்லாகி யார்.''', '''The dice, and gaming-hall, and gamester\'s art, they eager sought,
Thirsting for gain- the men in other days who came to nought.''',
                               '''Penniless are those who by reason of their attachment would never forsake gambling, the gambling-place and the handling (of dice).''');
        k[935] = Kural.factory(936, '''பொருட்பால்''', '''சூது''', '''அகடாரார் அல்லல் உழப்பர்சூ தென்னும்
  முகடியான் மூடப்பட் டார்.''', '''Gambling\'s Misfortune\'s other name: o\'er whom she casts her veil,
They suffer grievous want, and sorrows sore bewail.''',
                               '''Those who are swallowed by the goddess called "gambling" will never have their hunger satisfied, but suffer the pangs of hell in the next world.''');
        k[936] = Kural.factory(937, '''பொருட்பால்''', '''சூது''', '''பழகிய செல்வமும் பண்பும் கெடுக்கும்
  கழகத்துக் காலை புகின்.''', '''Ancestral wealth and noble fame to ruin haste,
If men in gambler\'s halls their precious moments waste.''',
                               '''To waste time at the place of gambling will destroy inherited wealth and goodness of character.''');
        k[937] = Kural.factory(938, '''பொருட்பால்''', '''சூது''', '''பொருள்கெடுத்துப் பொய்மேற் கொளீஇ அருள்கெடுத்து
  அல்லல் உழப்பிக்கும் சூது.''', '''Gambling wastes wealth, to falsehood bends the soul: it drives away
All grace, and leaves the man to utter misery a prey.''',
                               '''Gambling destroys property, teaches falsehood, puts an end to benevolence, and brings in misery (here and hereafter).''');
        k[938] = Kural.factory(939, '''பொருட்பால்''', '''சூது''', '''உடைசெல்வம் ஊண்ஒளி கல்விஎன்று ஐந்தும்
  அடையாவாம் ஆயங் கொளின்.''', '''Clothes, wealth, food, praise, and learning, all depart
From him on gambler\'s gain who sets his heart.''',
                               '''The habit of gambling prevents the attainment of these five: clothing, wealth, food, fame and learning.''');
        k[939] = Kural.factory(940, '''பொருட்பால்''', '''சூது''', '''இழத்தொறூஉம் காதலிக்கும் சூதேபோல் துன்பம்
  உழத்தொறூஉம் காதற்று உயிர்.''', '''Howe\'er he lose, the gambler\'s heart is ever in the play;
E\'en so the soul, despite its griefs, would live on earth alway.''',
                               '''As the gambler loves (his vice) the more he loses by it, so does the soul love (the body) the more it suffers through it.''');
        k[940] = Kural.factory(941, '''பொருட்பால்''', '''மருந்து''', '''மிகினும் குறையினும் நோய்செய்யும் நூலோர்
  வளிமுதலா எண்ணிய மூன்று.''', '''The learned books count three, with wind as first; of these,
As any one prevail, or fail; \'twill cause disease.''',
                               '''If (food and work are either) excessive or deficient, the three things enumerated by (medical) writers, flatulence, biliousness, and phlegm, will cause (one) disease.''');
        k[941] = Kural.factory(942, '''பொருட்பால்''', '''மருந்து''', '''மருந்தென வேண்டாவாம் யாக்கைக்கு அருந்தியது
  அற்றது போற்றி உணின்.''', '''No need of medicine to heal your body\'s pain,
If, what you ate before digested well, you eat again.''',
                               '''No medicine is necessary for him who eats after assuring (himself) that what he has (already) eaten has been digested.''');
        k[942] = Kural.factory(943, '''பொருட்பால்''', '''மருந்து''', '''அற்றால் அறவறிந்து உண்க அஃதுடம்பு
  பெற்றான் நெடிதுய்க்கும் ஆறு.''', '''Who has a body gained may long the gift retain,
If, food digested well, in measure due he eat again.''',
                               '''If (one\'s food has been) digested let one eat with moderation; (for) that is the way to prolong the life of an embodied soul.''');
        k[943] = Kural.factory(944, '''பொருட்பால்''', '''மருந்து''', '''அற்றது அறிந்து கடைப்பிடித்து மாறல்ல
  துய்க்க துவரப் பசித்து.''', '''Knowing the food digested well, when hunger prompteth thee,
With constant care, the viands choose that well agree.''',
                               '''(First) assure yourself that your food has been digested and never fail to eat, when very hungry, whatever is not disagreeable (to you).''');
        k[944] = Kural.factory(945, '''பொருட்பால்''', '''மருந்து''', '''மாறுபாடு இல்லாத உண்டி மறுத்துண்ணின்
  ஊறுபாடு இல்லை உயிர்க்கு.''', '''With self-denial take the well-selected meal;
So shall thy frame no sudden sickness feel.''',
                               '''There will be no disaster to one\'s life if one eats with moderation, food that is not disagreeable.''');
        k[945] = Kural.factory(946, '''பொருட்பால்''', '''மருந்து''', '''இழிவறிந்து உண்பான்கண் இன்பம்போல் நிற்கும்
  கழிபேர் இரையான்கண் நோய்.''', '''On modest temperance as pleasures pure,
So pain attends the greedy epicure.''',
                               '''As pleasure dwells with him who eats moderately, so disease (dwells) with the glutton who eats voraciously.''');
        k[946] = Kural.factory(947, '''பொருட்பால்''', '''மருந்து''', '''தீயள வன்றித் தெரியான் பெரிதுண்ணின்
  நோயள வின்றிப் படும்.''', '''Who largely feeds, nor measure of the fire within maintains,
That thoughtless man shall feel unmeasured pains.''',
                               '''He will be afflicted with numberless diseases, who eats immoderately, ignorant (of the rules of health).''');
        k[947] = Kural.factory(948, '''பொருட்பால்''', '''மருந்து''', '''நோய்நாடி நோய்முதல் நாடி அதுதணிக்கும்
  வாய்நாடி வாய்ப்பச் செயல்.''', '''Disease, its cause, what may abate the ill:
Let leech examine these, then use his skill.''',
                               '''Let the physician enquire into the (nature of the) disease, its cause and its method of cure and treat it faithfully according to (medical rule).''');
        k[948] = Kural.factory(949, '''பொருட்பால்''', '''மருந்து''', '''உற்றான் அளவும் பிணியளவும் காலமும்
  கற்றான் கருதிச் செயல்.''', '''The habitudes of patient and disease, the crises of the ill
These must the learned leech think over well, then use his skill.''',
                               '''The learned (physician) should ascertain the condition of his patient; the nature of his disease, and the season (of the year) and (then) proceed (with his treatment).''');
        k[949] = Kural.factory(950, '''பொருட்பால்''', '''மருந்து''', '''உற்றவன் தீர்ப்பான் மருந்துழைச் செல்வானென்று
  அப்பால் நாற்கூற்றே மருந்து.''', '''For patient, leech, and remedies, and him who waits by patient\'s side,
The art of medicine must fourfold code of laws provide.''',
                               '''Medical science consists of four parts, viz., patient, physician, medicine and compounder; and each of these (again) contains four sub-divisions.''');
        k[950] = Kural.factory(951, '''பொருட்பால்''', '''குடிமை''', '''இற்பிறந்தார் கண்அல்லது இல்லை இயல்பாகச்
  செப்பமும் நாணும் ஒருங்கு.''', '''Save in the scions of a noble house, you never find
Instinctive sense of right and virtuous shame combined.''',
                               '''Consistency (of thought, word and deed) and fear (of sin) are conjointly natural only to the high-born.''');
        k[951] = Kural.factory(952, '''பொருட்பால்''', '''குடிமை''', '''ஒழுக்கமும் வாய்மையும் நாணும்இம் மூன்றும்
  இழுக்கார் குடிப்பிறந் தார்.''', '''In these three things the men of noble birth fail not:
In virtuous deed and truthful word, and chastened thought.''',
                               '''The high-born will never deviate from these three; good manners, truthfulness and modesty.''');
        k[952] = Kural.factory(953, '''பொருட்பால்''', '''குடிமை''', '''நகைஈகை இன்சொல் இகழாமை நான்கும்
  வகையென்ப வாய்மைக் குடிக்கு.''', '''The smile, the gift, the pleasant word, unfailing courtesy
These are the signs, they say, of true nobility.''',
                               '''A cheerful countenance, liberality, pleasant words, and an unreviling disposition, these four are said to be the proper qualities of the truly high-born.''');
        k[953] = Kural.factory(954, '''பொருட்பால்''', '''குடிமை''', '''அடுக்கிய கோடி பெறினும் குடிப்பிறந்தார்
  குன்றுவ செய்தல் இலர்.''', '''Millions on millions piled would never win
The men of noble race to soul-degrading sin.''',
                               '''Though blessed with immense wealth, the noble will never do anything unbecoming.''');
        k[954] = Kural.factory(955, '''பொருட்பால்''', '''குடிமை''', '''வழங்குவ துள்வீழ்ந்தக் கண்ணும் பழங்குடி
  பண்பில் தலைப்பிரிதல் இன்று.''', '''Though stores for charity should fail within, the ancient race
Will never lose its old ancestral grace.''',
                               '''Though their means fall off, those born in ancient families, will not lose their character (for liberality).''');
        k[955] = Kural.factory(956, '''பொருட்பால்''', '''குடிமை''', '''சலம்பற்றிச் சால்பில செய்யார்மா சற்ற
  குலம்பற்றி வாழ்தும்என் பார்.''', '''Whose minds are set to live as fits their sire\'s unspotted fame,
Stooping to low deceit, commit no deeds that gender shame.''',
                               '''Those who seek to preserve the irreproachable honour of their families will not viciously do what is detrimental thereto.''');
        k[956] = Kural.factory(957, '''பொருட்பால்''', '''குடிமை''', '''குடிப்பிறந்தார் கண்விளங்கும் குற்றம் விசும்பின்
  மதிக்கண் மறுப்போல் உயர்ந்து.''', '''The faults of men of noble race are seen by every eye,
As spots on her bright orb that walks sublime the evening sky.''',
                               '''The defects of the noble will be observed as clearly as the dark spots in the moon.''');
        k[957] = Kural.factory(958, '''பொருட்பால்''', '''குடிமை''', '''நலத்தின்கண் நாரின்மை தோன்றின் அவனைக்
  குலத்தின்கண் ஐயப் படும்.''', '''If lack of love appear in those who bear some goodly name,
\'Twill make men doubt the ancestry they claim.''',
                               '''If one of a good family betrays want of affection, his descent from it will be called in question.''');
        k[958] = Kural.factory(959, '''பொருட்பால்''', '''குடிமை''', '''நிலத்தில் கிடந்தமை கால்காட்டும் காட்டும்
  குலத்தில் பிறந்தார்வாய்ச் சொல்.''', '''Of soil the plants that spring thereout will show the worth:
The words they speak declare the men of noble birth.''',
                               '''As the sprout indicates the nature of the soil, (so) the speech of the noble indicates (that of one\'s birth).''');
        k[959] = Kural.factory(960, '''பொருட்பால்''', '''குடிமை''', '''நலம்வேண்டின் நாணுடைமை வேண்டும் குலம்
  வேண்டின் வேண்டுக யார்க்கும் பணிவு.''', '''Who seek for good the grace of virtuous shame must know;
Who seek for noble name to all must reverence show.''',
                               '''He who desires a good name must desire modesty; and he who desires (the continuance of) a family greatness must be submissive to all.''');
        k[960] = Kural.factory(961, '''பொருட்பால்''', '''மானம்''', '''இன்றி அமையாச் சிறப்பின ஆயினும்
  குன்ற வருப விடல்.''', '''Though linked to splendours man no otherwise may gain,
Reject each act that may thine honour\'s clearness stain.''',
                               '''Actions that would degrade (one\'s) family should not be done; though they may be so important that not doing them would end in death.''');
        k[961] = Kural.factory(962, '''பொருட்பால்''', '''மானம்''', '''சீரினும் சீரல்ல செய்யாரே சீரொடு
  பேராண்மை வேண்டு பவர்.''', '''Who seek with glory to combine honour\'s untarnished fame,
Do no inglorious deeds, though men accord them glory\'s name.''',
                               '''Those who desire (to maintain their) honour, will surely do nothing dishonourable, even for the sake of fame.''');
        k[962] = Kural.factory(963, '''பொருட்பால்''', '''மானம்''', '''பெருக்கத்து வேண்டும் பணிதல் சிறிய
  சுருக்கத்து வேண்டும் உயர்வு.''', '''Bow down thy soul, with increase blest, in happy hour;
Lift up thy heart, when stript of all by fortune\'s power.''',
                               '''In great prosperity humility is becoming; dignity, in great adversity.''');
        k[963] = Kural.factory(964, '''பொருட்பால்''', '''மானம்''', '''தலையின் இழிந்த மயிரனையர் மாந்தர்
  நிலையின் இழிந்தக் கடை.''', '''Like hairs from off the head that fall to earth,
When fall\'n from high estate are men of noble birth.''',
                               '''They who have fallen from their (high) position are like the hair which has fallen from the head.''');
        k[964] = Kural.factory(965, '''பொருட்பால்''', '''மானம்''', '''குன்றின் அனையாரும் குன்றுவர் குன்றுவ
  குன்றி அனைய செயின்.''', '''If meanness, slight as \'abrus\' grain, by men be wrought,
Though like a hill their high estate, they sink to nought.''',
                               '''Even those who are exalted like a hill will be thought low, if they commit deeds that are debasing.''');
        k[965] = Kural.factory(966, '''பொருட்பால்''', '''மானம்''', '''புகழ்இன்றால் புத்தேள்நாட்டு உய்யாதால் என்மற்று
  இகழ்வார்பின் சென்று நிலை.''', '''It yields no praise, nor to the land of Gods throws wide the gate:
Why follow men who scorn, and at their bidding wait?''',
                               '''Of what good is it (for the high-born) to go and stand in vain before those who revile him ? it only brings him loss of honour and exclusion from heaven.''');
        k[966] = Kural.factory(967, '''பொருட்பால்''', '''மானம்''', '''ஒட்டார்பின் சென்றொருவன் வாழ்தலின் அந்நிலையே
  கெட்டான் எனப்படுதல் நன்று.''', '''Better \'twere said, \'He\'s perished!\' than to gain
The means to live, following in foeman\'s train.''',
                               '''It is better for a man to be said of him that he died in his usual state than that he eked out his life by following those who disgraced him.''');
        k[967] = Kural.factory(968, '''பொருட்பால்''', '''மானம்''', '''மருந்தோமற்று ஊன்ஓம்பும் வாழ்க்கை பெருந்தகைமை
  பீடழிய வந்த இடத்து.''', '''When high estate has lost its pride of honour meet,
Is life, that nurses this poor flesh, as nectar sweet?''',
                               '''For the high-born to keep their body in life when their honour is gone will certainly not prove a remedy against death.''');
        k[968] = Kural.factory(969, '''பொருட்பால்''', '''மானம்''', '''மயிர்நீப்பின் வாழாக் கவரிமா அன்னார்
  உயிர்நீப்பர் மானம் வரின்.''', '''Like the wild ox that, of its tuft bereft, will pine away,
Are those who, of their honour shorn, will quit the light of day.''',
                               '''Those who give up (their) life when (their) honour is at stake are like the yark which kills itself at the loss of (even one of) its hairs.''');
        k[969] = Kural.factory(970, '''பொருட்பால்''', '''மானம்''', '''இளிவரின் வாழாத மானம் உடையார்
  ஒளிதொழுது ஏத்தும் உலகு.''', '''Who, when dishonour comes, refuse to live, their honoured memory
Will live in worship and applause of all the world for aye!''',
                               '''The world will (always) praise and adore the fame of the honourable who would rather die than suffer indignity.''');
        k[970] = Kural.factory(971, '''பொருட்பால்''', '''பெருமை''', '''ஒளிஒருவற்கு உள்ள வெறுக்கை இளிஒருவற்கு
  அஃதிறந்து வாழ்தும் எனல்.''', '''The light of life is mental energy; disgrace is his
Who says, \'I \'ill lead a happy life devoid of this.\'''',
                               '''One\'s light is the abundance of one\'s courage; one\'s darkness is the desire to live destitute of such (a state of mind.)''');
        k[971] = Kural.factory(972, '''பொருட்பால்''', '''பெருமை''', '''பிறப்பொக்கும் எல்லா உயிர்க்கும் சிறப்பொவ்வா
  செய்தொழில் வேற்றுமை யான்.''', '''All men that live are one in circumstances of birth;
Diversities of works give each his special worth.''',
                               '''All human beings agree as regards their birth but differ as regards their characteristics, because of the different qualities of their actions.''');
        k[972] = Kural.factory(973, '''பொருட்பால்''', '''பெருமை''', '''மேலிருந்தும் மேலல்லார் மேலல்லர் கீழிருந்தும்
  கீழல்லார் கீழல் லவர்.''', '''The men of lofty line, whose souls are mean, are never great
The men of lowly birth, when high of soul, are not of low estate.''',
                               '''Though (raised) above, the base cannot become great; though (brought) low, the great cannot become base.''');
        k[973] = Kural.factory(974, '''பொருட்பால்''', '''பெருமை''', '''ஒருமை மகளிரே போலப் பெருமையும்
  தன்னைத்தான் கொண்டொழுகின் உண்டு.''', '''Like single-hearted women, greatness too,
Exists while to itself is true.''',
                               '''Even greatness, like a woman\'s chastity, belongs only to him who guards himself.''');
        k[974] = Kural.factory(975, '''பொருட்பால்''', '''பெருமை''', '''பெருமை யுடையவர் ஆற்றுவார் ஆற்றின்
  அருமை உடைய செயல்.''', '''The man endowed with greatness true,
Rare deeds in perfect wise will do.''',
                               '''(Though reduced) the great will be able to perform, in the proper way, deeds difficult (for others to do).''');
        k[975] = Kural.factory(976, '''பொருட்பால்''', '''பெருமை''', '''சிறியார் உணர்ச்சியுள் இல்லை பெரியாரைப்
  பேணிக் கொள் வேம் என்னும்
  நோக்கு.''', '''\'As votaries of the truly great we will ourselves enroll,\'
Is thought that enters not the mind of men of little soul.''',
                               '''It is never in the nature of the base to seek the society of the great and partake of their nature.''');
        k[976] = Kural.factory(977, '''பொருட்பால்''', '''பெருமை''', '''இறப்பே புரிந்த தொழிற்றாம் சிறப்புந்தான்
  சீரல் லவர்கண் படின்.''', '''Whene\'er distinction lights on some unworthy head,
Then deeds of haughty insolence are bred.''',
                               '''Even nobility of birth, wealth and learning, if in (the possession of) the base, will (only) produce everincreasing pride.''');
        k[977] = Kural.factory(978, '''பொருட்பால்''', '''பெருமை''', '''பணியுமாம் என்றும் பெருமை சிறுமை
  அணியுமாம் தன்னை வியந்து.''', '''Greatness humbly bends, but littleness always
Spreads out its plumes, and loads itself with praise.''',
                               '''The great will always humble himself; but the mean will exalt himself in self-admiration.''');
        k[978] = Kural.factory(979, '''பொருட்பால்''', '''பெருமை''', '''பெருமை பெருமிதம் இன்மை சிறுமை
  பெருமிதம் ஊர்ந்து விடல்.''', '''Greatness is absence of conceit; meanness, we deem,
Riding on car of vanity supreme.''',
                               '''Freedom from conceit is (the nature of true) greatness; (while) obstinacy therein is (that of) meanness.''');
        k[979] = Kural.factory(980, '''பொருட்பால்''', '''பெருமை''', '''அற்றம் மறைக்கும் பெருமை சிறுமைதான்
  குற்றமே கூறி விடும்.''', '''Greatness will hide a neighbour\'s shame;
Meanness his faults to all the world proclaim.''',
                               '''The great hide the faults of others; the base only divulge them.''');
        k[980] = Kural.factory(981, '''பொருட்பால்''', '''சான்றாண்மை''', '''கடன்என்ப நல்லவை எல்லாம் கடன்அறிந்து
  சான்றாண்மை மேற்கொள் பவர்க்கு.''', '''All goodly things are duties to the men, they say
Who set themselves to walk in virtue\'s perfect way.''',
                               '''It is said that those who are conscious of their duty and behave with a perfect goodness will regard as natural all that is good.''');
        k[981] = Kural.factory(982, '''பொருட்பால்''', '''சான்றாண்மை''', '''குணநலம் சான்றோர் நலனே பிறநலம்
  எந்நலத்து உள்ளதூஉம் அன்று.''', '''The good of inward excellence they claim,
The perfect men; all other good is only good in name.''',
                               '''The only delight of the perfect is that of their goodness; all other (sensual) delights are not to be included among any (true) delights.''');
        k[982] = Kural.factory(983, '''பொருட்பால்''', '''சான்றாண்மை''', '''அன்புநாண் ஒப்புரவு கண்ணோட்டம் வாய்மையொடு
  ஐந்துசால் ஊன்றிய தூண்.''', '''Love, modesty, beneficence, benignant grace,
With truth, are pillars five of perfect virtue\'s resting-place.''',
                               '''Affection, fear (of sin), benevolence, favour and truthfulness; these are the five pillars on which perfect goodness rests.''');
        k[983] = Kural.factory(984, '''பொருட்பால்''', '''சான்றாண்மை''', '''கொல்லா நலத்தது நோன்மை பிறர்தீமை
  சொல்லா நலத்தது சால்பு.''', '''The type of \'penitence\' is virtuous good that nothing slays;
To speak no ill of other men is perfect virtue\'s praise.''',
                               '''Penance consists in the goodness that kills not , and perfection in the goodness that tells not others\' faults.''');
        k[984] = Kural.factory(985, '''பொருட்பால்''', '''சான்றாண்மை''', '''ஆற்றுவார் ஆற்றல் பணிதல் அதுசான்றோர்
  மாற்றாரை மாற்றும் படை.''', '''Submission is the might of men of mighty acts; the sage
With that same weapon stills his foeman\'s rage.''',
                               '''Stooping (to inferiors) is the strength of those who can accomplish (an undertaking); and that is the weapon with which the great avert their foes.''');
        k[985] = Kural.factory(986, '''பொருட்பால்''', '''சான்றாண்மை''', '''சால்பிற்குக் கட்டளை யாதெனின் தோல்வி
  துலையல்லார் கண்ணும் கொளல்.''', '''What is perfection\'s test? The equal mind.
To bear repulse from even meaner men resigned.''',
                               '''The touch-stone of perfection is to receive a defeat even at the hands of one\'s inferiors.''');
        k[986] = Kural.factory(987, '''பொருட்பால்''', '''சான்றாண்மை''', '''இன்னாசெய் தார்க்கும் இனியவே செய்யாக்கால்
  என்ன பயத்ததோ சால்பு.''', '''What fruit doth your perfection yield you, say!
Unless to men who work you ill good repay?''',
                               '''Of what avail is perfect goodness if it cannot do pleasing things even to those who have pained (it) ?''');
        k[987] = Kural.factory(988, '''பொருட்பால்''', '''சான்றாண்மை''', '''இன்மை ஒருவற்கு இனிவன்று சால்பென்னும்
  திண்மைஉண் டாகப் பெறின்.''', '''To soul with perfect virtue\'s strength endued,
Brings no disgrace the lack of every earthly good.''',
                               '''Poverty is no disgrace to one who abounds in good qualities.''');
        k[988] = Kural.factory(989, '''பொருட்பால்''', '''சான்றாண்மை''', '''ஊழி பெயரினும் தாம்பெயரார் சான்றாண்மைக்கு
  ஆழி எனப்படு வார்.''', '''Call them of perfect virtue\'s sea the shore,
Who, though the fates should fail, fail not for evermore.''',
                               '''Those who are said to be the shore of the sea of perfection will never change, though ages may change.''');
        k[989] = Kural.factory(990, '''பொருட்பால்''', '''சான்றாண்மை''', '''சான்றவர் சான்றாண்மை குன்றின் இருநிலந்தான்
  தாங்காது மன்னோ பொறை.''', '''The mighty earth its burthen to sustain must cease,
If perfect virtue of the perfect men decrease.''',
                               '''If there is a defect in the character of the perfect, (even) the great world cannot bear (its) burden.''');
        k[990] = Kural.factory(991, '''பொருட்பால்''', '''பண்புடைமை''', '''எண்பதத்தால் எய்தல் எளிதென்ப யார்மாட்டும்
  பண்புடைமை என்னும் வழக்கு.''', '''Who easy access give to every man, they say,
Of kindly courtesy will learn with ease the way.''',
                               '''If one is easy of access to all, it will be easy for one to obtain the virtue called goodness.''');
        k[991] = Kural.factory(992, '''பொருட்பால்''', '''பண்புடைமை''', '''அன்புடைமை ஆன்ற குடிப்பிறத்தல் இவ்விரண்டும்
  பண்புடைமை என்னும் வழக்கு.''', '''Benevolence and high born dignity,
These two are beaten paths of courtesy.''',
                               '''Affectionateness and birth in a good family, these two constitute what is called a proper behaviour to all.''');
        k[992] = Kural.factory(993, '''பொருட்பால்''', '''பண்புடைமை''', '''உறுப்பொத்தல் மக்களொப்பு அன்றால் வெறுத்தக்க
  பண்பொத்தல் ஒப்பதாம் ஒப்பு.''', '''Men are not one because their members seem alike to outward view;
Similitude of kindred quality makes likeness true.''',
                               '''Resemblance of bodies is no resemblance of souls; true resemblance is the resemblance of qualities that attract.''');
        k[993] = Kural.factory(994, '''பொருட்பால்''', '''பண்புடைமை''', '''யனொடு நன்றி புரிந்த பயனுடையார்
  பண்புபா ராட்டும் உலகு.''', '''Of men of fruitful life, who kindly benefits dispense,
The world unites to praise the \'noble excellence.\'''',
                               '''The world applauds the character of those whose usefulness results from their equity and charity.''');
        k[994] = Kural.factory(995, '''பொருட்பால்''', '''பண்புடைமை''', '''நகையுள்ளும் இன்னா திகழ்ச்சி பகையுள்ளும்
  பண்புள பாடறிவார் மாட்டு.''', '''Contempt is evil though in sport. They who man\'s nature know,
E\'en in their wrath, a courteous mind will show.''',
                               '''Reproach is painful to one even in sport; those (therefore) who know the nature of others exhibit (pleasing) qualities even when they are hated.''');
        k[995] = Kural.factory(996, '''பொருட்பால்''', '''பண்புடைமை''', '''பண்புடையார்ப் பட்டுண்டு உலகம் அதுஇன்றேல்
  மண்புக்கு மாய்வது மன்.''', '''The world abides; for \'worthy\' men its weight sustain.
Were it not so, \'twould fall to dust again.''',
                               '''The (way of the) world subsists by contact with the good; if not, it would bury itself in the earth and perish.''');
        k[996] = Kural.factory(997, '''பொருட்பால்''', '''பண்புடைமை''', '''அரம்போலும் கூர்மைய ரேனும் மரம்போல்வர்
  மக்கட்பண்பு இல்லா தவர்.''', '''Though sharp their wit as file, as blocks they must remain,
Whose souls are void of \'courtesy humane\'.''',
                               '''He who is destitute of (true) human qualities (only) resembles a tree, though he may possess the sharpness of a file.''');
        k[997] = Kural.factory(998, '''பொருட்பால்''', '''பண்புடைமை''', '''நண்பாற்றார் ஆகி நயமில செய்வார்க்கும்
  பண்பாற்றார் ஆதல் கடை.''', '''Though men with all unfriendly acts and wrongs assail,
\'Tis uttermost disgrace in \'courtesy\' to fail.''',
                               '''It is wrong (for the wise) not to exhibit (good) qualities even towards those who bearing no friendship (for them) do only what is hateful.''');
        k[998] = Kural.factory(999, '''பொருட்பால்''', '''பண்புடைமை''', '''நகல்வல்லர் அல்லார்க்கு மாயிரு ஞாலம்
  பகலும்பாற் பட்டன்று இருள்.''', '''To him who knows not how to smile in kindly mirth,
Darkness in daytime broods o\'er all the vast and mighty earth.''',
                               '''To those who cannot rejoice, the wide world is buried darkness even in (broad) day light.''');
        k[999] = Kural.factory(1000, '''பொருட்பால்''', '''பண்புடைமை''', '''பண்பிலான் பெற்ற பெருஞ்செல்வம் நன்பால்
  கலந்தீமை யால்திரிந் தற்று.''', '''Like sweet milk soured because in filthy vessel poured,
Is ample wealth in churlish man\'s unopened coffers stored.''',
                               '''The great wealth obtained by one who has no goodness will perish like pure milk spoilt by the impurity of the vessel.''');
        k[1000] = Kural.factory(1001, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''வைத்தான்வாய் சான்ற பெரும்பொருள் அஃதுண்ணான்
  செத்தான் செயக்கிடந்தது இல்.''', '''Who fills his house with ample store, enjoying none,
Is dead. Nought with the useless heap is done.''',
                                '''He who does not enjoy the immense riches he has heaped up in his house, is (to be reckoned as) dead, (for) there is nothing achieved (by him).''');
        k[1001] = Kural.factory(1002, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''பொருளானாம் எல்லாமென்று ஈயாது இவறும்
  மருளானாம் மாணாப் பிறப்பு''', '''Who giving nought, opines from wealth all blessing springs,
Degraded birth that doting miser\'s folly brings.''',
                                '''He who knows that wealth yields every pleasure and yet is so blind as to lead miserly life will be born a demon.''');
        k[1002] = Kural.factory(1003, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''ஈட்டம் இவறி இசைவேண்டா ஆடவர்
  தோற்றம் நிலக்குப் பொறை.''', '''Who lust to heap up wealth, but glory hold not dear,
It burthens earth when on the stage of being they appear.''',
                                '''A burden to the earth are men bent on the acquisition of riches and not (true) fame.''');
        k[1003] = Kural.factory(1004, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''எச்சமென்று என்எண்ணுங் கொல்லோ ஒருவரால்
  நச்சப் படாஅ தவன்.''', '''Whom no one loves, when he shall pass away,
What doth he look to leave behind, I pray?''',
                                '''What will the miser who is not liked (by any one) regard as his own (in the world to come) ?''');
        k[1004] = Kural.factory(1005, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''கொடுப்பதூஉம் துய்ப்பதூஉம் இல்லார்க்கு அடுக்கிய
  கோடியுண் டாயினும் இல்.''', '''Amid accumulated millions they are poor,
Who nothing give and nought enjoy of all they store.''',
                                '''Those who neither give (to others) nor enjoy (their property) are (truly) destitute, though possessing immense riches.''');
        k[1005] = Kural.factory(1006, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''ஏதம் பெருஞ்செல்வம் தான்துவ்வான் தக்கார்க்கொன்று
  ஈதல் இயல்பிலா தான்.''', '''Their ample wealth is misery to men of churlish heart,
Who nought themselves enjoy, and nought to worthy men impart.''',
                                '''He who enjoys not (his riches) nor relieves the wants of the worthy is a disease to his wealth.''');
        k[1006] = Kural.factory(1007, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''அற்றார்க்கொன்று ஆற்றாதான் செல்வம் மிகநலம்
  பெற்றாள் தமியள்மூத் தற்று.''', '''Like woman fair in lonelihood who aged grows,
Is wealth of him on needy men who nought bestows.''',
                                '''The wealth of him who never bestows anything on the destitute is like a woman of beauty growing old without a husband.''');
        k[1007] = Kural.factory(1008, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''நச்சப் படாதவன் செல்வம் நடுவூருள்
  நச்சு மரம்பழுத் தற்று.''', '''When he whom no man loves exults in great prosperity,
\'Tis as when fruits in midmost of the town some poisonous tree.''',
                                '''The wealth of him who is disliked (by all) is like the fruit-bearing of the etty tree in the midst of a town.''');
        k[1008] = Kural.factory(1009, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''அன்பொரீஇத் தற்செற்று அறநோக்காது ஈட்டிய
  ஒண்பொருள் கொள்வார் பிறர்.''', '''Who love abandon, self-afflict, and virtue\'s way forsake
To heap up glittering wealth, their hoards shall others take.''',
                                '''Strangers will inherit the riches that have been acquired without regard for friendship, comfort and charity.''');
        k[1009] = Kural.factory(1010, '''பொருட்பால்''', '''நன்றியில்செல்வம்''', '''சீருடைச் செல்வர் சிறுதுனி மாரி
  வறங்கூர்ந் தனையது உடைத்து.''', '''\'Tis as when rain cloud in the heaven grows day,
When generous wealthy man endures brief poverty.''',
                                '''The short-lived poverty of those who are noble and rich is like the clouds becoming poor (for a while).''');
        k[1010] = Kural.factory(1011, '''பொருட்பால்''', '''நாணுடைமை''', '''கருமத்தால் நாணுதல் நாணுந் திருநுதல்
  நல்லவர் நாணுப் பிற.''', '''To shrink abashed from evil deed is \'generous shame\';
Other is that of bright-browed one of virtuous fame.''',
                                '''True modesty is the fear of (evil) deeds; all other modesty is (simply) the bashfulness of virtuous maids.''');
        k[1011] = Kural.factory(1012, '''பொருட்பால்''', '''நாணுடைமை''', '''ஊணுடை எச்சம் உயிர்க்கெல்லாம் வேறல்ல
  நாணுடைமை மாந்தர் சிறப்பு.''', '''Food, clothing, and other things alike all beings own;
By sense of shame the excellence of men is known.''',
                                '''Food, clothing and the like are common to all men but modesty is peculiar to the good.''');
        k[1012] = Kural.factory(1013, '''பொருட்பால்''', '''நாணுடைமை''', '''ஊனைக் குறித்த உயிரெல்லாம் நாண்என்னும்
  நன்மை குறித்தது சால்பு.''', '''All spirits homes of flesh as habitation claim,
And perfect virtue ever dwells with shame.''',
                                '''As the body is the abode of the spirit, so the excellence of modesty is the abode of perfection.''');
        k[1013] = Kural.factory(1014, '''பொருட்பால்''', '''நாணுடைமை''', '''அணிஅன்றோ நாணுடைமை சான்றோர்க்கு அஃதின்றேல்
  பிணிஅன்றோ பீடு நடை.''', '''And is not shame an ornament to men of dignity?
Without it step of stately pride is piteous thing to see.''',
                                '''Is not the modesty ornament of the noble ? Without it, their haughtiness would be a pain (to others).''');
        k[1014] = Kural.factory(1015, '''பொருட்பால்''', '''நாணுடைமை''', '''பிறர்பழியும் தம்பழியும் நாணுவார் நாணுக்கு
  உறைபதி என்னும் உலகு.''', '''As home of virtuous shame by all the world the men are known,
Who feel ashamed for others, guilt as for their own.''',
                                '''The world regards as the abode of modesty him who fear his own and other\'s guilt.''');
        k[1015] = Kural.factory(1016, '''பொருட்பால்''', '''நாணுடைமை''', '''நாண்வேலி கொள்ளாது மன்னோ வியன்ஞாலம்
  பேணலர் மேலா யவர்.''', '''Unless the hedge of shame inviolate remain,
For men of lofty soul the earth\'s vast realms no charms retain.''',
                                '''The great make modesty their barrier (of defence) and not the wide world.''');
        k[1016] = Kural.factory(1017, '''பொருட்பால்''', '''நாணுடைமை''', '''நாணால் உயிரைத் துறப்பர் உயிர்ப்பொருட்டால்
  நாண்துறவார் நாணாள் பவர்.''', '''The men of modest soul for shame would life an offering make,
But ne\'er abandon virtuous shame for life\'s dear sake.''',
                                '''The modest would rather lose their life for the sake of modesty than lose modesty for the sake of life.''');
        k[1017] = Kural.factory(1018, '''பொருட்பால்''', '''நாணுடைமை''', '''பிறர்நாணத் தக்கது தான்நாணா னாயின்
  அறம்நாணத் தக்கது உடைத்து.''', '''Though know\'st no shame, while all around asha med must be:
Virtue will shrink away ashamed of thee!''',
                                '''Virtue is likely to forsake him who shamelessly does what others are ashamed of.''');
        k[1018] = Kural.factory(1019, '''பொருட்பால்''', '''நாணுடைமை''', '''குலஞ்சுடும் கொள்கை பிழைப்பின் நலஞ்சுடும்
  நாணின்மை நின்றக் கடை.''', '''\'Twill race consume if right observance fail;
\'Twill every good consume if shamelessness prevail.''',
                                '''Want of manners injures one\'s family; but want of modesty injures one\'s character.''');
        k[1019] = Kural.factory(1020, '''பொருட்பால்''', '''நாணுடைமை''', '''நாண்அகத் தில்லார் இயக்கம் மரப்பாவை
  நாணால் உயிர்மருட்டி அற்று.''', '''\'Tis as with strings a wooden puppet apes life\'s functions, when
Those void of shame within hold intercourse with men.''',
                                '''The actions of those who are without modesty at heart are like those of puppet moved by a string.''');
        k[1020] = Kural.factory(1021, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''கருமம் செயஒருவன் கைதூவேன் என்னும்
  பெருமையின் பீடுடையது இல்.''', '''Who says \'I\'ll do my work, nor slack my hand\',
His greatness, clothed with dignity supreme, shall stand.''',
                                '''There is no higher greatness than that of one saying. I will not cease in my effort (to raise my family).''');
        k[1021] = Kural.factory(1022, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''ஆள்வினையும் ஆன்ற அறிவும் எனஇரண்டின்
  நீள்வினையால் நீளும் குடி.''', '''The manly act and knowledge full, when these combine
In deed prolonged, then lengthens out the race\'s line.''',
                                '''One\'s family is raised by untiring perseverance in both effort and wise contrivances.''');
        k[1022] = Kural.factory(1023, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''குடிசெய்வல் என்னும் ஒருவற்குத் தெய்வம்
  மடிதற்றுத் தான்முந் துறும்.''', '''\'I\'ll make my race renowned,\' if man shall say,
With vest succinct the goddess leads the way.''',
                                '''The Deity will clothe itself and appear before him who resolves on raising his family.''');
        k[1023] = Kural.factory(1024, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''சூழாமல் தானே முடிவெய்தும் தம்குடியைத்
  தாழாது உஞற்று பவர்க்கு.''', '''Who labours for his race with unremitting pain,
Without a thought spontaneously, his end will gain.''',
                                '''Those who are prompt in their efforts (to better their family) need no deliberation, such efforts will of themselves succeed.''');
        k[1024] = Kural.factory(1025, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''குற்றம் இலனாய்க் குடிசெய்து வாழ்வானைச்
  சுற்றமாச் சுற்றும் உலகு.''', '''With blameless life who seeks to build his race\'s fame,
The world shall circle him, and kindred claim.''',
                                '''People will eagerly seek the friendship of the prosperous soul who has raised his family without foul means.''');
        k[1025] = Kural.factory(1026, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''நல்லாண்மை என்பது ஒருவற்குத் தான்பிறந்த
  இல்லாண்மை ஆக்கிக் கொளல்.''', '''Of virtuous manliness the world accords the praise
To him who gives his powers, the house from which he sprang to raise.''',
                                '''A man\'s true manliness consists in making himself the head and benefactor of his family.''');
        k[1026] = Kural.factory(1027, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''அமரகத்து வன்கண்ணர் போலத் தமரகத்தும்
  ஆற்றுவார் மேற்றே பொறை.''', '''The fearless hero bears the brunt amid the warrior throng;
Amid his kindred so the burthen rests upon the strong.''',
                                '''Like heroes in the battle-field, the burden (of protection etc.) is borne by those who are the most efficient in a family.''');
        k[1027] = Kural.factory(1028, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''குடிசெய்வார்க் கில்லை பருவம் மடிசெய்து
  மானங் கருதக் கெடும்.''', '''Wait for no season, when you would your house uprear;
\'Twill perish, if you wait supine, or hold your honour dear.''',
                                '''As a family suffers by (one\'s) indolence and false dignity there is to be so season (good or bad) to those who strive to raise their family.''');
        k[1028] = Kural.factory(1029, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''இடும்பைக்கே கொள்கலம் கொல்லோ குடும்பத்தைக்
  குற்ற மறைப்பான் உடம்பு.''', '''Is not his body vase that various sorrows fill,
Who would his household screen from every ill?''',
                                '''Is it only to suffering that his body is exposed who undertakes to preserve his family from evil ?''');
        k[1029] = Kural.factory(1030, '''பொருட்பால்''', '''குடிசெயல்வகை''', '''இடுக்கண்கால் கொன்றிட வீழும் அடுத்தூன்றும்
  நல்லாள் இலாத குடி.''', '''When trouble the foundation saps the house must fall,
If no strong hand be nigh to prop the tottering wall.''',
                                '''If there are none to prop up and maintain a family (in distress), it will fall at the stroke of the axe of misfortune.''');
        k[1030] = Kural.factory(1031, '''பொருட்பால்''', '''உழவு''', '''சுழன்றும்ஏர்ப் பின்னது உலகம் அதனால்
  உழந்தும் உழவே தலை.''', '''Howe\'er they roam, the world must follow still the plougher\'s team;
Though toilsome, culture of the ground as noblest toil esteem.''',
                                '''Agriculture, though laborious, is the most excellent (form of labour); for people, though they go about (in search of various employments), have at last to resort to the farmer.''');
        k[1031] = Kural.factory(1032, '''பொருட்பால்''', '''உழவு''', '''உழுவார் உலகத்தார்க்கு ஆணிஅஃ தாற்றாது
  எழுவாரை எல்லாம் பொறுத்து.''', '''The ploughers are the linch-pin of the world; they bear
Them up who other works perform, too weak its toils to share.''',
                                '''Agriculturists are (as it were) the linch-pin of the world for they support all other workers who cannot till the soil.''');
        k[1032] = Kural.factory(1033, '''பொருட்பால்''', '''உழவு''', '''உழுதுண்டு வாழ்வாரே வாழ்வார்மற் றெல்லாம்
  தொழுதுண்டு பின்செல் பவர்.''', '''Who ploughing eat their food, they truly live:
The rest to others bend subservient, eating what they give.''',
                                '''They alone live who live by agriculture; all others lead a cringing, dependent life.''');
        k[1033] = Kural.factory(1034, '''பொருட்பால்''', '''உழவு''', '''பலகுடை நீழலும் தங்குடைக்கீழ்க் காண்பர்
  அலகுடை நீழ லவர்.''', '''O\'er many a land they \'ll see their monarch reign,
Whose fields are shaded by the waving grain.''',
                                '''Patriotic farmers desire to bring all other states under the control of their own king.''');
        k[1034] = Kural.factory(1035, '''பொருட்பால்''', '''உழவு''', '''இரவார் இரப்பார்க்கொன்று ஈவர் கரவாது
  கைசெய்தூண் மாலை யவர்.''', '''They nothing ask from others, but to askers give,
Who raise with their own hands the food on which they live.''',
                                '''Those whose nature is to live by manual labour will never beg but give something to those who beg.''');
        k[1035] = Kural.factory(1036, '''பொருட்பால்''', '''உழவு''', '''உழவினார் கைம்மடங்கின் இல்லை விழைவதூஉம்
  விட்டேம்என் பார்க்கும் நிலை.''', '''For those who \'ve left what all men love no place is found,
When they with folded hands remain who till the ground.''',
                                '''If the farmer\'s hands are slackened, even the ascetic state will fail.''');
        k[1036] = Kural.factory(1037, '''பொருட்பால்''', '''உழவு''', '''தொடிப்புழுதி கஃசா உணக்கின் பிடித்தெருவும்
  வேண்டாது சாலப் படும்.''', '''Reduce your soil to that dry state, When ounce is quarter-ounce\'s weight;
Without one handful of manure, Abundant crops you thus secure.''',
                                '''If the land is dried so as to reduce one ounce of earth to a quarter, it will grow plentifully even without a handful of manure.''');
        k[1037] = Kural.factory(1038, '''பொருட்பால்''', '''உழவு''', '''ஏரினும் நன்றால் எருவிடுதல் கட்டபின்
  நீரினும் நன்றதன் காப்பு.''', '''To cast manure is better than to plough;
Weed well; to guard is more than watering now''',
                                '''Manuring is better than ploughing; after weeding, watching is better than watering (it).''');
        k[1038] = Kural.factory(1039, '''பொருட்பால்''', '''உழவு''', '''செல்லான் கிழவன் இருப்பின் நிலம்புலந்து
  இல்லாளின் ஊடி விடும்.''', '''When master from the field aloof hath stood;
Then land will sulk, like wife in angry mood.''',
                                '''If the owner does not (personally) attend to his cultivation, his land will behave like an angry wife and yield him no pleasure.''');
        k[1039] = Kural.factory(1040, '''பொருட்பால்''', '''உழவு''', '''இலமென்று அசைஇ இருப்பாரைக் காணின்
  நிலமென்னும் நல்லாள் நகும்.''', '''The earth, that kindly dame, will laugh to see,
Men seated idle pleading poverty.''',
                                '''The maiden, Earth, will laugh at the sight of those who plead poverty and lead an idle life.''');
        k[1040] = Kural.factory(1041, '''பொருட்பால்''', '''நல்குரவு''', '''இன்மையின் இன்னாதது யாதெனின் இன்மையின்
  இன்மையே இன்னா தது.''', '''You ask what sharper pain than poverty is known;
Nothing pains more than poverty, save poverty alone.''', '''There is nothing that afflicts (one) like poverty.''');
        k[1041] = Kural.factory(1042, '''பொருட்பால்''', '''நல்குரவு''', '''இன்மை எனவொரு பாவி மறுமையும்
  இம்மையும் இன்றி வரும்.''', '''Malefactor matchless! poverty destroys
This world\'s and the next world\'s joys.''',
                                '''When cruel poverty comes on, it deprives one of both the present and future (bliss).''');
        k[1042] = Kural.factory(1043, '''பொருட்பால்''', '''நல்குரவு''', '''தொல்வரவும் தோலும் கெடுக்கும் தொகையாக
  நல்குரவு என்னும் நசை.''', '''Importunate desire, which poverty men name,
Destroys both old descent and goodly fame.''',
                                '''Hankering poverty destroys at once the greatness of (one\'s) ancient descent and (the dignity of one\'s) speech.''');
        k[1043] = Kural.factory(1044, '''பொருட்பால்''', '''நல்குரவு''', '''இற்பிறந்தார் கண்ணேயும் இன்மை இளிவந்த
  சொற்பிறக்கும் சோர்வு தரும்.''', '''From penury will spring, \'mid even those of noble race,
Oblivion that gives birth to words that bring disgrace.''',
                                '''Even in those of high birth, poverty will produce the fault of uttering mean words.''');
        k[1044] = Kural.factory(1045, '''பொருட்பால்''', '''நல்குரவு''', '''நல்குரவு என்னும் இடும்பையுள் பல்குரைத்
  துன்பங்கள் சென்று படும்.''', '''From poverty, that grievous woe,
Attendant sorrows plenteous grow.''', '''The misery of poverty brings in its train many (more) miseries.''');
        k[1045] = Kural.factory(1046, '''பொருட்பால்''', '''நல்குரவு''', '''நற்பொருள் நன்குணர்ந்து சொல்லினும் நல்கூர்ந்தார்
  சொற்பொருள் சோர்வு படும்.''', '''Though deepest sense, well understood, the poor man\'s words convey,
Their sense from memory of mankind will fade away.''',
                                '''The words of the poor are profitless, though they may be sound in thought and clear in expression.''');
        k[1046] = Kural.factory(1047, '''பொருட்பால்''', '''நல்குரவு''', '''அறஞ்சாரா நல்குரவு ஈன்றதா யானும்
  பிறன்போல நோக்கப் படும்.''', '''From indigence devoid of virtue\'s grace,
The mother e\'en that bare, estranged, will turn her face.''',
                                '''He that is reduced to absolute poverty will be regarded as a stranger even by his own mother.''');
        k[1047] = Kural.factory(1048, '''பொருட்பால்''', '''நல்குரவு''', '''இன்றும் வருவது கொல்லோ நெருநலும்
  கொன்றது போலும் நிரப்பு.''', '''And will it come today as yesterday,
The grief of want that eats my soul away?''',
                                '''Is the poverty that almost killed me yesterday, to meet me today too ?''');
        k[1048] = Kural.factory(1049, '''பொருட்பால்''', '''நல்குரவு''', '''நெருப்பினுள் துஞ்சலும் ஆகும் நிரப்பினுள்
  யாதொன்றும் கண்பாடு அரிது.''', '''Amid the flames sleep may men\'s eyelids close,
In poverty the eye knows no repose.''',
                                '''One may sleep in the midst of fire; but by no means in the midst of poverty.''');
        k[1049] = Kural.factory(1050, '''பொருட்பால்''', '''நல்குரவு''', '''துப்புர வில்லார் துவரத் துறவாமை
  உப்பிற்கும் காடிக்கும் கூற்று.''', '''Unless the destitute will utterly themselves deny,
They cause their neighbour\'s salt and vinegar to die.''',
                                '''The destitute poor, who do not renounce their bodies, only consume their neighbour\'s salt and water.''');
        k[1050] = Kural.factory(1051, '''பொருட்பால்''', '''இரவு''', '''இரக்க இரத்தக்கார்க் காணின் கரப்பின்
  அவர்பழி தம்பழி அன்று.''', '''When those you find from whom \'tis meet to ask,- for aid apply;
Theirs is the sin, not yours, if they the gift deny.''',
                                '''If you meet with those that may be begged of, you may beg; (but) if they withhold (their gift) it is their blame and not yours.''');
        k[1051] = Kural.factory(1052, '''பொருட்பால்''', '''இரவு''', '''இன்பம் ஒருவற்கு இரத்தல் இரந்தவை
  துன்பம் உறாஅ வரின்.''', '''Even to ask an alms may pleasure give,
If what you ask without annoyance you receive.''',
                                '''Even begging may be pleasant, if what is begged for is obtained without grief (to him that begs).''');
        k[1052] = Kural.factory(1053, '''பொருட்பால்''', '''இரவு''', '''கரப்பிலா நெஞ்சின் கடனறிவார் முன்நின்று
  இரப்புமோ ரேஎர் உடைத்து.''', '''The men who nought deny, but know what\'s due, before their face
To stand as suppliants affords especial grace.''',
                                '''There is even a beauty in standing before and begging of those who are liberal in their gifts and understand their duty (to beggars).''');
        k[1053] = Kural.factory(1054, '''பொருட்பால்''', '''இரவு''', '''இரத்தலும் ஈதலே போலும் கரத்தல்
  கனவிலும் தேற்றாதார் மாட்டு.''', '''Like giving alms, may even asking pleasant seem,
From men who of denial never even dream.''',
                                '''To beg of such as never think of withholding (their charity) even in their dreams, is in fact the same as giving (it oneself);''');
        k[1054] = Kural.factory(1055, '''பொருட்பால்''', '''இரவு''', '''கரப்பிலார் வையகத்து உண்மையால் கண்ணின்று
  இரப்பவர் மேற்கொள் வது.''', '''Because on earth the men exist, who never say them nay,
Men bear to stand before their eyes for help to pray.''',
                                '''As there are in the world those that give without refusing, there are (also) those that prefer to beg by simply standing before them.''');
        k[1055] = Kural.factory(1056, '''பொருட்பால்''', '''இரவு''', '''கரப்பிடும்பை யில்லாரைக் காணின் நிரப்பிடும்பை
  எல்லாம் ஒருங்கு கெடும்.''', '''It those you find from evil of \'denial\' free,
At once all plague of poverty will flee.''',
                                '''All the evil of begging will be removed at the sight of those who are far from the evil of refusing.''');
        k[1056] = Kural.factory(1057, '''பொருட்பால்''', '''இரவு''', '''இகழ்ந்தெள்ளாது ஈவாரைக் காணின் மகிழ்ந்துள்ளம்
  உள்ளுள் உவப்பது உடைத்து.''', '''If men are found who give and no harsh words of scorn employ,
The minds of askers, through and through, will thrill with joy.''',
                                '''Beggars rejoice exceedingly when they behold those who bestow (their alms) with kindness and courtesy.''');
        k[1057] = Kural.factory(1058, '''பொருட்பால்''', '''இரவு''', '''இரப்பாரை இல்லாயின் ஈர்ங்கண்மா ஞாலம்
  மரப்பாவை சென்றுவந் தற்று.''', '''If askers cease, the mighty earth, where cooling fountains flow,
Will be a stage where wooden puppets come and go.''',
                                '''If there were no beggars, (the actions done in) the cool wide world would only resemble the movement of a puppet.''');
        k[1058] = Kural.factory(1059, '''பொருட்பால்''', '''இரவு''', '''ஈவார்கண் என்னுண்டாம் தோற்றம் இரந்துகோள்
  மேவார் இலாஅக் கடை.''', '''What glory will there be to men of generous soul,
When none are found to love the askers\' role?''',
                                '''What (praise) would there be to givers (of alms) if there were no beggars to ask for and reveive (them).''');
        k[1059] = Kural.factory(1060, '''பொருட்பால்''', '''இரவு''', '''இரப்பான் வெகுளாமை வேண்டும் நிரப்பிடும்பை
  தானேயும் சாலும் கரி.''', '''Askers refused from wrath must stand aloof;
The plague of poverty itself is ample proof.''',
                                '''He who begs ought not to be angry (at a refusal); for even the misery of (his own) poverty should be a sufficient reason (for so doing).''');
        k[1060] = Kural.factory(1061, '''பொருட்பால்''', '''இரவச்சம்''', '''கரவாது உவந்தீயும் கண்ணன்னார் கண்ணும்
  இரவாமை கோடி உறும்.''', '''Ten million-fold \'tis greater gain, asking no alms to live,
Even from those, like eyes in worth, who nought concealing gladly give.''',
                                '''Not to beg (at all) even from those excellent persons who cheerfully give without refusing, will do immense good.''');
        k[1061] = Kural.factory(1062, '''பொருட்பால்''', '''இரவச்சம்''', '''இரந்தும் உயிர்வாழ்தல் வேண்டின் பரந்து
  கெடுக உலகியற்றி யான்.''', '''If he that shaped the world desires that men should begging go,
Through life\'s long course, let him a wanderer be and perish so.''',
                                '''If the Creator of the world has decreed even begging as a means of livelihood, may he too go abegging and perish.''');
        k[1062] = Kural.factory(1063, '''பொருட்பால்''', '''இரவச்சம்''', '''இன்மை இடும்பை இரந்துதீர் வாமென்னும்
  வன்மையின் வன்பாட்ட தில்.''', '''Nothing is harder than the hardness that will say,
\'The plague of penury by asking alms we\'ll drive away.\'''',
                                '''There is no greater folly than the boldness with which one seeks to remedy the evils of poverty by begging (rather than by working).''');
        k[1063] = Kural.factory(1064, '''பொருட்பால்''', '''இரவச்சம்''', '''இடமெல்லாம் கொள்ளாத் தகைத்தே இடமில்லாக்
  காலும் இரவொல்லாச் சால்பு.''', '''Who ne\'er consent to beg in utmost need, their worth
Has excellence of greatness that transcends the earth.''',
                                '''Even the whole world cannot sufficiently praise the dignity that would not beg even in the midst of destitution.''');
        k[1064] = Kural.factory(1065, '''பொருட்பால்''', '''இரவச்சம்''', '''தெண்ணீர் அடுபுற்கை ஆயினும் தாள்தந்தது
  உண்ணலின் ஊங்கினிய தில்.''', '''Nothing is sweeter than to taste the toil-won cheer,
Though mess of pottage as tasteless as the water clear.''',
                                '''Even thin gruel is ambrosia to him who has obtained it by labour.''');
        k[1065] = Kural.factory(1066, '''பொருட்பால்''', '''இரவச்சம்''', '''ஆவிற்கு நீரென்று இரப்பினும் நாவிற்கு
  இரவின் இளிவந்த தில்.''', '''E\'en if a draught of water for a cow you ask,
Nought\'s so distasteful to the tongue as beggar\'s task.''',
                                '''There is nothing more disgraceful to one\'s tongue than to use it in begging water even for a cow.''');
        k[1066] = Kural.factory(1067, '''பொருட்பால்''', '''இரவச்சம்''', '''இரப்பன் இரப்பாரை எல்லாம் இரப்பின்
  கரப்பார் இரவன்மின் என்று.''', '''One thing I beg of beggars all, \'If beg ye may,
Of those who hide their wealth, beg not, I pray.\'''',
                                '''I beseech all beggars and say, "If you need to beg, never beg of those who give unwillingly."''');
        k[1067] = Kural.factory(1068, '''பொருட்பால்''', '''இரவச்சம்''', '''இரவென்னும் ஏமாப்பில் தோணி கரவென்னும்
  பார்தாக்கப் பக்கு விடும்.''', '''The fragile bark of beggary
Wrecked on denial\'s rock will lie.''',
                                '''The unsafe raft of begging will split when it strikes on the rock of refusal.''');
        k[1068] = Kural.factory(1069, '''பொருட்பால்''', '''இரவச்சம்''', '''இரவுள்ள உள்ளம் உருகும் கரவுள்ள
  உள்ளதூஉம் இன்றிக் கெடும்.''', '''The heart will melt away at thought of beggary,
With thought of stern repulse \'twill perish utterly.''',
                                '''To think of (the evil of) begging is enough to melt one\'s heart; but to think of refusal is enough to break it.''');
        k[1069] = Kural.factory(1070, '''பொருட்பால்''', '''இரவச்சம்''', '''கரப்பவர்க்கு யாங்கொளிக்கும் கொல்லோ இரப்பவர்
  சொல்லாடப் போஒம் உயிர்.''', '''E\'en as he asks, the shamefaced asker dies;
Where shall his spirit hide who help denies?''',
                                '''Saying \'No\' to a beggar takes away his life. (but as that very word will kill the refuser) where then would the latter\'s life hide itself ?''');
        k[1070] = Kural.factory(1071, '''பொருட்பால்''', '''கயமை''', '''மக்களே போல்வர் கயவர் அவரன்ன
  ஒப்பாரி யாங்கண்ட தில்.''', '''The base resemble men in outward form, I ween;
But counterpart exact to them I\'ve never seen.''',
                                '''The base resemble men perfectly (as regards form); and we have not seen such (exact) resemblance (among any other species).''');
        k[1071] = Kural.factory(1072, '''பொருட்பால்''', '''கயமை''', '''நன்றறி வாரிற் கயவர் திருவுடையர்
  நெஞ்சத்து அவலம் இலர்.''', '''Than those of grateful heart the base must luckier be,
Their minds from every anxious thought are free!''',
                                '''The low enjoy more felicity than those who know what is good; for the former are not troubled with anxiety (as to the good).''');
        k[1072] = Kural.factory(1073, '''பொருட்பால்''', '''கயமை''', '''தேவர் அனையர் கயவர் அவருந்தாம்
  மேவன செய்தொழுக லான்.''', '''The base are as the Gods; they too
Do ever what they list to do!''', '''The base resemble the Gods; for the base act as they like.''');
        k[1073] = Kural.factory(1074, '''பொருட்பால்''', '''கயமை''', '''அகப்பட்டி ஆவாரைக் காணின் அவர஧ன்
  மிகப்பட்டுச் செம்மாக்கும் கீழ்.''', '''When base men those behold of conduct vile,
They straight surpass them, and exulting smile.''',
                                '''The base feels proud when he sees persons whose acts meaner than his own.''');
        k[1074] = Kural.factory(1075, '''பொருட்பால்''', '''கயமை''', '''அச்சமே கீழ்களது ஆசாரம் எச்சம்
  அவாவுண்டேல் உண்டாம் சிறிது.''', '''Fear is the base man\'s virtue; if that fail,
Intense desire some little may avail.''',
                                '''(The principle of) behaviour in the mean is chiefly fear; if not, hope of gain, to some extent.''');
        k[1075] = Kural.factory(1076, '''பொருட்பால்''', '''கயமை''', '''அறைபறை அன்னர் கயவர்தாம் கேட்ட
  மறைபிறர்க்கு உய்த்துரைக்க லான்.''', '''The base are like the beaten drum; for, when they hear
The sound the secret out in every neighbour\'s ear.''',
                                '''The base are like a drum that is beaten, for they unburden to others the secrets they have heard.''');
        k[1076] = Kural.factory(1077, '''பொருட்பால்''', '''கயமை''', '''ஈர்ங்கை விதிரார் கயவர் கொடிறுடைக்கும்
  கூன்கையர் அல்லா தவர்க்கு.''', '''From off their moistened hands no clinging grain they shake,
Unless to those with clenched fist their jaws who break.''',
                                '''The mean will not (even) shake off (what sticks to) their hands (soon after a meal) to any but those who would break their jaws with their clenched fists.''');
        k[1077] = Kural.factory(1078, '''பொருட்பால்''', '''கயமை''', '''சொல்லப் பயன்படுவர் சான்றோர் கரும்புபோல்
  கொல்லப் பயன்படும் கீழ்.''', '''The good to those will profit yield fair words who use;
The base, like sugar-cane, will profit those who bruise.''',
                                '''The great bestow (their alms) as soon as they are informed; (but) the mean, like the sugar-cane, only when they are tortured to death.''');
        k[1078] = Kural.factory(1079, '''பொருட்பால்''', '''கயமை''', '''உடுப்பதூஉம் உண்பதூஉம் காணின் பிறர்மேல்
  வடுக்காண வற்றாகும் கீழ்.''', '''If neighbours clothed and fed he see, the base
Is mighty man some hidden fault to trace?''',
                                '''The base will bring an evil (accusation) against others, as soon as he sees them (enjoying) good food and clothing.''');
        k[1079] = Kural.factory(1080, '''பொருட்பால்''', '''கயமை''', '''எற்றிற் குரியர் கயவரொன்று உற்றக்கால்
  விற்றற்கு உரியர் விரைந்து.''', '''For what is base man fit, if griefs assail?
Himself to offer, there and then, for sale!''',
                                '''The base will hasten to sell themselves as soon as a calamity has befallen them. For what else are they fitted ?''');
        k[1080] = Kural.factory(1081, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''அணங்குகொல் ஆய்மயில் கொல்லோ கனங்குழை
  மாதர்கொல் மாலும்என் நெஞ்சு.''', '''Goddess? or peafowl rare? She whose ears rich jewels wear,
Is she a maid of human kind? All wildered is my mind!''',
                                '''Is this jewelled female a celestial, a choice peahen, or a human being ? My mind is perplexed.''');
        k[1081] = Kural.factory(1082, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''நோக்கினாள் நோக்கெதிர் நோக்குதல் தாக்கணங்கு
  தானைக்கொண் டன்ன துடைத்து.''', '''She of the beaming eyes, To my rash look her glance replies,
As if the matchless goddess\' hand Led forth an armed band.''',
                                '''This female beauty returning my looks is like a celestial maiden coming with an army to contend against me.''');
        k[1082] = Kural.factory(1083, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''பண்டறியேன் கூற்றென் பதனை இனியறிந்தேன்
  பெண்டகையால் பேரமர்க் கட்டு.''', '''Death\'s form I formerly Knew not; but now \'tis plain to me;
He comes in lovely maiden\'s guise, With soul-subduing eyes.''',
                                '''I never knew before what is called Yama; I see it now; it is the eyes that carry on a great fight with (the help of) female qualities.''');
        k[1083] = Kural.factory(1084, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''கண்டார் உயிருண்ணும் தோற்றத்தால் பெண்டகைப்
  பேதைக்கு அமர்த்தன கண்.''', '''In sweet simplicity, A woman\'s gracious form hath she;
But yet those eyes, that drink my life, Are with the form at strife!''',
                                '''These eyes that seem to kill those who look at them are as it were in hostilities with this feminine simplicity.''');
        k[1084] = Kural.factory(1085, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''கூற்றமோ கண்ணோ பிணையோ மடவரல்
  நோக்கமிம் மூன்றும் உடைத்து.''', '''The light that on me gleams, Is it death\'s dart? or eye\'s bright beams?
Or fawn\'s shy glance? All three appear In form of maiden here.''',
                                '''Is it Yama, (a pair of) eyes or a hind ?- Are not all these three in the looks of this maid ?''');
        k[1085] = Kural.factory(1086, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''கொடும்புருவம் கோடா மறைப்பின் நடுங்கஞர்
  செய்யல மன்இவள் கண்.''', '''If cruel eye-brow\'s bow, Unbent, would veil those glances now;
The shafts that wound this trembling heart Her eyes no more would dart.''',
                                '''Her eyes will cause (me) no trembling sorrow, if they are properly hidden by her cruel arched eye-brows.''');
        k[1086] = Kural.factory(1087, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''கடாஅக் களிற்றின்மேற் கட்படாம் மாதர்
  படாஅ முலைமேல் துகில்.''', '''As veil o\'er angry eyes Of raging elephant that lies,
The silken cincture\'s folds invest This maiden\'s panting breast.''',
                                '''The cloth that covers the firm bosom of this maiden is (like) that which covers the eyes of a rutting elephant.''');
        k[1087] = Kural.factory(1088, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''ஒண்ணுதற் கோஒ உடைந்ததே ஞாட்பினுள்
  நண்ணாரும் உட்குமென் பீடு.''', '''Ah! woe is me! my might, That awed my foemen in the fight,
By lustre of that beaming brow Borne down, lies broken now!''',
                                '''On her bright brow alone is destroyed even that power of mine that used to terrify the most fearless foes in the battlefield.''');
        k[1088] = Kural.factory(1089, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''பிணையேர் மடநோக்கும் நாணும் உடையாட்கு
  அணியெவனோ ஏதில தந்து.''', '''Like tender fawn\'s her eye; Clothed on is she with modesty;
What added beauty can be lent; By alien ornament?''',
                                '''Of what use are other jewels to her who is adorned with modesty, and the meek looks of a hind ?''');
        k[1089] = Kural.factory(1090, '''காமத்துப்பால்''', '''தகையணங்குறுத்தல்''', '''உண்டார்கண் அல்லது அடுநறாக் காமம்போல்
  கண்டார் மகிழ்செய்தல் இன்று.''', '''The palm-tree\'s fragrant wine, To those who taste yields joys divine;
But love hath rare felicity For those that only see!''',
                                '''Unlike boiled honey which yields delight only when it is drunk, love gives pleasure even when looked at.''');
        k[1090] = Kural.factory(1091, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''இருநோக்கு இவளுண்கண் உள்ளது ஒருநோக்கு
  நோய்நோக்கொன் றந்நோய் மருந்து.''', '''A double witchery have glances of her liquid eye;
One glance is glance that brings me pain; the other heals again.''',
                                '''There are two looks in the dyed eyes of this (fair one); one causes pain, and the other is the cure thereof.''');
        k[1091] = Kural.factory(1092, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''கண்களவு கொள்ளும் சிறுநோக்கம் காமத்தில்
  செம்பாகம் அன்று பெரிது.''', '''The furtive glance, that gleams one instant bright,
Is more than half of love\'s supreme delight.''',
                                '''A single stolen glance of her eyes is more than half the pleasure (of sexual embrace).''');
        k[1092] = Kural.factory(1093, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''நோக்கினாள் நோக்கி இறைஞ்சினாள் அஃதவள்
  யாப்பினுள் அட்டிய நீர்.''', '''She looked, and looking drooped her head:
On springing shoot of love \'its water shed!''',
                                '''She has looked (at men) and stooped (her head); and that (sign) waters as it were (the corn of) our love.''');
        k[1093] = Kural.factory(1094, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''யான்நோக்கும் காலை நிலன்நோக்கும் நோக்காக்கால்
  தான்நோக்கி மெல்ல நகும்.''', '''I look on her: her eyes are on the ground the while:
I look away: she looks on me with timid smile.''',
                                '''When I look, she looks down; when I do not, she looks and smiles gently.''');
        k[1094] = Kural.factory(1095, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''குறிக்கொண்டு நோக்காமை அல்லால் ஒருகண்
  சிறக்கணித்தாள் போல நகும்''', '''She seemed to see me not; but yet the maid
Her love, by smiling side-long glance, betrayed.''',
                                '''She not only avoids a direct look at me, but looks as it were with a half-closed eye and smiles.''');
        k[1095] = Kural.factory(1096, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''உறாஅ தவர்போல் சொலினும் செறாஅர்சொல்
  ஒல்லை உணரப் படும்.''', '''Though with their lips affection they disown,
Yet, when they hate us not, \'tis quickly known.''',
                                '''Though they may speak harshly as if they were strangers, the words of the friendly are soon understood.''');
        k[1096] = Kural.factory(1097, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''செறாஅச் சிறுசொல்லும் செற்றார்போல் நோக்கும்
  உறாஅர்போன்று உற்றார் குறிப்பு.''', '''The slighting words that anger feign, while eyes their love reveal.
Are signs of those that love, but would their love conceal.''',
                                '''Little words that are harsh and looks that are hateful are (but) the expressions of lovers who wish to act like strangers.''');
        k[1097] = Kural.factory(1098, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''அசையியற்கு உண்டாண்டோர் ஏஎர்யான் நோக்கப்
  பசையினள் பைய நகும்.''', '''I gaze, the tender maid relents the while;
And, oh the matchless grace of that soft smile!''',
                                '''When I look, the pitying maid looks in return and smiles gently; and that is a comforting sign for me.''');
        k[1098] = Kural.factory(1099, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''ஏதிலார் போலப் பொதுநோக்கு நோக்குதல்
  காதலார் கண்ணே உள.''', '''The look indifferent, that would its love disguise,
Is only read aright by lovers\' eyes.''',
                                '''Both the lovers are capable of looking at each other in an ordinary way, as if they were perfect strangers.''');
        k[1099] = Kural.factory(1100, '''காமத்துப்பால்''', '''குறிப்பறிதல்''', '''கண்ணொடு கண்இணை நோக்கொக்கின் வாய்ச்சொற்கள்
  என்ன பயனும் இல.''', '''When eye to answering eye reveals the tale of love,
All words that lips can say must useless prove.''',
                                '''The words of the mouths are of no use whatever, when there is perfect agreement between the eyes (of lovers).''');
        k[1100] = Kural.factory(1101, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''கண்டுகேட்டு உண்டுயிர்த்து உற்றறியும் ஐம்புலனும்
  ஒண்தொடி கண்ணே உள.''', '''All joys that senses five- sight, hearing, taste, smell, touch- can give,
In this resplendent armlets-bearing damsel live!''',
                                '''The (simultaneous) enjoyment of the five senses of sight, hearing, taste, smell and touch can only be found with bright braceleted (women).''');
        k[1101] = Kural.factory(1102, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''பிணிக்கு மருந்து பிறமன் அணியிழை
  தன்நோய்க்குத் தானே மருந்து.''', '''Disease and medicine antagonists we surely see;
This maid, to pain she gives, herself is remedy.''',
                                '''The remedy for a disease is always something different (from it); but for the disease caused by this jewelled maid, she is herself the cure.''');
        k[1102] = Kural.factory(1103, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''தாம்வீழ்வார் மென்றோள் துயிலின் இனிதுகொல்
  தாமரைக் கண்ணான் உலகு.''', '''Than rest in her soft arms to whom the soul is giv\'n,
Is any sweeter joy in his, the Lotus-eyed-one\'s heaven?''',
                                '''Can the lotus-eyed Vishnu\'s heaven be indeed as sweet to those who delight to sleep in the delicate arms of their beloved ?''');
        k[1103] = Kural.factory(1104, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''நீங்கின் தெறூஉம் குறுகுங்கால் தண்ணென்னும்
  தீயாண்டுப் பெற்றாள் இவள்.''', '''Withdraw, it burns; approach, it soothes the pain;
Whence did the maid this wondrous fire obtain?''',
                                '''From whence has she got this fire that burns when I withdraw and cools when I approach ?''');
        k[1104] = Kural.factory(1105, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''வேட் ட பொழுதின் அவையவை
  போலுமே தோட் டார் கதுப்பினாள்
  தோள்.''', '''In her embrace, whose locks with flowery wreaths are bound,
Each varied form of joy the soul can wish is found.''',
                                '''The shoulders of her whose locks are adorned with flowers delight me as if they were the very sweets I have desired (to get).''');
        k[1105] = Kural.factory(1106, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''உறுதோறு உயிர்தளிர்ப்பத் தீண்டலால் பேதைக்கு
  அமிழ்தின் இயன்றன தோள்.''', '''Ambrosia are the simple maiden\'s arms; when I attain
Their touch, my withered life puts forth its buds again!''',
                                '''The shoulders of this fair one are made of ambrosia, for they revive me with pleasure every time I embrace them.''');
        k[1106] = Kural.factory(1107, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''தம்மில் இருந்து தமதுபாத்து உண்டற்றால்
  அம்மா அரிவை முயக்கு.''', '''As when one eats from household store, with kindly grace
Sharing his meal: such is this golden maid\'s embrace.''',
                                '''The embraces of a gold-complexioned beautiful female are as pleasant as to dwell in one\'s own house and live by one\'s own (earnings) after distributing (a portion of it in charity).''');
        k[1107] = Kural.factory(1108, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''வீழும் இருவர்க்கு இனிதே வளியிடை
  போழப் படாஅ முயக்கு.''', '''Sweet is the strict embrace of those whom fond affection binds,
Where no dissevering breath of discord entrance finds.''',
                                '''To ardent lovers sweet is the embrace that cannot be penetrated even by a breath of breeze.''');
        k[1108] = Kural.factory(1109, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''ஊடல் உணர்தல் புணர்தல் இவைகாமம்
  கூடியார் பெற்ற பயன்.''', '''The jealous variance, the healing of the strife, reunion gained:
These are the fruits from wedded love obtained.''',
                                '''Love quarrel, reconciliation and intercourse - these are the advantages reaped by those who marry for lust.''');
        k[1109] = Kural.factory(1110, '''காமத்துப்பால்''', '''புணர்ச்சிமகிழ்தல்''', '''அறிதோறு அறியாமை கண்டற்றால் காமம்
  செறிதோறும் சேயிழை மாட்டு.''', '''The more men learn, the more their lack of learning they detect;
\'Tis so when I approach the maid with gleaming jewels decked.''',
                                '''As (one\'s) ignorance is discovered the more one learns, so does repeated intercourse with a well-adorned female (only create a desire for more).''');
        k[1110] = Kural.factory(1111, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''நன்னீரை வாழி அனிச்சமே நின்னினும்
  மென்னீரள் யாம்வீழ் பவள்.''', '''O flower of the sensitive plant! than thee
More tender\'s the maiden beloved by me.''',
                                '''May you flourish, O Anicham! you have a delicate nature. But my beloved is more delicate than you.''');
        k[1111] = Kural.factory(1112, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''மலர்காணின் மையாத்தி நெஞ்சே இவள்கண்
  பலர்காணும் பூவொக்கும் என்று.''', '''You deemed, as you saw the flowers, her eyes were as flowers, my soul,
That many may see; it was surely some folly that over you stole!''',
                                '''O my soul, fancying that flowers which are seen by many can resemble her eyes, you become confused at the sight of them.''');
        k[1112] = Kural.factory(1113, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''முறிமேனி முத்தம் முறுவல் வெறிநாற்றம்
  வேலுண்கண் வேய்த்தோ ளவட்கு.''', '''As tender shoot her frame; teeth, pearls; around her odours blend;
Darts are the eyes of her whose shoulders like the bambu bend.''',
                                '''The complexion of this bamboo-shouldered one is that of a shoot; her teeth, are pearls; her breath, fragrance; and her dyed eyes, lances.''');
        k[1113] = Kural.factory(1114, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''காணின் குவளை கவிழ்ந்து நிலன்நோக்கும்
  மாணிழை கண்ணொவ்வேம் என்று.''', '''The lotus, seeing her, with head demiss, the ground would eye,
And say, \'With eyes of her, rich gems who wears, we cannot vie.\'''',
                                '''If the blue lotus could see, it would stoop and look at the ground saying, "I can never resemble the eyes of this excellent jewelled one."''');
        k[1114] = Kural.factory(1115, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''அனிச்சப்பூக் கால்களையாள் பெய்தாள் நுகப்பிற்கு
  நல்ல படாஅ பறை.''', '''The flowers of the sensitive plant as a girdle around her she placed;
The stems she forgot to nip off; they \'ll weigh down the delicate waist.''',
                                '''No merry drums will be beaten for the (tender) waist of her who has adorned herself with the anicham without having removed its stem.''');
        k[1115] = Kural.factory(1116, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''மதியும் மடந்தை முகனும் அறியா
  பதியின் கலங்கிய மீன்.''', '''The stars perplexed are rushing wildly from their spheres;
For like another moon this maiden\'s face appears.''',
                                '''The stars have become confused in their places not being able to distinguish between the moon and the maid\'s countenance.''');
        k[1116] = Kural.factory(1117, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''அறுவாய் நிறைந்த அவிர்மதிக்குப் போல
  மறுவுண்டோ மாதர் முகத்து.''', '''In moon, that waxing waning shines, as sports appear,
Are any spots discerned in face of maiden here?''',
                                '''Could there be spots in the face of this maid like those in the bright full moon ?''');
        k[1117] = Kural.factory(1118, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''மாதர் முகம்போல் ஒளிவிட வல்லையேல்
  காதலை வாழி மத஧.''', '''Farewell, O moon! If that thine orb could shine
Bright as her face, thou shouldst be love of mine.''',
                                '''If you can indeed shine like the face of women, flourish, O moon, for then would you be worth loving ?''');
        k[1118] = Kural.factory(1119, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''மலரன்ன கண்ணாள் முகமொத்தி யாயின்
  பலர்காணத் தோன்றல் மதி.''', '''If as her face, whose eyes are flowers, thou wouldst have charms for me,
Shine for my eyes alone, O moon, shine not for all to see!''',
                                '''O moon, if you wish to resemble the face of her whose eyes are like (these) flowers, do not appear so as to be seen by all.''');
        k[1119] = Kural.factory(1120, '''காமத்துப்பால்''', '''நலம்புனைந்துரைத்தல்''', '''அனிச்சமும் அன்னத்தின் தூவியும் மாதர்
  அடிக்கு நெருஞ்சிப் பழம்.''', '''The flower of the sensitive plant, and the down on the swan\'s white breast,
As the thorn are harsh, by the delicate feet of this maiden pressed.''',
                                '''The anicham and the feathers of the swan are to the feet of females, like the fruit of the (thorny) Nerunji.''');
        k[1120] = Kural.factory(1121, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''பாலொடு தேன்கலந் தற்றே பணிமொழி
  வாலெயிறு ஊறிய நீர்.''', '''The dew on her white teeth, whose voice is soft and low,
Is as when milk and honey mingled flow.''',
                                '''The water which oozes from the white teeth of this soft speeched damsel is like a mixture of milk and honey.''');
        k[1121] = Kural.factory(1122, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''உடம்பொடு உயிரிடை என்னமற் றன்ன
  மடந்தையொடு எம்மிடை நட்பு.''', '''Between this maid and me the friendship kind
Is as the bonds that soul and body bind.''',
                                '''The love between me and this damsel is like the union of body and soul.''');
        k[1122] = Kural.factory(1123, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''கருமணியிற் பாவாய்நீ போதாயாம் வீழும்
  திருநுதற்கு இல்லை இடம்.''', '''For her with beauteous brow, the maid I love, there place is none;
To give her image room, O pupil of mine eye, begone!''',
                                '''O you image in the pupil (of my eye)! depart; there is no room for (my) fair-browed beloved.''');
        k[1123] = Kural.factory(1124, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''வாழ்தல் உயிர்க்கன்னள் ஆயிழை சாதல்
  அதற்கன்னள் நீங்கும் இடத்து.''', '''Life is she to my very soul when she draws nigh;
Dissevered from the maid with jewels rare, I die!''',
                                '''My fair-jewelled one resembles the living soul (when she is in union with me), the dying soul when she leaves me.''');
        k[1124] = Kural.factory(1125, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''உள்ளுவன் மன்யான் மறப்பின் மறப்பறியேன்
  ஒள்ளமர்க் கண்ணாள் குணம்.''', '''I might recall, if I could once forget; but from my heart
Her charms fade not, whose eyes gleam like the warrior\'s dart.''',
                                '''If I had forgotten her who has bright battling eyes, I would have remembered (thee); but I never forget her. (Thus says he to her maid).''');
        k[1125] = Kural.factory(1126, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''கண்ணுள்ளின் போகார் இமைப்பின் பருகுவரா
  நுண்ணியர்எம் காத லவர்.''', '''My loved one\'s subtle form departs not from my eyes;
I wink them not, lest I should pain him where he lies.''',
                                '''My lover would not depart from mine eyes; even if I wink, he would not suffer (from pain); he is so ethereal.''');
        k[1126] = Kural.factory(1127, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''கண்ணுள்ளார் காத லவராகக் கண்ணும்
  எழுதேம் கரப்பாக்கு அறிந்து.''', '''My love doth ever in my eyes reside;
I stain them not, fearing his form to hide.''',
                                '''As my lover abides in my eyes, I will not even paint them, for he would (then) have to conceal himself.''');
        k[1127] = Kural.factory(1128, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''நெஞ்சத்தார் காத லவராக வெய்துண்டல்
  அஞ்சுதும் வேபாக் கறிந்து.''', '''Within my heart my lover dwells; from food I turn
That smacks of heat, lest he should feel it burn.''',
                                '''As my lover is in my heart, I am afraid of eating (anything) hot, for I know it would pain him.''');
        k[1128] = Kural.factory(1129, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''இமைப்பின் கரப்பாக்கு அறிவல் அனைத்திற்கே
  ஏதிலர் என்னும்இவ் வூர்.''', '''I fear his form to hide, nor close my eyes:
\'Her love estranged is gone!\' the village cries.''',
                                '''I will not wink, knowing that if I did, my lover would hide himself; and for this reason, this town says, he is unloving.''');
        k[1129] = Kural.factory(1130, '''காமத்துப்பால்''', '''காதற்சிறப்புரைத்தல்''', '''உவந்துறைவர் உள்ளத்துள் என்றும் இகந்துறைவர்
  ஏதிலர் என்னும்இவ் வூர்.''', '''Rejoicing in my very soul he ever lies;
\'Her love estranged is gone far off!\' the village cries.''',
                                '''My lover dwells in my heart with perpetual delight; but the town says he is unloving and (therefore) dwells afar.''');
        k[1130] = Kural.factory(1131, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''காமம் உழந்து வருந்தினார்க்கு ஏமம்
  மடலல்லது இல்லை வலி.''', '''To those who \'ve proved love\'s joy, and now afflicted mourn,
Except the helpful \'horse of palm\', no other strength remains.''',
                                '''To those who after enjoyment of sexual pleasure suffer (for want of more), there is no help so efficient as the palmyra horse.''');
        k[1131] = Kural.factory(1132, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''நோனா உடம்பும் உயிரும் மடலேறும்
  நாணினை நீக்கி நிறுத்து.''', '''My body and my soul, that can no more endure,
Will lay reserve aside, and mount the \'horse of palm\'.''',
                                '''Having got rid of shame, the suffering body and soul save themselves on the palmyra horse.''');
        k[1132] = Kural.factory(1133, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''நாணொடு நல்லாண்மை பண்டுடையேன் இன்றுடையேன்
  காமுற்றார் ஏறும் மடல்.''', '''I once retained reserve and seemly manliness;
To-day I nought possess but lovers\' \'horse of palm\'.''',
                                '''Modesty and manliness were once my own; now, my own is the palmyra horse that is ridden by the lustful.''');
        k[1133] = Kural.factory(1134, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''காமக் கடும்புனல் உய்க்கும் நாணொடு
  நல்லாண்மை என்னும் புணை.''', '''Love\'s rushing tide will sweep away the raft
Of seemly manliness and shame combined.''',
                                '''The raft of modesty and manliness, is, alas, carried-off by the strong current of lust.''');
        k[1134] = Kural.factory(1135, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''தொடலைக் குறுந்தொடி தந்தாள் மடலொடு
  மாலை உழக்கும் துயர்.''', '''The maid that slender armlets wears, like flowers entwined,
Has brought me \'horse of palm,\' and pangs of eventide!''',
                                '''She with the small garland-like bracelets has given me the palmyra horse and the sorrow that is endured at night.''');
        k[1135] = Kural.factory(1136, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''மடலூர்தல் யாமத்தும் உள்ளுவேன் மன்ற
  படல்ஒல்லா பேதைக்கென் கண்.''', '''Of climbing \'horse of palm\' in midnight hour, I think;
My eyes know no repose for that same simple maid.''',
                                '''Mine eyes will not close in sleep on your mistress\'s account; even at midnight will I think of mounting the palmyra horse.''');
        k[1136] = Kural.factory(1137, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''கடலன்ன காமம் உழந்தும் மடலேறாப்
  பெண்ணின் பெருந்தக்க தில்.''', '''There\'s nought of greater worth than woman\'s long-enduring soul,
Who, vexed by love like ocean waves, climbs not the \'horse of palm\'.''',
                                '''There is nothing so noble as the womanly nature that would not ride the palmyra horse, though plunged a sea of lust.''');
        k[1137] = Kural.factory(1138, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''நிறையரியர் மன்அளியர் என்னாது காமம்
  மறையிறந்து மன்று படும்.''', '''In virtue hard to move, yet very tender, too, are we;
Love deems not so, would rend the veil, and court publicity!''',
                                '''Even the Lust (of women) transgresses its secrecy and appears in public, forgetting that they are too chaste and liberal (to be overcome by it).''');
        k[1138] = Kural.factory(1139, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''அறிகிலார் எல்லாரும் என்றேஎன் காமம்
  மறுகின் மறுகும் மருண்டு.''', '''\'There\'s no one knows my heart,\' so says my love,
And thus, in public ways, perturbed will rove.''',
                                '''My lust, feeling that it is not known by all, reels confused in the streets (of this town).''');
        k[1139] = Kural.factory(1140, '''காமத்துப்பால்''', '''நாணுத்துறவுரைத்தல்''', '''யாம்கண்ணின் காண நகுப அறிவில்லார்
  யாம்பட்ட தாம்படா ஆறு.''', '''Before my eyes the foolish make a mock of me,
Because they ne\'er endured the pangs I now must drie.''',
                                '''Even strangers laugh (at us) so as to be seen by us, for they have not suffered.''');
        k[1140] = Kural.factory(1141, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''அலரெழ ஆருயிர் ந஧ற்கும் அதனைப்
  பலரறியார் பாக்கியத் தால்.''', '''By this same rumour\'s rise, my precious life stands fast;
Good fortune grant the many know this not!''',
                                '''My precious life is saved by the raise of rumour, and this, to my good luck no others are aware of.''');
        k[1141] = Kural.factory(1142, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''மலரன்ன கண்ணாள் அருமை அறியாது
  அலரெமக்கு ஈந்ததிவ் வூர்.''', '''The village hath to us this rumour giv\'n, that makes her mine;
Unweeting all the rareness of the maid with flower-like eyne.''',
                                '''Not knowing the value of her whose eyes are like flowers this town has got up a rumour about me.''');
        k[1142] = Kural.factory(1143, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''உறாஅதோ ஊரறிந்த கெளவை அதனைப்
  பெறாஅது பெற்றன்ன நீர்த்து.''', '''The rumour spread within the town, is it not gain to me?
It is as though that were obtained that may not be.''',
                                '''Will I not get a rumour that is known to the (whole) town ? For what I have not got is as if I had got it (already).''');
        k[1143] = Kural.factory(1144, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''கவ்வையால் கவ்விது காமம் அதுவின்றேல்
  தவ்வென்னும் தன்மை இழந்து.''', '''The rumour rising makes my love to rise;
My love would lose its power and languish otherwise.''',
                                '''Rumour increases the violence of my passion; without it it would grow weak and waste away.''');
        k[1144] = Kural.factory(1145, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''களித்தொறும் கள்ளுண்டல் வேட்டற்றால் காமம்
  வெளிப்படுந் தோறும் இனிது.''', '''The more man drinks, the more he ever drunk would be;
The more my love\'s revealed, the sweeter \'tis to me!''',
                                '''As drinking liquor is delightful (to one) whenever one is in mirth, so is lust delightful to me whenever it is the subject of rumour.''');
        k[1145] = Kural.factory(1146, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''கண்டது மன்னும் ஒருநாள் அலர்மன்னும்
  திங்களைப் பாம்புகொண் டற்று.''', '''I saw him but one single day: rumour spreads soon
As darkness, when the dragon seizes on the moon.''',
                                '''It was but a single day that I looked on (my lover); but the rumour thereof has spread like the seizure of the moon by the serpent.''');
        k[1146] = Kural.factory(1147, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''ஊரவர் கெளவை எருவாக அன்னைசொல்
  நீராக நீளும்இந் நோய்.''', '''My anguish grows apace: the town\'s report
Manures it; my mother\'s word doth water it.''',
                                '''This malady (of lust) is manured by the talk of women and watered by the (harsh) words of my mother.''');
        k[1147] = Kural.factory(1148, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''நெய்யால் எரிநுதுப்பேம் என்றற்றால் கெளவையால்
  காமம் நுதுப்பேம் எனல்.''', '''With butter-oil extinguish fire! \'Twill prove
Harder by scandal to extinguish love.''',
                                '''To say that one could extinguish passion by rumour is like extinguishing fire with ghee.''');
        k[1148] = Kural.factory(1149, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''அலர்நாண ஒல்வதோ அஞ்சலோம்பு என்றார்
  பலர்நாண நீத்தக் கடை.''', '''When he who said \'Fear not!\' hath left me blamed,
While many shrink, can I from rumour hide ashamed?''',
                                '''When the departure of him who said "fear not" has put me to shame before others, why need I be ashamed of scandal.''');
        k[1149] = Kural.factory(1150, '''காமத்துப்பால்''', '''அலரறிவுறுத்தல்''', '''தாம்வேண்டின் நல்குவர் காதலர் யாம்வேண்டும்
  கெளவை எடுக்கும்இவ் வூர்.''', '''If we desire, who loves will grant what we require;
This town sends forth the rumour we desire!''',
                                '''The rumour I desire is raised by the town (itself); and my lover would if desired consent (to my following him).''');
        k[1150] = Kural.factory(1151, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''செல்லாமை உண்டேல் எனக்குரை மற்றுநின்
  வல்வரவு வாழ்வார்க் குரை.''', '''If you will say, \'I leave thee not,\' then tell me so;
Of quick return tell those that can survive this woe.''',
                                '''If it is not departure, tell me; but if it is your speedy return, tell it to those who would be alive then.''');
        k[1151] = Kural.factory(1152, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''இன்கண் உடைத்தவர் பார்வல் பிரிவஞ்சும்
  புன்கண் உடைத்தால் புணர்வு.''', '''It once was perfect joy to look upon his face;
But now the fear of parting saddens each embrace.''',
                                '''His very look was once pleasing; but (now) even intercourse is painful through fear of separation.''');
        k[1152] = Kural.factory(1153, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''அரிதரோ தேற்றம் அறிவுடையார் கண்ணும்
  பிரிவோ ரிடத்துண்மை யான்.''', '''To trust henceforth is hard, if ever he depart,
E\'en he, who knows his promise and my breaking heart.''',
                                '''As even the lover who understands (everything) may at times depart, confidence is hardly possible.''');
        k[1153] = Kural.factory(1154, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''அளித்தஞ்சல் என்றவர் நீப்பின் தெளித்தசொல்
  தேறியார்க்கு உண்டோ தவறு.''', '''If he depart, who fondly said, \'Fear not,\' what blame\'s incurred
By those who trusted to his reassuring word?''',
                                '''If he who bestowed his love and said "fear not" should depart, will it be the fault of those who believed in (his) assuring words ?''');
        k[1154] = Kural.factory(1155, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''ஓம்பின் அமைந்தார் பிரிவோம்பல் மற்றவர்
  நீங்கின் அரிதால் புணர்வு.''', '''If you would guard my life, from going him restrain
Who fills my life! If he depart, hardly we meet again.''',
                                '''If you would save (my life), delay the departure of my destined (husband); for if he departs, intercourse will become impossible.''');
        k[1155] = Kural.factory(1156, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''பிரிவுரைக்கும் வன்கண்ணர் ஆயின் அரிதவர்
  நல்குவர் என்னும் நசை.''', '''To cherish longing hope that he should ever gracious be,
Is hard, when he could stand, and of departure speak to me.''',
                                '''If he is so cruel as to mention his departure (to me), the hope that he would bestow (his love) must be given up.''');
        k[1156] = Kural.factory(1157, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''துறைவன் துறந்தமை தூற்றாகொல் முன்கை
  இறைஇறவா நின்ற வளை.''', '''The bracelet slipping from my wrist announced before
Departure of the Prince that rules the ocean shore.''',
                                '''Do not the rings that begin to slide down my fingers forebode the separation of my lord ?''');
        k[1157] = Kural.factory(1158, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''இன்னாது இனன்இல்ஊர் வாழ்தல் அதனினும்
  இன்னாது இனியார்ப் பிரிவு.''', '''\'Tis sad to sojourn in the town where no kind kinsmen dwell;
\'Tis sadder still to bid a friend beloved farewell.''',
                                '''Painful is it to live in a friendless town; but far more painful is it to part from one\'s lover.''');
        k[1158] = Kural.factory(1159, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''தொடிற்சுடின் அல்லது காமநோய் போல
  விடிற்சுடல் ஆற்றுமோ தீ.''', '''Fire burns the hands that touch; but smart of love
Will burn in hearts that far away remove.''',
                                '''Fire burns when touched; but, like the sickness of love, can it also burn when removed ?''');
        k[1159] = Kural.factory(1160, '''காமத்துப்பால்''', '''பிரிவாற்றாமை''', '''அரிதாற்றி அல்லல்நோய் நீக்கிப் பிரிவாற்றிப்
  பின்இருந்து வாழ்வார் பலர்.''', '''Sorrow\'s sadness meek sustaining, Driving sore distress away,
Separation uncomplaining Many bear the livelong day!''',
                                '''As if there were many indeed that can consent to the impossible, kill their pain, endure separation and yet continue to live afterwards.''');
        k[1160] = Kural.factory(1161, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''மறைப்பேன்மன் யானிஃதோ நோயை இறைப்பவர்க்கு
  ஊற்றுநீர் போல மிகும்.''', '''I would my pain conceal, but see! it surging swells,
As streams to those that draw from ever-springing wells.''',
                                '''I would hide this pain from others; but it (only) swells like a spring to those who drain it.''');
        k[1161] = Kural.factory(1162, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''கரத்தலும் ஆற்றேன்இந் நோயைநோய் செய்தார்க்கு
  உரைத்தலும் நாணுத் தரும்.''', '''I cannot hide this pain of mine, yet shame restrains
When I would tell it out to him who caused my pains.''',
                                '''I cannot conceal this pain, nor can I relate it without shame to him who has caused it.''');
        k[1162] = Kural.factory(1163, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''காமமும் நாணும் உயிர்காவாத் தூங்கும்என்
  நோனா உடம்பின் அகத்து.''', '''My soul, like porter\'s pole, within my wearied frame,
Sustains a two-fold burthen poised, of love and shame.''',
                                '''(Both) lust and shame, with my soul for their shoulder pole balance themselves on a body that cannot bear them.''');
        k[1163] = Kural.factory(1164, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''காமக் கடல்மன்னும் உண்டே அதுநீந்தும்
  ஏமப் புணைமன்னும் இல்.''', '''A sea of love, \'tis true, I see stretched out before,
But not the trusty bark that wafts to yonder shore.''',
                                '''There is indeed a flood of lust; but there is no raft of safety to cross it with.''');
        k[1164] = Kural.factory(1165, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''துப்பின் எவனாவர் மன்கொல் துயர்வரவு
  நட்பினுள் ஆற்று பவர்.''', '''Who work us woe in friendship\'s trustful hour,
What will they prove when angry tempests lower?''',
                                '''He who can produce sorrow from friendship, what can he not bring forth out of enmity ?''');
        k[1165] = Kural.factory(1166, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''இன்பம் கடல்மற்றுக் காமம் அஃதடுங்கால்
  துன்பம் அதனிற் பெரிது.''', '''A happy love \'s sea of joy; but mightier sorrows roll
From unpropitious love athwart the troubled soul.''',
                                '''The pleasure of lust is (as great as) the sea; but the pain of lust is far greater.''');
        k[1166] = Kural.factory(1167, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''காமக் கடும்புனல் நீந்திக் கரைகாணேன்
  யாமத்தும் யானே உளேன்.''', '''I swim the cruel tide of love, and can no shore descry,
In watches of the night, too, \'mid the waters, only I!''',
                                '''I have swam across the terrible flood of lust, but have not seen its shore; even at midnight I am alone; still I live.''');
        k[1167] = Kural.factory(1168, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''மன்னுயிர் எல்லாம் துயிற்றி அளித்திரா
  என்னல்லது இல்லை துணை.''', '''All living souls in slumber soft she steeps;
But me alone kind night for her companing keeps!''',
                                '''The night which graciously lulls to sleep all living creatures, has me alone for her companion.''');
        k[1168] = Kural.factory(1169, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''கொடியார் கொடுமையின் தாம்கொடிய விந்நாள்
  நெடிய கழியும் இரா.''', '''More cruel than the cruelty of him, the cruel one,
In these sad times are lengthening hours of night I watch alone.''',
                                '''The long nights of these days are far more cruel than the heartless one who is torturing me.''');
        k[1169] = Kural.factory(1170, '''காமத்துப்பால்''', '''படர்மெலிந்திரங்கல்''', '''உள்ளம்போன்று உள்வழிச் செல்கிற்பின் வெள்ளநீர்
  நீந்தல மன்னோஎன் கண்.''', '''When eye of mine would as my soul go forth to him,
It knows not how through floods of its own tears to swim.''',
                                '''Could mine eyes travel like my thoughts to the abode (of my absent lord), they would not swim in this flood of tears.''');
        k[1170] = Kural.factory(1171, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''கண்தாம் கலுழ்வ தெவன்கொலோ தண்டாநோய்
  தாம்காட்ட யாம்கண் டது.''', '''They showed me him, and then my endless pain
I saw: why then should weeping eyes complain?''',
                                '''As this incurable malady has been caused by my eyes which showed (him) to me, why should they now weep for (him).''');
        k[1171] = Kural.factory(1172, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''தெரிந்துணரா நோக்கிய உண்கண் பரிந்துணராப்
  பைதல் உழப்பது எவன்.''', '''How glancing eyes, that rash unweeting looked that day,
With sorrow measureless are wasting now away!''',
                                '''The dyed eyes that (then) looked without foresight, why should they now endure sorrow, without feeling sharply (their own fault).''');
        k[1172] = Kural.factory(1173, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''கதுமெனத் தாநோக்கித் தாமே கலுழும்
  இதுநகத் தக்க துடைத்து.''', '''The eyes that threw such eager glances round erewhile
Are weeping now. Such folly surely claims a smile!''',
                                '''They themselves looked eagerly (on him) and now they weep. Is not this to be laughed at ?''');
        k[1173] = Kural.factory(1174, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''பெயலாற்றா நீருலந்த உண்கண் உயலாற்றா
  உய்வில்நோய் என்கண் நிறுத்து.''', '''Those eyes have wept till all the fount of tears is dry,
That brought upon me pain that knows no remedy.''',
                                '''These painted eyes have caused me a lasting mortal disease; and now they can weep no more, the tears having dried up.''');
        k[1174] = Kural.factory(1175, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''படலாற்றா பைதல் உழக்கும் கடலாற்றாக்
  காமநோய் செய்தஎன் கண்.''', '''The eye that wrought me more than sea could hold of woes,
Is suffering pangs that banish all repose.''',
                                '''Mine eyes have caused me a lust that is greater than the sea and (they themselves) endure the torture of sleeplessness.''');
        k[1175] = Kural.factory(1176, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''ஓஒ இனிதே எமக்கிந்நோய் செய்தகண்
  தாஅம் இதற்பட் டது.''', '''Oho! how sweet a thing to see! the eye
That wrought this pain, in the same gulf doth lie.''',
                                '''The eyes that have given me this disease have themselves been seized with this (suffering). Oh! I am much delighted.''');
        k[1176] = Kural.factory(1177, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''உழந்துழந் துள்நீர் அறுக விழைந்திழைந்து
  வேண்டி அவர்க்கண்ட கண்.''', '''Aching, aching, let those exhaust their stream,
That melting, melting, that day gazed on him.''',
                                '''The eyes that became tender and gazed intently on him, may they suffer so much as to dry up the fountain of their tears.''');
        k[1177] = Kural.factory(1178, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''பேணாது பெட்டார் உளர்மன்னோ மற்றவர்க்
  காணாது அமைவில கண்.''', '''Who loved me once, onloving now doth here remain;
Not seeing him, my eye no rest can gain.''',
                                '''He is indeed here who loved me with his lips but not with his heart but mine eyes suffer from not seeing him.''');
        k[1178] = Kural.factory(1179, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''வாராக்கால் துஞ்சா வரின்துஞ்சா ஆயிடை
  ஆரஞர் உற்றன கண்.''', '''When he comes not, all slumber flies; no sleep when he is there;
Thus every way my eyes have troubles hard to bear.''',
                                '''When he is away they do not sleep; when he is present they do not sleep; in either case, mine eyes endure unbearable agony.''');
        k[1179] = Kural.factory(1180, '''காமத்துப்பால்''', '''கண்விதுப்பழிதல்''', '''மறைபெறல் ஊரார்க்கு அரிதன்றால் எம்போல்
  அறைபறை கண்ணார் அகத்து.''', '''It is not hard for all the town the knowledge to obtain,
When eyes, as mine, like beaten tambours, make the mystery plain.''',
                                '''It is not difficult for the people of this place to understand the secret of those whose eyes, like mine, are as it were beaten drums.''');
        k[1180] = Kural.factory(1181, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''நயந்தவர்க்கு நல்காமை நேர்ந்தேன் பசந்தவென்
  பண்பியார்க்கு உரைக்கோ பிற.''', '''I willed my lover absent should remain;
Of pining\'s sickly hue to whom shall I complain?''',
                                '''I who (then) consented to the absence of my loving lord, to whom can I (now) relate the fact of my having turned sallow.''');
        k[1181] = Kural.factory(1182, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''அவர்தந்தார் என்னும் தகையால் இவர்தந்தென்
  மேனிமேல் ஊரும் பசப்பு.''', '''\'He gave\': this sickly hue thus proudly speaks,
Then climbs, and all my frame its chariot makes.''',
                                '''Sallowness, as if proud of having been caused by him, would now ride on my person.''');
        k[1182] = Kural.factory(1183, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''சாயலும் நாணும் அவர்கொண்டார் கைம்மாறா
  நோயும் பசலையும் தந்து.''', '''Of comeliness and shame he me bereft,
While pain and sickly hue, in recompense, he left.''',
                                '''He has taken (away) my beauty and modesty, and given me instead disease and sallowness.''');
        k[1183] = Kural.factory(1184, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''உள்ளுவன் மன்யான் உரைப்பது அவர்திறமால்
  கள்ளம் பிறவோ பசப்பு.''', '''I meditate his words, his worth is theme of all I say,
This sickly hue is false that would my trust betray.''',
                                '''I think (of him); and what I speak about is but his excellence; still is there sallowness; and this is deceitful.''');
        k[1184] = Kural.factory(1185, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''உவக்காண்எம் காதலர் செல்வார் இவக்காண்என்
  மேனி பசப்பூர் வது.''', '''My lover there went forth to roam;
This pallor of my frame usurps his place at home.''',
                                '''Just as my lover departed then, did not sallowness spread here on my person ?''');
        k[1185] = Kural.factory(1186, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''விளக்கற்றம் பார்க்கும் இருளேபோல் கொண்கன்
  முயக்கற்றம் பார்க்கும் பசப்பு.''', '''As darkness waits till lamp expires, to fill the place,
This pallor waits till I enjoy no more my lord\'s embrace.''',
                                '''Just as darkness waits for the failing light; so does sallowness wait for the laxity of my husband\'s intercourse.''');
        k[1186] = Kural.factory(1187, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''புல்லிக் கிடந்தேன் புடைபெயர்ந்தேன் அவ்வளவில்
  அள்ளிக்கொள் வற்றே பசப்பு.''', '''I lay in his embrace, I turned unwittingly;
Forthwith this hue, as you might grasp it, came on me.''',
                                '''I who was in close embrace just turned aside and the moment I did so, sallowness came on me like something to be seized on.''');
        k[1187] = Kural.factory(1188, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''பசந்தாள் இவள்என்பது அல்லால் இவளைத்
  துறந்தார் அவர்என்பார் இல்.''', '''On me, because I pine, they cast a slur;
But no one says, \'He first deserted her.\'''',
                                '''Besides those who say "she has turned sallow" there are none who say "he has forsaken her".''');
        k[1188] = Kural.factory(1189, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''பசக்கமன் பட்டாங்கென் மேனி நயப்பித்தார்
  நன்னிலையர் ஆவர் எனின்.''', '''Well! let my frame, as now, be sicklied o\'er with pain,
If he who won my heart\'s consent, in good estate remain!''',
                                '''If he is clear of guilt who has conciliated me (to his departure) let my body suffer its due and turn sallow.''');
        k[1189] = Kural.factory(1190, '''காமத்துப்பால்''', '''பசப்புறுபருவரல்''', '''பசப்பெனப் பேர்பெறுதல் நன்றே நயப்பித்தார்
  நல்காமை தூற்றார் எனின்.''', '''\'Tis well, though men deride me for my sickly hue of pain;
If they from calling him unkind, who won my love, refrain.''',
                                '''It would be good to be said of me that I have turned sallow, if friends do not reproach with unkindness him who pleased me (then).''');
        k[1190] = Kural.factory(1191, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''தாம்வீழ்வார் தம்வீழப் பெற்றவர் பெற்றாரே
  காமத்துக் காழில் கனி.''', '''The bliss to be beloved by those they love who gains,
Of love the stoneless, luscious fruit obtains.''',
                                '''The women who are beloved by those whom they love, have they have not got the stone-less fruit of sexual delight ?''');
        k[1191] = Kural.factory(1192, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''வாழ்வார்க்கு வானம் பயந்தற்றால் வீழ்வார்க்கு
  வீழ்வார் அளிக்கும் அளி.''', '''As heaven on living men showers blessings from above,
Is tender grace by lovers shown to those they love.''',
                                '''The bestowal of love by the beloved on those who love them is like the rain raining (at the proper season) on those who live by it.''');
        k[1192] = Kural.factory(1193, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''வீழுநர் வீழப் படுவார்க்கு அமையுமே
  வாழுநம் என்னும் செருக்கு.''', '''Who love and are beloved to them alone
Belongs the boast, \'We\'ve made life\'s very joys our own.\'''',
                                '''The pride that says "we shall live" suits only those who are loved by their beloved (husbands).''');
        k[1193] = Kural.factory(1194, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''வீழப் படுவார் கெழீஇயிலர் தாம்வீழ்வார்
  வீழப் படாஅர் எனின்.''', '''Those well-beloved will luckless prove,
Unless beloved by those they love.''',
                                '''Even those who are esteemed (by other women) are devoid of excellence, if they are not loved by their beloved.''');
        k[1194] = Kural.factory(1195, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''நாம்காதல் கொண்டார் நமக்கெவன் செய்பவோ
  தாம்காதல் கொள்ளாக் கடை.''', '''From him I love to me what gain can be,
Unless, as I love him, he loveth me?''',
                                '''He who is beloved by me, what will he do to me, if I am not beloved by him ?''');
        k[1195] = Kural.factory(1196, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''ஒருதலையான் இன்னாது காமம்காப் போல
  இருதலை யானும் இனிது.''', '''Love on one side is bad; like balanced load
By porter borne, love on both sides is good.''',
                                '''Lust, like the weight of the KAVADI, pains if it lies in one end only but pleases if it is in both.''');
        k[1196] = Kural.factory(1197, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''பருவரலும் பைதலும் காணான்கொல் காமன்
  ஒருவர்கண் நின்றொழுகு வான்.''', '''While Kaman rushes straight at me alone,
Is all my pain and wasting grief unknown?''',
                                '''Would not cupid who abides and contends in one party (only) witness the pain and sorrow (in that party)?''');
        k[1197] = Kural.factory(1198, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''வீழ்வாரின் இன்சொல் பெறாஅது உலகத்து
  வாழ்வாரின் வன்கணார் இல்.''', '''Who hear from lover\'s lips no pleasant word from day to day,
Yet in the world live out their life,- no braver souls than they!''',
                                '''There is no one in the world so hard-hearted as those who can live without receiving (even) a kind word from their beloved.''');
        k[1198] = Kural.factory(1199, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''நசைஇயார் நல்கார் எனினும் அவர்மாட்டு
  இசையும் இனிய செவிக்கு.''', '''Though he my heart desires no grace accords to me,
Yet every accent of his voice is melody.''',
                                '''Though my beloved bestows no love on one, still are his words sweet to my ears.''');
        k[1199] = Kural.factory(1200, '''காமத்துப்பால்''', '''தனிப்படர்மிகுதி''', '''உறாஅர்க்கு உறுநோய் உரைப்பாய் கடலைச்
  செறாஅஅய் வாழிய நெஞ்சு.''', '''Tell him thy pain that loves not thee?
Farewell, my soul, fill up the sea!''',
                                '''Live, O my soul, would you who relate your great sorrow to strangers, try rather to fill up your own sea (of sorrow).''');
        k[1200] = Kural.factory(1201, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''உள்ளினும் தீராப் பெருமகிழ் செய்தலால்
  கள்ளினும் காமம் இனிது.''', '''From thought of her unfailing gladness springs,
Sweeter than palm-rice wine the joy love brings.''',
                                '''Sexuality is sweeter than liquor, because when remembered, it creates a most rapturous delight.''');
        k[1201] = Kural.factory(1202, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''எனைத்தொனறு ஏனிதேகாண் காமம்தாம் வீழ்வார்
  நினைப்ப வருவதொன்று ஏல்.''', '''How great is love! Behold its sweetness past belief!
Think on the lover, and the spirit knows no grief.''',
                                '''Even to think of one\'s beloved gives one no pain. Sexuality, in any degree, is always delightful.''');
        k[1202] = Kural.factory(1203, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''நினைப்பவர் போன்று நினையார்கொல் தும்மல்
  சினைப்பது போன்று கெடும்.''', '''A fit of sneezing threatened, but it passed away;
He seemed to think of me, but do his fancies stray?''',
                                '''I feel as if I am going to sneeze but do not, and (therefore) my beloved is about to think (of me) but does not.''');
        k[1203] = Kural.factory(1204, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''யாமும் உளேங்கொல் அவர்நெஞ்சத்து எந்நெஞ்சத்து
  ஓஒ உளரே அவர்.''', '''Have I a place within his heart!
From mine, alas! he never doth depart.''', '''He continues to abide in my soul, do I likewise abide in his ?''');
        k[1204] = Kural.factory(1205, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''தம்நெஞ்சத்து எம்மைக் கடிகொண்டார் நாணார்கொல்
  எம்நெஞ்சத்து ஓவா வரல்.''', '''Me from his heart he jealously excludes:
Hath he no shame who ceaseless on my heart intrudes?''',
                                '''He who has imprisoned me in his soul, is he ashamed to enter incessantly into mine.''');
        k[1205] = Kural.factory(1206, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''மற்றியான் என்னுளேன் மன்னோ அவரொடியான்
  உற்றநாள் உள்ள உளேன்.''', '''How live I yet? I live to ponder o\'er
The days of bliss with him that are no more.''',
                                '''I live by remembering my (former) intercourse with him; if it were not so, how could I live ?''');
        k[1206] = Kural.factory(1207, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''மறப்பின் எவனாவன் மற்கொல் மறப்பறியேன்
  உள்ளினும் உள்ளம் சுடும்.''', '''If I remembered not what were I then? And yet,
The fiery smart of what my spirit knows not to forget!''',
                                '''I have never forgotten (the pleasure); even to think of it burns my soul; could I live, if I should ever forget it ?''');
        k[1207] = Kural.factory(1208, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''எனைத்து நினைப்பினும் காயார் அனைத்தன்றோ
  காதலர் செய்யும் சிறப்பு.''', '''My frequent thought no wrath excites. It is not so?
This honour doth my love on me bestow.''',
                                '''He will not be angry however much I may think of him; is it not so much the delight my beloved affords me ?''');
        k[1208] = Kural.factory(1209, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''விளியுமென் இன்னுயிர் வேறல்லம் என்பார்
  அளியின்மை ஆற்ற நினைந்து.''', '''Dear life departs, when his ungracious deeds I ponder o\'er,
Who said erewhile, \'We\'re one for evermore\'.''',
                                '''My precious life is wasting away by thinking too much on the cruelty of him who said we were not different.''');
        k[1209] = Kural.factory(1210, '''காமத்துப்பால்''', '''நினைந்தவர்புலம்பல்''', '''விடாஅது சென்றாரைக் கண்ணினால் காணப்
  படாஅதி வாழி மதி.''', '''Set not; so may\'st thou prosper, moon! that eyes may see
My love who went away, but ever bides with me.''',
                                '''May you live, O Moon! Do not set, that I mine see him who has departed without quitting my soul.''');
        k[1210] = Kural.factory(1211, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''காதலர் தூதொடு வந்த கனவினுக்கு
  யாதுசெய் வேன்கொல் விருந்து.''', '''It came and brought to me, that nightly vision rare,
A message from my love,- what feast shall I prepare?''',
                                '''Where with shall I feast the dream which has brought me my dear one\'s messenger ?''');
        k[1211] = Kural.factory(1212, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''கயலுண்கண் யானிரப்பத் துஞ்சிற் கலந்தார்க்கு
  உயலுண்மை சாற்றுவேன் மன்.''', '''If my dark, carp-like eye will close in sleep, as I implore,
The tale of my long-suffering life I\'ll tell my loved one o\'er.''',
                                '''If my fish-like painted eyes should, at my begging, close in sleep, I could fully relate my sufferings to my lord.''');
        k[1212] = Kural.factory(1213, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவினால் நல்கா தவரைக் கனவினால்
  காண்டலின் உண்டென் உயிர்.''', '''Him, who in waking hour no kindness shows,
In dreams I see; and so my lifetime goes!''',
                                '''My life lasts because in my dream I behold him who does not favour me in my waking hours.''');
        k[1213] = Kural.factory(1214, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''கனவினான் உண்டாகும் காமம் நனவினான்
  நல்காரை நாடித் தரற்கு.''', '''Some pleasure I enjoy when him who loves not me
In waking hours, the vision searches out and makes me see.''',
                                '''There is pleasure in my dream, because in it I seek and obtain him who does not visit me in my wakefulness.''');
        k[1214] = Kural.factory(1215, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவினால் கண்டதூஉம் ஆங்கே கனவுந்தான்
  கண்ட பொழுதே இனிது.''', '''As what I then beheld in waking hour was sweet,
So pleasant dreams in hour of sleep my spirit greet.''',
                                '''I saw him in my waking hours, and then it was pleasant; I see him just now in my dream, and it is (equally) pleasant.''');
        k[1215] = Kural.factory(1216, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவென ஒன்றில்லை ஆயின் கனவினால்
  காதலர் நீங்கலர் மன்.''', '''And if there were no waking hour, my love
In dreams would never from my side remove.''',
                                '''Were there no such thing as wakefulness, my beloved (who visited me) in my dream would not depart from me.''');
        k[1216] = Kural.factory(1217, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவினால் நல்காக் கொடியார் கனவனால்
  என்எம்மைப் பீழிப் பது.''', '''The cruel one, in waking hour, who all ungracious seems,
Why should he thus torment my soul in nightly dreams?''',
                                '''The cruel one who would not favour me in my wakefulness, what right has he to torture me in my dreams?''');
        k[1217] = Kural.factory(1218, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''துஞ்சுங்கால் தோள்மேலர் ஆகி விழிக்குங்கால்
  நெஞ்சத்தர் ஆவர் விரைந்து.''', '''And when I sleep he holds my form embraced;
And when I wake to fill my heart makes haste!''',
                                '''When I am asleep he rests on my shoulders, (but) when I awake he hastens into my soul.''');
        k[1218] = Kural.factory(1219, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவினால் நல்காரை நோவர் கனவினால்
  காதலர்க் காணா தவர்.''', '''In dreams who ne\'er their lover\'s form perceive,
For those in waking hours who show no love will grieve.''',
                                '''They who have no dear ones to behold in their dreams blame him who visits me not in my waking hours.''');
        k[1219] = Kural.factory(1220, '''காமத்துப்பால்''', '''கனவுநிலையுரைத்தல்''', '''நனவினால் நம்நீத்தார் என்பர் கனவினால்
  காணார்கொல் இவ்வூ ரவர்.''', '''They say, that he in waking hours has left me lone;
In dreams they surely see him not,- these people of the town;''',
                                '''The women of this place say he has forsaken me in my wakefulness. I think they have not seen him visit me in my dreams.''');
        k[1220] = Kural.factory(1221, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''மாலையோ அல்லை மணந்தார் உயிருண்ணும்
  வேலைநீ வாழி பொழுது.''', '''Thou art not evening, but a spear that doth devour
The souls of brides; farewell, thou evening hour!''',
                                '''Live, O you evening are you (the former) evening? No, you are the season that slays (married) women.''');
        k[1221] = Kural.factory(1222, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''புன்கண்ணை வாழி மருள்மாலை எம்கேள்போல்
  வன்கண்ண தோநின் துணை.''', '''Thine eye is sad; Hail, doubtful hour of eventide!
Of cruel eye, as is my spouse, is too thy bride?''',
                                '''A long life to you, O dark evening! You are sightless. Is your help-mate (also) as hard-hearted as mine.''');
        k[1222] = Kural.factory(1223, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''பனிஅரும்பிப் பைதல்கொள் மாலை துனிஅரும்பித்
  துன்பம் வளர வரும்.''', '''With buds of chilly dew wan evening\'s shade enclose;
My anguish buds space and all my sorrow grows.''',
                                '''The evening that (once) came in with trembling and dimness (now) brings me an aversion for life and increasing sorrow.''');
        k[1223] = Kural.factory(1224, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''காதலர் இல்வழி மாலை கொலைக்களத்து
  ஏதிலர் போல வரும்.''', '''When absent is my love, the evening hour descends,
As when an alien host to field of battle wends.''',
                                '''In the absence of my lover, evening comes in like slayers on the field of slaughter.''');
        k[1224] = Kural.factory(1225, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''காலைக்குச் செய்தநன்று என்கொல் எவன்கொல்யான்
  மாலைக்குச் செய்த பகை.''', '''O morn, how have I won thy grace? thou bring\'st relief
O eve, why art thou foe! thou dost renew my grief.''',
                                '''What good have I done to morning (and) what evil to evening?''');
        k[1225] = Kural.factory(1226, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''மாலைநோய் செய்தல் மணந்தார் அகலாத
  காலை அறிந்த திலேன்.''', '''The pangs that evening brings I never knew,
Till he, my wedded spouse, from me withdrew.''',
                                '''Previous to my husband\'s departure, I know not the painful nature of evening.''');
        k[1226] = Kural.factory(1227, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''காலை அரும்பிப் பகலெல்லாம் போதாகி
  மாலை மலரும்இந் நோய்.''', '''My grief at morn a bud, all day an opening flower,
Full-blown expands in evening hour.''',
                                '''This malady buds forth in the morning, expands all day long and blossoms in the evening.''');
        k[1227] = Kural.factory(1228, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''அழல்போலும் மாலைக்குத் தூதாகி ஆயன்
  குழல்போலும் கொல்லும் படை.''', '''The shepherd\'s pipe is like a murderous weapon, to my ear,
For it proclaims the hour of ev\'ning\'s fiery anguish near.''',
                                '''The shepherd\'s flute now sounds as a fiery forerunner of night, and is become a weapon that slays (me).''');
        k[1228] = Kural.factory(1229, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''பதிமருண்டு பைதல் உழக்கும் மதிமருண்டு
  மாலை படர்தரும் போழ்து.''', '''If evening\'s shades, that darken all my soul, extend;
From this afflicted town will would of grief ascend.''',
                                '''When night comes on confusing (everyone\'s) mind, the (whole) town will lose its sense and be plunged in sorrow.''');
        k[1229] = Kural.factory(1230, '''காமத்துப்பால்''', '''பொழுதுகண்டிரங்கல்''', '''பொருள்மாலை யாளரை உள்ளி மருள்மாலை
  மாயும்என் மாயா உயிர்.''', '''This darkening eve, my darkling soul must perish utterly;
Remembering him who seeks for wealth, but seeks not me.''',
                                '''My (hitherto) unextinguished life is now lost in this bewildering night at the thought of him who has the nature of wealth.''');
        k[1230] = Kural.factory(1231, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''சிறுமை நமக்கொழியச் சேட்சென்றார் உள்ளி
  நறுமலர் நாணின கண்.''', '''Thine eyes grown dim are now ashamed the fragrant flow\'rs to see,
Thinking on him, who wand\'ring far, leaves us in misery.''',
                                '''While we endure the unbearable sorrow, your eyes weep for him who is gone afar, and shun (the sight of) fragrant flowers.''');
        k[1231] = Kural.factory(1232, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''நயந்தவர் நல்காமை சொல்லுவ போலும்
  பசந்து பனிவாரும் கண்.''', '''The eye, with sorrow wan, all wet with dew of tears,
As witness of the lover\'s lack of love appears.''',
                                '''The discoloured eyes that shed tears profusely seem to betray the unkindness of our beloved.''');
        k[1232] = Kural.factory(1233, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''தணந்தமை சால அறிவிப்ப போலும்
  மணந்தநாள் வீங்கிய தோள்.''', '''These withered arms, desertion\'s pangs abundantly display,
That swelled with joy on that glad nuptial day.''',
                                '''The shoulders that swelled on the day of our union (now) seem to announce our separation clearly (to the public).''');
        k[1233] = Kural.factory(1234, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''பணைநீங்கிப் பைந்தொடி சோரும் துணைநீங்கித்
  தொல்கவின் வாடிய தோள்.''', '''When lover went, then faded all their wonted charms,
And armlets\' golden round slips off from these poor wasted arms.''',
                                '''In the absence of your consort, your shoulders having lost their former beauty and fulness, your bracelets of pure gold have become loose.''');
        k[1234] = Kural.factory(1235, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''கொடியார் கொடுமை உரைக்கும் தொடியொடு
  தொல்கவின் வாடிய தோள்.''', '''These wasted arms, the bracelet with their wonted beauty gone,
The cruelty declare of that most cruel one.''',
                                '''The (loosened) bracelets, and the shoulders from which the old beauty has faded, relate the cruelty of the pitiless one.''');
        k[1235] = Kural.factory(1236, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''தொடியொடு தோள்நெகிழ நோவல் அவரைக்
  கொடியர் எனக்கூறல் நொந்து.''', '''I grieve, \'tis pain to me to hear him cruel chid,
Because the armlet from my wasted arm has slid.''',
                                '''I am greatly pained to hear you call him a cruel man, just because your shoulders are reduced and your bracelets loosened.''');
        k[1236] = Kural.factory(1237, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''பாடுபெறுதியோ நெஞ்சே கொடியார்க்கென் வாடுதோட்
  பூசல் உரைத்து.''', '''My heart! say ought of glory wilt thou gain,
If to that cruel one thou of thy wasted arms complain?''',
                                '''Can you O my soul! gain glory by relating to the (so-called) cruel one the clamour of my fading shoulders?''');
        k[1237] = Kural.factory(1238, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''முயங்கிய கைகளை ஊக்கப் பசந்தது
  பைந்தொடிப் பேதை நுதல்.''', '''One day the fervent pressure of embracing arms I checked,
Grew wan the forehead of the maid with golden armlet decked.''',
                                '''When I once loosened the arms that were in embrace, the forehead of the gold-braceleted women turned sallow.''');
        k[1238] = Kural.factory(1239, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''முயக்கிடைத் தண்வளி போழப் பசப்புற்ற
  பேதை பெருமழைக் கண்.''', '''As we embraced a breath of wind found entrance there;
The maid\'s large liquid eyes were dimmed with care.''',
                                '''When but a breath of breeze penetrated our embrace, her large cool eyes became sallow.''');
        k[1239] = Kural.factory(1240, '''காமத்துப்பால்''', '''உறுப்புநலனழிதல்''', '''கண்ணின் பசப்போ பருவரல் எய்தின்றே
  ஒண்ணுதல் செய்தது கண்டு.''', '''The dimness of her eye felt sorrow now,
Beholding what was done by that bright brow.''',
                                '''Was it at the sight of what the bright forehead had done that the sallowness of her eyes became sad?''');
        k[1240] = Kural.factory(1241, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''நினைத்தொன்று சொல்லாயோ நெஞ்சே எனைத்தொன்றும்
  எவ்வநோய் தீர்க்கும் மருந்து.''', '''My heart, canst thou not thinking of some med\'cine tell,
Not any one, to drive away this grief incurable?''',
                                '''O my soul, will you not think and tell me some medicine be it what it may, that can cure this incurable malady?''');
        k[1241] = Kural.factory(1242, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''காதல் அவரிலர் ஆகநீ நோவது
  பேதைமை வாழியென் நெஞ்சு.''', '''Since he loves not, thy smart
Is folly, fare thee well my heart!''',
                                '''May you live, O my soul! While he is without love, for you to suffer is (simple) folly.''');
        k[1242] = Kural.factory(1243, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''இருந்துள்ளி என்பரிதல் நெஞ்சே பரிந்துள்ளல்
  பைதல்நோய் செய்தார்கண் இல்.''', '''What comes of sitting here in pining thought, O heart? He knows
No pitying thought, the cause of all these wasting woes.''',
                                '''O my soul! why remain (here) and suffer thinking (of him)? There are no lewd thoughts (of you) in him who has caused you this disease of sorrow.''');
        k[1243] = Kural.factory(1244, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''கண்ணும் கொளச்சேறி நெஞ்சே இவையென்னைத்
  தின்னும் அவர்க்காணல் உற்று.''', '''O rid me of these eyes, my heart; for they,
Longing to see him, wear my life away.''',
                                '''O my soul! take my eyes also with you, (if not), these would eat me up (in their desire) to see him.''');
        k[1244] = Kural.factory(1245, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''செற்றார் எனக்கை விடல்உண்டோ நெஞ்சேயாம்
  உற்றால் உறாஅ தவர்.''', '''O heart, as a foe, can I abandon utterly
Him who, though I long for him, longs not for me?''',
                                '''O my soul! can he who loves not though he is beloved, be forsaken saying he hates me (now)?''');
        k[1245] = Kural.factory(1246, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''கலந்துணர்த்தும் காதலர்க் கண்டாற் புலந்துணராய்
  பொய்க்காய்வு காய்திஎன் நெஞ்சு.''', '''My heart, false is the fire that burns; thou canst not wrath maintain,
If thou thy love behold, embracing, soothing all thy pain.''',
                                '''O my soul! when you see the dear one who remove dislike by intercourse, you are displeased and continue to be so. Nay, your displeasure is (simply) false.''');
        k[1246] = Kural.factory(1247, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''காமம் விடுஒன்றோ நாண்விடு நன்னெஞ்சே
  யானோ பொறேன்இவ் விரண்டு.''', '''Or bid thy love, or bid thy shame depart;
For me, I cannot bear them both, my worthy heart!''',
                                '''O my good soul, give up either lust or honour, as for me I can endure neither.''');
        k[1247] = Kural.factory(1248, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''பரிந்தவர் நல்காரென்று ஏங்கிப் பிரிந்தவர்
  பின்செல்வாய் பேதைஎன் நெஞ்சு.''', '''Thou art befooled, my heart, thou followest him who flees from thee;
And still thou yearning criest: \'He will nor pity show nor love to me.\'''',
                                '''You are a fool, O my soul! to go after my departed one, while you mourn that he is not kind enough to favour you.''');
        k[1248] = Kural.factory(1249, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''உள்ளத்தார் காத லவரால் உள்ளிநீ
  யாருழைச் சேறியென் நெஞ்சு.''', '''My heart! my lover lives within my mind;
Roaming, whom dost thou think to find?''',
                                '''O my soul! to whom would you repair, while the dear one is within yourself?''');
        k[1249] = Kural.factory(1250, '''காமத்துப்பால்''', '''நெஞ்சொடுகிளத்தல்''', '''துன்னாத் துறந்தாரை நெஞ்சத்து உடையேமா
  இன்னும் இழத்தும் கவின்.''', '''If I should keep in mind the man who utterly renounces me,
My soul must suffer further loss of dignity.''',
                                '''If I retain in my heart him who has left me without befriending me, I shall lose even the (inward) beauty that remains.''');
        k[1250] = Kural.factory(1251, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''காமக் கணிச்சி உடைக்கும் நிறையென்னும்
  நாணுத்தாழ் வீழ்த்த கதவு.''', '''Of womanly reserve love\'s axe breaks through the door,
Barred by the bolt of shame before.''',
                                '''The axe of lust can break the door of chastity which is bolted with the bolt of modesty.''');
        k[1251] = Kural.factory(1252, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''காமம் எனவொன்றோ கண்ணின்றென் நெஞ்சத்தை
  யாமத்தும் ஆளும் தொழில்.''', '''What men call love is the one thing of merciless power;
It gives my soul no rest, e\'en in the midnight hour.''',
                                '''Even at midnight is my mind worried by lust, and this one thing, alas! is without mercy.''');
        k[1252] = Kural.factory(1253, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''மறைப்பேன்மன் காமத்தை யானோ குறிப்பின்றித்
  தும்மல்போல் தோன்றி விடும்.''', '''I would my love conceal, but like a sneeze
It shows itself, and gives no warning sign.''',
                                '''I would conceal my lust, but alas, it yields not to my will but breaks out like a sneeze.''');
        k[1253] = Kural.factory(1254, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''நிறையுடையேன் என்பேன்மன் யானோஎன் காமம்
  மறையிறந்து மன்று படும்.''', '''In womanly reserve I deemed myself beyond assail;
But love will come abroad, and casts away the veil.''',
                                '''I say I would be firm, but alas, my malady breaks out from its concealment and appears in public.''');
        k[1254] = Kural.factory(1255, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''செற்றார்பின் செல்லாப் பெருந்தகைமை காமநோய்
  உற்றார் அறிவதொன்று அன்று.''', '''The dignity that seeks not him who acts as foe,
Is the one thing that loving heart can never know.''',
                                '''The dignity that would not go after an absent lover is not known to those who are sticken by love.''');
        k[1255] = Kural.factory(1256, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''செற்றவர் பின்சேறல் வேண்டி அளித்தரோ
  எற்றென்னை உற்ற துயர்.''', '''My grief how full of grace, I pray you see!
It seeks to follow him that hateth me.''',
                                '''The sorrow I have endured by desiring to go after my absent lover, in what way is it excellent?''');
        k[1256] = Kural.factory(1257, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''நாணென ஒன்றோ அறியலம் காமத்தால்
  பேணியார் பெட்ப செயின்.''', '''No sense of shame my gladdened mind shall prove,
When he returns my longing heart to bless with love.''',
                                '''I know nothing like shame when my beloved does from love (just) what is desired (by me).''');
        k[1257] = Kural.factory(1258, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''பன்மாயக் கள்வன் பணிமொழி அன்றோநம்
  பெண்மை உடைக்கும் படை.''', '''The words of that deceiver, versed in every wily art,
Are instruments that break through every guard of woman\'s heart!''',
                                '''Are not the enticing words of my trick-abounding roguish lover the weapon that breaks away my feminine firmness?''');
        k[1258] = Kural.factory(1259, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''புலப்பல் எனச்சென்றேன் புல்லினேன் நெஞ்சம்
  கலத்தல் உறுவது கண்டு.''', '''\'I \'ll shun his greeting\'; saying thus with pride away I went:
I held him in my arms, for straight I felt my heart relent.''',
                                '''I said I would feign dislike and so went (away); (but) I embraced him the moment I say my mind began to unite with him!''');
        k[1259] = Kural.factory(1260, '''காமத்துப்பால்''', '''நிறையழிதல்''', '''நிணந்தீயில் இட்டன்ன நெஞ்சினார்க்கு உண்டோ
  புணர்ந்தூடி நிற்பேம் எனல்.''', '''\'We \'ll stand aloof and then embrace\': is this for them to say,
Whose hearts are as the fat that in the blaze dissolves away?''',
                                '''Is it possible for those whose hearts melt like fat in the fire to say they can feign a strong dislike and remain so?''');
        k[1260] = Kural.factory(1261, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''வாளற்றுப் புற்கென்ற கண்ணும் அவர்சென்ற
  நாளொற்றித் தேய்ந்த விரல்.''', '''My eyes have lost their brightness, sight is dimmed; my fingers worn,
With nothing on the wall the days since I was left forlorn.''',
                                '''My finger has worn away by marking (on the wall) the days he has been absent while my eyes have lost their lustre and begin to fail.''');
        k[1261] = Kural.factory(1262, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''இலங்கிழாய் இன்று மறப்பின்என் தோள்மேல்
  கலங்கழியும் காரிகை நீத்து.''', '''O thou with gleaming jewels decked, could I forget for this one day,
Henceforth these bracelets from my arms will slip, my beauty worn away.''',
                                '''O you bright-jewelled maid, if I forget (him) today, my shoulders will lose their beauty even in the other life and make my bracelets loose.''');
        k[1262] = Kural.factory(1263, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''உரன்நசைஇ உள்ளம் துணையாகச் சென்றார்
  வரல்நசைஇ இன்னும் உளேன்.''', '''On victory intent, His mind sole company he went;
And I yet life sustain! And long to see his face again!''',
                                '''I still live by longing for the arrival of him who has gone out of love for victory and with valour as his guide.''');
        k[1263] = Kural.factory(1264, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''கூடிய காமம் பிரிந்தார் வரவுள்ளிக்
  கோடுகொ டேறுமென் நெஞ்சு.''', '''\'He comes again, who left my side, and I shall taste love\'s joy,\'-
My heart with rapture swells, when thoughts like these my mind employ.''',
                                '''My heart is rid of its sorrow and swells with rapture to think of my absent lover returning with his love.''');
        k[1264] = Kural.factory(1265, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''காண்கமன் கொண்கனைக் கண்ணாரக் கண்டபின்
  நீங்கும்என் மென்தோள் பசப்பு.''', '''O let me see my spouse again and sate these longing eyes!
That instant from my wasted frame all pallor flies.''',
                                '''May I look on my lover till I am satisfied and thereafter will vanish the sallowness of my slender shoulders.''');
        k[1265] = Kural.factory(1266, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''வருகமன் கொண்கன் ஒருநாள் பருகுவன்
  பைதல்நோய் எல்லாம் கெட.''', '''O let my spouse but come again to me one day!
I\'ll drink that nectar: wasting grief shall flee away.''',
                                '''May my husband return some day; and then will I enjoy (him) so as to destroy all this agonizing sorrow.''');
        k[1266] = Kural.factory(1267, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''புலப்பேன்கொல் புல்லுவேன் கொல்லோ கலப்பேன்கொல்
  கண்அன்ன கேளிர் விரன்.''', '''Shall I draw back, or yield myself, or shall both mingled be,
When he returns, my spouse, dear as these eyes to me.''',
                                '''On the return of him who is as dear as my eyes, am I displeased or am I to embrace (him); or am I to do both?''');
        k[1267] = Kural.factory(1268, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''வினைகலந்து வென்றீக வேந்தன் மனைகலந்து
  மாலை அயர்கம் விருந்து.''', '''O would my king would fight, o\'ercome, devide the spoil;
At home, to-night, the banquet spread should crown the toil.''',
                                '''Let the king fight and gain (victories); (but) let me be united to my wife and feast the evening.''');
        k[1268] = Kural.factory(1269, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''ஒருநாள் எழுநாள்போல் செல்லும்சேண் சென்றார்
  வருநாள்வைத்து ஏங்கு பவர்க்கு.''', '''One day will seem like seven to those who watch and yearn
For that glad day when wanderers from afar return.''',
                                '''To those who suffer waiting for the day of return of their distant lovers one day is as long as seven days.''');
        k[1269] = Kural.factory(1270, '''காமத்துப்பால்''', '''அவர்வயின்விதும்பல்''', '''பெறின்என்னாம் பெற்றக்கால் என்னாம் உறினென்னாம்
  உள்ளம் உடைந்துக்கக் கால்.''', '''What\'s my return, the meeting hour, the wished-for greeting worth,
If she heart-broken lie, with all her life poured forth?''',
                                '''After (my wife) has died of a broken heart, what good will there be if she is to receive me, has received me, or has even embraced me?''');
        k[1270] = Kural.factory(1271, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''கரப்பினுங் கையிகந் தொல்லாநின் உண்கண்
  உரைக்கல் உறுவதொன் றுண்டு.''', '''Thou hid\'st it, yet thine eye, disdaining all restraint,
Something, I know not, what, would utter of complaint.''',
                                '''Though you would conceal (your feelings), your painted eyes would not, for, transgressing (their bounds), they tell (me) something.''');
        k[1271] = Kural.factory(1272, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''கண்ணிறைந்த காரிகைக் காம்பேர்தோட் பேதைக்குப்
  பெண்நிறைந்த நீர்மை பெரிது.''', '''The simple one whose beauty fills mine eye, whose shoulders curve
Like bambu stem, hath all a woman\'s modest sweet reserve.''',
                                '''Unusually great is the female simplicity of your maid whose beauty fills my eyes and whose shoulders resemble the bamboo.''');
        k[1272] = Kural.factory(1273, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''மணியில் திகழ்தரு நூல்போல் மடந்தை
  அணியில் திகழ்வதொன்று உண்டு.''', '''As through the crystal beads is seen the thread on which they \'re strung
So in her beauty gleams some thought cannot find a tongue.''',
                                '''There is something that is implied in the beauty of this woman, like the thread that is visible in a garland of gems.''');
        k[1273] = Kural.factory(1274, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''முகைமொக்குள் உள்ளது நாற்றம்போல் பேதை
  நகைமொக்குள் உள்ளதொன் றுண்டு.''', '''As fragrance in the opening bud, some secret lies
Concealed in budding smile of this dear damsel\'s eyes.''',
                                '''There is something in the unmatured smile of this maid like the fragrance that is contained in an unblossomed bud.''');
        k[1274] = Kural.factory(1275, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''செறிதொடி செய்திறந்த கள்ளம் உறுதுயர்
  தீர்க்கும் மருந்தொன்று உடைத்து.''', '''The secret wiles of her with thronging armlets decked,
Are medicines by which my raising grief is checked.''',
                                '''The well-meant departure of her whose bangles are tight-fitting contains a remedy that can cure my great sorrow.''');
        k[1275] = Kural.factory(1276, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''பெரிதாற்றிப் பெட்பக் கலத்தல் அரிதாற்றி
  அன்பின்மை சூழ்வ துடைத்து.''', '''While lovingly embracing me, his heart is only grieved:
It makes me think that I again shall live of love bereaved.''',
                                '''The embrace that fills me with comfort and gladness is capable of enduring (my former) sorrow and meditating on his want of love.''');
        k[1276] = Kural.factory(1277, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''தண்ணந் துறைவன் தணந்தமை நம்மினும்
  முன்னம் உணர்ந்த வளை.''', '''My severance from the lord of this cool shore,
My very armlets told me long before.''',
                                '''My bracelets have understood before me the (mental) separation of him who rules the cool seashore.''');
        k[1277] = Kural.factory(1278, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''நெருநற்றுச் சென்றார்எம் காதலர் யாமும்
  எழுநாளேம் மேனி பசந்து.''', '''My loved one left me, was it yesterday?
Days seven my pallid body wastes away!''',
                                '''It was but yesterday my lover departed (from me); and it is seven days since my complexion turned sallow.''');
        k[1278] = Kural.factory(1279, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''தொடிநோக்கி மென்தோளும் நோக்கி அடிநோக்கி
  அஃதாண் டவள்செய் தது.''', '''She viewed her tender arms, she viewed the armlets from them slid;
She viewed her feet: all this the lady did.''',
                                '''She looked at her bracelets, her tender shoulders, and her feet; this was what she did there (significantly).''');
        k[1279] = Kural.factory(1280, '''காமத்துப்பால்''', '''குறிப்பறிவுறுத்தல்''', '''பெண்ணினால் பெண்மை உடைத்தென்ப கண்ணினால்
  காமநோய் சொல்லி இரவு.''', '''To show by eye the pain of love, and for relief to pray,
Is womanhood\'s most womanly device, men say.''',
                                '''To express their love-sickness by their eyes and resort to begging bespeaks more than ordinary female excellence.''');
        k[1280] = Kural.factory(1281, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''உள்ளக் களித்தலும் காண மகிழ்தலும்
  கள்ளுக்கில் காமத்திற் குண்டு.''', '''Gladness at the thought, rejoicing at the sight,
Not palm-tree wine, but love, yields such delight.''',
                                '''To please by thought and cheer by sight is peculiar, not to liquor but lust.''');
        k[1281] = Kural.factory(1282, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''தினைத்துணையும் ஊடாமை வேண்டும் பனைத்துணையும்
  காமம் நிறைய வரின்.''', '''When as palmyra tall, fulness of perfect love we gain,
Distrust can find no place small as the millet grain.''',
                                '''If women have a lust that exceeds even the measure of the palmyra fruit, they will not desire (to feign) dislike even as much as the millet.''');
        k[1282] = Kural.factory(1283, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''பேணாது பெட்பவே செய்யினும் கொண்கனைக்
  காணா தமையல கண்.''', '''Although his will his only law, he lightly value me,
My heart knows no repose unless my lord I see.''',
                                '''Though my eyes disregard me and do what is pleasing to my husband, still will they not be satisfied unless they see him.''');
        k[1283] = Kural.factory(1284, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''ஊடற்கண் சென்றேன்மன் தோழி அதுமறந்து
  கூடற்கண் சென்றதுஎன் னெஞ்சு.''', '''My friend, I went prepared to show a cool disdain;
My heart, forgetting all, could not its love restrain.''',
                                '''O my friend! I was prepared to feign displeasure but my mind forgetting it was ready to embrace him.''');
        k[1284] = Kural.factory(1285, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''எழுதுங்கால் கோல்காணாக் கண்ணேபோல் கொண்கன்
  பழிகாணேன் கண்ட இடத்து.''', '''The eye sees not the rod that paints it; nor can I
See any fault, when I behold my husband nigh.''',
                                '''Like the eyes which see not the pencil that paints it, I cannot see my husband\'s fault (just) when I meet him.''');
        k[1285] = Kural.factory(1286, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''காணுங்கால் காணேன் தவறாய காணாக்கால்
  காணேன் தவறல் லவை.''', '''When him I see, to all his faults I \'m blind;
But when I see him not, nothing but faults I find.''',
                                '''When I see my husband, I do not see any faults; but when I do not see him, I do not see anything but faults.''');
        k[1286] = Kural.factory(1287, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''உய்த்தல் அறிந்து புனல்பாய் பவரேபோல்
  பொய்த்தல் அறிந்தென் புலந்து.''', '''As those of rescue sure, who plunge into the stream,
So did I anger feign, though it must falsehood seem?''',
                                '''Like those who leap into a stream which they know will carry them off, why should a wife feign dislike which she knows cannot hold out long?''');
        k[1287] = Kural.factory(1288, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''இளித்தக்க இன்னா செயினும் களித்தார்க்குக்
  கள்ளற்றே கள்வநின் மார்பு.''', '''Though shameful ill it works, dear is the palm-tree wine
To drunkards; traitor, so to me that breast of thine!''',
                                '''O you rogue! your breast is to me what liquor is to those who rejoice in it, though it only gives them an unpleasant disgrace.''');
        k[1288] = Kural.factory(1289, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''மலரினும் மெல்லிது காமம் சிலர்அதன்
  செவ்வி தலைப்படு வார்.''', '''Love is tender as an opening flower. In season due
To gain its perfect bliss is rapture known to few.''',
                                '''Sexual delight is more delicate than a flower, and few are those who understand its real nature.''');
        k[1289] = Kural.factory(1290, '''காமத்துப்பால்''', '''புணர்ச்சிவிதும்பல்''', '''கண்ணின் துனித்தே கலங்கினாள் புல்லுதல்
  என்னினும் தான்விதுப் புற்று.''', '''Her eye, as I drew nigh one day, with anger shone:
By love o\'erpowered, her tenderness surpassed my own.''',
                                '''She once feigned dislike in her eyes, but the warmth of her embrace exceeded my own.''');
        k[1290] = Kural.factory(1291, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''அவர்நெஞ்சு அவர்க்காதல் கண்டும் எவன்நெஞ்சே
  நீஎமக்கு ஆகா தது.''', '''You see his heart is his alone
O heart, why not be all my own?''',
                                '''O my soul! although you have seen how his soul stands by him, how is it you do not stand by me?''');
        k[1291] = Kural.factory(1292, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''உறாஅ தவர்க்கண்ட கண்ணும் அவரைச்
  செறாஅரெனச் சேறியென் நெஞ்சு.''', '''\'Tis plain, my heart, that he \'s estranged from thee;
Why go to him as though he were not enemy?''',
                                '''O my soul! although you have known him who does not love me, still do you go to him, saying "he will not be displeased."''');
        k[1292] = Kural.factory(1293, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''கெட்டார்க்கு நட்டார்இல் என்பதோ நெஞ்சேநீ
  பெட்டாங்கு அவர்பின் செலல்.''', '''\'The ruined have no friends, \'they say; and so, my heart,
To follow him, at thy desire, from me thou dost depart.''',
                                '''O my soul! do you follow him at pleasure under the belief that the ruined have no friends?''');
        k[1293] = Kural.factory(1294, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''இனிஅன்ன நின்னொடு சூழ்வார்யார் நெஞ்சே
  துனிசெய்து துவ்வாய்காண் மற்று.''', '''\'See, thou first show offended pride, and then submit,\' I bade;
Henceforth such council who will share with thee my heart?''',
                                '''O my soul! you would not first seem sulky and then enjoy (him); who then would in future consult you about such things?''');
        k[1294] = Kural.factory(1295, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''பெறாஅமை அஞ்சும் பெறின்பிரிவு அஞ்சும்
  அறாஅ இடும்பைத்தென் நெஞ்சு.''', '''I fear I shall not gain, I fear to lose him when I gain;
And thus my heart endures unceasing pain.''',
                                '''My soul fears when it is without him; it also fears when it is with him; it is subject to incessant sorrow.''');
        k[1295] = Kural.factory(1296, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''தனியே இருந்து நினைத்தக்கால் என்னைத்
  தினிய இருந்ததென் நெஞ்சு.''', '''My heart consumes me when I ponder lone,
And all my lover\'s cruelty bemoan.''',
                                '''My mind has been (here) in order to eat me up (as it were) whenever I think of him in my solitude.''');
        k[1296] = Kural.factory(1297, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''நாணும் மறந்தேன் அவர்மறக் கல்லாஎன்
  மாணா மடநெஞ்சிற் பட்டு.''', '''Fall\'n \'neath the sway of this ignoble foolish heart,
Which will not him forget, I have forgotten shame.''',
                                '''I have even forgotten my modesty, having been caught in my foolish mind which is not dignified enough to forget him.''');
        k[1297] = Kural.factory(1298, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''எள்ளின் இளிவாம்என்று எண்ணி அவர்திறம்
  உள்ளும் உயிர்க்காதல் நெஞ்சு.''', '''If I contemn him, then disgrace awaits me evermore;
My soul that seeks to live his virtues numbers o\'er.''',
                                '''My soul which clings to life thinks only of his (own) gain in the belief that it would be disgraceful for it to despise him.''');
        k[1298] = Kural.factory(1299, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''துன்பத்திற்கு யாரே துணையாவார் தாமுடைய
  நெஞ்சந் துணையல் வழி.''', '''And who will aid me in my hour of grief,
If my own heart comes not to my relief?''',
                                '''Who would help me out of one\'s distress, when one\'s own soul refuses help to one?''');
        k[1299] = Kural.factory(1300, '''காமத்துப்பால்''', '''நெஞ்சொடுபுலத்தல்''', '''தஞ்சம் தமரல்லர் ஏதிலார் தாமுடைய
  நெஞ்சம் தமரல் வழி.''', '''A trifle is unfriendliness by aliens shown,
When our own heart itself is not our own!''',
                                '''It is hardly possible for strangers to behave like relations, when one\'s own soul acts like a stranger.''');
        k[1300] = Kural.factory(1301, '''காமத்துப்பால்''', '''புலவி''', '''புல்லா திராஅப் புலத்தை அவர்உறும்
  அல்லல்நோய் காண்கம் சிறிது.''', '''Be still reserved, decline his profferred love;
A little while his sore distress we \'ll prove.''',
                                '''Let us witness awhile his keen suffering; just feign dislike and embrace him not.''');
        k[1301] = Kural.factory(1302, '''காமத்துப்பால்''', '''புலவி''', '''உப்பமைந் தற்றால் புலவி அதுசிறிது
  மிக்கற்றால் நீள விடல்.''', '''A cool reserve is like the salt that seasons well the mess,
Too long maintained, \'tis like the salt\'s excess.''',
                                '''A little dislike is like salt in proportion; to prolong it a little is like salt a little too much.''');
        k[1302] = Kural.factory(1303, '''காமத்துப்பால்''', '''புலவி''', '''அலந்தாரை அல்லல்நோய் செய்தற்றால் தம்மைப்
  புலந்தாரைப் புல்லா விடல்.''', '''\'Tis heaping griefs on those whose hearts are grieved;
To leave the grieving one without a fond embrace.''',
                                '''For men not to embrace those who have feigned dislike is like torturing those already in agony.''');
        k[1303] = Kural.factory(1304, '''காமத்துப்பால்''', '''புலவி''', '''ஊடி யவரை உணராமை வாடிய
  வள்ளி முதலரிந் தற்று.''', '''To use no kind conciliating art when lover grieves,
Is cutting out the root of tender winding plant that droops.''',
                                '''Not to reconcile those who have feigned dislike is like cutting a faded creeper at its root.''');
        k[1304] = Kural.factory(1305, '''காமத்துப்பால்''', '''புலவி''', '''நலத்தகை நல்லவர்க்கு ஏஎர் புலத்தகை
  பூஅன்ன கண்ணார் அகத்து.''', '''Even to men of good and worthy mind, the petulance
Of wives with flowery eyes lacks not a lovely grace.''',
                                '''An increased shyness in those whose eyes are like flowers is beautiful even to good and virtuous husbands.''');
        k[1305] = Kural.factory(1306, '''காமத்துப்பால்''', '''புலவி''', '''துனியும் புலவியும் இல்லாயின் காமம்
  கனியும் கருக்காயும் அற்று.''', '''Love without hatred is ripened fruit;
Without some lesser strife, fruit immature.''',
                                '''Sexual pleasure, without prolonged and short-lived dislike, is like too ripe, and unripe fruit.''');
        k[1306] = Kural.factory(1307, '''காமத்துப்பால்''', '''புலவி''', '''ஊடலின் உண்டாங்கோர் துன்பம் புணர்வது
  நீடுவ தன்றுகொல் என்று.''', '''A lovers\' quarrel brings its pain, when mind afraid
Asks doubtful, \'Will reunion sweet be long delayed?\'''',
                                '''The doubt as to whether intercourse would take place soon or not, creates a sorrow (even) in feigned dislike.''');
        k[1307] = Kural.factory(1308, '''காமத்துப்பால்''', '''புலவி''', '''நோதல் எவன்மற்று நொந்தாரென்று அஃதறியும்
  காதலர் இல்லா வழி.''', '''What good can grieving do, when none who love
Are there to know the grief thy soul endures?''',
                                '''What avails sorrow when I am without a wife who can understand the cause of my sorrow?''');
        k[1308] = Kural.factory(1309, '''காமத்துப்பால்''', '''புலவி''', '''நீரும் நிழலது இனிதே புலவியும்
  வீழுநர் கண்ணே இனிது.''', '''Water is pleasant in the cooling shade;
So coolness for a time with those we love.''',
                                '''Like water in the shade, dislike is delicious only in those who love.''');
        k[1309] = Kural.factory(1310, '''காமத்துப்பால்''', '''புலவி''', '''ஊடல் உணங்க விடுவாரோடு என்நெஞ்சம்
  கூடுவேம் என்பது அவா.''', '''Of her who leaves me thus in variance languishing,
To think within my heart with love is fond desire.''',
                                '''It is nothing but strong desire that makes her mind unite with me who can leave her to her own dislike.''');
        k[1310] = Kural.factory(1311, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''பெண்ணியலார் எல்லாரும் கண்ணின் பொதுஉண்பர்
  நண்ணேன் பரத்தநின் மார்பு.''', '''From thy regard all womankind Enjoys an equal grace;
O thou of wandering fickle mind, I shrink from thine embrace!''',
                                '''You are given to prostitution; all those who are born as womankind enjoy you with their eyes in an ordinary way. I will not embrace you.''');
        k[1311] = Kural.factory(1312, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''ஊடி இருந்தேமாத் தும்மினார் யாம்தம்மை
  நீடுவாழ் கென்பாக் கறிந்து.''', '''One day we silent sulked; he sneezed: The reason well I knew;
He thought that I, to speak well pleased, Would say, \'Long life to you!\'''',
                                '''When I continued to be sulky he sneezed and thought I would (then) wish him a long life.''');
        k[1312] = Kural.factory(1313, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''கோட்டுப்பூச் சூடினும் காயும் ஒருத்தியைக்
  காட்டிய சூடினீர் என்று.''', '''I wreathed with flowers one day my brow, The angry tempest lowers;
She cries, \'Pray, for what woman now Do you put on your flowers?\'''',
                                '''Even if I were adorned with a garland of branch-flowers, she would say I did so to show it to another woman.''');
        k[1313] = Kural.factory(1314, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''யாரினும் காதலம் என்றேனா ஊடினாள்
  யாரினும் யாரினும் என்று.''', '''\'I love you more than all beside,\' \'T was thus I gently spoke;
\'What all, what all?\' she instant cried; And all her anger woke.''',
                                '''When I said I loved her more than any other woman, she said "more than others, yes, more than others," and remained sulky.''');
        k[1314] = Kural.factory(1315, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''இம்மைப் பிறப்பில் பிரியலம் என்றேனாக்
  கண்நிறை நீர்கொண் டனள்.''', '''\'While here I live, I leave you not,\' I said to calm her fears.
She cried, \'There, then, I read your thought\'; And straight dissolved in tears.''',
                                '''When I said I would never part from her in this life her eyes were filled with tears.''');
        k[1315] = Kural.factory(1316, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''உள்ளினேன் என்றேன்மற் றென்மறந்தீர் என்றென்னைப்
  புல்லாள் புலத்தக் கனள்.''', '''\'Each day I called to mind your charms,\' \'O, then, you had forgot,\'
She cried, and then her opened arms, Forthwith embraced me not.''',
                                '''When I said I had remembered her, she said I had forgotten her and relaxing her embrace, began to feign dislike.''');
        k[1316] = Kural.factory(1317, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''வழுத்தினாள் தும்மினேன் ஆக அழித்தழுதாள்
  யாருள்ளித் தும்மினீர் என்று.''', '''She hailed me when I sneezed one day; But straight with anger seized,
She cried; \'Who was the woman, pray, Thinking of whom you sneezed?\'''',
                                '''When I sneezed she blessed me, but at once changed (her mind) and wept, asking, "At the thought of whom did you sneeze?"''');
        k[1317] = Kural.factory(1318, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''தும்முச் செறுப்ப அழுதாள் நுமர்உள்ளல்
  எம்மை மறைத்திரோ என்று.''', '''And so next time I checked my sneeze; She forthwith wept and cried,
(That woman difficult to please), \'Your thoughts from me you hide\'.''',
                                '''When I suppressed my sneezing, she wept saying, \'I suppose you (did so) to hide from me your own people\'s remembrance of you\'.''');
        k[1318] = Kural.factory(1319, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''தன்னை உணர்த்தினும் காயும் பிறர்க்கும்நீர்
  இந்நீரர் ஆகுதிர் என்று.''', '''I then began to soothe and coax, To calm her jealous mind;
\'I see\', quoth she, \'to other folks How you are wondrous kind\'''',
                                '''Even when I try to remove her dislike, she is displeased and says, "This is the way you behave towards (other women)."''');
        k[1319] = Kural.factory(1320, '''காமத்துப்பால்''', '''புலவி நுணுக்கம்''', '''நினைத்திருந்து நோக்கினும் காயும் அனைத்துநீர்
  யாருள்ளி நோக்கினீர் என்று.''', '''I silent sat, but thought the more, And gazed on her. Then she
Cried out, \'While thus you eye me o\'er, Tell me whose form you see\'.''',
                                '''Even when I look on her contemplating (her beauty), she is displeased and says, "With whose thought have you (thus) looked on my person?"''');
        k[1320] = Kural.factory(1321, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''இல்லை தவறவர்க்கு ஆயினும் ஊடுதல்
  வல்லது அவர்அள஧க்கு மாறு.''', '''Although there be no fault in him, the sweetness of his love
Hath power in me a fretful jealousy to move.''',
                                '''Although my husband is free from defects, the way in which he embraces me is such as to make me feign dislike.''');
        k[1321] = Kural.factory(1322, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''ஊடலின் தோன்றும் சிறுதுனி நல்லளி
  வாடினும் பாடு பெறும்.''', '''My \'anger feigned\' gives but a little pain;
And when affection droops, it makes it bloom again.''',
                                '''His love will increase though it may (at first seem to) fade through the short-lived distress caused by (my) dislike.''');
        k[1322] = Kural.factory(1323, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''புலத்தலின் புத்தேள்நாடு உண்டோ நிலத்தொடு
  நீரியைந் தன்னார் அகத்து.''', '''Is there a bliss in any world more utterly divine,
Than \'coyness\' gives, when hearts as earth and water join?''',
                                '''Is there a celestial land that can please like the feigned dislike of those whose union resembles that of earth and water?''');
        k[1323] = Kural.factory(1324, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''புல்லி விடாஅப் புலவியுள் தோன்றுமென்
  உள்ளம் உடைக்கும் படை.''', '''\'Within the anger feigned\' that close love\'s tie doth bind,
A weapon lurks, which quite breaks down my mind.''',
                                '''In prolonged dislike after an embrace there is a weapon that can break my heart.''');
        k[1324] = Kural.factory(1325, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''தவறிலர் ஆயினும் தாம்வீழ்வார் மென்றோள்
  அகறலின் ஆங்கொன் றுடைத்து.''', '''Though free from fault, from loved one\'s tender arms
To be estranged a while hath its own special charms.''',
                                '''Though free from defects, men feel pleased when they cannot embrace the delicate shoulders of those whom they love.''');
        k[1325] = Kural.factory(1326, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''உணலினும் உண்டது அறல்இனிது காமம்
  புணர்தலின் ஊடல் இனிது.''', '''\'Tis sweeter to digest your food than \'tis to eat;
In love, than union\'s self is anger feigned more sweet.''',
                                '''To digest what has been eaten is more delightful than to eat more; likewise love is more delightful in dislike than intercourse.''');
        k[1326] = Kural.factory(1327, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''ஊடலில் தோற்றவர் வென்றார் அதுமன்னும்
  கூடலிற் காணப் படும்.''', '''In lovers\' quarrels, \'tis the one that first gives way,
That in re-union\'s joy is seen to win the day.''',
                                '''Those are conquerors whose dislike has been defeated and that is proved by the love (which follows).''');
        k[1327] = Kural.factory(1328, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''ஊடிப் பெறுகுவம் கொல்லோ நுதல்வெயர்ப்பக்
  கூடலில் தோன்றிய உப்பு.''', '''And shall we ever more the sweetness know of that embrace
With dewy brow; to which \'feigned anger\' lent its piquant grace.''',
                                '''Will I enjoy once more through her dislike, the pleasure of that love that makes her forehead perspire?''');
        k[1328] = Kural.factory(1329, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''ஊடுக மன்னோ ஒளியிழை யாமிரப்ப
  நீடுக மன்னோ இரா.''', '''Let her, whose jewels brightly shine, aversion feign!
That I may still plead on, O night, prolong thy reign!''',
                                '''May the bright-jewelled one feign dislike, and may the night be prolonged for me to implore her!''');
        k[1329] = Kural.factory(1330, '''காமத்துப்பால்''', '''ஊடலுவகை''', '''ஊடுதல் காமத்திற்கு இன்பம் அதற்கின்பம்
  கூடி முயங்கப் பெறின்.''', '''A \'feigned aversion\' coy to pleasure gives a zest;
The pleasure\'s crowned when breast is clasped to breast.''',
                                '''Dislike adds delight to love; and a hearty embrace (thereafter) will add delight to dislike.''');
        return k


class Thirukkural:
    db = None  # container of Kurals

    def __init__(self):
        if (not Thirukkural.db):
            Thirukkural.db = Kural.load_data_base();

    def get_kural_no(self, no):
        assert (no >= 1 and no <= 1330)
        return Thirukkural.db[no - 1];

    def get_kurals_from_adhikaram(self, name):
        return [k for k in Thirukkural.db if k.adhikaram.find(name) >= 0];

    def get_kurals_from_pal(self, name):
        return [k for k in Thirukkural.db if k.pal.find(name) >= 0];

    @staticmethod
    def iterator():
        """குறட்பாக்களை ஒவ்வொன்றாக குறள் எண் மற்றும் குறட்பாவையும் மாறாபட்டியல் (tuple)
        ஆக விவரிக்கும்"""
        for k in Thirukkural.db:
            yield (k.no, k.ta)

    @staticmethod
    def occurrence(சொல்):
        கண்ட_இடம் = []
        for கு_எண், குறள் in Thirukkural.iterator():
            if (குறள்.find(சொல்) >= 0):
                கண்ட_இடம்.append(கு_எண்)
        return கண்ட_இடம்


Thirukkural.db = None;
