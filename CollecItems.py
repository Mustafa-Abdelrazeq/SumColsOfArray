import os , shutil
import pandas as pd
from tqdm import tqdm
ExcelPath =r'C:\Users\Mustafa\Desktop\Failed.xlsx'
excel = pd.read_excel(ExcelPath)
orginalPath = r'D:\\'
def CollectItems(orginalPath , excel):
    ListColumn = excel.to_list()
    for Path , Dir , Files in tqdm(os.walk(orginalPath)):
        # print(Path)
        # print(Dir)
        # print(File)
        
        for SearchInFile in ListColumn[:] :
            for file in Files:
                if SearchInFile.lower() == file.lower():
                    os.makedirs(orginalPath+ 'FailedFiles',exist_ok=True )
                    JoiningPath = os.path.join(Path , SearchInFile)
                    shutil.copy (JoiningPath , orginalPath+'FailedFiles')
                    print(SearchInFile)
                    ListColumn.remove(SearchInFile)
    print('Done')
    return pd.DataFrame(ListColumn).to_excel(ExcelPath)
CollectItems(orginalPath , excel[0])


