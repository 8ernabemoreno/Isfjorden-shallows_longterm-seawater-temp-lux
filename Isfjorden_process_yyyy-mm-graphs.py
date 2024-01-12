# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:19:30 2023

@author: 8erna
"""
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

## Using S1 shallow (S1s) as example. Adjust path as necessary
df = pd.read_csv(r"D:/BERNATRACIUS/2022/NatureScientificData/Figshare/S1s.csv")

# see first values of the data frame
df.head()

# to know the overall shape of the data frame (e.g., know how many data points there are)
df.shape[0], df.shape[1] 

# use of a vectorised operation. pd.to_datetime converts columns to datetime objects  
# .dt accessor extracts the YYYY, MM and DD in separate columns
# df.dt.tz_localize (GMT-2) converts the original time (which is in GMT+2) to UTC standard time  

df['py_date'] = pd.to_datetime(df['Date']+ ' ' + df['Time_24h(GMT+2)'], format='%d/%m/%Y %H:%M:%S')
df['py_date'] = df['py_date'].dt.tz_localize('Etc/GMT-2').dt.tz_convert('UTC')
df['YYYY'] = df['py_date'].dt.year
df['MM'] = df['py_date'].dt.month
df['DD'] = df['py_date'].dt.day

annual = pd.DataFrame(index=np.arange(17), columns=['YYYY', 'TMax','TAvg','TMin','luxMax', 'luxAvg'])
YYYY = np.arange(2006, 2023, 1)

# Create a loop to obtain annual maxima, means, and minima (for temperature); and annual maxima and means (for light intensity - since minimum is 0 during dark seasons/polar night)
for i in range (17):
    filt = df['YYYY'] == YYYY[i]
    # The == operator compares the value or equality of two objects
    a = df[filt].reset_index()
    annual['YYYY'][i] = YYYY[i]
    annual['TMax'][i] = a['Temperature_C'].max()
    annual['TAvg'][i] = a['Temperature_C'].mean()
    annual['TMin'][i] = a['Temperature_C'].min()
    b = df[filt].reset_index()
    annual['luxMax'][i] = b['Lux'].max()
    annual['luxAvg'][i] = b['Lux'].mean()    

## Save to new .csv file, adjust path as necessary
annual.to_csv(r'D:/BERNATRACIUS/2022/NatureScientificData/Figshare/annualMean_ S1shallow.csv')

## Create a graph of all time series
fig,ax = plt.subplots(figsize=(40,10))
ax.scatter(df['py_date'], df['Temperature_C'],color='black', s=0.1)
ax.set_title('S1 shallow',fontsize=14)
ax.set_ylabel('°C', fontsize=20)
ax.set_xlabel('Date', fontsize=20)

## Create a graph with the monthly means with a line per year   
monthly_avg = df.groupby(['YYYY', 'MM'])['Temperature_C'].mean().reset_index()
fig1, ax = plt.subplots()
for YYYY in monthly_avg['YYYY'].unique():
    year_data = monthly_avg[monthly_avg['YYYY']==YYYY]
    ax.plot(year_data['MM'], year_data['Temperature_C'], label=str(YYYY))
ax.set_xlabel('Month')
ax.set_ylim(-2, 8)
ax.set_ylabel('°C')
ax.legend(loc='best')
plt.show()

## Create monthly maxima (MM_max), average (MM_avg), and minima (MM_min)
MM_max = df.groupby(['YYYY', 'MM'])['Temperature_C'].max().reset_index()
MM_avg = df.groupby(['YYYY', 'MM'])['Temperature_C'].mean().reset_index()
MM_min = df.groupby(['YYYY', 'MM'])['Temperature_C'].min().reset_index()

#Create a list 
MM_max['date'] = pd.to_datetime(MM_max['YYYY'].astype(str)+'-'+MM_max['MM'].astype(str))
MM_avg['date'] = pd.to_datetime(MM_avg['YYYY'].astype(str)+'-'+MM_avg['MM'].astype(str))
MM_min['date'] = pd.to_datetime(MM_min['YYYY'].astype(str)+'-'+MM_min['MM'].astype(str))

## Create a graph with pyplot showing temperature monthly maxima, averages, and minima - by year  
f1, ax = plt.subplots(figsize=(20,5))
ax.plot(MM_max['date'], MM_max['Temperature_C'], color='red', linewidth=0.5, linestyle='-', label="max")
ax.scatter(MM_avg['date'], MM_avg['Temperature_C'],color='black', s=5)
ax.plot(MM_avg['date'], MM_avg['Temperature_C'], color='black', linewidth=1, label="average")
ax.plot(MM_min['date'], MM_min['Temperature_C'], color='blue', linewidth=0.5, label="min")
ax.fill_between(MM_max['date'], MM_max['Temperature_C'], MM_avg['Temperature_C'], color='darkred', alpha=.1, linewidth=0)
ax.fill_between(MM_avg['date'], MM_avg['Temperature_C'], MM_min['Temperature_C'], color='blue', alpha=.1, linewidth=0)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylim(-2, 10)
ax.set_ylabel('°C', fontsize=14)
ax.set_title('monthly avg temperature - S1 shallow ', fontsize=14)

## Set major ticks for years
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.grid(True)
## Set minor ticks for months
ax.xaxis.set_minor_locator(mdates.MonthLocator())
## Set legend 
f1.legend(loc='center right')
## Save figure in high resolution
f1.savefig("S1s_MM-Tavg.jpg", dpi=600)

## Create a graph with pyplot showing light intensity monthly maxima and averages - by year  
MM_maxlux = df.groupby(['YYYY', 'MM'])['Lux'].max().reset_index()
MM_avglux = df.groupby(['YYYY', 'MM'])['Lux'].mean().reset_index()

MM_maxlux['date'] = pd.to_datetime(MM_maxlux['YYYY'].astype(str)+'-'+MM_maxlux['MM'].astype(str))
MM_avglux['date'] = pd.to_datetime(MM_avglux['YYYY'].astype(str)+'-'+MM_avglux['MM'].astype(str))

f2, ax = plt.subplots(figsize=(17,5))
ax.scatter(MM_avglux['date'], MM_avglux['Lux'],color='black', s=5)
ax.plot(MM_avglux['date'], MM_avglux['Lux'], color='black', linewidth=0.5)
ax.set_ylim(0,550)

## Add secondary y-axis 
ax2 = ax.twinx()
ax2.scatter(MM_maxlux['date'], MM_maxlux['Lux'], color='Crimson', s=25)
ax2.tick_params(axis='y')
## Find out the maximum values and set y_limits according to that
ax2.set_ylim(100,5250)

ax.set_title('monthly avg and max lux - S1 shallow', fontsize=14)
ax.set_ylabel('avg lux', fontsize=14)
ax2.set_ylabel('max lux', fontsize=14)

## Set major ticks for years
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.grid(True)

## Set minor ticks for months
ax.xaxis.set_minor_locator(mdates.MonthLocator())

f2.legend(loc='center right')
## Save figure, adjust path as necessary
f2.savefig('D:/BERNATRACIUS/2022/NatureScientificData/Figs/S1s_MM-lux.jpg', dpi=600)  

## Do the same with other datasets...