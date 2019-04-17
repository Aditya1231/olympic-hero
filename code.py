# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data = pd.read_csv(path)
data = data.rename(columns = {'Total':'Total_Medals'})
data.head(10)
#Code starts here



# --------------
#Code starts here

choice = ['Summer','Winter','Both']
#data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
#data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'both',data['Better_Event'])
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],
'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
better_event = data['Better_Event'].value_counts().keys().tolist()[0]
print(better_event)


# --------------
#Code starts here
top_countries = pd.DataFrame(data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']])

#print(top_countries['Total_Medals'])

top_countries=top_countries[:-1]

def top_ten(data,col):
    country_list = []
    #demo = df.nlargest(10,col)
    #country_list = list(df['Country_Name'])
    country_list = list((data.nlargest(10,col)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10_summer)
print(top_10_winter)
print(top_10)

s1 = set(top_10_summer)
s2 = set(top_10_winter)
s3 = set(top_10)

set1 = s1.intersection(s2)
result_set = set1.intersection(s3)
common = list(result_set)
print(common)


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

print(type(summer_df))
print(type(winter_df))
print(type(top_df))

summer_df.plot(x='Country_Name',y='Total_Summer',kind='bar')
winter_df.plot(x='Country_Name',y='Total_Winter',kind='bar')
top_df.plot(x='Country_Name',y='Total_Medals',kind='bar')





# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name'] 
print(summer_max_ratio)
print(summer_country_gold)
#print(summer_df)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name'] 
print(winter_max_ratio)
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name'] 
print(top_max_ratio)
print(top_country_gold)




# --------------
#Code starts here
data_1 = data.drop(data.index[-1])

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total'] * 1


print(data_1['Total_Points'])
most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here

best = data[data['Country_Name']==best_country]
#print(best)

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


