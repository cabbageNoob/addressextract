'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-09-07 15:03:49
'''
import json

def writejson2file(data, filename):
    with open(filename, 'w',encoding='utf8') as outfile:
        data = json.dumps(dict(data), indent=4, ensure_ascii=False)
        outfile.write(data)

def readjson(filename):
    with open(filename,'rb') as outfile:
        return json.load(outfile)