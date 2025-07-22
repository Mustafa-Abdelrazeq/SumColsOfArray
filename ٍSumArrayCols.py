import numpy as np 

RandomArray = np.random.randint(1,9 , (3,3))


def SumColsFromArray (RandomArray):
    # Show Array At First
    print('Your Array is : \n',RandomArray,'\n')
    # assumed [i] will be cols so (RandomArray.shape[1])
    for col in range(RandomArray.shape[1]):
        # position of [SumCol] after first loop to reset to zero for each loop
        SumCol = 0
        # assumed [i] will be cols so (RandomArray.shape[1])
        for row in range (RandomArray.shape[0]):
            SumCol+=RandomArray[row][col] 
            # print(RandomArray[x][i] )

        print(f'This is Sum of [{col+1}] Column is : {SumCol}')
SumColsFromArray (RandomArray)