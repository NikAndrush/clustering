import nltk

f=open('afterPT.txt','r')
g=f.read()
st = nltk.FreqDist(g.split())
print(st)
st2 = st.most_common(1000)
b=""
for i in st2:
 b+=i[0]+' '

f2=open('dictionary.txt','w')
f2.write(b)
f.close()
f2.close()