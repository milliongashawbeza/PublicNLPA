from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
# importing the modules
from IPython.display import display
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
docs = ["የኢትዮጵያ ቤት ኪንግ ፕሪሚዬር ሊግ አሸናፊው ፋሲል ከነማ ትናንት በአዲስ አበባ ሸራተን አዲስ ሆቴል የገቢ ማሰባሰቢያ ቴሌቶን ማዘጋጀቱ ይታወሳል",
         "በገቢ ማሰባሰቢያ ዝግጅቱ ከፍተኛ የመንግሥት የሥራ ኃላፊዎችን ጨምሮ የተለያዩ የኅብረተሰብ ክፍሎች ተሳትፈዋል፡፡  ስለ ተደረገው የገቢ ማሰባሰቢያ ቴሌቶን መግለጫ የሰጡት የክለቡ ፕሬዚዳንትና የጎንደር ከተማ ከንቲባ አቶ ሞላ መልካሙ ቴሌቶኑ ኢትዮጵያዊነት አምሮና ደምቆ የታየበትና የስፖርት ዓላማን ያሳካ ነበር ብለዋል",
         "በቴሌቶኑ አሁንም በስልክና በተለያዩ አማራጮች ቃል የሚገቡ እንዳሉ ሆኖ ከ170 ሚሊዮን ብር በላይ መሰብሰቡም ተገልጿል"
         "ቀዳማዊት እመቤት ዝናሽ ታያቸው በሁሉም ክልሎች የክለቡ አምባሳደሮች መሰየማቸው ፋሲል ከነማ የኢትዮጵያ ክለብ መሆኑን የሚገልጽ ነው ብለዋል። በቴሌቶኑ ከሁሉም የኢትዮጵያ ክፍሎች ድጋፎች መደረጋቸው ሌላኛው ፍሲል የኢትዮጵያ ክለብ መሆኑን የሚያሳይ እንደሆነ ተናግረዋል። በድጋፉ ለተሳተፉ ሁሉም አካላት ምስጋናም አቅርበዋል",
         "በቀጣይ ክለቡ የያዛቸውን ትላልቅ ፕሮጀክቶች ከግብ ለማድረስና ክለቡ በአፍሪካ መድረክ ረዥም ርቀት እንዲጓዝ አሁንም የሁሉም ድጋፍ ያስፈልጋል ተብሏል።",
         "የክለቡ ሥራ አስኪያጅ አቶ አቢዮት ብርሃኑ ክለቡ በቀጣይ ከመንግሥት በጀት ተላቆ የራሱ ቋሚ ሀብት እንዲኖረው ሥራዎች በእቅድ እየተሠሩ ስለመሆናቸው ተናግረዋል",
         "ከቴሌቶኑ የሚገኘው ገቢ ለደሞዝና ለእለታዊ ወጭዎች ሳይሆን አካዳሚ መገንባት ጨምሮ ለተያያዙት ትላልቅ ፕሮጀክቶች እንደሚውልም ተጠቅሷል"

        ]
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform(docs)
first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[0]

# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(),
                  columns=["tfidf"])
d=df.sort_values(by=["tfidf"], ascending=False)

display(d)
