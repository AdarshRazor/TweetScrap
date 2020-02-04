# -*- coding: utf-8 -*-
"""
Twitter Tweet Scrapper - 1.0
Tweet Scrapper with Extra Features

Adarsh Anand
11:30 02.02.2020
"""

from twitterscraper import query_tweets
import datetime as dt
import  pandas as pd
from tkinter.filedialog import *
from tkinter.simpledialog import *
import tkinter
import os

root = tkinter.Tk()        
root.withdraw()
root.focus()
root.lift()

f1 = askdirectory()

#begin_date=dt.date(2020,1,15)
#end_date=dt.date(2020,2,3)

#limit  = 1000
#lang = 'en'
#user=realDonaldTrump

hashtag=askstring("Hashtag","Enter the hashtag : ")
limit=askinteger("limit","Enter the limit : ")
lang=askstring("language","Enter the language : ")
bdate=askstring("Begin date","Enter the begin date (YYYY,M,D)")
edate=askstring("End date","Enter the end date (YYYY,M,D)")

l = [int(i) for i in bdate.split(",")]
k = [int(i) for i in edate.split(",")]
begin_date = dt.date(l[0],l[1],l[2])
end_date = dt.date(k[0],k[1],k[2])

tweets=query_tweets(hashtag, begindate = begin_date, enddate = end_date, limit=limit, lang=lang)

dc = pd.DataFrame(t.__dict__ for t in tweets)
df=pd.DataFrame(dc, columns=['screen_name', 'username', 'text', 'hashtags'])
file = f1+r"\%s.xlsx"%hashtag
export_excel=df[~df.duplicated(subset=['text'])].to_excel (file) #removing the duplicate texts
os.startfile(file)
print (df)
