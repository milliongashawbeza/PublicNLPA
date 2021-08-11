from amharic_bigram_generator import *
from amharic_tokenizer import *
print(bigramm("ዛሬ ፍርድ ቤት እና ትምህርት ቤት ነበርኩ"))
v = bigramm("ዛሬ ፍርድ ቤት እና ትምህርት ቤት ነበርኩ ።")
print(word_tokenize(v))