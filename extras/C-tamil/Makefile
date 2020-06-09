all: tamil-letters.c
	gcc tamil-letters.c -D BUILD_TAMIL_LETTERS=1 -Wall -o tamil-letters
clean:
	rm tamil-letters *~

test: all
	./tamil-letters
