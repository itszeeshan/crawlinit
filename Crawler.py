import logging
from ntpath import join
from typing_extensions import Self
from urllib.parse import urljoin
from numpy import empty
import requests
from bs4 import BeautifulSoup
import sys
sys.tracebacklimit=0
from torch import argsort
from traitlets import Undefined
import argparse

parser = argparse.ArgumentParser()

level = logging.DEBUG
fmt= '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(filename='spam.log', level=level, format=fmt)

class Crawler:
    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def get_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def append_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.get_url(url)
        for url in self.get_linked_urls(url, html):
            self.append_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            print(f'Crawling through: {url}')
            output = args.output
            if output is not None:
                with open(output, 'a') as f:
                    if url is not None:
                        f.write(join(url) + "\n")
            try:
                self.crawl(url)
            except ValueError:
                print(f'loading.....')
            finally:
                self.visited_urls.append(url)

    

if __name__ == '__main__':
    twitter = 'https://twitter.com/itszeeshan2'
    print(f"""
    _______  ______ _______ _  _  _             _____ __   _      _____ _______
    |       |_____/ |_____| |  |  | |             |   | \  |        |      |   
    |_____  |    \_ |     | |__|__| |_____      __|__ |  \_|      __|__    |   

    by Zeeshan --> Twitter: {twitter}
    """)

    parser.add_argument("-d", "--domain", help = "Domain to crawl")
    parser.add_argument("-o", "--output", help = "Save results to file")
    args = parser.parse_args()
    Crawler(urls=["https://"+args.domain]).run()
