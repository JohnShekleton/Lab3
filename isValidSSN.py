def isValidSSN(ssn):
    '''Description:  returns True if the string is valid ssn
       Prescription: ssn is a string
    '''
    if len(ssn) != 11:
        return False
    if ssn[0:3].isdigit() and ssn[4:6].isdigit() and ssn[7:].isdigit()\
    and ssn[3] == '-' and ssn[6] == '-'
        return True
    else:
        return False
    
