import csv
import datetime
import pandas as pd
import pickle
import snscrape.modules.twitter as sntwitter
import warnings 
from collections import defaultdict
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Suppress warnings
warnings.filterwarnings("ignore")

# Read list of individual terms from file
with open("XYZ.txt", "r") as ind_terms_file:
    ind_terms_list = ind_terms_file.readline().split(',')
    ind_terms_query = ' OR '.join(ind_terms_list)

# Read list of individual handles from file
with open('ABC.txt', 'r', encoding='utf-8-sig') as handles_file:
    handles_list = handles_file.readline().split(',')
    handles_list = [handle.lower() for handle in handles_list[11:]]


def get_tweets(twitter_names, since):
    """
    Scrapes tweets for given Twitter handles and saves them to separate CSV files.
    :param twitter_names: List of Twitter handles
    :param since: Date in YYYY-MM-DD format, starting from which tweets need to be scraped
    :return: Combined pandas DataFrame of all the scraped tweets
    """
    def_dict = defaultdict(lambda: defaultdict(list))
    for name in twitter_names:
        print(name)
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'({ind_terms_query}) ({name}) since:{since}').get_items()):
            key = f'{name}_{i}'
            def_dict[key] = [name, tweet.content, tweet.date, tweet.username, tweet.likeCount, tweet.retweetCount]
            data = pd.DataFrame(def_dict.values(), columns=['handle', 'content', 'date', 'username', 'likes', 'retweets'])
            data.to_csv(f'C:/Users/{name}.csv', index=False)
    return data


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    df = get_tweets(handles_list, '2021-06-29')
    print(df)
    end_time = datetime.datetime.now()
    print(f'Duration: {end_time - start_time}')
