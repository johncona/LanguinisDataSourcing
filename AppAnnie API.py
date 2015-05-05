#AppAnnie API Key: 

#Documentation: http://support.appannie.com/categories/20082753-Analytics-API
#1000 calls per day
#30 calls per minute

import json, requests, time
import json_to_csv

k = '95dad7eb17d7976acd353014aa833099b650f42f'
startDate = "2014-09-10"
endDate = startDate

def app_annie_accounts():
    global accounts
    #http://support.appannie.com/hc/en-us/articles/204208994-1-Account-Connections-List
    #Get the Account_IDs associated with the account
    url = 'http://api.appannie.com/v1.2/accounts?'
    payload = {'page_index': '0'}
    headers = {'Accept': 'application/json', 'Authorization': 'bearer 95dad7eb17d7976acd353014aa833099b650f42f'}
    r = requests.get(url,params=payload, headers=headers)
    r_json = r.json()
    accounts = []
    markets = set(['ios', 'google-play'])
    for a in r_json['accounts']:
        if a['market'] in markets:
            accounts.append(a['account_id'])
        else:
            pass
    return accounts
    
def app_annie_apps(account_num,k):
    global apps
    #http://support.appannie.com/hc/en-us/articles/204208964-2-Account-Connection-Product-List
    url = "http://api.appannie.com/v1.2/accounts/"+ str(account_num) + "/products?"
    payload = "page_index:0"
    headers = {"Authorization": "bearer " + k, "Accept": "application/json"}
    r = requests.get(url,params=payload, headers=headers)
    r_json = r.json()
    print r_json['products']
    apps = r_json['products']
    return apps
    
def app_annie_sales(acc_id, app_id, startDate, endDate):
    global sales_json
    #http://support.appannie.com/hc/en-us/articles/204208914-3-Product-Sales-
    url = "http://api.appannie.com/v1.2/accounts/" + str(acc_id) + "/products/" + str(app_id) + "/sales?"
    payload = {"account_id":str(acc_id), "break_down":"date","start_date": startDate,"end_date":endDate} #"application+country+date,iap"
    headers = {"Authorization": "bearer " + k, "Accept": "application/json"}
    r = requests.get(url,params=payload, headers=headers)
    sales_json = r.json()
    print sales_json
    time.sleep(3.5)
    return sales_json

#Get the Reviews associated with the account
def app_annie_reviews(acc_id,market,app_id,start_date,end_date):
    global review_json
    #http://support.appannie.com/hc/en-us/articles/204208934-6-Product-Reviews-
    url = "http://api.appannie.com/v1.2/apps/" + str(market) + "/app/" + str(app_id) + "/reviews?"
    payload = {"start_date":start_date,"end_date":end_date}
    headers = {"Authorization": "bearer " + k, "Accept": "application/json"}  
    r = requests.get(url,params=payload, headers=headers)
    rev_json = r.json()
    print rev_json
    time.sleep(5)
    return rev_json

startDate = '2015-03-01'
endDate = '2015-03-30'
market = 'ios'

apps_file = "app_annie_connected_apps.csv"

a = open(apps_file,'w')

app_annie_accounts()

for acc in accounts:
    app_annie_apps(acc,k)
    json_to_csv.json_to_csv(app,apps_file)
    
a.close()

#app_annie_sales(acc, app, startDate, endDate)
#need to capture the market, product_id, etc.
#app_annie_reviews(acc, market,app,startDate,endDate)