import nltk
import re
def bigramm(s):
    sentence = s.split()
    bigramed = list(nltk.bigrams(sentence))
   # trigrammed =list(nltk.trigrams(sentence))
    bigramlist = [('ነገር','ግን'),('ፊት','ለፍፊት'),('ፍርድ','ቤት'),('ትምህርት','ቤት'),('ሥነ','ቃል'),('ሥነ','ፅሁፍ'),('ሥነ','ጥበብ'),
                  ('አዲሥ','አበባ'),('አዲስ','አበባ'),('ባህር','ዳር'),('ባሕር','ዳር'),('መንፈስ','ቅዱሥ'),('ራስ','ዳሽን'),('ሰሜን','ተራሮች'),
                  ('አዝዋ','ሆቴል'),('ዩኒሰን','ሆቴል'),('ምርጫ','ቅስቀሳ'),('በሚያስደንቅ','ሁኔታ')
                  ]

    isec = set(bigramed) & set(bigramlist)
    if(len(isec)==0):
        return s
    newdata=[]
    i=[]
    c=[]
    for f in bigramed:
        if f in isec:
          newdata.append(str(f).replace("'", "").replace(", ", "_"))
          c.append(str(f).replace("'", "").replace(", ", "_"))
          i.append(int(1))
        else:
          newdata.append(str(f).replace("'", "").replace(", ", " "))
          i.append(int(0))
          c.append(tuple(f))

    w=[]
    k=[]
    s=[]
    l=[]
    b=0
    f=0
    for x in range(len(i)):
        if(x==0):
            b=0
        else:
            b=x-1
        if(x<len(i)):
            f=x+1
        else:
            f=x
       # if(i[b]!=1):
            #l.append(i[x])
            #s.append(c[x])

    
    b2=0
    b=0
    y=0
    for x in range(len(i)):
        #Two forwards
        if(x==0 or x==1 or x==2):
           b2=x
        else:
          b2=x-2
          y=0 #forward loop
        if(x<len(i)-1):
            y=x+1
        else:y=x
        b=0 #backward loop
        if(x==0):
            b=x
        else:b=x-1
        b3=0
        if(x==0 or x==1 or x==2):
            b3=x
        else:b3=x-3

        if(i[x]==0 and i[y]==1 and i[b]==0 and i[b2]==0):
                   #  print(c[x][0])
             k.append(c[x][0])
        elif(i[x]==0 and i[y]==1 and i[b]==0):
            continue
        elif(i[x]==0 and i[y]==1 and i[b]==0 and i[b2]==1):
            continue
        elif(i[x]==1 and i[y]==0):
                # print(c[x])
              k.append(c[x])
        elif(i[x]==0 and i[y]==0 and i[b]==0 and i[b2]==0and i[b3]==0):
             k.append(c[x][0])
        elif(i[x]==0 and i[y]==0 and i[b]==0 and i[b2]==0and i[b3]==1):
            k.append(c[x][1])
        elif(i[x]==0 and i[y]==0 and i[b]==0 and i[b2]==1):
                 k.append(c[x][1])
        elif(i[x]==0 and i[b]==0):
            k.append(c[x])
        elif(i[x]==0 and i[b]==1):
            k.append(c[x][1])
           # print(c[x])
        #print(k)

        se = ' '.join(k)
        x = re.sub('[()]','',se)
    return x

#s = "ዛሬ ፍርድ ቤት እና ትምህርት ቤት ነበርኩ"
#sentence = ['ፍርድ','ቤት', 'beginning','ትምህርት','ቤት', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
#sentence = s.split()














































































#print(texts)
#print(*map(' '.join, isec), sep=', ')
