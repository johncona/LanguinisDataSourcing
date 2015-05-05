#AppAnnie API Key: 

#Documentation: http://support.appannie.com/categories/20082753-Analytics-API
#1000 calls per day
#30 calls per minute

import json, requests, time
import json_to_csv
import pandas as pd

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
    accounts = r_json['accounts'] #[]
    return accounts
    
def app_annie_apps(account_num,k,market):
    global apps
    #http://support.appannie.com/hc/en-us/articles/204208964-2-Account-Connection-Product-List
    url = "http://api.appannie.com/v1.2/accounts/"+ str(account_num) + "/products?"
    payload = "page_index:0"
    headers = {"Authorization": "bearer " + k, "Accept": "application/json"}
    r = requests.get(url,params=payload, headers=headers)
    r_json = r.json()
    try:
        if r_json['products'] != []:
            try:
                apps = r_json['products'][0]
                apps['market'] = market
                apps['account_id'] = account_num
            except:
                apps = r_json['products']
                apps['market'] = market
                apps['account_id'] = account_num
        else:
            apps = []
    except KeyError:
        apps = []
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
accounts_file = "app_annie_connected_accounts.csv"

#Pull all the accounts into the accounts_file
p = 'w'
app_annie_accounts()
json_to_csv.json_to_csv(accounts,accounts_file,p)

df = pd.read_csv(accounts_file)
df = df[df["type"] == "apps"]
df = df.dropna()
df = df.drop_duplicates()
df.to_csv(accounts_file)

for index, row in df.iterrows():
    market = row['market']
    account_id = row['account_id']
    app_annie_apps(account_id,k,market)
    json_to_csv.json_to_csv(apps,apps_file,p)

#app_annie_sales(acc, app, startDate, endDate)
#need to capture the market, product_id, etc.
#app_annie_reviews(acc, market,app,startDate,endDate)