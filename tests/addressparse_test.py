'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-05 21:49:43
'''
import sys, os
sys.path.insert(0, os.getcwd())
import time
from addressparse.address import Address
from addressparse.address_interface import find_address

address = Address(is_max_address=True)
# address.add_vague_text(['红花岗', '花溪'])
# address.add_vague_text('贵州省-遵义市-遵义县-虾子镇-乐安村-乐石台')


def find_address_test():
    t1=time.time()
    af = find_address(address, '我家在江西鄱阳，你家在江西省南昌')
    print(af)  # ['江西鄱阳', '江西省南昌']
    print(str(time.time() - t1))

if __name__ == '__main__':
    find_address_test()