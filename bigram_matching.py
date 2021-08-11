import re
bigrams = ["ፍርድ ቤት","ትምህርት ቤት"]
text = "for ther real ፍርድ ቤት ksdkada aksdaka ds"
re.sub('('+'|'.join('\\b'+re.escape(g)+'\\b' for g in bigrams)+')', lambda m: m.group(0).replace(' ', '_'), text)