'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-11-24 11:12:21
'''
import sys, os, time
sys.path.insert(0, os.getcwd())

from addressparse.address import Address
from addressparse.find_address import find_address, extract_locations

if __name__ == '__main__':
    address = Address(is_max_address=True)
    text = '中国传媒大学位于北京市朝阳区'
    t1 = time.time()
    af = find_address(address, text)
    print(af)
    print(time.time() - t1)
    
    t1 = time.time()
    af = extract_locations(text)
    print(af)
    print(time.time() - t1)