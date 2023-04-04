import csv
import os
import pandas as pd

#Read SSM output file
with open(fname+".txt") as fin:
	for line in fin:
		if "(" in line: 
			s=line.split(" ")
			l1=s[0].split("/")
			l2=s[1].split("/")
			f1=l1[len(l1)-1]
			f1=f1[:-2]			
			f2=l2[len(l2)-1]
			f2=f2[:-2]
			sc=s[2][:-2]
			data={"file1":[f1],"file2":[f2],"score":[sc]}
			#print(data)
			
			if not os.path.isfile("paper-gm.csv"):
				df=pd.DataFrame(data)
				df.to_csv("paper-gm.csv",header=False, index=False)
			else:
				df=pd.DataFrame(data)
				df.to_csv("paper-gm.csv",header=False,mode='a', index=False)
			
		else:
			s=line.split(" ")
			l1=s[0].split("/")
			l2=s[1].split("/")
			f1=l1[len(l1)-1]
			f1=f1[:-2]			
			f2=l2[len(l2)-1]
			f2=f2[:-2]
			sc=s[2][:-2]
			data={"file1":[f1],"file2":[f2],"score":[sc]}
			#print(data)
			
			if not os.path.isfile("paper-gm.csv"):
				df=pd.DataFrame(data)
				df.to_csv("paper-gm.csv",header=False, index=False)
			else:
				df=pd.DataFrame(data)
				df.to_csv("paper-gm.csv",header=False,mode='a', index=False)
			
			
