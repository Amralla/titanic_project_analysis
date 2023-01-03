import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
# read file
data= pd.read_excel("csvFile/titanic.xls")
print(data.head())
# shape of data
print(data.shape)
# name of column or feature 
print(data.columns)
# information of data  data_type and num_value
print(data.info())
# you shoud know difrience between numerical and catogerical 
print(data.describe())
# clean data 
data.drop(['fare','home.dest','name'],axis=1,inplace=True)
data['age'].fillna(0,inplace=True) 
#histogram
data.hist(figsize=(5,5))
plt.show()
# outliers 
df_copy=data.copy()
df_copy.iloc[0:10,3]=500
print(df_copy.head(10))
# histogram in outlier
df_copy.hist()
plt.show()
# in age have outlier
print(df_copy[df_copy['age']>100]['age'].index)
# drop outlier
df_copy.drop(df_copy[df_copy['age']>100]['age'].index,inplace=True)
#histogrm after delete outlier 
df_copy.hist()
plt.show()
#shape after outlier
print(df_copy.shape)
# nymber of value and repetitive
print(df_copy['sex'].value_counts())
# value without repetitive
print(df_copy['sex'].unique())
gender=df_copy[df_copy['sex']=='male']
print(gender)
survived=gender[gender['survived']==1]
print(survived.shape)
#print(df_copy[df_copy['survived']==1])
# the number of survived of male!
precentige=(survived.shape[0]/gender.shape[0])*100
print(round(precentige))
def fun():
    for gen in df_copy['sex'].unique():
        print(gen)
        gender=df_copy[df_copy['sex']==gen]
        survived1=gender[gender['survived']==1]
        precentige1=(survived1.shape[0]/gender.shape[0])*100
        print("the precentige is: {:.2f}".format(precentige1))
        print("\n ==== \n") 
#---------
# survived from pclass
def fun2():
    for pclass in df_copy['pclass'].unique():
        print(pclass)
        div=df_copy[df_copy['pclass']==pclass]
        survived2=div[div['survived']==1]
        precentige2=(survived2.shape[0]/div.shape[0])*100
        print("the surviced of  div is : {:.2f}".format(precentige2))
        print("\n ====\n")
#--------
fun2()

print('/'*60)
df_copy['new_age']=df_copy['age'].copy()
def age_to_catogry(age):
    if age  < 4:
        return 0
    elif age<10:
        return 1
    elif age < 21:
        return 2;
    elif age < 33 :
        return 3
    elif age < 50 :
        return 4
    return 5;

# for i in range(df_copy.shape[0]):
#     df_copy['new_age'].iloc[i]=age_to_catogry(df_copy['age'].iloc[i])
# ======
df_copy['new_age']=df_copy['age'].apply(age_to_catogry)
df_copy['new_age'].hist()
plt.show()

#save data 
#df_copy.to_csv('new_data.csv',sep='\t',encoding='utf8')
pp=pd.read_csv('new_data.csv',sep='\t',encoding='utf8')
print(pp.head())