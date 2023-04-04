import os
import numpy as np
import pandas as pd
from am import ApproachMatch
import pickle


class getGrade:
    def gradeIcorrect(self,fp1,fp2,t):
        try:
            test=t #number of test case passed
            fn=0  #Assume there is no flase negative
            aproach=ApproachMatch()
            ssm=aproach.findApproach(fp1,fp2)#Get similarity score using SSM method
            input_data={"testcases": test,"ssm": ssm,"fn": fn}
            df = pd.DataFrame(input_data)
            regr_rf=pickle.load(open("q3_gm.sav", 'rb'))#load pre-trained grading model for question1
            pred_g=regr_rf.predict(df.values)
            #print(pred_g)
            return pred_g
        except FileNotFoundError as e:
            print(str(e))
            exit()
        

g=getGrade()

fp1="../../../Exp/DataSet/APR_Data_set/Python/data/question_3/code/Incorrect/wrong_3_008.py" #incorrect solution
fp2="../../../Exp/DataSet/APR_Data_set/Python/data/question_3/code/Correct/correct_3_005.py" #reference solution
t=9

grade=g.gradeIcorrect(fp1,fp2,t)
print(grade)






