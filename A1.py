# Q1. Write a function that inputs a number and prints the multiplication table of that number.

def subPrintMultiplicationTable(intNumberOfTable):
    for intCounter in range(1,11):
        print(intNumberOfTable," * ",intCounter, " = ",intCounter*intNumberOfTable)

#subPrintMultiplicationTable(7)

# Q2. Write a program to print twin primes less than 1000. If two consecutive odd numbers
# are both prime then they are known as twin primes

def boolCheckPrimeNumber(intNumberToCheck):
    for intCounter in range(intNumberToCheck-1,1,-1):
        if intNumberToCheck % intCounter == 0:
            return bool(0)
    return bool(1)

def PrintTwinPrimes(intUpperLimit):
    for intCounter in range(3,intUpperLimit-1,2):
        if boolCheckPrimeNumber(intCounter) and boolCheckPrimeNumber(intCounter+2):
            print(intCounter," and ", intCounter+2)

#PrintTwinPrimes(1000)

# Q3. Write a program to find out the prime factors of a number. Example: prime factors of 56 - 2, 2, 2,7
def PrintPrimeFactors(intNumber):
    while intNumber % 2 == 0:
        intNumber=int(intNumber/2)
        print(2,end = " ")

    for intCounter in range(3,intNumber+2,2):
        if intNumber % intCounter == 0:
            intNumber=int(intCounter/intCounter)
            print(intCounter, end=" ")

#PrintPrimeFactors(3131)

''' Q4. Write a program to implement these formulae of permutations and combinations. 
    Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!. 
    Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!
'''

def fcnReturnFactorial(intNumber):
    if intNumber == 0:
        return 1
    intFactorial = 1
    for intNumber in range(intNumber,1,-1):
        intFactorial = intFactorial * intNumber
        intNumber = intNumber - 1

    return intFactorial

def fcnPrintPermutationAndCombination(intN,intR):
    print("Permutation : ",int(fcnReturnFactorial(intN)/fcnReturnFactorial(intN-intR)))
    print("Combination : ",int(fcnReturnFactorial(intN)/(fcnReturnFactorial(intR)*fcnReturnFactorial(intN-intR))))

#fcnPrintPermutationAndCombination(10,5)

# Q5. Write a function that converts a decimal number to binary number

def fcnReturnMaxBase(intDecimalNumber):
    intMaxBase = 0
    while 1 :
        if 2**intMaxBase > intDecimalNumber:
            break
        intMaxBase=intMaxBase+1
    return intMaxBase-1,intDecimalNumber-(2**(intMaxBase-1))

def PrintBinaryCode(intDecimalNumber):
    intMaxBase, intFactoredDecimal = fcnReturnMaxBase(intDecimalNumber)
    listTrueBases = []
    listTrueBases.append(intMaxBase)
    while intFactoredDecimal > 0 :
        intMaxBase, intFactoredDecimal = fcnReturnMaxBase(intFactoredDecimal)
        listTrueBases.append(intMaxBase)
    print("The Binary of ",intDecimalNumber," is : ")
    for intBinaryPrinter in range(int(listTrueBases[0]),-1,-1):
        if intBinaryPrinter in listTrueBases:
            print(1,end=" ")
        else:
            print(0, end=" ")

#PrintBinaryCode(2)

''' Q6. Write a function cubesum() that accepts an integer and 
returns the sum of the cubes of individual digits of that number. Use this function 
to make functions PrintArmstrong() and isArmstrong() to print Armstrong numbers 
and to find whether is an Armstrong number '''

def fcnCubeSum(intNumber):
    intCubeSum = 0
    while intNumber > 0:
        intCubeSum = intCubeSum + (intNumber % 10) ** 3
        intNumber = int(intNumber / 10)
    return intCubeSum

def isArmstrong(intNumber):
    return intNumber == fcnCubeSum(intNumber)

def PrintArmstrong(intNumber):
    if isArmstrong(intNumber):
        print(intNumber,"is an Armstrong Number.")
    else:
        print(intNumber,"is not an Armstrong Number.")

#PrintArmstrong(153)

# Q7. Write a function prodDigits() that inputs a number and returns the product of digits of that number

def fcnProductSum(intNumber):
    print("The product of the digits of {} is: ".format(intNumber), end=" ")
    intProductSum = 1
    while intNumber > 0:
        intProductSum = intProductSum * (intNumber % 10)
        intNumber = int(intNumber / 10)

    print(intProductSum)

#fcnProductSum(1331)

''' Q8. If all digits of a number n are multiplied by each other repeating with the product, 
the one digit number obtained at last is called the multiplicative digital root of n. 
The number of times digits need to be multiplied to reach one digit is called the multiplicative persistance of n. 
Example: 86 -> 48 -> 32 -> 6 (MDR 6, MPersistence 3) 341 -> 12->2 (MDR 2, MPersistence 2) 
Using the function prodDigits() of previous exercise write functions MDR() and MPersistence() that 
input a number and return its multiplicative digital root and multiplicative persistence respectively
'''

def fcnProductofDigits(intNumber,intPersistence):
    if  intNumber % 10 == intNumber:
        return intNumber, intPersistence
    intProductSum = 1
    while intNumber > 0:
        intProductSum = intProductSum * (intNumber % 10)
        intNumber = int(intNumber / 10)
    return fcnProductofDigits(intProductSum,intPersistence+1)

def PrintMultiplicativeDigitalRootAndPersistence(intNmber):
    intMDR, intMR = fcnProductofDigits(intNmber,0)
    print("The MDR is : {} and MR is : {}".format(intMDR,intMR))

#PrintMultiplicativeDigitalRootAndPersistence(341)

# Q9. Write a function sumPdivisors() that finds the sum of proper divisors of a number.
# Proper divisors of a number are those numbers by which the number is divisible, except the number itself.
# For example proper divisors of 36 are 1, 2, 3, 4, 6, 9, 18

def subSumOfDivisors(intNumber):
    print("The Divisors are :", end=" ")
    intSumOfDivisors = 0
    for intCounter in range(1,intNumber):
        if intNumber % intCounter == 0:
            intSumOfDivisors = intSumOfDivisors + intCounter
            print(intCounter,end=" ")

    print("\nThe Sum of the Divisors are : ",intSumOfDivisors)

#subSumOfDivisors(36)

''' Q10. A number is called perfect if the sum of proper divisors of that number is equal to the number. 
    For example 28 is perfect number, since 1+2+4+7+14=28.
    Write a program to print all the perfect numbers in a given range.
'''
def subCheckPerfectNumber(intNumber):
    intSumOfDivisors = 0
    for intCounter in range(1,intNumber):
        if intNumber % intCounter == 0:
            intSumOfDivisors = intSumOfDivisors + intCounter

    if intSumOfDivisors == intNumber :
        print(intNumber,"is a Perfect Number.")
    else:
        print(intNumber,"is not a Perfect Number.")

#subCheckPerfectNumber(28)

''' Q11. Two different numbers are called amicable numbers if the sum of the proper divisors of each 
    is equal to the other number. For example 220 and 284 are amicable numbers. 
    Sum of proper divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284 
    Sum of proper divisors of 284 = 1+2+4+71+142 = 220 Write a function to print pairs of amicable numbers in a range
'''
def fcnSumOfDivisorOfANumber(intNumber):
    intSumOfDivisors = 0
    for intCounter in range(1,intNumber):
        if intNumber % intCounter == 0:
            intSumOfDivisors = intSumOfDivisors + intCounter
    return intSumOfDivisors


def subPrintAmicablePairs(intNumber1):
    print("The List of Amicable Numbers in range {} are : ".format(intNumber1))
    for intCounter in range(1, intNumber1):
        for intCounter2 in range(intCounter+1,intNumber1):
            if fcnSumOfDivisorOfANumber(intCounter2) == intCounter and fcnSumOfDivisorOfANumber(intCounter) == intCounter2:
                print(intCounter,"&",intCounter2)

#subPrintAmicablePairs(500)

# Q12. Write a program which can filter odd numbers in a list by using filter function
def subFilterOddNumbersFromAList(ListNumbers):
    ListOddNumbers = []
    for ListItem in ListNumbers:
        if ListItem % 2 == 1:
            ListOddNumbers.append(ListItem)

    print(ListOddNumbers)

#subFilterOddNumbersFromAList([1,2,3,4,5,6,7,8,9,10,11])

# Q13. Write a program which can map() to make a list whose elements are cube of elements in a givelist
def subCubeOfAList(ListNumbers):
    ListCubeNumbers = []
    for ListItem in ListNumbers:
        ListCubeNumbers.append(ListItem**3)

    print(ListCubeNumbers)

#subCubeOfAList([1,2,3,4,5,6,7,8,9,10,11])

# Q14. Write a program which can map() and filter() to make a list whose elements are cube of even number in a given list

def subCubeOfAEvenListMember(ListNumbers):
    ListCubeNumbers = []
    for ListItem in ListNumbers:
        if ListItem % 2 == 0:
            ListCubeNumbers.append(ListItem**3)

    print(ListCubeNumbers)

subCubeOfAEvenListMember([1,2,3,4,5,6,7,8,9,10,11])





