MyList = [30 ,40,30,50,20,90,20,80,90,20,60]

def DistinctArray (OriginalArray):
    NewArray = []

    for i in OriginalArray:
        if not i in NewArray:
            NewArray.append(i)
    return NewArray
print(DistinctArray(MyList))
