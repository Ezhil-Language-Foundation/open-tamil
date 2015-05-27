# encoding: utf-8
class Foo
    @@agaram_letters = ["க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள"]
    def do_agaram()
        puts @@agaram_letters.length
    end
end

Foo.new.do_agaram

module Bar
    @@agaram_letters = ["க","ச","ட","த","ப","ற","ஞ","ங","ண","ந","ம","ன","ய","ர","ல","வ","ழ","ள"]
    def Bar.do_agaram()
        puts -5+@@agaram_letters.length
    end
end

# Bar.do_agaram
# 
# ['க','லி','யா','ண','மா','லை']

require 'tamil' 
puts Tamil.get_letters('கலியாணமாலை')
# 
puts 'experimental'
'கலியாணமாலை'.split('').each do |x|
  puts x
end
