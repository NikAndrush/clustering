import numpy
import math



class Matrix:
	dictionaryFile="dictionary.txt"
	textFile="afterPT.txt"
	f=open(dictionaryFile,'r')
	f2=open(textFile,'r')
	dictionary = f.read()
	dictionary=dictionary.split()
	text=f2.readlines()
	matrix=numpy.zeros([len(text),len(dictionary)])

	def __init__(self):
		dictionaryFile="dictionary.txt"
		textFile="afterPT.txt"
		f=open(dictionaryFile,'r')
		f2=open(textFile,'r')
		dictionary = f.read()
		dictionary=dictionary.split()
		text=f2.readlines()
		matrix=numpy.zeros([len(text),len(dictionary)])
	
	def getBag(self):
		print(str(len(self.text))+' '+str(len(self.dictionary)))
		i=0


		for line in self.text:
			j=0
			for word in self.dictionary:
				self.matrix[i][j]=line.count(word)
				j+=1
			i+=1
		return self.matrix




	def metrik(self,a,b):
		i=0
		r=0
		while(i<len(a)):
			if(a[i]!=0 and b[i]!=0):
							if(a[i]==b[i]):
								r+=a[i]*-2
							else:	
								r+=((a[i]+b[i])/math.fabs(a[i]-b[i]))*-1
			else:
				r+=(math.fabs(a[i]-b[i]))*1.2
			i+=1
		return r







	

	def getDistance(self,bag):
		dis=[]
		mn=0
		while  mn<len(self.text):
			dis.append([])
			mn+=1
		rez=numpy.zeros(len(bag[0]))

		i=0
		while i<(len(self.text)):
			j=i+1
			pastI=0
			reversI=i-1
			while pastI<i:
				dis[i].append([[dis[pastI][reversI][0][0],i],[i,pastI]])
				pastI+=1
			while j<(len(self.text)):
				b=0
				ag=[]
				bg=[]
				while b<(len(bag[0])):
					ag.append(bag[i][b])
					bg.append(bag[j][b])
					b+=1
				dis[i].append([[self.metrik(ag,bg),i],[i,j]])
				j+=1
			i+=1
			if(i%100==0):
				print(i)
		return dis



	


