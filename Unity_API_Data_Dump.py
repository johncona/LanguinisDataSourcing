# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:59:08 2015

@author: Giordano
"""

from datetime import datetime, timedelta, time
import date_check
import json_to_csv
import datetime

################################################################################################

full_current_date = datetime.datetime.utcnow()
full_yest_date = full_current_date + datetime.timedelta(days=-1)

API_KEY = "1a45eb16b4c44b10d4dae71a104da73be1efa707b4f36a9f67ce10050d68428e"
csv_file = "C:\Users\Giordano\Dropbox (Tilting Point)\Product\Data Dump\Languinis\\languinis_unity_data.csv"
d_name = 'Date'

################################################################################################

def unity_app_dump(API_KEY,start_date,end_date):
    import requests
    global unity_json
    #Statistics API
    #http://unityads.unity3d.com/help/Documentation%20for%20Publishers/Statistics-API-for-monetisation
    #Request Format:
    #http://gameads-admin.applifier.com/stats/monetization-api?apikey=<apikey>&fields=<fields>[&splitBy=<splitbyfields>][&scale=<scale>][&start=<startDate>][&end=<endDate>][&sourceIds=<sourceIds>]
    fields = 'revenue,views,started,adrequests,available,offers'    
    url = "http://gameads-admin.applifier.com/stats/monetization-api?" + API_KEY + "/adv/stats/"+ start_date + "/" + end_date
    payload = {"apikey":API_KEY,"fields":fields,"startdate":start_date,"enddate":end_date}    
    r =requests.get(url,params=payload)
    untiy_json = r.json()
    return unity_json

date_check.date_check(csv_file,d_name,full_yest_date)
unity_app_dump(API_KEY,date_check.dateMin,date_check.dateMax)
#unity_app_dump(API_KEY,"2015-03-28","2015-03-30")
json_to_csv.json_to_csv(untiy_json,csv_file)