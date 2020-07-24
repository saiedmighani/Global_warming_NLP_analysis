#!/usr/bin/env python
# coding: utf-8

# Written by Saied Mighani
#Latest update 20-07-19


#imports
import requests
import pandas as pd
import time


#Inspiration: https://github.com/scaress21/reddit_and_quibi/blob/master/code/01A_Gathering_Reddit_Data.ipynb

def get_reddit_posts(subreddit, post_num, time_1, API_limit, API_wait):
    """
    This function inputs the required details for pulling API's from the reddit using requests library. Parameters are:
    subreddit, post_num, time_1, API_limit, API_wait

    """
# Basic pushshift url to read from
    base_url = 'https://api.pushshift.io/reddit/submission/search'
# Setting up the before time as the latest read time.
    before_time = time_1 
# The pulled DataFrame to concat
    df_master = pd.DataFrame() 
#Looping over serveral pull requests considering the limitatiopn in reading APIs        
    #while (len(df_master) < post_num):  
    for _ in range(post_num // API_limit):
        
        #print(_)
#Parameteres for request get fro mreddit
        params = {
        'subreddit' : subreddit,
        'size' : API_limit,
        'before' : before_time,
                    }

        res = requests.get(base_url, params)
# Only concat to dataframe if it is imported correctly, other wise print an error message         
        if res.status_code == 200: 

            df = pd.DataFrame(res.json()['data'])
# Update the before time as the new posts are being read in the next while loop
            before_time = df["created_utc"].min()
            df_master = df_master.append(df, ignore_index=True)

#Printing the status terms while the data are being downloaded
            print_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(before_time))
            print(f'{API_limit} posts downloaded, oldest post:{print_time} - status code: {res.status_code}, now waiting {API_wait} seconds before next pull. Patience...')    

# limit on reddit API and wait until next loop
            time.sleep(API_wait) 
                
        else:
                
            print("An error occured while pulling API, please revisit parameters; status code: ", res.status_code)
    
#Making sure the posts are unique with unique ID's
    duplicates = df_master['id'].duplicated().sum()
    
# Checking the imported dataframe    
    def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) #source: https://www.geeksforgeeks.org/print-colors-python-terminal/
    for_print = "Does the imported dataframe match the request? " + str(post_num == len(df_master))
    prGreen(for_print)

#Final update confirming how many posts were gathered and if there are duplicates
    print(f'Final DataFrame shape: {df_master.shape}, there are {duplicates} duplicates')
    
    
#Return the final dataframe
    return df_master