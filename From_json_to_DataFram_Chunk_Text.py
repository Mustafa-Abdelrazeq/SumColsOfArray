
from datetime import datetime
from tqdm import tqdm
import numpy as np
import json
import os
import re
import pandas as pd 


print("Note :\nExcel can't Save the Large Text Completely.")
path = input('Enter The Directory of json Files like D:\\json_files\\Content2 : ').strip() 
path+= '\\'
SaveDir = input('Enter The Directory want to Save Excel Sheet  : ').strip() 
NameOFExcel = input('Enter Name OF Excel : ').strip() .strip() 

EmptyList = []
# List For encrypted json file 
encrypted = []
for i in os.listdir(path):
    try:
        if i.endswith('.json'):
            with open (path + i , 'r' ,encoding='utf-8-sig') as f:
                df = json.load(f)
                EmptyList.append(df)
                
    except :
        encrypted.append(i)

##################################################################
# Normalization Functions 

def normalizing_text (x) :
    x =  re.sub(r'[ٱأإآٱ]' , 'ا', x)
    x = re.sub(r'[!#$%&"()*+\-/.,:،;؛؟٠<=>?@[\]^_`{|}~ًٌٍَُِّْ]', '', x)
    return x.replace('ة' , 'ه').replace('ى','ي').replace('\n' , ' ').replace('  ' , ' ')


def rmv_One_char_En (phrase):
    new_phrase =  re.sub(r'[^\u0600-\u06FF\s]' , '' , phrase)
#     new_phrase =  re.sub(r'[\u0660-\u0669]' , '' , new_phrase)
    return ' '.join([i for i in  new_phrase.split() if len(i) > 1 ])

# Function To Call Last 2 Function
def allFuncHandling (x):
    return normalizing_text(rmv_One_char_En (x))
    
###################################################################
# Empty DataFrame to Use
df = pd.DataFrame()

df['Text'] = [[EmptyList[i]['pages_full_text'][x]['full_text'] for x in range(len(EmptyList[i]['pages_full_text']))] for i in tqdm(range(len(EmptyList)))]
df['document_id'] =  [EmptyList[i]['document_id'] for i in tqdm(range(len(EmptyList)))]
df['document_title'] =  [EmptyList[i]['document_title'] for i in tqdm(range(len(EmptyList)))]



df['Text'] = [allFuncHandling(' '.join(df['Text'][i]))for i in tqdm(range(len(df)))]

# LEngth Of Txt As a Chars 
df['Len_Full_txt'] = [len(i) for i in df['Text']]


def Creating_Chunks_Text (Full_Text):
    Splited_number = 3
#   Number Of Words From Last Chunk
    Num_w = 5
    df['Text_intro'] = [' '.join(i.split()[:int(len(i.split())/Splited_number) ]) for i in df[Full_Text] ]
    df['Text_Midel'] = [' '.join(i.split()[int(len(i.split())/Splited_number) - Num_w :int(len(i.split())/Splited_number) * 2 ]) for i in df[Full_Text] ]
    df['Text_Last'] = [' '.join(i.split()[(int(len(i.split())/Splited_number) * 2 ) - Num_w : ] ) for i in df[Full_Text] ]
    
    list_OF_Size = [300,500,1000,1500,2000]
    for Chunk_name in list_OF_Size:
        df[f'Text_intro_{Chunk_name}'] = [' '.join(i.split()[:Chunk_name]) for i in df['Text_intro']]
        df[f'Text_Midel_{Chunk_name}'] = [' '.join(i.split()[:Chunk_name]) for i in df['Text_Midel']]
        df[f'Text_Last_{Chunk_name}']  = [' '.join(i.split()[:Chunk_name]) for i in df['Text_Last']]
        
#         . in Concate Chunks To Help Us Know The End And Start for Chunks
        df[f'SmE_{Chunk_name}'] = df.apply(
        lambda row: ' '.join(row[f'Text_intro_{Chunk_name}'].split()[:int(np.ceil(Chunk_name/Splited_number))]) + ' . ' + 
                    ' '.join(row[f'Text_Midel_{Chunk_name}'].split()[:int(np.ceil(Chunk_name/Splited_number))]) + ' . ' + 
                    ' '.join(row[f'Text_Last_{Chunk_name}'].split()[:int(np.floor(Chunk_name/Splited_number))]),
        axis=1
    )


Creating_Chunks_Text ('Text')

################################################################################################################################
                                            #this Section Able To Provide The Full Text                                        
                                            #Not necessary  
    
# To Save Full Text in Columns => Cause of the Cell in Excel Can't Save Large Text 
# Then we Can Save Some Of sequence Text in a Different Cells

# char_num = 32750                                                                                                            
                                                                                                                             
# Range = int(np.ceil(df['Len_Full_txt'].max()/char_num))

# for chunk in range(1,Range + 1):
# Sort char_num Of Chars at Columns and Get the Previous 20 Chars To underStanding the Context
#     df[f'Text_{chunk}_chunk'] = [ i[(char_num * (chunk -1 ) ) : char_num * (chunk) ] for i in df['Text']]
#     Len OF Chars at the Chunks Columns 
#     df[f'LEn-Text(_{chunk}_chunk)'] = [ len(i) for i in df[f'Text_{chunk}_chunk']]

# Get Only Chunks Columns LEn To Sum them 
# To Verify the OF Length if We Want 
# Chunk_col_len = df.filter(like='LEn-Text')

# df['SumLEn'] = Chunk_col_len.sum( axis=1 )
# df['Aleady_Full_Text'] = [True if x == y else False for x , y in zip(df['SumLEn'] ,df['Len_Full_txt'])]
################################################################################################################################
# Droping the txt Cause OF the Excel Can't Save it Completely 

# df.drop(['Text' , 'Text_intro','Text_Midel','Text_Last'],axis=1,inplace=True)


now = datetime.now() 
full_date = now.strftime("%I-%d-%m-%y %a %p")


df.to_excel(f'{SaveDir}\\{NameOFExcel}-{full_date}.xlsx')

#To Give us Some Information  of The encrypted Jsons
if len(encrypted) > 0 :
    print(f'Found encrypted Files Have Name : ')
    print('__________________________________')
    for enc in encrypted:
        print(enc)
    print(f'You have {len(encrypted)} encrypted Files ')
print()
print('Done'.center(100,'-'))

