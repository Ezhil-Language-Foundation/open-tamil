txt2unicode
===========
Tamil Text font-based Encode to Unicode Converter and vice versa.

If you dont know what is your text encoding, don't worry; the module  **'txt2unicode'** will find it by best guess and convert to unicode for you, automatically!

Available Tamil Encoding Converters
===================================


| S.No  | எழுத்துரு | Encoding Name | To Unicode Converter | To Encode Convereter |
| ---- | :---------: | :---------: | :---------: | :---------: |
| 1 | அஞ்சல் | Anjal | anjal2unicode | unicode2anjal|
| 2 |  பாமினி | Bamini|  bamini2unicode| unicode2bamini|
| 3 | பூமி  | Boomi  |  boomi2unicode| unicode2boomi| 
| 4 | டியாச்ரிடிக்|       Diacritic|  diacritic2unicode | unicode2diacritic|
| 5 | தினகரன் | Dinakaran |  dinakaran2unicode | unicode2dinakaran|
| 6 | தினமணி  | Dinamani  | dinamani2unicode  | unicode2dinamani ||
| 7 | தினத்தந்தி |Dinathanthy |  dinathanthy2unicode|unicode2dinathanthy|            
| 8 | இன்டோவெப்   | Indoweb    | indoweb2unicode   | unicode2indoweb  |
| 9 |  கவிபிரியா |  Kavipriya  | kavipriya2unicode| unicode2kavipriya|     
| 10 | கோயல்என்   |  Koeln      | koeln2unicode    |  unicode2koeln  |
| 11| லிபி     |  Libi       |  libi2unicode    | unicode2libi   |
| 12| முரசொலி | Murasoli |  murasoli2unicode | unicode2murasoli |
| 13| மலை  |  Mylai    |mylai2unicode      | unicode2mylai|
| 14| நக்கீரன்  |Nakkeeran|     nakkeeran2unicode| unicode2nakkeeran|
| 15| பழைய விகடன்  | Old Vikatan  | oldvikatan2unicode | unicode2oldvikatan |
| 16| பல்லவர்  | Pallavar      | pallavar2unicode  | unicode2pallavar | 
| 17| ரோமன்   | Roman   | roman2unicode  | unicode2roman |
| 18| ஸ்ரீலிபி|Shreelipi|shreelipi2unicode| unicode2shreelipi|
| 19|  சாஃப்ட் வியூ |Softview|softview2unicode | unicode2softview|
| 20| டேப்    | Tab  | tab2unicode  | unicode2tab|
| 21| டேஸ்   | Tace  | tace2unicode | unicode2tace |
| 22| டாம்   |  Tam  |tam2unicode | unicode2tam|
| 23| டிஸ்கி |Tscii  |    tscii2unicode|   unicode2tscii|   
| 24| வானவில் |  Vanavil  | vanavil2unicode  |  unicode2vanavil |
| 25| வெப்உலகம்   | Webulagam | webulagam2unicode |  unicode2webulagam |
| 26| அனு   | Indica | indica2unicode |  unicode2indica |
| 27| அனு   | Anu | anu2unicode |  unicode2anu |
| 28| ஸ்ரீலிபி|Shreelipi (AVID)|shreelipiavid2unicode| unicode2shreelipiavid|
| 29| **கண்டுபுடி**| **AutoFind**    | **auto2unicode**|       **unicode2auto**           |

Automatic Input Encoding & Conversion to Unicode
================================================

The 'auto2unicode' function will try to find encode of input text. If it is found, then it will convert input text to unicode using appropriate encode converters among available encode converters.
  
  **Out of 25 encodes, 20 encodes can be found by this 'auto2unicode'.** 
  
  Except 'dinamani', 'nakkeeran' , 'murasoli' , 'tam' & 'webulagam' encodes, 'auto2unicode' function can find input text's encode and will convert it into unicode. [Why?](../../examples/txt2unicode/encodes_chars/README.md)
  
  Look at demo of [tscii2unicode](../../examples/txt2unicode/demo_tscii2utf8.py) converter

  Look at demo of [auto2unicode](../../examples/txt2unicode/demo_auto2utf8.py) converter
  
  Look at **limitation of 'auto2unicode'** [here](../../examples/txt2unicode/encodes_chars/README.md)
  
  

  
Convert From Unicode to Encode
==============================
  Here reverse engine of 'encode2unicode' used to convert back to encode from unicode.
  
  Look at above table for available 'unicode2encode' functions.
  
  Look at demo of [unicode2tscii](../../examples/txt2unicode/demo_utf8_2_tscii.py) converter
  
  Look at demo of [unicode2auto](../../examples/txt2unicode/demo_utf8_2_auto.py) converter
  

Test Status:
===========
  1. auto2unicode works
  2. tscii2unicode works
  3. unicode2tscii works
   


Todo:
====
  * Need to test all the above encodes
  * Need to add fonts2unicode converter for the above encodings
  

RoadMap:
=======
  * Look roadmap of txt2unicode [here](https://github.com/arulalant/txt2unicode/wiki/RoadMap)
  

Credits:
=======
  Thanks to following online & offline tools.
  1. http://kandupidi.com/converter/,
  2. http://www.suratha.com/reader.htm  and 
  3. http://nhm-converter.software.informer.com/1.0/ 
  
Regards,

Arulalan.T
