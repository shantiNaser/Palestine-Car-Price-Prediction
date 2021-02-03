# # # To know The number of NAN Row
# # print(df.isnull().sum())
# #
# #
# # nan_value = float("NaN")
# # df.replace("", nan_value, inplace=True)
# # df.dropna(subset = ["Car Name"], inplace=True)
# #
# #
# # print(df.isnull().sum())
# #  # To save the Change
# # df.to_excel("Naser.xlsx")
#
#
import pandas as pd
import re
df = pd.read_csv(r'Naser1.csv')
#
print(df.head())

for index in df.index:
    Str = df.loc[index,'Car Name']
    Str=re.sub(' +', ' ', Str)
    Str = Str.split(" ",1)
    if len(Str)!=2:
        continue
    print(str(index) + " : " + Str[0] + " , " + Str[1])
    df.loc[index,'Car Name']=Str[0]
    df.loc[index, 'Model']=Str[1]
    if index%500 == 0:
        df.to_csv("Naser3.csv")
        print("file ready"+str(index))


df.to_csv("Naser3.csv")
print("final file ready")
