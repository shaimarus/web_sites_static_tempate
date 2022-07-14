#!/usr/bin/env python

from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

#engine = create_engine('postgresql://postgres:postgres@3.73.116.68:5432/postgres')
engine = create_engine('postgresql://postgres:postgres@db-pg:5432/postgres')
df=pd.read_sql('select * from public.logs', engine)

df['time1']=pd.to_datetime(df['time1'])+timedelta(hours=6)
df['day1']=(pd.to_datetime(df['time1'])).dt.date


plt.rcParams['figure.figsize'] = [20, 10]
plt.title('Кол-во посещении сайта по дням')
plt.bar(df.groupby(['day1']).size().index,df.groupby(['day1']).size().values,width=0.001)
plt.xticks(rotation=90)
plt.savefig('pic1.pdf')
plt.close()

plt.rcParams['figure.figsize'] = [20, 10]
plt.title('Кол-во уникальных посещении сайта по дням')
plt.bar(df.groupby('day1')['ip'].nunique().index,df.groupby('day1')['ip'].nunique().values,width=0.001)
plt.xticks(rotation=90)
plt.savefig('pic2.pdf')
plt.close()


import requests


TOKEN = '5510341962:AAHdg5oh6-o4jDWLoBEsCpOsACVSnGTqFdE'
CHAT_ID = '491737145'
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

#your_message='sdfsdfsdfsdf1212'
#requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': your_message}) 

with open("pic1.pdf", "rb") as filexlsx:
    files = {'document':filexlsx}
    r=requests.post(SEND_URL, data={'chat_id': CHAT_ID, "caption":'Кол-во посещении сайта по дням'},files=files) 

with open("pic2.pdf", "rb") as filexlsx:
    files = {'document':filexlsx}
    r=requests.post(SEND_URL, data={'chat_id': CHAT_ID, "caption":'Кол-во уникальных посещении сайта по дням'},files=files) 

