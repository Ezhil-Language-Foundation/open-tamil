# -*- coding: utf8 -*-
# This file is distributed under MIT License
# 2015 Muthiah Annamalai <ezhillang@gmail.com>
#
units = (u'பூஜ்ஜியம்', u'ஒன்று', u'இரண்டு', u'மூன்று', u'நான்கு', u'ஐந்து', u'ஆறு', u'ஏழு', u'எட்டு', u'ஒன்பது', u'பத்து') # 0-10
teens = (u'பதினொன்று', u' பனிரண்டு', u'பதிமூன்று', u'பதினான்கு', u'பதினைந்து',u'பதினாறு', u'பதினேழு', u'பதினெட்டு', u'பத்தொன்பது') # 11-19
tens = (u'பத்து', u'இருபது', u'முப்பது', u'நாற்பது', u'ஐம்பது',u'அறுபது', u'எழுபது', u'எண்பது', u'தொன்னூறு') # 10-90
tens_suffix = (u'இருபத்தி', u'முப்பத்தி', u'நாற்பத்தி', u'ஐம்பத்தி', u'அறுபத்தி', u'எழுபத்தி', u'எண்பத்தி', u'தொன்னூற்றி') # 10+-90+
hundreds = ( u'நூறு', u'இருநூறு', u'முன்னூறு', u'நாநூறு',u'ஐநூறு', u'அறுநூறு', u'எழுநூறு', u'எண்ணூறு', u'தொள்ளாயிரம்') #100 – 900
hundreds_suffix = (u'நூற்றி', u'இருநூற்றி', u'முன்னூற்று', u'நாநூற்று', u'ஐநூற்று', u'அறுநூற்று', u'எழுநூற்று', u'எண்ணூற்று',u'தொள்ளாயிரத்து') #100+ – 900+
one_thousand_prefix = (u'ஓர்',None)
thousands = (u'ஆயிரம்',u'ஆயிரத்தி')
one_prefix = (u'ஒரு',None)
lakh = (u'இலட்சம்',u'இலட்சத்தி')
crore = (u'கோடி',u'கோடியே')

print sum(map(len,[units,teens,tens,tens_suffix,hundreds,hundreds_suffix,one_thousand_prefix,thousands,one_prefix,lakh,crore]))

count = 0
for word_list in [units, teens,tens,tens_suffix,hundreds,hundreds_suffix,one_thousand_prefix,thousands,one_prefix,lakh,crore]:
    for word in word_list:
        if not word:
            break
        print(u"%02d) %s"%(count,word))
        count += 1

# 'C:\\Users\\muthu\\devel\\open-tamil\\examples\\pesum_kediyaram'
# import os; os.chdir('C:\\Users\\muthu\\devel\\open-tamil\\examples\\pesum_kediyaram')