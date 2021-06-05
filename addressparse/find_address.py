'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-05 21:49:05
'''
import re
import sys, os
sys.path.insert(0, os.getcwd())
import time
from addressparse.address import Address

def find_address(cls, data: str, is_max_address=True, ignore_special_characters=False) -> list:
    """查找地址

    :param cls: Address类对象
    :param data: 查找地址数据
    :param is_max_address: 是否查找最长地址
    :param ignore_special_characters: 是否去掉特殊字符
    :return: 地址列表
    """
    if ignore_special_characters:
        data = re.sub(r"[!#$%&'()*+,-./:：，。？！；‘’、《》;<=>?@[\]^_`{|}~\s]", '', data)
    ls = cls.max_match_cut(data)
    if is_max_address:
        max_address = []
        print('|'.join(sorted(ls, key=lambda x: len(x), reverse=True)))
        match = re.sub('|'.join(sorted(ls, key=lambda x: len(x), reverse=True)), lambda x: '*' * len(x.group()), data)
        for addr in re.finditer(r'[*]+', match):
            max_address.append([data[addr.start():addr.end()], addr.start(), addr.end()])
        return max_address
    return ls



if __name__ == '__main__':
    address = Address(is_max_address=True)
    t1=time.time()
    af = find_address(address, '我家在江西鄱阳，你家在江西省南昌')
    print(af)  # ['江西鄱阳', '江西省南昌']
    print(str(time.time() - t1))
    