## modified from https://github.com/WittmannF/imdb-tv-ratings/blob/master/IMDB_get_ratings.ipynb
from bs4 import BeautifulSoup as BS
import requests
from time import sleep
import numpy as np
import re
import pandas as pd

def get_ratings(serie_code, season):
    URL = f'https://www.imdb.com/title/{serie_code}/episodes?season={season}'
    c = requests.get(URL).content
    soup = BS(c, 'html.parser')
    allrates = soup.findAll("div", { "class" : 'ipl-rating-star small' })
    ratings = [float(re.search('ipl-rating-star__rating">(.*)</span', str(ar)).group(1)) for ar in allrates]
    return ratings

def extract_re(code, array):
    return re.search(code, str(array)).group(1)

def get_soup(URL):
    headers = {'Accept-Language': 'en'}
    c = requests.get(URL, headers=headers).content
    soup = BS(c, 'html.parser')
    return soup

RE_KEY = 'href="/title/(.*)/" title='
RE_TITLE = '">(.*)</a>'
RE_YEAR = 'secondaryInfo">((.*))</span>'
RE_RATING = '<strong title="(.*) based on'
RE_NRATINGS = 'based on (.*) user ratings">'

def get_top_ratings(URL):
    print('Send request')
    soup = get_soup(URL)

    print('Create lists with html tags')
    key_title_year = soup.findAll("td", {"class": "titleColumn"})
    rating_and_count = soup.findAll("td", {"class": "ratingColumn imdbRating"})

    print('Extract info from html formatting')
    keys = [extract_re(RE_KEY, n) for n in key_title_year]
    titles = [extract_re(RE_TITLE, n) for n in key_title_year]
    ratings = [extract_re(RE_RATING, n) for n in rating_and_count]
    nratings = [extract_re(RE_NRATINGS, n) for n in rating_and_count]
    years = [extract_re(RE_YEAR, n).replace('(','').replace(')','') for n in key_title_year]

    print('Convert to a dataframe')
    df = pd.DataFrame(zip(titles, years, ratings, nratings), index=keys, columns=['Title', 'Year', 'Rating', 'Rating Count'])

    print('Done')
    return df

flatten = lambda l: [item for sublist in l for item in sublist]

def print_stats(rates):
    print(f'Mean: {np.mean(flatten(rates))}')
    print(f'Median: {np.median(flatten(rates))}')

def get_all_ratings(serie_code, max_seasons=100):
    all_ratings = []
    for season in range(1,max_seasons+1):
        ratings = get_ratings(serie_code, season)
        try:
            unrepeated = ratings!=all_ratings[-1]
        except:
            unrepeated = True
        if len(ratings)>0 and unrepeated:
            all_ratings.append(ratings)
            print(f'Season {season} = {ratings}')
            sleep(1)
        else:
            print_stats(all_ratings)
            return convert2df(all_ratings, serie_code)
            break
    print_stats(all_ratings)
    return convert2df(all_ratings, serie_code)

def convert2df(all_ratings, code):
    season_number = []
    episode_number = []
    ratings = []
    for i in range(len(all_ratings)):
        for j in range(len(all_ratings[i])):
            season_number.append(i+1)
            episode_number.append(j+1)
            ratings.append(all_ratings[i][j])
    serie_df = pd.DataFrame(zip(season_number, episode_number, ratings), columns=['Season', 'Episode', 'Rating'])
    serie_df['Code'] = code
    return serie_df

soup = get_soup('https://www.imdb.com/chart/toptv')

name_code = soup.findAll("td", {"class": "titleColumn"}); name_code[0]

serie_ranks = soup.findAll("td", {"class": "ratingColumn imdbRating"}); serie_ranks[0]

serie_poster = soup.findAll("td", {"class": "posterColumn"}); serie_poster[0]

RE_CODE = 'href="/title/(.*)/" title='
RE_NAME = '">(.*)</a>'
RE_YEAR = '<span class="secondaryInfo">((.*))</span>'
RE_RATE = '<strong title="(.*) based on'
RE_NRATES = 'based on (.*) user ratings">'
RE_POSTER = 'src="(.*)" width'

names = [extract_re(RE_NAME, n) for n in name_code]
codes = [extract_re(RE_CODE, n) for n in name_code]
year = [extract_re(RE_YEAR, n) for n in name_code]
series_rates = [extract_re(RE_RATE, n) for n in serie_ranks]
number_rates = [extract_re(RE_NRATES, n) for n in serie_ranks]
poster_url = [extract_re(RE_POSTER, n) for n in serie_poster]

all_series = pd.DataFrame(zip(names, codes, year, series_rates, number_rates, poster_url), columns=['title', 'code', 'year', 'rating', 'rating_count', 'poster_url'])
all_series.index = all_series['code']
 
# all_series.to_csv("top250ratings.csv")

all_ratings = None
for code in all_series['code']:
    print(all_series[all_series.index==code]['title'][0])
    try:
        all_ratings = all_ratings.append(get_all_ratings(code))
    except: #initialize ratings_df if it is the first time
        all_ratings = get_all_ratings(code)

# all_ratings.to_csv('top250allratings.csv')
