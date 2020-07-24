def get_reddit_posts(subreddit, post_num, time_1, API_limit, API_wait):
#... <removed code> 
    for _ in range(post_num // API_limit):
#... <removed code> 
        params = {
        'subreddit' : subreddit,
        'size' : API_limit,
        'before' : before_time,
                    }
#... <removed code> 

        res = requests.get(base_url, params)
    
        if res.status_code == 200: 

            df = pd.DataFrame(res.json()['data'])
            df_master = df_master.append(df, ignore_index=True)
#... <removed code> 
    return df_master