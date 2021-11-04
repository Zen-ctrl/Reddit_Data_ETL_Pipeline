'''
This script will give a character count of post
titles according to the name of the subreddit
the user inputs
'''

import requests
from unidecode import unidecode
import csv


try:
        USER_INTAKE = input("What subreddit would you like to visit? ")
except:
        if "" in USER_INTAKE and " " not in USER_INTAKE:
                USER_INTAKE = "worldnews"
        '''
        The above block checks to see if the user has input any
        information. If nothing is entered, the variabe USER_INTAKE
        is set to worldnews. This will bring up json data for
        worldnews.
        '''


def reddit_extract():
    # Returns useful data about Reddit pots from a given sub
    # Set the necessary header information
    url = f'https://old.reddit.com/r/{USER_INTAKE}.json'
    # f string the input of the USER_INTAKE variabe
    head = {'user-agent': "Kwaku Ampadu-Nyarkoh v.0.0.1"}
    rawdata = requests.get(url, headers=head).json()
    # Return just the items of interests
    return rawdata['data']
rawobj = reddit_extract()


def reddit_transform(dataobj):
        '''Takes raw data from the reddit extraction \n
        and returns a curated dictionary data object.'''
        data = []
        # This list will absorb the info from the cleaned dict.
        for index, item in enumerate(dataobj['children']):
            store = item['data']['title'].lower().replace(",", "`")
            cleantitle = unidecode(store)
            # Makes all unidecode lowercase and repalces , for `
            obj = {'title': cleantitle, 'keywordCount': len(cleantitle)}
            # Dictionary object created here per
            # what cleantitle is, and its length
            data.append(obj)
            # The list is appened with whatever the dict had
        return(data)
titles = reddit_transform(rawobj)


def reddit_load_to_csv(titles):
    keys = titles[0].keys()
    with open('datasource.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        # Writes the keys to the csv
        dict_writer.writeheader()
        dict_writer.writerows(titles)
        # Writes the rows per the titles

reddit_load_to_csv(titles)
