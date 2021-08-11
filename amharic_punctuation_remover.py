from amharic_stop_words import *
import numpy as np


def clear_amharic_sentence(words):
    new_text = ""
    data=""
    for word in words:
        if stop_word_check(word):
            new_text = new_text + " " + word
    if(len(new_text)<1):
        new_text=words
    symbols = "!\"#$%&()*+-./,:;<=>?@[\]^`{|}~፣።\n"
    for i in symbols:
     new_text = np.char.replace(new_text,i,'')

    return str(new_text)


