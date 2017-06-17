import nltk
from nltk.corpus import stopwords
import re


stop=set(stopwords.words('english'))
stop.update(	['hello'], ['bye'],['thanks'],['thanksgiving'],['vincent'],['emil'],['wich'],['wait'],['ok'],['said'],['great'],['day'],['welcome']
	 ,['smiley'],['sorry'],['david'],['please'],['yes'],['see'], ['okay'], ['dont'], ['sure'],['would'],['one'],['let'],['like'],['need'],['hi']
	 ,['make'],['want'],['go'],['help'],['good'],['questions'],['question'],['answer'],['take'],['guys'],['guy'],['peter'],['steve'],['thomas']
	 ,['mark'],['thank'],['hey'],['john'],['thats'],['also'],['cause'],['somebody'])






 
 





def f_NLTK(st):
	

	st2 = [i for i in st.lower().split() if i not in stop]

	lk=nltk.pos_tag(st2)
	
	
	
	lk[:]=[item for item in lk if item[1]!='RB']
	lk[:]=[item for item in lk if item[1]!='VBG']
	lk[:]=[item for item in lk if item[1]!='VBD']
	lk[:]=[item for item in lk if item[1]!='NNS']
	lk[:]=[item for item in lk if item[1]!='VBP']
	lk[:]=[item for item in lk if item[1]!='CD']
	lk[:]=[item for item in lk if item[1]!='VBZ']
	lk[:]=[item for item in lk if item[1]!='JJR']
	lk[:]=[item for item in lk if item[1]!='RBR']
	lk[:]=[item for item in lk if item[1]!='PRP']

	#print(lk)

	stR=[]
	for werb in lk:
		stR.append(werb[0])
	#		lk.remove(werb)
			

	return(stR)
	





def preTreatment(st):
	
	
	
	tm=""
	i=0
	
	while st[i]!=':':
		tm+=st[i]
		i+=1
	b=i+1
	
	while st[b]!=':':
		tm+=st[b-1]
		b+=1
	st=re.sub(tm,'',st)
	st=st[0:-4]



	st=re.sub('Smiley: Open Mouthed','',st)
	st=re.sub('Smiley: Smile','',st)
	st=re.sub('Smiley: Hot','',st)
	st=re.sub('Smiley: Tongue Out','',st)
	st=re.sub('Smiley: Sleeping Half Moon','',st)
	st=re.sub('Smiley: Wink','',st)
	st=re.sub('Smiley: Surprised','',st)
	st=re.sub('Smiley: Sad','',st)
	st=re.sub('Smiley: Pizza','',st)
	st=re.sub('Smiley: Thinking','',st)
	st=re.sub('Smiley: Angry','',st)
	st=re.sub('any questions later let us know','',st)
	st=re.sub('happy holidays','',st)
	st=re.sub("you're welcome",'',st)
	st=re.sub('happy new year','',st)
	st=re.sub('Any questions later, just let us know','',st)




	st=re.sub(r'A:|Q:',' ',st)
	st=re.sub('u00a0|u20ac|u20a|u00d0|u00e2|u2122|u2014|u00b4|u00d1|u00b0|u00b2|u0081|u201a|u0192|u00b9|u00b5|u02dc|u00b3|u00be|u0152|u00bc|u2039|u00bf|u00bb|u008f|u00b8|u017d|u00c2|u00b6|u00bd|u2021|u00ba|u00b1|u2019|u0090|u00b7|u2022|57|u00a1|u0178','',st)
	



	st = re.sub(r'\<[^>]*\>', ' ', st)
	st=re.sub(r'^|\\n|\s+$', ' ', st)
	st=re.sub(r'[/\-\\,.\?''"]',' ',st)
	st=re.sub(r'[..]',' ',st)
	st=re.sub(r'\W',' ',st)

	


	

	lk=f_NLTK(st)
	
	return lk



f=open('blinded_chats_g.json','r')
f4= open('afterPT.txt','w')


for line in f.readlines():
	if(line.strip()=="{" or line.strip()=="}"):
		continue
	st=str(preTreatment(line))
	st=re.sub(r'\[','',st)
	st=re.sub(r'\]','',st)
	f4.write(st+'\n')


f.close()
f4.close()