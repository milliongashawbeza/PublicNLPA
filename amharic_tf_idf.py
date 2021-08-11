import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# this is a very toy example, do not try this at home unless you want to understand the usage differences
docs1 = ["the house had a tiny little mouse",
        "the cat saw the mouse",
        "the mouse ran away from the house",
        "the cat finally ate the mouse",
        "the end of the mouse story"
        ]
docs2 = ["የኢትዮጵያ ቤት ኪንግ ፕሪሚዬር ሊግ አሸናፊው ፋሲል ከነማ ትናንት በአዲስ አበባ ሸራተን አዲስ ሆቴል የገቢ ማሰባሰቢያ ቴሌቶን ማዘጋጀቱ ይታወሳል",
         "በገቢ ማሰባሰቢያ ዝግጅቱ ከፍተኛ የመንግሥት የሥራ ኃላፊዎችን ጨምሮ የተለያዩ የኅብረተሰብ ክፍሎች ተሳትፈዋል፡፡  ስለ ተደረገው የገቢ ማሰባሰቢያ ቴሌቶን መግለጫ የሰጡት የክለቡ ፕሬዚዳንትና የጎንደር ከተማ ከንቲባ አቶ ሞላ መልካሙ ቴሌቶኑ ኢትዮጵያዊነት አምሮና ደምቆ የታየበትና የስፖርት ዓላማን ያሳካ ነበር ብለዋል",
         "በቴሌቶኑ አሁንም በስልክና በተለያዩ አማራጮች ቃል የሚገቡ እንዳሉ ሆኖ ከ170 ሚሊዮን ብር በላይ መሰብሰቡም ተገልጿል"
         "ቀዳማዊት እመቤት ዝናሽ ታያቸው በሁሉም ክልሎች የክለቡ አምባሳደሮች መሰየማቸው ፋሲል ከነማ የኢትዮጵያ ክለብ መሆኑን የሚገልጽ ነው ብለዋል። በቴሌቶኑ ከሁሉም የኢትዮጵያ ክፍሎች ድጋፎች መደረጋቸው ሌላኛው ፍሲል የኢትዮጵያ ክለብ መሆኑን የሚያሳይ እንደሆነ ተናግረዋል። በድጋፉ ለተሳተፉ ሁሉም አካላት ምስጋናም አቅርበዋል",
         "በቀጣይ ክለቡ የያዛቸውን ትላልቅ ፕሮጀክቶች ከግብ ለማድረስና ክለቡ በአፍሪካ መድረክ ረዥም ርቀት እንዲጓዝ አሁንም የሁሉም ድጋፍ ያስፈልጋል ተብሏል።",
         "የክለቡ ሥራ አስኪያጅ አቶ አቢዮት ብርሃኑ ክለቡ በቀጣይ ከመንግሥት በጀት ተላቆ የራሱ ቋሚ ሀብት እንዲኖረው ሥራዎች በእቅድ እየተሠሩ ስለመሆናቸው ተናግረዋል",
         "ከቴሌቶኑ የሚገኘው ገቢ ለደሞዝና ለእለታዊ ወጭዎች ሳይሆን አካዳሚ መገንባት ጨምሮ ለተያያዙት ትላልቅ ፕሮጀክቶች እንደሚውልም ተጠቅሷል"

        ]
# instantiate CountVectorizer()
cv = CountVectorizer()

# this steps generates word counts for the words in your docs
word_count_vector = cv.fit_transform(docs2)
wcv = word_count_vector.shape
print(wcv)
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
# print idf values
df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(), columns=["idf_weights"])

# sort ascending
sa = df_idf.sort_values(by=['idf_weights'])
# count matrix
count_vector = cv.transform(docs2)

# tf-idf scores
tf_idf_vector = tfidf_transformer.transform(count_vector)
print(sa)
print("###############")
print(tf_idf_vector)
print("%%%%%%%%%%")
feature_names = cv.get_feature_names()

# get tfidf vector for first document
first_document_vector = tf_idf_vector[0]

# print the scores
df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
df.sort_values(by=["tfidf"], ascending=False)

print(df)