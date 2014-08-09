
Look at all available files of `encodes_chars` directory [here]() 

[all.encodes.common.chars.txt](all.encodes.common.chars.txt) file contains **commonly available 916 compound characters among all encodings**.

So if your input text fully falls only under the compund characters of `all.encodes.common.chars.txt`, then `auto2unicode` will fails. :-(


Look at the files [dinamani2utf8.unique.chars.txt](dinamani2utf8.unique.chars.txt),  [nakkeeran2utf8.unique.chars.txt](nakkeeran2utf8.unique.chars.txt) and [murasoli2utf8.unique.chars.txt](murasoli2utf8.unique.chars.txt). There are fully empty!

It seems these two encodes characters are fully falls under commonly available
916 compound characters [all.encodes.common.chars.txt](all.encodes.common.chars.txt).

So there is **zero %** chance to identify `dinamani`, `nakkeeran` and `murasoli` encodes by using `auto2unicode` function.

Look at the files [tam2utf8.unique.chars.txt](tam2utf8.unique.chars.txt) and [webulagam2utf8.unique.chars.txt](webulagam2utf8.unique.chars.txt), it has only one unique compound characters.

So there is (1/916)x100 = **0.10917030567685589 %** chances to identify `tam` and `webulagam` encode by using `auto2unicode` function.


**Tip** : If you need to find auto encode of your input text, then make sure that
atleast one compund characters from encode_name.unique.chars.txt file available in your 
input text. Find your encode unique compound characters [here]() 


| S.No  | Enocdes | Unique Chars|
| ---- | :--------- | :---------: |
| 1  |  [Anjal](anjal2utf8.unique.chars.txt) | 190 |
| 2  | [Bamini](bamini2utf8.unique.chars.txt)  | 118 |
| 3  | [Boomi](boomi2utf8.unique.chars.txt)  | 99 |
| 4  | [Dinakaran](dinakaran2utf8.unique.chars.txt) | 87 |
| 5  | [Dinamani](dinamani2utf8.unique.chars.txt)  | **0** |
| 6  | [Dinathanthy](dinathanthy2utf8.unique.chars.txt)  | 172  |
| 7  | [Indoweb](indoweb2utf8.unique.chars.txt)     | 230   |  
| 8  | [Kavipriya](kavipriya2utf8.unique.chars.txt)  | 39 |
| 9  | [Koeln](koeln2utf8.unique.chars.txt)     | 109  |
| 10 | [Libi](libi2utf8.unique.chars.txt)       | 155  |
| 11  | [Murasoli](murasoli2utf8.unique.chars.txt)  | **0** |
| 12 | [Mylai](mylai2utf8.unique.chars.txt)  | 189 |
| 13  | [Nakkeeran](nakkeeran2utf8.unique.chars.txt)   | **0** |
| 14  | [OldVikatan](oldvikatan2utf8.unique.chars.txt)   |   92  |
| 15  | [Pallavar](pallavar2utf8.unique.chars.txt)       |  163   |
| 16 | [Roman](roman2utf8.unique.chars.txt)  | 342 |
| 17  | [Tab](tab2utf8.unique.chars.txt)  | 62 |
| 18 | [Tam](tam2utf8.unique.chars.txt)  | **1** |
| 19 | [Tscii](tscii2utf8.unique.chars.txt)   | 213 |   
| 20   | [Webulagam](webulagam2utf8.unique.chars.txt)       |  **1**  |


| S.No| Common Compound Characters                 | Count |
| ---| -------------------------------------------------------|:-----:|
| 1 | [common characters in all encodes](all.encodes.common.chars.txt) | 916 |




#[eg 1](demo_tscii2utf8.py):#


```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = tscii2unicode(text)
>>> print uni
```
திருவள்ளுவர் அருளிய திருக்குறள்  

*unicode for above tscii characters are as shown above*


#[eg 2](../demo_auto2utf8.py):#

```python
>>> text = """¾¢ÕÅûÙÅ÷ 
«ÕÇ¢Â ¾¢ÕìÌÈû  """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Whola! found encode :  tscii2utf8"**

*It print above msg and return converted unicode characters.*

திருவள்ளுவர் அருளிய திருக்குறள்  

*unicode for above tscii characters are as shown above*


#eg 3:#

```python
>>> text = """ù£tPùP\[tI
è£n\[nwh ùSô ªþ£ ùaô """

>>> uni = auto2unicode(text)
>>> print uni
```

**"Sorry, couldn't find encode :-(**

**Need more words to find unique encode out side of 916 common compound characters"**

*It print above msg and return None.*


Look closely at characters of input & output of `eg 2` & `eg 3` 

In `eg 2` input text has atleast one / more compound characters from [tscii2utf8.unique.chars.txt](tscii2utf8.unique.chars.txt).

But in `eg 3` input fully falls only under the compund characters of 
[all.encodes.common.chars.txt](all.encodes.common.chars.txt). So it couldn't find correct encodes of input text ! 

For other encodes user need to look at this `encodes_chars` [directory files]() &
identify atleast one unique char, incert in input text. so that `auto2unicode` function
can identiy encode for you ! 


#[eg 4](../demo_utf8_2_tscii.py):#

*The below code shows example for reverse engine, i.e. `unicode2encode`*

```python
>>> tscii = """¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  """
>>> uni_1 = tscii2unicode(tscii)
>>> tscii_from_uni = unicode2tscii(uni_1)
>>> uni_2 = tscii2unicode(tscii_from_uni)

>>> print "Tscii original input", tscii
>>> print "From tscii to unicode :", uni_1 
>>> print "From unicode to tscii :", tscii_from_uni
>>> print "Again back to unicode from above tscii :", uni_2
```

  *Outputs of the above snippet which convert in bothways* 

Tscii original input : ¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû 

From tscii to unicode : திருவள்ளுவர் அருளிய திருக்குறள்  

From unicode to tscii : ¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû  

Again back to unicode from above tscii : திருவள்ளுவர் அருளிய திருக்குறள்  


#[eg 5](demo_utf8_2_auto.py):#
*The below code shows example for auto reverse engine, i.e. `unicode2auto`*

```python
>>> uni_1 = """திருவள்ளுவர் அருளிய திருக்குறள்    """
>>> tscii = unicode2tscii(uni_1)
>>> tscii_sample = tscii.split(' ')[0]
>>> tscii_from_auto = unicode2auto(uni_1, tscii_sample)
>>> uni_2 = auto2unicode(tscii_from_auto)

>>> print "Unicode original input :", uni_1
>>> print "From unicode to tscii :", tscii  
>>> print "From unicode to tscii :", tscii_from_auto
>>> print "From unicode to tscii by auto function :", uni_2
```
 
 *Outputs of the above snippet which convert in bothways by auto functions*

Whola! found encode :  tscii2utf8

Whola! found encode :  tscii2utf8

Unicode original input : திருவள்ளுவர் அருளிய திருக்குறள்    

From unicode to tscii : ¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû    

From unicode to tscii by auto function : ¾¢ÕÅûÙÅ÷ «ÕÇ¢Â ¾¢ÕìÌÈû    

Again back to unicode from above tscii by auto function: திருவள்ளுவர் அருளிய திருக்குறள்  


------------------------------------------------------------------------------------------------------------

Regards,

Arulalan.T 

Date : 09.08.2014
