# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:24:25 2015

@author: Giordano
"""

import mixpanel_api

api_key = "122d4943394fb9d73f00c8a4b7e69723"
secret_key = "68d1c606da4b0e3180b6907b85092ab1"

#https://mixpanel.com/docs/api-documentation/data-export-api#libs-python

mp_connection = mixpanel_api.Mixpanel(api_key,secret_key)

units = 'day'
intervals = 90
types = ["unique","general"]

events = ['Install']#, 'First Time Launch','User: Facebook Login']#,'User: New Session', 'Tutorial Completion Event', 'Sent Crash Log', 'Liked Game', 'Facebook Request Sent','Facebook Request Failed', 'Collected Daily Reward','IAP: Buy 10 Coins Success', 'IAP: Buy 20 Coins Success','IAP: Buy 55 Coins Success','IAP: Buy 110 Coins Success','IAP: Buy 220 Coins Success','IAP: Buy 560 Coins Success','IAP: Buy Unlock Gate Success']

csv_base = '"C:\Users\Giordano\Dropbox (Tilting Point)\Product\Data Dump\Languinis\\Languinis_Event_Data_'

for t in types:
    #run through the request 
    methods = ['events']
    payload = {'event' : events,'unit' : units,'interval' : intervals,'type': t}
    mp_connection.request(methods, payload)
    df = json_normalize(data['data']['values'])
    df = df.from_dict(data['data']['values']) # puts the data into a dataframe
    df.to_csv(csv_base+t+'.csv')