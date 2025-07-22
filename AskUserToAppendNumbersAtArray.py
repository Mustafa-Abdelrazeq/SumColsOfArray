import numpy as np

def CreateNumber (Msg):
    while True :
        try :
            number = int(input(Msg))
            return int(number)
        except ValueError :
                print('Wrong Number ')
            

# CreateNumber('Please Enter Number : ')

def AskUserToContinueOrBreak():
    answer =  int(input('Do You Want Append Number\nTo Array Press 1 : '))
    return answer

def AppendNumberAtList():
    EmptyList = []
    while AskUserToContinueOrBreak() == 1:
        Num = CreateNumber('Please Enter Number : ')
        EmptyList.append(Num)
    return f'The Len Of Your Array is ({len(EmptyList)}) \nAnd It Is Your Array {EmptyList}\n'
        
print(AppendNumberAtList())