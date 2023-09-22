from wordle import Wordle
import spacy
import enchant
import re
d = enchant.Dict("en_US")

nlp = spacy.load("en_core_web_sm")
spacy_words = set(nlp.vocab.strings)

def words_f(spacy_words):
    c_words = []
    for w in spacy_words:
        if d.check(w) and  re.match("[a-z]", w.lower()) and "-" not in w and len(w) >2: 
            c_words.append(w.lower())
        else: 
            continue
    return c_words


if __name__ == "__main__": 
    nlp = spacy.load("en_core_web_sm")
    spacy_words = set(nlp.vocab.strings)
    w = Wordle(words_f(spacy_words), 0)
    #w = Wordle(words_f(spacy_words), 0, True)
    w.play()
