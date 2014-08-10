txt2unicode
===========
Tamil Text Encode to Unicode Converter and vice versa.

Don't you know what is your text encode ? Don't worry. This `txt2unicode` will find it & convert to unicode for you :-)


Available Tamil Encode Converters
=================================

| S.No  | எழுத்துரு | Encode Name | To Unicode Converter | To Encode Convereter |
| ---- | :---------: | :---------: | :---------: | :---------: |
| 1 | அஞ்சல் | Anjal | anjal2unicode | unicode2anjal|
| 2 |  பாமினி | Bamini|  bamini2unicode| unicode2bamini|
| 3 | பூமி  | Boomi  |  boomi2unicode| unicode2boomi| 
| 4 | தினகரன் | Dinakaran |  dinakaran2unicode | unicode2dinakaran|
| 5 | தினமணி  | Dinamani  | dinamani2unicode  | unicode2dinamani ||
| 6 | தினத்தந்தி |Dinathanthy |  dinathanthy2unicode|unicode2dinathanthy|
| 7 | இன்டோவெப்   | Indoweb    | indoweb2unicode   | unicode2indoweb  |
| 8 |  கவிபிரியா |  Kavipriya  | kavipriya2unicode| unicode2kavipriya|     
| 9 | கோயல்என்   |  Koeln      | koeln2unicode    |  unicode2koeln  |
| 10| லிபி     |  Libi       |  libi2unicode    | unicode2libi   |
| 11| முரசொலி | Murasoli |  murasoli2unicode | unicode2murasoli |
| 12| மலை  |  Mylai    |mylai2unicode      | unicode2mylai|
| 13| நக்கீரன்  |Nakkeeran|     nakkeeran2unicode| unicode2nakkeeran|
| 14| பழைய விகடன்  | Old Vikatan  | oldvikatan2unicode | unicode2oldvikatan |
| 15| பல்லவர்  | Pallavar      | pallavar2unicode  | unicode2pallavar | 
| 16| ரோமன்   | Roman   | roman2unicode  | unicode2roman |
| 17| டேப்    | Tab  | tab2unicode  | unicode2tab|
| 18| டாம்   |  Tam  |tam2unicode | unicode2tam|
| 19| டிஸ்கி |Tscii  |    tscii2unicode|   unicode2tscii|       
| 20| வெப்உலகம்   | Webulagam | webulagam2unicode |  unicode2webulagam |
| 21| **கண்டுபுடி**| **AutoFind**    | **auto2unicode**|       **unicode2auto**           |




Auto Find Input Encode & Convert to Unicode
===========================================

  `auto2unicode` function will try to find encode of input text. If it is found, then it will convert input text to unicode using appropriate encode converters among available encode converters.
  
  **Out of 20 encodes, 15 encodes can be found by this `auto2unicode`.** 
  
  Except `dinamani`, `nakkeeran` , `murasoli` , `tam` & `webulagam` encodes, `auto2unicode` function can find input text's encode and will convert it into unicode. [Why?](../../examples/txt2unicode/encodes_chars/README.md)
  
  Look at demo of [tscii2unicode](../../examples/txt2unicode/demo_tscii2utf8.py) converter

  Look at demo of [auto2unicode](../../examples/txt2unicode/demo_auto2utf8.py) converter
  
  Look at **limitation of `auto2unicode`** [here](../../examples/txt2unicode/encodes_chars/README.md)
  
  

  
Convert From Unicode to Encode
==============================
  Here reverse engine of `encode2unicode` used to convert back to encode from unicode.
  
  Look at above table for available `unicode2encode` functions.
  
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
  Thanks to http://kandupidi.com/converter/ and http://www.suratha.com/reader.htm online tools.
  
Regards,

Arulalan.T
  
