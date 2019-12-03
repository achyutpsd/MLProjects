# -*- coding: utf-8 -*-
"""
Created on December 3.12.2019

@author: Achyut Babu
"""
import os
import time
import requests
import sys



def retrieve_html(startyear,endyear):
    for year in range(startyear,endyear):
       
        for month in range(1,13):
            if(month <10):
                url='https://en.tutiempo.net/climate/0{}-{}/ws-486980.html'.format(month,year)
            else:
                 url='https://en.tutiempo.net/climate/{}-{}/ws-486980.html'.format(month,year)
                  
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
    sys.stdout.flush()
                
if __name__=="__main__":
    start_time = time.time()
    retrieve_html(2013,2018)
    stop_time = time.time()
    print("Time Taken {}".format(start_time-stop_time))
    