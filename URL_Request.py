import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

class url_request:
    def __init__(self):
        self.data = self.get_URL_data()
        self.jobs = dict()
        urls = self.crawl()
        for i in urls:
            try:
                self.extract_data(self.get_URL_data(i))
            except:
                pass
        
    def get_URL_data(self):
        URL = "https://www.indeed.com/jobs?q=Software+Engineer&explvl=entry_level"
        #Request of the stated URL Above
        new_urls = deque([URL])
        #Get next overall serach URL (i.e. next 20 job postings)
        for x in range(1,16):
            new_urls.append(URL + "&start=" + str(x*10))
        processed_urls = set()
        local_urls = set()
        foreign_urls = set()
        broken_urls = set()
        load = str()

        #Process URL
        while len(new_urls) > 0:
            url = new_urls.popleft()
            processed_urls.add(url)
            load += "#"
            print(load,end='\r')
            for _ in range(20):
                try:
                    response = requests.get(url)
                except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
                    broken_urls.add(url)
                    continue
                parts = urlsplit(url)
                base = "{0.netloc}".format(parts)
                strip_base = base.replace("www.","")
                base_url = "{0.scheme}://{0.netloc}".format(parts)
                path = url[:url.rfind('/')+1]

                soup = BeautifulSoup(response.text, "lxml")
                for link in soup.find_all('a'):
                    if "href" in link.attrs:
                        anchor = link.attrs["href"]
                    else:
                        anchor = ''
                    #rc indicated job link
                    if anchor.startswith('/rc'):
                        local_link = base_url + anchor
                        local_urls.add(local_link)
    ##                elif strip_base in anchor:
    ##                    local_urls.add(anchor)
    ##                elif not anchor.startswith('http'):
    ##                    local_link = path + anchor
    ##                    local_urls.add(local_link)
                    else:
                        foreign_urls.add(anchor)

        print("")
        return local_urls

        
    def get_URL_data(self, URL):
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
    def extract_data(self, data):
        for div in data.find_all(name="div", attrs={"class":"jobsearch-jobDescriptionText"}):
            for s in div.contents:
                txt = str(s.contents)
                idx = txt.find("year")
                if idx == -1 or idx is None:
                    pass
                else:
                    #Parse until number
                    tx = txt[idx]
                    while tx not in {'1','2','3','4','5','6'} or tx == '/':
                        idx -= 1
                        tx = txt[idx]
                    if tx in self.jobs:
                        self.jobs[tx] += 1
                    else:
                       self.jobs[tx] = 1

    def get_jobs(self):
        return self.jobs
                        

