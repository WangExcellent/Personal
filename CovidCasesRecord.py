
"""
this is the module part named as Covid_Cases_Record
relative functions:
    total cases : retrieve_cases
    daily new cases: retrieve_daily
    death rate: retrieve_death_rate
    recovered rate: retrieve_recovered_rate

"""


import pandas as pd


class CovidCasesRecord():
    def __init__(self,country_i):
        self.country_i=country_i
        self.state=None
        self.Lat=None
        self.Long=None
        if self.country_i=="Australia":
            self.state=["Australian Capital Territory","New South Wales","Northern Territory","Queensland","South Australia","Tasmania","Victoria","Western Australia"]
        if self.country_i=="Canada":
            self.state=["Alberta","British Columbia","Diamond Princess","Grand Princess","Manitoba","New Brunswick","Newfoundland and Labrador","Northwest Territories","Nova Scotia","Nunavut","Ontario","Prince Edward Island","Quebec","Repatriated Travellers","Saskatchewan","Yukon"]
        if self.country_i=="China":
            self.state=["Anhui","Beijing","Chongqing","Fujian","Gansu","Guangdong","Guangxi","Guizhou","Hainan","Hebei","Heilongjiang","Henan","Hong Kong","Hubei","Hunan","Inner Mongolia","Jiangsu","Jiangxi","Jilin","Liaoning","Macau","Ningxia","Qinghai","Shaanxi","Shandong","Shanghai","Shanxi","Sichuan","Tianjin","Tibet","Unknown","Xinjiang","Yunnan","Zhejiang"]
        if self.country_i=="Denmark":
            self.state=["Faroe Islands","Greenland"]
        if self.country_i=="France":
            self.state=["French Guiana","French Polynesia","Guadeloupe","Martinique","Mayotte","New Caledonia","Reunion","Saint Barthelemy","Saint Pierre and Miquelon","St Martin","Wallis and Futuna"]
        if self.country_i=="Netherlands":
            self.state=["Aruba","Bonaire, Sint Eustatius and Saba","Curacao","Sint Maarten"]
        if self.country_i=="United Kingdom":
            self.state=["Anguilla","Bermuda","British Virgin Islands","Cayman Islands","Channel Islands","Falkland Islands (Malvinas)","Gibraltar","Isle of Man","Montserrat","Saint Helena, Ascension and Tristan da Cunha","Turks and Caicos Islands"]
            
    def retrieve_cases(self,country_i):
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' 
        df=pd.read_csv(url) 
        
        #Group up all the cases in different states within one country
        df=df.drop(['Province/State','Lat','Long'],axis=1)
        df0=df.drop(['Country/Region'],axis=1)
        col_name=df0.columns.values.tolist()
        ddf=df.groupby("Country/Region")[col_name].sum()
        
        output=ddf[ddf.index==self.country_i]
        return output
        
    def retrieve_daily(self,country_i):
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' 
        df=pd.read_csv(url) 
        
        #Group up all the cases in different states within one country
        df=df.drop(['Province/State','Lat','Long'],axis=1)
        #group and give it a name of columns for new dataframe
        df0=df.drop(['Country/Region'],axis=1)
        col_name=df0.columns.values.tolist()
        ddf=df.groupby("Country/Region")[col_name].sum()
        
        dddf=ddf[ddf.index==self.country_i]
        daily=ddf[ddf.index==self.country_i]
        for n in range(dddf.shape[1]-1):
            for i in range(dddf.shape[0]):
                confirm=dddf.iloc[i,n+1]-dddf.iloc[i,n]
                daily.iloc[i,n+1]=confirm
        
        output=daily
        return output
    
    def retrieve_death_rate(self,country_i):
        CCR=CovidCasesRecord(self.country_i)
        cases_i=CCR.retrieve_cases(self.country_i)
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv' 
        df=pd.read_csv(url)
        df=df.drop(['Province/State','Lat','Long'],axis=1)
        #group and give it a name of columns for new dataframe
        df0=df.drop(['Country/Region'],axis=1)
        col_name=df0.columns.values.tolist()
        death_cases=df.groupby("Country/Region")[col_name].sum()
        
        ddf=death_cases[death_cases.index==self.country_i]
        death_rate=death_cases[death_cases.index==self.country_i]
        
        for n in range(ddf.shape[1]-1):
            for i in range(ddf.shape[0]):
                rate=ddf.iloc[i,n]/cases_i.iloc[i,n]
                death_rate.iloc[i,n+1]=rate
                
        output=death_rate.drop(['1/22/20'],axis=1)
        return output
    
    def retrieve_recovered_rate(self,country):
        CCR=CovidCasesRecord(self.country_i)
        cases_i=CCR.retrieve_cases(self.country_i)
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv' 
        df=pd.read_csv(url)
        df=df.drop(['Province/State','Lat','Long'],axis=1)
        #group and give it a name of columns for new dataframe
        df0=df.drop(['Country/Region'],axis=1)
        col_name=df0.columns.values.tolist()
        recovered_cases=df.groupby("Country/Region")[col_name].sum()
        
        ddf=recovered_cases[recovered_cases.index==self.country_i]
        recovered_rate=recovered_cases[recovered_cases.index==self.country_i]
        
        for n in range(ddf.shape[1]-1):
            for i in range(ddf.shape[0]):
                rate=ddf.iloc[i,n]/cases_i.iloc[i,n]
                recovered_rate.iloc[i,n+1]=rate
                
        output=recovered_rate.drop(['1/22/20'],axis=1)
        return output
    
    def retrieve_infect_rate(self,country_i):
        pop=pd.read_csv("population_2018.csv")
        CCR=CovidCasesRecord(self.country_i)
        cases_i=CCR.retrieve_cases(self.country_i)
        a=0
        for n in range(pop.shape[0]):
            if pop.iloc[n,0]==self.country_i:
                a=n
        poptotal=pop.iloc[a,1]
        infect_rate=cases_i/poptotal
        
        output=infect_rate
        return output
        
        