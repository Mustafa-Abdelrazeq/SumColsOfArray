import numpy as np
import GenerateKeys as gK
import pandas as pd



def CreateArray (NumberOFIndex):
    Arr_Emp = np.random.randint(1,100 , NumberOFIndex)

    return Arr_Emp
NumberOFIndex = gK.HowManyKeys('Enter How Many Index in Array : ')

def AddedKeysInArray (Arr_Emp , SearchNumber):
    if SearchNumber in Arr_Emp:
        for i in range(len(Arr_Emp)):
            if  Arr_Emp[i]== SearchNumber :
                print(f'{Arr_Emp}\nyour Number place in Array in {i+1}')
                return i 
    else :
        return 'This Number Not in Array.'
    

if __name__ == 'main':
    SearchNumber = gK.HowManyKeys('Enter Number To Search in array  : ')
    print(AddedKeysInArray (CreateArray (NumberOFIndex) , SearchNumber))
