#Plotting Wuhan corona virus cases in order to check for outliers.
#v.1 2020/2/4
#Armani Chien

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Read csv file
df=pd.read_csv('WuhanDb.csv')
#print(df)

#check summary
dfDesc=df.describe()
#print(dfDesc)
#print(df.min())
#print(df.max())
#print(df.mean())

#Obtain top & last 5 of the data
#print(df.head(5))
#print(df.tail(5))

#Obtain random sample
#print(df.sample(5))

#Transpose - flipping the rows and columns
#print(df.T)


#sorting by the column & arranging the rows according
#print(df.sort_values(by="Province"))

#Taking values
#print(df.isnull().sum())
df1 = df[['Province','Confirmed']]

#getting rid of the first row
df1 = df1[1:]
#print(df1)

#plotting with Pandas
df1.plot(kind='bar',x='Province',y='Confirmed', title='Confirmed Cases vs. Provinces')
plt.show()


dfChina = df1[0:34]
#print(dfChina)
df2 = df1.sort_values(by="Province")
dfNotChina = df1[36:]
#print(dfNotChina)

#plotting with seaborn
ax = sns.barplot(x="Province",
                 y="Confirmed",
                 data=df1)
plt.title('Confirmed Cases vs. Provinces')
plt.show()

#Plotting all cases in China
ax = sns.barplot(x="Province",
                 y="Confirmed",
                 data=dfChina)
plt.title('Confirmed Cases vs. Provinces in China')
plt.show()

#Plotting all cases not in China
ax = sns.barplot(x="Province",
                 y="Confirmed",
                 data=dfNotChina)
plt.title('Confirmed Cases vs. Province/Countries not in China')
plt.show()


#Adding up all cities in China into the China category
dfChinaSum = dfChina.sum().rename('Confirmed').reset_index()
dfChinaSum = dfChinaSum[1:]
dfChinaSum = dfChinaSum.loc[:,['Confirmed']]
dfChinaSum.insert(loc=0, column='Province', value='China')
#print(dfChinaSum)

ConcatCountries = pd.concat([dfChinaSum, dfNotChina], sort=False, ignore_index=True)
#print(ConcatCountries)
#Plotting The Concat'd dataframe
dfNotChinaDescending = dfNotChina.sort_values(by="Confirmed",ascending=False)
ax = sns.barplot(x="Province",
                 y="Confirmed",
                 data=ConcatCountries)
plt.title('Confirmed Cases vs. Countries')
plt.show()

#Combining cases in all countries that is not in China

dfNotChinaSum = dfNotChina.sum().rename('Confirmed').reset_index() #Taking the sum of all cases that are not in China and it caused the country names to add up
dfNotChinaSum = dfNotChinaSum.loc[:,['Confirmed']] #Taking out column titled index
dfNotChinaSum = dfNotChinaSum.drop(dfNotChinaSum.index[0]) #Taking out row index 0
dfNotChinaSum = dfNotChinaSum.reset_index() #Reseting index
dfNotChinaSum = dfNotChinaSum.loc[:,['Confirmed']] #deleting the messed up column titled index
dfNotChinaSum.insert(loc=0, column='Province', value='OutsideOfChina') #Adding a column for provinces since everything but cases count was removed
print(dfNotChinaSum)

#Joining NotChina and China into one data frame to plot with seaborn
ConcatCountries = pd.concat([dfChinaSum, dfNotChinaSum], sort=False, ignore_index=True)

#Plotting with seaborn
dfNotChinaDescending = dfNotChina.sort_values(by="Confirmed",ascending=False)
ax = sns.barplot(x="Province",
                 y="Confirmed",
                 data=ConcatCountries)
plt.show()
print(ConcatCountries)