'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-06 14:59:16
'''
import sys, os
sys.path.insert(0, os.getcwd())
import time
from addressparse.address import Address
from addressparse.supplement_address import key_to_address

address = Address(is_max_address=True)


def max_key_filter(keys):
    """最多关键词过滤算法

    依据关键词出现的次数来判断改地址的重要性
    """

    def inner(x):
        flag = 0
        for key in keys:
            if key in x:
                flag += 1
        return flag

    return inner


def correct_address(cls, sentence):
    """自动纠错地址

    :param cls: Address类对象
    :param sentence: 要纠错的句子
    :return: 纠错后的地址
    """
    keys = cls.max_match_cut(sentence)
    all_ = key_to_address(cls, keys)
    filter_address = list(sorted(all_, key=max_key_filter(keys), reverse=True))
    if filter_address:
        max_address = max(filter_address, key=lambda x: len(x))
        return max_address
    return filter_address

if __name__ == '__main__':
    print(correct_address(address, '贵州省遵义市花溪区'))  # 贵州省-贵阳市-花溪区
    print(correct_address(address, '江西省南昌市万年县'))  # 
    print(correct_address(address, '朝阳区桂林街道'))