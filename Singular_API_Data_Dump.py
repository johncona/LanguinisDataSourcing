# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:59:08 2015
@author: Andrew
"""

from datetime import datetime, timedelta, time
import requests
import date_check
import datetime

################################################################################################

full_current_date = datetime.datetime.utcnow()
full_yest_date = full_current_date + datetime.timedelta(days=-1)

################################################################################################

#API Details
API_KEY = "53194788c8bc002025b993dd703cab6c5928e6990a3111e0175f98add69f99db"

################################################################################################

csv_file = "C:\Users\Giordano\Dropbox (Tilting Point)\Product\Data Dump\Languinis\languinis_singular_data.csv"

d_name = 'date'

################################################################################################

def singular_app_dump(API_KEY,start_date,end_date):
    global sing_json
    url = "https://www.singular.net/api/" + API_KEY + "/adv/stats/"+ start_date + "/" + end_date
    r = requests.get(url)
    sing_json = r.json()
    return sing_json

def parse_sing_json(data,file_name):
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

date_check.date_check(csv_file,d_name,full_yest_date)
singular_app_dump(API_KEY,date_check.dateMin,date_check.dateMax)
parse_sing_json(sing_json,csv_file)