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
from utils.nlpir_tokenizer import tokenizer4IR

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

def get_location(tokens):
    """
    get location by the pos of the word, such as 'ns'
    eg: get_location('内蒙古赤峰市松山区')
    :param: tokens<list>
    :return: location_list<list> eg: [['江西鄱阳四十里街镇集镇', 4, 15], ['万年县', 19, 22]]
    """
    location_list = []
    if tokens == None:
        return []
    length = len(tokens)
    if length == 0:
        return []
    end = -1
    for start in range(0, length):
        if start <= end:
            continue
        word = tokens[start]['text']
        begin_idx = tokens[start]['begin']
        end_idx = tokens[start]['end']
        nature = tokens[start]['pos']
        if nature == 'ns':
            loc_tmp = word
            for end in range(start + 1, length):
                next_pos = tokens[end]['pos']
                next_word = tokens[end]['text']
                if next_pos=='ns' or 'n' == next_pos[0]:
                    loc_tmp += next_word
                    end_idx = tokens[end]['end']
                else:
                    break
            location_list.append([loc_tmp, begin_idx, end_idx])
    return location_list

def extract_locations(text):
    """
    extract locations by from texts
    eg: extract_locations('我家住在陕西省安康市汉滨区。')
    :param: raw_text<string>
    :return: location_list<list> eg: ['陕西省安康市汉滨区', '安康市汉滨区', '汉滨区']
    """
    if text=='':
        return []
    seg_list = tokenizer4IR(text)
    location_list = get_location(seg_list)
    return location_list



if __name__ == '__main__':
    address = Address(is_max_address=True)
    t1=time.time()
    af = find_address(address, '我家在江西鄱阳，你家在江西省南昌')
    print(af)  # ['江西鄱阳', '江西省南昌']
    print(str(time.time() - t1))

    t1=time.time()
    af = extract_locations('我家在江西鄱阳，你家在江西省南昌')
    print(af)  # ['江西鄱阳', '江西省南昌']
    print(str(time.time() - t1))