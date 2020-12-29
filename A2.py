#Q1. Given two matrices please print the product of those two matrices

def fcnReturnMatrixProduct(lstA, lstB):

    intRowA = len(lstA)
    intColA = len(lstA[0])
    intRowB = len(lstB)
    intColB = len(lstB[0])

    if intColA != intRowB:
        return "Matrix product cannot be calculated"

    lstAB = []
    temp_row = intColB * [0]

    for _ in range(intRowA):
        lstAB.append(temp_row[:])

    for intI in range(0,intRowA):
        for intJ in range(0,intColB):
            intSum=0
            for intK in range(0, intRowB):
                intSum = intSum + (lstA[intI][intK]*lstA[intK][intJ])
            lstAB[intI][intJ] = intSum

    return lstAB

#print(fcnReturnMatrixProduct([[1,3,4],[2,5,7],[5,9,6]],[[1,0,0],[0,1,0],[0,0,1]]))

'''
Q2: Select a number randomly with probability proportional to its magnitude from the given array of n elements.
Consider an experiment, selecting an element from the list A randomly with probability proportional to its magnitude. 
Assume we are doing the same experiment for 100 times with replacement, in each experiment 
you will print a number that is selected randomly from A.

Ex 1: A = [0 5 27 6 13 28 100 45 10 79]
Let f(x) denote the number of times x getting selected in 100 experiments.
f(100) > f(79) > f(45) > f(28) > f(27) > f(13) > f(10) > f(6) > f(5) > f(0)
'''

import random

def fcnRandomNumberGenerator(lstA):

    intSumOfArray = 0
    for intIterator in lstA:
        intSumOfArray += intIterator

    intCummulativeSum = 0
    lstCummulativeSum = []
    for intIndex in lstA:
        lstCummulativeSum.append(intCummulativeSum + intIndex/intSumOfArray)
        intCummulativeSum += intIndex/intSumOfArray

    intRandomNumber = random.uniform(0,1)

    for intCtr in range (0,len(lstCummulativeSum)):
        if intRandomNumber < lstCummulativeSum[intCtr]:
            return lstA[intCtr]


def fcnReturnDictonaryForGeneratedRandomNumberFromAList(lstA,intNumOfExperiments):

    dictRandomNumber = { intCtr : 1 for intCtr in lstA}
    for intCtr in range(0,intNumOfExperiments):
        intRandomNumber = fcnRandomNumberGenerator(lstA)
        dictRandomNumber[intRandomNumber] += 1
    return dictRandomNumber

#print(fcnReturnDictonaryForGeneratedRandomNumberFromAList([1,5,27,6,13,28,100,45,10,79],1))

'''
Q3: Replace the digits in the string with #
Consider a string that will have digits in that, we need to remove all the characters which are not digits and replace the digits with #

Ex 1: A = 234                Output: ###
Ex 2: A = a2b3c4             Output: ###
Ex 3: A = abc                Output:   (empty string)
Ex 5: A = #2a$#b%c%561#      Output: ####
'''

def fcnStringManipulation(strString):
    strStringToReturn = ""
    for intCtr in range(len(strString)):
        if strString[intCtr].isnumeric():
            strStringToReturn += "#"
    return strStringToReturn

#print(fcnStringManipulation("123"))

'''
Q4: Students marks dashboard
Consider the marks list of class students given in two lists
Student = ['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10']
Mark = [45, 78, 12, 14, 48, 43, 45, 98, 35, 80]
from the above two lists the Student[0] got Marks[0], Student[1] got Marks[1] and so on.
Your task is to print the name of students
a. Who got top 5 ranks, in the descending order of marks
b. Who got least 5 ranks, in the increasing order of marks
d. Who got marks between >25th percentile <75th percentile, in the increasing order of marks.
'''

def fcnStudentDashboard(lstStudents, lstMarks, intTop):

    dctStudents = dict(zip(lstStudents,lstMarks))
    dctASortedStudents = sorted(dctStudents.items(), key=lambda vntItem: vntItem[1])
    dctDSortedStudents = sorted(dctStudents.items(), key=lambda vntItem: vntItem[1], reverse=True)

#    print(dctStudents,"\n",dctASortedStudents,"\n",dctDSortedStudents,"\n")
    print("Top {} ranks".format(intTop))
    for intCtr in range(len(dctDSortedStudents)):
        if intCtr <= intTop:
            print(dctDSortedStudents[intCtr])

    print("\nBottom {} ranks".format(intTop))
    for intCtr in range(len(dctASortedStudents)):
        if intCtr <= intTop:
            print(dctASortedStudents[intCtr])

    print("\nBetween 25 and 75 percentiles")
    lstMarksNormalized = list(map(lambda x: x/max(lstMarks), lstMarks))
    for intCtr in range(len(lstStudents)):
        if  0.25 < lstMarksNormalized[intCtr] < 0.75:
            print(lstStudents[intCtr])

Student = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7', 'student8',
               'student9', 'student10']
Mark = [45, 78, 12, 14, 48, 43, 45, 98, 35, 80]
#fcnStudentDashboard(Student,Mark, 5)


'''Q5: Find the closest points
Consider you are given n data points in the form of list of tuples like S=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),..,(xn,yn)] 
and a point P=(p,q) your task is to find 5 closest points(based on cosine distance) in S from P
Cosine distance between two points (x,y) and (p,q) is defined as $cos^{-1}(\frac{(x\cdot p+y\cdot q)}{\sqrt(x^2+y^2)\cdot\sqrt(p^2+q^2)})$
Ex:
S= [(1,2),(3,4),(-1,1),(6,-7),(0, 6),(-5,-8),(-1,-1),(6,0),(1,-1)]
P= (3,-4)
'''
import math
def fcnEuclideanDistance(intX, intY):
    return math.sqrt(intX**2 + intY**2)

def fcnReturnClosestPoints(lstPoints, tupNewPoint):

    intP = tupNewPoint[0]
    intQ = tupNewPoint[1]
    lstDistance= []
    for intX, intY in lstPoints:
        intDistance = math.acos((intX*intQ + intY*intP)/((fcnEuclideanDistance(intX,intY)*fcnEuclideanDistance(intP,intQ))))
        lstDistance.append(intDistance)

    dctPointsWithDistance = dict(zip(lstPoints,lstDistance))

    for vntKey, vntValue in sorted(dctPointsWithDistance.items(), key=lambda vntItem: vntItem[1])[:5]:
        print("%s: %s" % (vntKey, vntValue))


#fcnReturnClosestPoints([(1,2),(3,4),(-1,1),(6,-7),(0, 6),(-5,-8),(-1,-1),(6,0),(1,-1)],(3,-4))

'''
Q6: Find which line separates oranges and apples
Consider you are given two set of data points in the form of list of tuples like

Red =[(R11,R12),(R21,R22),(R31,R32),(R41,R42),(R51,R52),..,(Rn1,Rn2)]
Blue=[(B11,B12),(B21,B22),(B31,B32),(B41,B42),(B51,B52),..,(Bm1,Bm2)]
and set of line equations(in the string format, i.e list of strings)
Lines = [a1x+b1y+c1,a2x+b2y+c2,a3x+b3y+c3,a4x+b4y+c4,..,K lines]
Note: You need to do string parsing here and get the coefficients of x,y and intercept.
Your task here is to print "YES"/"NO" for each line given. You should print YES, if all the red points are one side of 
the line and blue points are on other side of the line, otherwise you should print NO.
Ex:
Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

Output:
YES
NO
NO
YES
'''

import re

def fcnCheckSpaceOfPointWRTLines(lstLineParameters, tupPoints):

    lstLineParameters = list(map(float,lstLineParameters))

    return lstLineParameters[0]*tupPoints[0] + lstLineParameters[1]*tupPoints[1] - lstLineParameters[2]

def fcnCheckPointsAcrossLines(lstRedPoints, lstBluePoints, lstLines):

    lstResult = []
    for vntItem in lstLines:
        lstLineParameters = re.split(r'x(.*)y',vntItem)
        intRedPositives = 0
        intRedNegatives = 0
        for intCtr in range(0,len(lstRedPoints)):
            intResultRed = fcnCheckSpaceOfPointWRTLines(lstLineParameters,lstRedPoints[intCtr])
            intResultBlue = fcnCheckSpaceOfPointWRTLines(lstLineParameters,lstBluePoints[intCtr])
            if intResultRed >= 0 and intResultBlue < 0:
                intRedPositives += 1
            elif intResultRed < 0 and intResultBlue >= 0:
                intRedNegatives += 1
            else:
                pass

        if intRedPositives == len(lstRedPoints) or intRedNegatives == len(lstRedPoints):
            lstResult.append("True")
        else:
            lstResult.append("False")

    return lstResult

lstRed= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
lstBlue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
lstLines = ["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

#print(fcnCheckPointsAcrossLines(lstRed,lstBlue,lstLines ))

'''
Q7: Filling the missing values in the specified format
You will be given a string with digits and '_'(missing value) symbols you have to replace the '_' symbols as explained
Ex 1: _, _, _, 24 ==> 24/4, 24/4, 24/4, 24/4 i.e we. have distributed the 24 equally to all 4 places 
Ex 2: 40, _, _, _, 60 ==> (60+40)/5,(60+40)/5,(60+40)/5,(60+40)/5,(60+40)/5 ==> 20, 20, 20, 20, 20 i.e. 
the sum of (60+40) is distributed qually to all 5 places
Ex 3: 80, _, _, _, _  ==> 80/5,80/5,80/5,80/5,80/5 ==> 16, 16, 16, 16, 16 i.e. 
the 80 is distributed qually to all 5 missing values that are right to it
Ex 4: _, _, 30, _, _, _, 50, _, _  
==> we will fill the missing values from left to right 
    a. first we will distribute the 30 to left two missing values (10, 10, 10, _, _, _, 50, _, _)
    b. now distribute the sum (10+50) missing values in between (10, 10, 12, 12, 12, 12, 12, _, _) 
    c. now we will distribute 12 to right side missing values (10, 10, 12, 12, 12, 12, 4, 4, 4)
for a given string with comma seprate values, which will have both missing values numbers like ex: "_, _, x, _, _, _" 
you need fill the missing values Q: your program reads a string like ex: "_, _, x, _, _, _" and returns the filled sequence Ex:
Input1: "_,_,_,24"
Output1: 6,6,6,6

Input2: "40,_,_,_,60"
Output2: 20,20,20,20,20

Input3: "80,_,_,_,_"
Output3: 16,16,16,16,16

Input4: "_,_,30,_,_,_,50,_,_"
Output4: 10,10,12,12,12,12,4,4,4
'''

def fcnreturnEqualDistribution(strInput):
    lstInput = re.split(r',',strInput)
    lstOutput = []
    intFirstNumber = 0
    intLastNumber = 0
    intFirstNumIndex = 0
    intLastNumIndex = 0
    for intCtr in range(0,len(lstInput)):
        if lstInput[intCtr] != "_":
            intLastNumber = int(lstInput[intCtr])
            intLastNumIndex = intCtr
            for intBackCtr in range(intLastNumIndex,intFirstNumIndex-1,-1):
                lstInput[intBackCtr] = (intLastNumber+intFirstNumber)//(intLastNumIndex-intFirstNumIndex+1)
                if intBackCtr == intFirstNumIndex:
                    intFirstNumIndex =  intLastNumIndex
                    intFirstNumber = lstInput[intBackCtr]
        elif intCtr == len(lstInput)-1:
            intLastNumber = 0
            intLastNumIndex = intCtr
            for intBackCtr in range(intLastNumIndex,intFirstNumIndex-1,-1):
                lstInput[intBackCtr] = (intLastNumber+intFirstNumber)//(intLastNumIndex-intFirstNumIndex+1)
                if intBackCtr == intFirstNumIndex:
                    intFirstNumIndex =  intLastNumIndex
                    intFirstNumber = lstInput[intBackCtr]



    return lstInput

#print(fcnreturnEqualDistribution("_,_,_,24"))
#print(fcnreturnEqualDistribution("40,_,_,_,60"))
#print(fcnreturnEqualDistribution("80,_,_,_,_"))
#print(fcnreturnEqualDistribution("_,_,30,_,_,_,50,_,_"))
#print(fcnreturnEqualDistribution("_,_,_,_,_,_,_,_,_"))

'''
Q8: Find the probabilities
You will be given a list of lists, each sublist will be of length 2 i.e. [[x,y],[p,q],[l,m]..[r,s]] consider its 
like a martrix of n rows and two columns

The first column F will contain only 5 uniques values (F1, F2, F3, F4, F5)
The second column S will contain only 3 uniques values (S1, S2, S3)
your task is to find
a. Probability of P(F=F1|S==S1), P(F=F1|S==S2), P(F=F1|S==S3)
b. Probability of P(F=F2|S==S1), P(F=F2|S==S2), P(F=F2|S==S3)
c. Probability of P(F=F3|S==S1), P(F=F3|S==S2), P(F=F3|S==S3)
d. Probability of P(F=F4|S==S1), P(F=F4|S==S2), P(F=F4|S==S3)
e. Probability of P(F=F5|S==S1), P(F=F5|S==S2), P(F=F5|S==S3)
Ex:
[[F1,S1],[F2,S2],[F3,S3],[F1,S2],[F2,S3],[F3,S2],[F2,S1],[F4,S1],[F4,S3],[F5,S1]]

a. P(F=F1|S==S1)=1/4, P(F=F1|S==S2)=1/3, P(F=F1|S==S3)=0/3
b. P(F=F2|S==S1)=1/4, P(F=F2|S==S2)=1/3, P(F=F2|S==S3)=1/3
c. P(F=F3|S==S1)=0/4, P(F=F3|S==S2)=1/3, P(F=F3|S==S3)=1/3
d. P(F=F4|S==S1)=1/4, P(F=F4|S==S2)=0/3, P(F=F4|S==S3)=1/3
e. P(F=F5|S==S1)=1/4, P(F=F5|S==S2)=0/3, P(F=F5|S==S3)=0/3
'''

def fcnReturnProbability(lstExperiments):
    dctExperimentsWithResults = {}
    dctResultsForExp = {}
    dctResultsWithOccurence = {}

    for vntExp, vntResult in lstExperiments:
        if vntResult in dctResultsWithOccurence:
            dctResultsWithOccurence[vntResult] += 1
        else:
            dctResultsWithOccurence[vntResult] = 1

        if vntExp in dctExperimentsWithResults:
            dctResultsForExp = dctExperimentsWithResults[vntExp]
            if vntResult in dctResultsForExp:
                dctResultsForExp[vntResult] += 1
            else:
                dctResultsForExp[vntResult] = 1
        else:
            dctResultsForExp = {vntResult:1}
        dctExperimentsWithResults[vntExp] = dctResultsForExp

    print(dctExperimentsWithResults)
    print(dctResultsWithOccurence)
    for vntExp in dctExperimentsWithResults:
        print("")
        for vntResult in dctResultsWithOccurence:
            if vntResult in dctExperimentsWithResults[vntExp]:
                intOccurence = dctExperimentsWithResults[vntExp][vntResult]
            else:
                intOccurence = 0

            print(f"P(F={vntExp}|S=={vntResult})={intOccurence}/{dctResultsWithOccurence[vntResult]}", end=" ")

#fcnReturnProbability([["F1","S1"],["F2","S2"],["F3","S3"],["F1","S2"],["F2","S3"],["F3","S2"],["F2","S1"],["F4","S1"],["F4","S3"],["F5","S1"]])

'''
Q9: Operations on sentences
You will be given two sentences S1, S2 your task is to find

a. Number of common words between S1, S2
b. Words in S1 but not in S2
c. Words in S2 but not in S1
Ex:

S1= "the first column F will contain only 5 unique values"
S2= "the second column S will contain only 3 unique values"
Output:
a. 7
b. ['first','F','5']
c. ['second','S','3']
'''

def fcnSentenceOperation(strS1, strS2):
    lstS1 = re.split(" ",strS1)
    lstS2 = re.split(" ",strS2)
    lstInS1ButNotInS2 = []
    lstInS2ButNotInS1 = []
    intCountOfCommonElements = 0
    intCountOfCommonElementsBefore = 0

    for vntItem1 in lstS1:
        intCountOfCommonElementsBefore = intCountOfCommonElements
        for vntItem2 in lstS2:
            if vntItem1 == vntItem2:
                intCountOfCommonElements += 1
        if intCountOfCommonElementsBefore == intCountOfCommonElements:
            lstInS1ButNotInS2.append(vntItem1)
    intCountOfCommonElements2 = 0
    intCountOfCommonElementsBefore = 0
    for vntItem2 in lstS2:
        intCountOfCommonElementsBefore = intCountOfCommonElements2
        for vntItem1 in lstS1:
            if vntItem1 == vntItem2:
                intCountOfCommonElements2 += 1
        if intCountOfCommonElementsBefore == intCountOfCommonElements2:
            lstInS2ButNotInS1.append(vntItem2)

    print("The Number of Common items are: ",intCountOfCommonElements)
    print("The list of items in S1 but not in S2: ",lstInS1ButNotInS2)
    print("The list of items in S2 but not in S1: ",lstInS2ButNotInS1)


S1 = "the first column F will contain only 5 unique values"
S2 = "the second column S will contain only 3 unique values"
#fcnSentenceOperation(S1,S2)

'''
Q10: Error Function
You will be given a list of lists, each sublist will be of length 2 i.e. [[x,y],[p,q],[l,m]..[r,s]] 
consider its like a matrix of n rows and two columns
a. the first column Y will contain integer values
b. the second column $Y_{score}$ will be having float values
Your task is to find the value of $f(Y,Y_{score}) = -1*\frac{1}{n}\Sigma_{for each Y,Y_{score} pair}(Ylog10(Y_{score})+(1-Y)log10(1-Y_{score}))$ here n is the number of rows in the matrix
Ex:
[[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]
output:
0.44982
$\frac{-1}{8}\cdot((1\cdot log_{10}(0.4)+0\cdot log_{10}(0.6))+(0\cdot log_{10}(0.5)+1\cdot log_{10}(0.5)) + ... + (1\cdot log_{10}(0.8)+0\cdot log_{10}(0.2)) )$
'''

import math

def fcnReturnLogLoss(lstPoints):
    intLogLoss = 0
    for intY, intP in lstPoints:
        intLogLoss += (intY*math.log10(intP)+(1-intY)*math.log10(1-intP))*(-1)
    return intLogLoss/len(lstPoints)

print(fcnReturnLogLoss([[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]))