import os
import sys 
import csv
import itertools
from ssm import SSM
from generate_ast import generateAst
from winnowing import winnow
path=sys.argv[1] #Read Data folder path

cfl=os.listdir(path) #List all files in the specified folder
#print(list(itertools.combinations(cfl,2)))

#Code for generate pairwise file list and save into csv file
if not os.path.isfile(path+"/"+os.path.basename(path)+"-pl.csv"):
	with open(path+"/"+os.path.basename(path)+"-pl.csv", "w" ) as f: 
		w=csv.writer(f)
		w.writerows(list(itertools.combinations(cfl,2)))

def fremove(fname):
	if os.path.isfile(fname):
		os.remove(fname)
print("similarity checking starts here...")


with open(path+"/"+os.path.basename(path)+"-pl.csv", "r") as f:
    lis = [line.split() for line in f] # create a list of lists from csv file
    for i, x in enumerate(lis):		
        fremove("program1.txt")
        fremove("program1_count.txt")
        fremove("program1_lev0.txt")
        fremove("program1_lev1.txt")
        fremove("program1_lev2.txt")
        fremove("program2.txt")
        fremove("program2_count.txt")
        fremove("program2_lev0.txt")
        fremove("program2_lev1.txt")
        fremove("program2_lev2.txt")
        #print(x[0].split(",")[1][1:-1])
        f1=str(x).split(",")[0][2:]
        f2=str(x).split(",")[1][:-2]
        f1=f1.replace('"', '')
        f2=f2.replace('"', '')
        if f1.find(".py") == -1: 
            file1=path+"/"+f1
        else:
            file1=path+"/"+f1
        if f2.find(".py") == -1:
            file2=path+"/"+f2
        else:
            file2=path+"/"+f2
        ga=generateAst()
        ga.generateMain(file1,"1")
        ga.generateMain(file2,"2")
        w=winnow()
        w.winnowMain("program1","program2")
        #ssm=SSM()
        #ssm.ssmCheck(file1,file2,os.path.basename(path))
