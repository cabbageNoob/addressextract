'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-05 20:01:26
'''
from pyhanlp import HanLP

def get_location(word_pos_list):
    """
    get location by the pos of the word, such as 'ns'
    eg: get_location('内蒙古赤峰市松山区')
    :param: word_pos_list<list>
    :return: location_list<list> eg: ['陕西省安康市汉滨区', '安康市汉滨区', '汉滨区']
    """
    location_list = []
    if word_pos_list==[]:
        return []

    for i,t in enumerate(word_pos_list):
        word = t[0]
        nature = t[1]
        if nature == 'ns':
            loc_tmp = word
            count = i + 1
            while count < len(word_pos_list):
                next_word_pos = word_pos_list[count]
                next_pos = next_word_pos[1]
                next_word = next_word_pos[0]
                if next_pos=='ns' or 'n' == next_pos[0]:
                    loc_tmp += next_word
                else:
                    break
                count += 1
            location_list.append(loc_tmp)

    return location_list # max(location_list)

def extract_locations(text):
    """
    extract locations by from texts
    eg: extract_locations('我家住在陕西省安康市汉滨区。')
    :param: raw_text<string>
    :return: location_list<list> eg: ['陕西省安康市汉滨区', '安康市汉滨区', '汉滨区']
    """
    if text=='':
        return []
    seg_list = [(str(t.word), str(t.nature)) for t in HanLP.segment(text)]
    location_list = get_location(seg_list)
    return location_list

if __name__ == '__main__':
    print(extract_locations('我家住在陕西省安康市汉滨区。旁边的鄱阳县四十里街镇'))