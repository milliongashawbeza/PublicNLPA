import nltk
from nltk import CFG
from amharic_bigram_generator import *
from amharic_tokenizer import *
#grammer = nltk.data.load('/home/milli/PycharmProjects/AmharicLP/amharic_dataset.cfg','cfg')
grammer1 = CFG.fromstring("""
#
S -> NP VP 
VP -> NP ADV_V
V_X -> VPP|VM|VF|VU

PP -> P NP 

V -> "saw" | "ate" | "walked" | "አየ" | "ሰማ" | "ሮ" 

#NP -> Det N | Det N PP |N_X| ADJ N|ADJ NPF|ADJ N_X |N_X N_X|P_A_N P_A_N
NP -> P_A_N P_A_N P_A_N | N_X P_N|P_A_N P_A_N| P_A_N

#Prepostion Adjective Noun
P_A_N -> P ADJ N_X | A N_X | P_N
#Prepostion and Noun 
P_N -> P N_X | N_X

#adverb verb
ADV_V -> ADV V_X|V_X|ADV ADV V_X

#Noun X , NOUNS of all forms 
N_X -> NPF|NPM|NPP|N_Place|N_Country|N_Hotel|N_Mountain|N_P_P
NPF -> "ሰላማዊት" | "ትግስት" | "ማህሌት" 
NPM -> "ሰለሞን" | "ዘውዱ" | "አለየ" 
N_P_P -> "እኔ"|"እሱ"|"እሱዋ"|"እነሱ"|"እኛ"|"እነርሱ"
N_Place -> "ባህር_ዳር"|"ባሕር_ዳር"|"ሃዋሳ"|"ሻሸመኔ"|"ድሬ_ደዋ"|"አዲሥ_አበባ"|"ጅማ"|"አዲስ_አበባ"
N_Country ->"ጀርመን"|"ኮሎምብያ"|"ቻይና"|"አሜሪካ"|"ደቡብ_ኮሪያ"|"ኢትዮጵያ"
N_Hotel ->"አዝዋ_ሆቴል"|"ዩኒሰን_ሆቴል"
N_Mountain ->"ራስ_ዳሽን"|"ሰሜን_ተራሮች"

VPP -> "ተናደድኩ"|"ተደሰትኩ"|"ተናደድሁ"|"ሳቅኩ"|"ሳቅሁ"|"እየሁ"|"ሮጥኩ"|"ሮጥሁ"
VM -> "ተናደደ"|"ተደሰተ"|"ሳቀ"|"ገባ"|"መጣ"|"ሄደ"
VF -> "ተናደደች"|"ተደሰተች"|"ሳቀች"|"አየች"|"ገባች"|"ሄደች" 
VU -> "ተናደዱ"|"ተደሰቱ"|"ሳቁ"|"ገቡ"

#VPPP -> "ተናድድጄ"|"ተደስቼ"|"ስቄ"|"አይቼ"|"ሩጬ"
VMP -> "ተናዶ"|"ተደስቶ"|"ስቆ"|"አይቶ"|"ገብቶ"
VFP -> "ተናዳ"|"ተደስታ"|"ስቃ"|"ገብታ"
VUF -> "ተናደው"|"ተደስተው"|"ስቀው"|"ገብተው" 

ADV -> "ክፉኛ"|"በፍጥነት"|"በዝግታ"|"በርጋታ"|"ባስታውሎት"|"ትላንት"|"ዛሬ"|"በጥዋት"|"ጥዋት"
ADJ ->"አዲስ"|"አሮጌ"|"መጀመሪያ"|"መጨረሻ"|"ረጅም"|"አጭር"|"ጥቁር"|"ነጭ"|"ከታላቁ"
Det -> "a" | "an" | "the" | "my" | "የ" | "ከ" 
N -> "man" | "dog" | "cat" | "telescope" | "park" | "ሰው" | "ውሻ" | "ድመት" | "ቴሌስኮፕ" | "ፓርክ" |"ትምህርት_ቤት"|"ፍርድ_ቤት"
P -> "እና"|"በላይ"|"በታች"|"በኃላ"|"ፊት_ለፊት"|"ከኃላ"|"ከርቀት"|" በቅርብ"|"ውስጥ"|" በውስጥ"|"ውጭ"|"ብቻውን"|"ስለ"|"በመሀል"|"ነገር_ግን"|"ለ"|"ከ"|"ወደ"

""")
parser = nltk.ChartParser(grammer1)
sent = "ሰላማዊት ጀርመን እና ቻይና በኃላ አሮጌ አሜሪካ ባስታውሎት ሄደች"
sent3 = "ዘውዱ ከ አዲስ አበባ ወደ ባህር ዳር ዛሬ ጥዋት ሄደ"
sent2 = "ዘውዱ ውሻ ትምህርት ቤት ውስጥ ባስታውሎት አየ"
big = bigramm(sent3)
x = big.split()
#s2 = bigramm(sent2)
tokenized_word=word_tokenize(big)
tokenized_word2=word_tokenize(big)
print(tokenized_word)

#sent = "በለጠ saw Bob in ".split()
rd_parser = nltk.RecursiveDescentParser(grammer1)
for tree in rd_parser.parse(tokenized_word):
    print(tree)