import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

def get_URL_data():
    URL = "https://www.indeed.com/jobs?q=Software+Engineer&explvl=entry_level"
    #Request of the stated URL Above
    page = requests.get(URL)

    soup = BeautifulSoup(page.text,"html.parser")

    print(soup.prettify())

get_URL_data()
