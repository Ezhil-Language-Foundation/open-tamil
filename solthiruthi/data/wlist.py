# (C) 2017 Muthu Annamalai
# Build bi-gram and unigram models of a given text corpus
# into a model.
from ngram import LetterModels

f = 'tamilvu_dictionary_words.txt'
ug = LetterModels.Unigram(f)
ug.frequency_model()
ug.save('tvu_unigram.txt')

bg = LetterModels.Bigram(f)
bg.language_model(verbose=False)
bg.save('tvu_bigram.txt')

