# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:32:11 2015
@author: Andrew
"""
import pandas as pd
import datetime

###############################################################################

full_current_date = datetime.datetime.utcnow()
full_yest_date = full_current_date + datetime.timedelta(days=-1)

###############################################################################

def date_check(file_n,c_name,full_yest_date):
    global dateMin, dateMax
    try:
        #Find the max date in the file
        df = pd.read_csv(file_n)
        max_date = df[c_name].max()
        a = df[c_name].unique()
        if len(a) == 0:
            max_date_obj = full_current_date.strftime("20%y-%m-%d") #NEED TO FIX THIS LOGIC
        else:
            max_date_obj = datetime.datetime.strptime(max_date, "20%y-%m-%d")
    except ValueError:
        max_date_obj = full_current_date.strftime("20%y-%m-%d") 
        pass
    #Find yesterdays date    
    ydate = full_yest_date.strftime("20%y-%m-%d")
    
    #identify the min and max dates in the file
    if max_date_obj >= max_date_obj:
        max_date_obj = datetime.datetime.strptime(max_date_obj, "20%y-%m-%d")
        it_date = max_date_obj + datetime.timedelta(days=+1)
        if it_date == full_yest_date:
            dateMin = ydate
            dateMax = ydate
        elif it_date > full_yest_date:
            dateMin=""
            dateMax=""
        else:
            dateMin = it_date.strftime("20%y-%m-%d")
            dateMax = ydate
    elif max_date_obj == None: #NEED TO FIX THIS LOGIC
        dateMin = ydate
        dateMax = ydate
    else:
        print "ISSUE"
        dateMin, dateMax = 0, 0
    return dateMin, dateMax
    
###############################################################################