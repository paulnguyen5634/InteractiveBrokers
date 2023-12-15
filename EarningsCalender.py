import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
from selenium import webdriver
import time

# Import date class from datetime module
from datetime import date
 
# Returns the current local date
today = date.today()
print("Today date is: ", today)

year = today.year

month = today.month
if month < 10:
    month = str(month)
    month = ''.join(('0',month))
    
day = today.day
#day+=1 This is to get the next day's earning calender
if day < 10:
    day = str(day)
    day = ''.join(('0',day))

headers = {
    "Accept":"application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Origin":"https://www.nasdaq.com",
    "Referer":"https://www.nasdaq.com",
    "User-Agent":"your user agent..."
}
 
url = 'https://api.nasdaq.com/api/calendar/earnings?' 
#Change this according to day
payload = {"date":f"{year}-{month}-{day}"} 
source = requests.get( url=url, headers=headers, params=payload, verify=True ) 
data = source.json()

from pprint import pprint
pprint(data)

print(data['data']['rows'])
print(type(data))

for i in range(0,len(data['data']['rows'])):
    
    mrkt_cap = data['data']['rows'][i]['marketCap']
    mrkt_cap = mrkt_cap.replace('$', '')
    mrkt_cap = mrkt_cap.replace(',', '')
    
    forecastEPS = data['data']['rows'][i]['epsForecast']
    
    numAnalysts = data['data']['rows'][i]['noOfEsts']
    
    releaseTime = data['data']['rows'][i]['time'] 
    
    if int(mrkt_cap)/1000000000 > 1 and releaseTime == 'time-pre-market':
        print(data['data']['rows'][i]['symbol'])
        print(releaseTime)
        print(data['data']['rows'][i]['marketCap'])
        print('Forcasted EPS: '+forecastEPS)
        print('Num analysts: ' + numAnalysts + "\n")