
import pandas as pd
file = pd.read_table(r"C:\Users\user\Desktop\pass.txt")

#print(file.head())
#print(file.columns)

file = file.where(file['password'].str.len() >= 8 , ).dropna()
#print(len(file))

with open('passwords.txt','w',encoding='utf-8') as f:
    for i in file['password']:
        f.write(f'{i}\n')
    f.close()
    print('done ...')

'''
From 233535 password into 170499 ,
After filtered all passwords from passwords which have length shorter than 8 .

example:
    
    1234asd  : it will remove from file becouse has length 7.
    abdulla123 : it will not remove this word from file becouse has lenght 10 .

'''