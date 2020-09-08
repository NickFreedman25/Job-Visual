import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

class URL_Request:
    def __init__(self):
        self.data = self.get_URL_data()
        
    def get_URL_data(self):
        URL = "https://www.indeed.com/jobs?q=Software+Engineer&explvl=entry_level"
        #Request of the stated URL Above
        page = requests.get(URL)

        soup = BeautifulSoup(page.text,"html.parser")
        
        return soup

    def extract_data(self):
        jobs = []
        for div in self.data.find_all(name="div", attrs={"class":"row"}):
            for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
                jobs.append(a["title"])
        print(jobs)

data = URL_Request()
data.extract_data()    
