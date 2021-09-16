"""
Todo:
1. Rename this file, change Index_Name to your index number in class (Please refer to pdf in NTULearn) followed by your name, for example A1_09_Alex_Lee.
2. You are required to complete the functions as per question, the instructions of each functions are written
as comment within the function, you are reminded to amend the return values whenever is required by the instructions
3. You are not suppose to add in any extra or new functions besides the given
4. You are not suppose to change the name of any given function
4. You are given some test data with command calling the function and the expected results in the main program
for your own testing
5. You will be graded based on the correct output with additional test cases that are prepared by the guider
6. You will also be graded on the quality of code, in terms of readability (so please insert comment when required),
efficiency and maintainability.

"""
#This is a validation of bar code program

'''
The following table gives an example to illustrate how a GTIN-13 Check Digit is calculated:

 

positions                         N1    N2   N3   N4   N5   N6   N7   N8   N9   N10   N11   N12   N13
Number without Check Digit         6     2    9    1    0    4    1    5    0     0     2     1    -
Step 1: Multiply                   x     x    x    x    x    x    x    x    x     x     x     x
by                                 1     3    1    3    1    3    1    3    1     3     1     3
Step 2: Add results                =     =    =    =    =    =    =    =    =     =     =     =
to create sum                      6     6    9    3    0   12    1   15    0     0     2     3
                                                                                                 = 57
Step 3: Subtract the sum from nearest equal or higher multiple of ten = 60- 57 = 3 (Check Digit)
Number with Check Digit            6     2    9    1    0    4    1    5    0     0     2     1    3



'''



#Question 1
def lastDigit(barcode):
    """ Question 1 instructions
          This function will receive a 13 digits barcode numbers string, you may assume the barcode is
          already validated to be 13 digits before it is sent in
          This function will return the last numeric digit as a number to the caller
          Example '6291041500213'  return 3
    """
    lastnumber = int(barcode[-1])
    return lastnumber

#Question 2
def splitOddEven(barcode):
    """ Question 2 instructions
          This function will receive a 12 or 13 digits character string, then 
          return the first 6 odd position digits as the first return string and 
          return the first 6 even position digits as the second return string.
          You may assume the barcode sent in are all numerical digits and has at least 12 character length
          Example '6291041500213'  return '690102', '214501'
    """
    oddstring=''
    evenstring=''
    for i in range(12):
        if i % 2 == 0:
            oddstring += barcode[i]
        else:
            evenstring += barcode[i]
    return oddstring, evenstring
    
    
#Question 3
def partSum(numString, multiplier):
    """ Question 3 instructions
          This function will receive a string containing numbers
          you are required to add up fist 6 digits in the string and multiply the sum by the sent in multiplier
          the function will return caller the sum
          For example before calling the function, if the numString is '690102' and multiplier is 1,
                                                   this function will return (6+9+0+1+0+2) * 1 => 18
          For example before calling the function, if the numString is '214501' and multiplier is 3,
                                                   this function will return (2+1+4+5+0+1) * 3 => 39                                                  

    """
    initialsum = 0
    for i in range(6):
        initialsum += int(numString[i])
    finalsum = initialsum * int(multiplier)
    return finalsum
        
#Question 4
def findlastdigit(barcode):
    """ Question 4 instructions
          This function will receive a validated 12 or 13 digits barcode number string with no special
          characters or leading or tailing spaces.
          you are required to make use of the functions you built for Question 2 to 4 to work out the
          last digit of the barcode given. Note that you are NOT suppose to use answer for question 1
          to simply extract out the last digit.
          Example '6291041500213'  return 3
          Example '629104150021'  return 3
          Hint : this funtion must call splitOddEven and partSum
    """
    splittuple = splitOddEven(barcode)
    oddsum = partSum(splittuple[0], 1)
    evensum = partSum(splittuple[1], 3)
    totalsum = oddsum + evensum
    lastdigitfind = 10 - (totalsum % 10)
    if lastdigitfind == 10:
        lastdigitfind = 0
    return lastdigitfind


#Question 5
def validateFormat(barcode):
    """ Question 5 instructions
        This function will accept a barcode, which may or may not be delimited,
        a delimited barcode may be '6291-0415-0021-3' or '6291-0415-0021' or '629-104-150-021-3'
        a non delimited barcode is simply '6291041500213' or '629104150021'
        You are required to ensure that the barcode contain only digits and/or -;
        12 or 13 digits when converted to a non delimited barcode, and has no leading or tailing spaces.
        Hence, the barcode sent in may also contain leading or tailing spaces 
        This function will return True if the following conditions meet :
            1.there is no leading or tailing spaces like '6291041500213 ' or 
                   ' 6291041500213' or ' 6291041500213 '
            2.every character in the barcode is either digit or '-'
            3.non delimited barcode derived from the barcode should be either 12 or 13 digits..

        The function will return False otherwise.
    """
    validatesymbol = 0
    delimitedsymbol = 0
    if barcode[0] == '' or barcode[-1] == '':
        validatesymbol += 1
    for i in range(len(barcode)):
        try:
            int(barcode[i])
        except ValueError:
            if barcode[i] == '-':
                delimitedsymbol += 1
            else:
                validatesymbol += 1
    if delimitedsymbol == 0 and validatesymbol == 0:
        if len(barcode) == 12 or len(barcode) == 13:
            pass
        else:
            validatesymbol += 1
    if validatesymbol == 0:
        return True
    else:
        return False

#Question 6
def checkBarcode(barcode):
    """ Question 6 instructions
        This function will accept a barcode, which may or may not be delimited,
        a delimited barcode may be '6291-0415-0021-3' or '6291-0415-0021' or '629-104-150-021-3'
        a non delimited barcode is simply '6291041500213' or '629104150021'
        
        The barcode sent in may also contain leading or tailing spaces like '6291041500213 ' or 
        ' 6291041500213' or ' 6291041500213 '
        
        You are required to 
        1.  remove any leading of tailing spaces from the barcode
        2.  validate the barcode by calling validateFormat
            if the barcode is invalid, return "barcode not valid"
        3.  otherwise convert the barcode to nondelimited by removing the '-' in the barcode
        4.  depending on the number of numeric digits in the nondelimited barcode , if the number of numeric digits is
            =12, return the full barcode with the last digit appended
            =13, by checking on the last digit, return "Valid" if the barcode is a valid , "Invalid" if the barcode is not valid
        Hint : this function must call findlastdigit 
    """
    barcode = barcode.strip()
    if validateFormat(barcode) is False:
        return 'barcode not valid'
    else:
        barcode = barcode.replace('-','')
    if len(barcode) == 12:
        fullbarcode = barcode + str(findlastdigit(barcode))
        return fullbarcode
    elif len(barcode) == 13:
        if findlastdigit(barcode) == int(barcode[-1]):
            return 'Valid'
        else:
            return 'Invalid'

#Question 7
def formatBarcode(barcode):
    """ Question 7 instructions
        This function will accept a 13 digit barcode, it will convert the barcode to
        a delimited barcode like '6291-0415-0021-3' 
        This means that you required toinsert q '-' after every 4 digits
        The barcode sent in is assumed to be 13 digits and well validated, hence no validation is required for the barcode sent in within this function.
        Hint : you can use slicing for this 
    """
    barcodelist = [barcode[0:4],barcode[4:8],barcode[8:12],barcode[12]]
    delimitedbarcode = '-'.join(barcodelist)
    return delimitedbarcode

#Question 8
def barcodeGenerator(startcode, nos):
    """ Question 8 instructions
        This function will accept a barcode number in integer format, with nos to indicate the number of barcodes to be generated
        This function will return a list of 'nos' of delimited barcodes generated starting from the startcode 
        You may assume that the startcode is a integer and must be < 1 000 000 000 000
        Hint :  this function must call formatBarcode and checkBarcode
    """
    barcodelist = []
    twelvedigitbarcode = startcode
    for i in range(nos):
        fullbarcode = checkBarcode(str(twelvedigitbarcode))
        delimitedbarcode = formatBarcode(fullbarcode)
        barcodelist.append(delimitedbarcode)
        twelvedigitbarcode += 1
    return barcodelist



if __name__ == "__main__":
    
    #Test for Question 1   
    print("Q1")
    print(lastDigit("6291041500213"))   #should print 3   note 6291041500213 may not be valid
    print(lastDigit("0123456789012"))   #should print 2   note 0123456789012 may not be valid


    #Test for Question 2
    print("Q2")
    revlist=splitOddEven("6291041500213") #note 0123456789012 may not be valid
    print(revlist) #should print ('690102', '214501')

    #Test for Question 3
    print("Q3")
    print(partSum("690102",1)) #should print 18
    print(partSum("214501",3))  #should print 39
    
    #Test for Question 4
    print("Q4")
    print(findlastdigit("629104150021")) #should print 3
    print(findlastdigit("0123456789012")) #should print 2

    #Test for Question 5
    print("Q5")
    print(validateFormat("629104150021    ")) #should print False
    print(validateFormat("   6291041500213")) #should print False
    print(validateFormat("6291041503123")) #should print True
    print(validateFormat("ab291041503er")) #should print False   
    print(validateFormat("6291-0415-0312-3")) #should print True
    print(validateFormat("ab29-10415-03e-r")) #should print False      
    
    #Test for Question 6
    print("Q6")
    print(checkBarcode("629104150021    ")) #should print 6291041500213
    print(checkBarcode("   6291041500213")) #should print Valid
    print(checkBarcode("6291041503")) #should print barcode not valid
    print(checkBarcode("ab291041503")) #should print barcode not valid    

    #Test for Question 7
    print("Q7")
    print(formatBarcode("6291041500212")) #should print 6291-0415-0021-2 note 6291041500212 may not be valid
    print(formatBarcode("6291041500213")) #should print 6291-0415-0021-3 note 6291041500213 may not be valid
  
    #Test for Question 8
    print("Q8")
    generatedList = barcodeGenerator(987654321012,10)
    for each in generatedList:
        print(each)
    ''' Expected output
        9876-5432-1012-8
        9876-5432-1013-5
        9876-5432-1014-2
        9876-5432-1015-9
        9876-5432-1016-6
        9876-5432-1017-3
        9876-5432-1018-0
        9876-5432-1019-7
        9876-5432-1020-3
        9876-5432-1021-0
    '''



        

                
        
    
    

        

                
        
    

