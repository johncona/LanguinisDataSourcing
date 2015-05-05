# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:52:04 2015 @author: Andrew
"""

import requests
import pandas as pd
import datetime
import date_check

################################################################################################

full_current_date = datetime.datetime.utcnow()
full_yest_date = full_current_date + datetime.timedelta(days=-1)

################################################################################################

#Connect to Chartboost API
#https://dashboard.chartboost.com/login?redirect=%2Ftools%2Fapi

ID = "5488d70843150f50b61b62dc"
USIG = "4bee1ae43cf18f19f42ea3f30288767beea6140d"

file_name = "C:\Users\Giordano\Dropbox (Tilting Point)\Product\Data Dump\Languinis\\chartboost_output.csv"

c_name = 'dt'

################################################################################################

def chartboost_app_dump(ID,USIG,dateMin,dateMax):
    global cb_json
    if dateMin == "":
        cb_json = ""
    else:
        url = "https://analytics.chartboost.com/v3/metrics/app?dateMin=" + dateMin + "&dateMax=" + dateMax + "&userId=" + ID + "&userSignature=" + USIG
        r = requests.get(url)
        cb_json = r.json()
    return cb_json

def parse_cb_json(data,file_name):
    if data == "":
        pass
    else:
        import json
        from pandas.io.json import json_normalize
        json_file = 'data.json'
        
        with open(json_file, 'a') as outfile:
            json.dump(data[0], outfile)
                
        #Provides a normalized JSON response from Mixpanels data
        df = json_normalize(data)
        
        with open(file_name, 'a') as f:
            df.to_csv(f, header=False)
        
        #Puts the data in the dataframe - Only for first loop for an application
        #df.to_csv(csv_file, encoding='utf-8')

date_check.date_check(file_name,c_name,full_yest_date)
chartboost_app_dump(ID,USIG,date_check.dateMin,date_check.dateMax)
parse_cb_json(cb_json,file_name)