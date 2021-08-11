import nltk


def trigramm(s):
    sentence = s.split()
    #bigramed = list(nltk.bigrams(sentence))
    trigrammed =list(nltk.trigrams(sentence))
    trigrlist = [('የህዝብ', 'ተወካዮች','ቢሮ'), ('የሚንስትሮች','ምክር', 'ቤት')]
    isec = set(trigrammed) & set(trigrlist)

    newdata = []
    i = []
    c = []
    for f in trigrammed:
        if f in isec:
            newdata.append(str(f).replace("'", "").replace(", ", "_"))
            c.append(str(f).replace("'", "").replace(", ", "_"))
            i.append(int(1))
        else:
            newdata.append(str(f).replace("'", "").replace(", ", " "))
            i.append(int(0))
            c.append(tuple(f))


    w = []
    k = []
    s = []
    l = []
    b = 0
    f = 0
    for x in range(len(i)):
        if (x == 0):
            b = 0
        else:
            b = x - 1
        if (x < len(i)):
            f = x + 1
        else:
            f = x
    # if(i[b]!=1):
    # l.append(i[x])
    # s.append(c[x])

    b2 = 0
    b = 0
    y = 0
    t=[]
    for x in range(len(i)):
        # Two forwards
        if (x == 0 or x == 1):
            b2 = x
        else:
            b2 = x - 2
            y = 0  # forward loop
        if (x < len(i) - 1):
            y = x + 1
        else:
            y = x
        b = 0  # backward loop
        if (x == 0):
            b = x
        else:
            b = x - 1
        y2=0 # two forwards
        if(x<len(i)-2):
            y2=x+2
        else:
            y2=x
        if(i[y]==1 and i[x]==0):
           continue
        elif(i[b]==1 and i[x]==0):
            continue
        elif(i[y]==1):
            t.append(c[x])
        elif(i[y2]==1):
            t.append((c[x][0],c[x][1]))
        elif(i[b2]==1):
            t.append(c[x][1],c[x][2])
        elif(i[x]==1):
            t.append(c[x])
        elif(i[x]==0 and i[y]==0 and i[y2]==0):
            t.append(c[x][0])


        if (i[x] == 0 and i[y] == 1 and i[b] == 0 and i[b2 == 0]):
            #  print(c[x][0])
            k.append(c[x][0])
        elif (i[x] == 0 and i[y] == 1 and i[b] == 0 and i[b2 == 1]):
            continue
        elif (i[x] == 1 and i[y] == 0):
            # print(c[x])
            k.append(c[x])
        elif (i[x] == 0 and i[y] == 0 and i[b] == 0 and i[b2] == 0):
            k.append(c[x])
        elif (i[x] == 0 and i[y] == 0 and i[b] == 0 and i[b2] == 1):
            k.append(c[x][1])
        elif (i[x] == 0 and i[b] == 0):
            k.append(c[x])
        elif (i[x] == 0 and i[b] == 1):
            k.append(c[x][1])
        # print(c[x])
    print(t)
    return k

# s = "ዛሬ ፍርድ ቤት እና ትምህርት ቤት ነበርኩ"
# sentence = ['ፍርድ','ቤት', 'beginning','ትምህርት','ቤት', 'God', 'created', 'the', 'heaven','and', 'the', 'earth', '.']
# sentence = s.split()


# print(texts)
# print(*map(' '.join, isec), sep=', ')
