all:
	javac -d `pwd`/bin/  -sourcepath `pwd`/src/com/tamil/ -encoding utf8  `pwd`/src/com/tamil/*.java
	cd bin && jar cvf tamil.jar com/ && cd ..
	mv ./bin/tamil.jar ../
	make test

test: tamil.jar
	