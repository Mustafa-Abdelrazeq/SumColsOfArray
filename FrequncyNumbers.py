def UserInput(Msg):
    while True:
        try:
            num = int(input(Msg))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def FrequqncyOFNumber(number , FrqNumber):
    itrator = 1
    Count = 0
    dictionary = {}
    for i in number:
        if i == FrqNumber:
            Count+=itrator
        # if i in dictionary.keys() :
        #     dictionary[i] += itrator
        # else:
        #     dictionary[i] = itrator


    return Count
# UserInputVar = UserInput("Enter Your Number : ")
# SearchNumber = UserInput("Enter The Number For Count it's Frequancy.: ")
# print(FrequqncyOFNumber(UserInputVar , SearchNumber))

#----------------------------------------------------------------
# Another Solution

def FrequqncyOFNumberAnotherSolution(number , FrqNumber):
    remainder = 0
    count = 0
    while number > 0:
        remainder = number % 10
        number = number // 10
        print(number)
        if FrqNumber == remainder:
            count+=1
        
    return count
UserInputVar = UserInput("Enter Your Number : ")
SearchNumber = UserInput("Enter The Number For Count it's Frequancy.: ")
print(FrequqncyOFNumberAnotherSolution(UserInputVar , SearchNumber))


