def UserName (Msg):
    UserName = input (Msg)
    return UserName

def CaseStatue():
    return input('\nFor Create Password Enter 1 \nFor Reset Password Enter  2 : ')

def CheckingOFUserInput ():
    while True :
        try:
            ChooseUser = CaseStatue()
            if int(ChooseUser) == 1:
                NumberOfChars = 3
                return NumberOfChars
            elif int(ChooseUser) == 2:
                NumberOfChars = -3
                return NumberOfChars
        except:
             ChooseUser

def EncryptName ():
    NumberOFStepsChars = CheckingOFUserInput ()
    Name = UserName ("Please Enter Your Name : ")
    EncryptedName = ''    
    for  char in Name:
        EncryptedName  +=  chr(ord(char) + NumberOFStepsChars) 
    return EncryptedName
print(EncryptName ())


