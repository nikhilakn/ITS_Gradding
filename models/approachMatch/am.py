import sys
import os
import csv
import pandas as pd
import random
from ssm.winnowing import winnow
from ssm.generate_ast import generateAst
import pickle

class ApproachMatch:
	def fremove(self,fname):
			if os.path.isfile(fname):
				os.remove(fname)
	def findApproach(self, path_file1, path_file2): #path_file1 is the path to incorrect submission, path_file2 is the path to reference solution

		ga=generateAst()
		ga.generateMain(path_file1,"1")
		ga.generateMain(path_file2,"2")
		w=winnow()
		sim=w.winnowMain("program1","program2")	
		self.fremove("program1.txt")
		self.fremove("program1_count.txt")
		self.fremove("program1_lev0.txt")
		self.fremove("program1_lev1.txt")
		self.fremove("program1_lev2.txt")
		self.fremove("program2.txt")
		self.fremove("program2_count.txt")
		self.fremove("program2_lev0.txt")
		self.fremove("program2_lev1.txt")
		self.fremove("program2_lev2.txt")
		return sim
		


#am=ApproachMatch()
#fp1="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Incorrect/wrong_1_008.py"
#fp2="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Correct/correct_1_005.py"
#crl=am.findApproach(fp1,fp2)
#print(crl)

