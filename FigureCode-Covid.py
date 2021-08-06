"""
Created on Tue May  4 16:18:30 2021
@author: ziqin

This is the main part
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from CovidCasesRecord import CovidCasesRecord


country=["Japan"]#enter the countries you want to check within 7

cases=list()
for i in range(len(country)):
    country_i=country[i]
    CCR=CovidCasesRecord(country_i)
    cases_i=CCR.retrieve_daily(country_i)#Change the function if you want get other kinds of data
    cases.append(cases_i)
    

#make up a figure
fig=plt.figure(figsize=(18,6),dpi=900)
ax=fig.add_subplot(111)

COLORS=['r','g','b','aqua','c','m','y']#add more color options if you want check more than 7 countries
COLORS0=['coral','forestgreen','navy','darkcyan','indigo','dimgrey','goldenrod']
"""
This is the part for statistics of total and daily cases
"""


off_y=np.zeros(len(cases[0]))
index=cases[0].T.index

if len(country)>1:
    for i in range(len(country)):
        print(1)
        q=cases[i].T
        q.columns=[country[i]]
        t=pd.Series(q[country[i]].values,index=index)
        plt.bar(index,t,bottom=off_y,label=country[i],color=COLORS[i],width=1,alpha=0.3)
        add_y=t
        off_y=off_y+add_y
else:
    q=cases[0].T
    q.columns=[country[0]]
    t=pd.Series(q[country[0]].values,index=index)
    plt.bar(index,t,bottom=off_y,label=country[0],color=COLORS[0],width=1,alpha=1)

plt.xlabel("Date",fontsize=20)
plt.ylabel("Daily Confirmed Cases",fontsize=20)



"""
This is the part for statistics of death rate and recovered rate
"""
"""

index=cases[0].T.index

if len(country)>1:
    for i in range(len(country)):
        print(1)
        q=cases[i].T
        q.columns=[country[i]]
        t=pd.Series(q[country[i]].values,index=index)
        plt.plot(index,t,label=country[i],color=COLORS[i],alpha=1)
        
else:
    q=cases[0].T
    q.columns=[country[0]]
    t=pd.Series(q[country[0]].values,index=index)
    plt.plot(index,t,label=country[0],color=COLORS[0],alpha=1)

plt.xlabel("Date",fontsize=20)
plt.ylabel("Death Rate of Covid-19",fontsize=20)

"""

"""
This is the plot of infect rate of total population per capita
"""


infect=list()
for i in range(len(country)):
    country_i=country[i]
    CCR=CovidCasesRecord(country_i)
    infect_i=CCR.retrieve_infect_rate(country_i)
    infect.append(infect_i)

ax0=ax.twinx()

s=infect[0].T
for i in range(len(country)):
    s=infect[i].T
    plt.plot(index,s,label=country[i],color=COLORS0[i],alpha=1)
    

ax0.legend(loc='lower left')




"""
This is a plot and ticks part for all the objectives
"""


ax.legend(loc='upper left')
plt.grid(':',alpha=0.5)

locator=mdates.AutoDateLocator()
formatter=mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
#ax.xaxis.set_major_formatter(formatter)


#locator=mdates.MonthLocator()
#formatter=mdates.ConciseDateFormatter(locator)
#ax.xaxis.set_major_locator(locator)
#ax.xaxis.set_major_formatter(formatter)






#dayseries=pd.date_range('20200122',periods=cases_i.shape[1],freq='D')

