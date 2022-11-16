
import pandas as pd
import numpy as np
import random

def createData(number):

    random.seed(20221113)
    number = 10000

    ##  Create `gender`.
    gender = [random.choice(['male', 'female']) for _ in range(number)]

    ##  Create `height`.
    for g in gender:

        if(g=='male'):

            pass

        else:

            pass

        continue

    [random.choice(['male', 'female']) for _ in range(number)]
    [round(random.gauss(80, 20), 2) for _ in range(number)]
    return


if(__name__=='__main__'):

    createData()
    pass

'''
import numpy as np
import random

total = 10000
noise =  not False
hw1_score = np.zeros([total])
hw2_score = np.zeros([total])
hw3_score = np.zeros([total])
exam_score= np.zeros([total])
attendance = np.zeros([total])
Bonus = np.zeros([total])
Gender = np.zeros([total])
Grade  = np.zeros([total])
Height = np.zeros([total])
Weight  = np.zeros([total])

for i in range(total):
    exam_score[i] = random.gauss(70, 15)
    hw1_score[i] = random.gauss(10, 2)
    hw2_score[i] = random.gauss(15, 3)
    hw3_score[i] = random.gauss(25, 10)
    attendance[i] = random.randint(0,50)
    Bonus[i] = random.randint(0,1)
    Gender[i] = random.randint(0,1)
    Grade[i] = random.randint(1,6)
    Height[i] = random.gauss(165, 10)
    Weight[i] = random.gauss(60, 10)

    if Gender[i]== 0: 
        Weight[i] = Weight[i]*1.4
        Height[i] += random.randint(10,30)


#  have some linear relationship for 
    if noise:
        if Gender[i]== 0: 
            exam_score[i] = exam_score[i] * 1.5
        else:
            attendance[i] = attendance[i] + random.randint(5,15)

        if attendance[i] > 40:
            exam_score[i] = (exam_score[i]/5)*2 +30
        if Grade[i] > 4 : attendance[i] = attendance[i] - random.randint(10,20)
        if attendance[i] < 0 : attendance[i]=0 
'''