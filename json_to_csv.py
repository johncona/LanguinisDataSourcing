# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:25:40 2015
@author: Giordano
"""

def json_to_csv(data,file_name,perm):
    try:
        import json
        from pandas.io.json import json_normalize
        json_file = 'data.json'
            
        with open(json_file, perm) as outfile:
            try:
                json.dump(data[0], outfile)
            except KeyError:
                json.dump(data, outfile)
        
        #Provides a normalized JSON response from Mixpanels data
        df = json_normalize(data)
            
        with open(file_name, 'a') as f:
            df.to_csv(f, header=False, encoding='utf-8')
    except IndexError:
        print "IndexError"
        pass