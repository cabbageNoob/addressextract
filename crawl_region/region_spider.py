'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-07 15:03:12
'''
import os, sys
import requests

from bs4 import BeautifulSoup
sys.path.insert(0, os.getcwd())

from crawl_region import config
from utils.load_util import writejson2file

class RegionSpider():
    def __init__(self):
        self.base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/'
        # 初始化headers
        self.headers = {'User-Agent': config.user_agent}
        self.address_path = config.address_path
        self.address = {}

    def get_page(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser", from_encoding="GBK")
                return soup
        except Exception as e:
            print(e)
            for i in range(1, 10):
                print('请求超时，第%s次重复请求' % i)
                try:
                    response = requests.get(url, headers=self.headers, timeout=5)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, "html.parser", from_encoding="GBK")
                        return soup
                except Exception as e:
                    print(e)
                    continue             

    def spider_province(self, url, path=[]):
        url = self.base_url + url
        soup = self.get_page(url)
        tr_lists = soup.find_all('tr', class_='provincetr')
        for tr in tr_lists:
            for td in tr.find_all('td'):
                province = td.find('a')
                if province != None:
                    print(province.text)
                    self.address.setdefault(province.text, {})
                    self.spider_city(province.get('href'), [province.text])
                writejson2file(self.address, self.address_path)

    def spider_city(self, url, path):
        url = self.base_url + url
        soup = self.get_page(url)
        tr_lists = soup.find_all('tr', class_='citytr')
        for tr in tr_lists:
            td = tr.find_all('td')[-1]
            city = td.find('a')
            if city != None:
                self.address.get(path[0]).setdefault(city.text, {})
                self.spider_country(city.get('href'), [path[0], city.text])

    def spider_country(self, url, path):
        prefix_url = url.split('/')[0] + '/'
        url = self.base_url + url
        soup = self.get_page(url)
        tr_lists = soup.find_all('tr', class_='countytr')
        for tr in tr_lists:
            td = tr.find_all('td')[-1]
            country = td.find('a')
            if country != None:                
                self.address.get(path[0]).get(path[1]).setdefault(country.text, {})
                self.spider_town(prefix_url + country.get('href'), [path[0], path[1], country.text])

    def spider_town(self, url, path):
        prefix_url = '/'.join(url.split('/')[:2]) + '/'
        url = self.base_url + url
        soup = self.get_page(url)
        tr_lists = soup.find_all('tr', class_='towntr')
        for tr in tr_lists:
            td = tr.find_all('td')[-1]
            town = td.find('a')
            if town != None:                
                self.address.get(path[0]).get(path[1]).get(path[2]).setdefault(town.text, [])
                self.spider_village(prefix_url + town.get('href'), [path[0], path[1], path[2], town.text])

    def spider_village(self, url, path):
        url = self.base_url + url
        soup = self.get_page(url)
        tr_lists = soup.find_all('tr', class_='villagetr')
        for tr in tr_lists:
            village = tr.find_all('td')[-1]
            if village != None:                
                self.address.get(path[0]).get(path[1]).get(path[2]).get(path[3]).append(village.text)    

if __name__ == '__main__':
    region_spider = RegionSpider()
    content = region_spider.spider_province('index.html')
