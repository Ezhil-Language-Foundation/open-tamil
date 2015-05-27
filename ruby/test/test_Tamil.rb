# encoding: utf-8
# (C) 2015 Muthiah Annamalai
require 'minitest/autorun'
require 'tamil'

class TamilTest < Minitest::Unit::TestCase
  def test_total_letters
    assert_equal Tamil::TA_UYIR_LEN,12
    assert_equal Tamil::TA_ACCENT_LEN, 13 #12 + 1
    assert_equal Tamil::TA_AYUDHA_LEN, 1
    assert_equal Tamil::TA_UYIR_LEN, 12
    assert_equal Tamil::TA_MEI_LEN, 18
    assert_equal Tamil::TA_AGARAM_LEN, 18
    assert_equal Tamil::TA_SANSKRIT_LEN, 6
    assert_equal Tamil::TA_UYIRMEI_LEN, 216
    assert_equal Tamil::TA_GRANTHA_UYIRMEI_LEN, 24*12
    assert_equal Tamil::TA_LETTERS_LEN, 323
  end
  
  def test_accent
    assert_equal Tamil.accent_len(),13
  end

  def test_agaram
        assert_equal Tamil.agaram_len(), Tamil::TA_AGARAM_LEN
        assert_equal Tamil::AGARAM_LETTERS.length,18
  end
     
  def test_uyir
    obj = Tamil
    (0..obj.agaram_len()-1).each do |idx|
        assert_equal idx >= 0, true
        assert_includes  obj::AGARAM_LETTERS,obj.agaram(idx)
    end
  end
  
  def test_get_letters
    obj = Tamil
    assert_equal ['b','l','a','a'], obj.get_letters('blaa')
    assert_equal ['க','லி','யா','ண','மா','லை'],obj.get_letters('கலியாணமாலை')
  end
end
