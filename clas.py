#алгоритм без схлопывания кластеров

from matrix import Matrix
import time
import math
from decimal import Decimal



bag = Matrix().getBag()

min_in_tf_bag=0



masCluster=[]
masClusDist=[]
flag=True



def sortCluster():
	for it in masCluster:
		i=0
		while (i<(len(masCluster)-1)):
			if(len(masCluster[i][2])<len(masCluster[i+1][2])):
				change=masCluster[i]
				masCluster[i]=masCluster[i+1]
				masCluster[i+1]=change
			i+=1
	return masCluster[0]
			

def tfIdf_M():

	dictionary=[]
	for k in range(0,len(bag[0])):
		dictionary.append(0)
	i=0
			
	for line in bag:
		sum=0
		for k in line:
			sum+=k
		b=0
		while(b<len(bag[0])):
			if(sum==0):
				line[b]=0
			else:
				line[b]= (line[b]/sum)
			b+=1

def tfIdf():

	dictionary=[]
	for k in range(0,len(bag[0])):
		dictionary.append(0)
	i=0
	while (i<len(bag[0])):
		for line in bag:
			if(line[i]!=0):
				dictionary[i]+=1
		i+=1
			
	
	for line in bag:
		sum=0
		for k in line:
			sum+=k
		b=0
		while(b<len(bag[0])):
			if(sum==0):
				line[b]=0
			else:
				line[b]= (line[b]/sum)*(math.log10(len(bag)/dictionary[b]))
			b+=1
	

def getMin():
	masAllMin=[]
	masMin=[]
	i=0
	while i<len(masDistance):
		f=min(masDistance[i])
		for m in masDistance[i]:
			if m[0]==f[0]:
				masAllMin.append(m)
		i+=1

	
	masMin=min(masAllMin)
	

	return masMin

def average(indEX):
	av=[]
	count=[]
	for i in bag[0]:
		av.append(0)
		count.append(0.0)
	for i in indEX:
		j=0
		while j<len(av):
			av[j]+=bag[i][j]
			if(bag[i][j]!=0):
				count[j]+=1
			j+=1


	i=0
	while i<len(av):
		if((count[i]/len(indEX))<0.4):
			av[i]=0
		elif((count[i]/len(indEX))>=0.65):
			av[i]/=count[i]
		else:
			av[i]/=len(indEX)
		i+=1

	return av


def addInCluster(indEX,num='j'):

	if (num=='j'):
		if(len(masCluster)!=0):
			av=average(indEX)
			masCluster.append([(masCluster[-1][0]+1),av,indEX])
			return masCluster[-1]
		else:
			av=average(indEX)
			masCluster.append([0,av,indEX])
			return masCluster[0]
	else:
		av=average(indEX)
		masCluster[num][1]=av
		masCluster[num][2]=indEX
		newDistance(masCluster[num],num)
		return masCluster[num]


def newDistance(clus,num='j'):
	

	if(num=='j'):
		av=clus[1]
		indEX=[]

		for i in masDistance:
			indEX.append(i[0][0][1])
		
		masD=0
		for i in indEX:
			masDistance[masD].append([[Matrix().metrik(bag[i],av),clus[0]],[masDistance[masD][0][0][1]]])
			masD+=1
	else:
		for n in masDistance:
			for k in n:
				if(len(k[1])==1):
					if(k[0][1]==clus[0]):
						k[0][0]=Matrix().metrik(bag[k[1][0]],clus[1])

def delMin(indEX,inCl=0):

	for k in indEX:
		for ind in masDistance:
			if ind[0][0][1]==k:
				masDistance.remove(ind)
				break
	
	for pop in indEX:
		for it in masDistance:
			for inIt in it:		
					if(inIt[1][1]==pop):
						it.remove(inIt)
						break


	


def between(miN):
	
	ki=5
	testType=type(ki)
	indEX=miN[1]
	
	
	if(len(indEX)==1):
		
		indEX=masCluster[miN[0][1]][2]
	
		indEX.append(miN[1][0])
		delMin(miN[1])
		addInCluster(indEX,miN[0][1])
		

	else:
		nClus=addInCluster(indEX)
		newDistance(nClus)	
		delMin(indEX)		

	





tfIdf_M()

masDistance= Matrix().getDistance(bag)




it=0

while(len(masDistance)>1):

	
	print('=================================')
	
	print('============'+str(it)+'=====================')
	
	
	print('=================================')
	
	print('=================================')
	l=getMin()
		
	between(l)

	it+=1







print('=================================')

for cluster in masCluster:
	print("cluster - "+str(cluster[0])+" contain dialogs - "+str(cluster[2]))

print('=================================')

print('=================================')

print('most popular cluster = '+str(sortCluster()[0])+" contain dialogs -" +str(sortCluster()[2]))

print('=================================')

print('=================================')
