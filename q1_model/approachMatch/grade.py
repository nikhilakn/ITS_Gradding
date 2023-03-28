import os
import numpy as np
import pandas as pd
from am import ApproachMatch
import pickle


class getGrade:
    def gradeIcorrect(self,fp1,fp2,t):
        fp1="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Incorrect/wrong_1_008.py" #incorrect solution
        fp2="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Correct/correct_1_005.py" #reference solution
        test=t #number of test case passed
        fn=0  #Assume there is no flase negative
        aproach=ApproachMatch()
        ssm=aproach.findApproach(fp1,fp2)
        data={"testcases": test,"ssm": ssm,"fn": fn}
        df = pd.DataFrame(data)
        regr_rf=pickle.load(open("q1_gm.sav", 'rb'))
        pred_g=regr_rf.predict(df.values)
        print(pred_g)
        

g=getGrade()

fp1="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Incorrect/wrong_1_008.py" #incorrect solution
fp2="../../../Exp/DataSet/APR_Data_set/Python/data/question_1/code/Correct/correct_1_005.py" #reference solution
t=9
g.gradeIcorrect(fp1,fp2,t)






