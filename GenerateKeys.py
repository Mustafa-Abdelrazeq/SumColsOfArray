import random 
import string


def HowManyKeys(Msg):
    while True :
        try:
            Keys_mum = int(input(Msg))
            if Keys_mum > 0 :
                return Keys_mum
        except:
            print("Please Enter Numbers : ")
# HowManyKeys('Enter How Many Keys You Want : ')

def Key ():
    ListOFRandomLetters =[]
    for i in range (4):
        Letters = string.ascii_uppercase
        KeyPart = "".join(random.choices(Letters , k=4)) 
        ListOFRandomLetters.append(KeyPart)

    return "-".join(ListOFRandomLetters)

def CreatedSerials ():
    NumberOFSerials = HowManyKeys('Enter How Many Keys You Want : ')
    for i in range(NumberOFSerials):
       print( Key ())
# CreatedSerials()

