def get_reddit_posts(subreddit, post_num, before_time, API_limit, API_wait):
    #Base url
    base_url = "https://api.pushshift.io/reddit/submission/search"
    #Getting the posts before July 1st
    before_time = int(time.mktime(time.strptime('1 July, 2020', '%d %B, %Y'))), # The latest pull time
    #... <removed code> 
    for _ in range(post_num // API_limit):
        #... <removed code> 
        #requests parameters 
        params = {
        'subreddit' : subreddit,
        'size' : API_limit,
        'before' : before_time,
                    }
        #... <removed code> 
        #API request
        res = requests.get(base_url, params)
    
        if res.status_code == 200:
            df = pd.DataFrame(res.json()['data'])
            df_master = df_master.append(df, ignore_index=True)
            # limit on reddit API and wait until next loop
            time.sleep(API_wait)  
        else:
            print("An error occured while pulling API, please revisit parameters; status code: ", res.status_code)
    #... <removed code> 
    return df_master