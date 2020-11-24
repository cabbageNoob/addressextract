'''
Descripttion: 
Author: cjh (492795090@qq.com)
Date: 2020-11-24 11:07:48
'''
import json
import sys, os
sys.path.insert(0, os.getcwd())
pwd_path = os.path.abspath(os.path.dirname(__file__))
 
from ctypes import * #Python的一个外部库，提供和C语言兼容的数据类型，可以很方便地调用C DLL中的函数.访问dll，首先需引入ctypes库
libFile=os.path.join(pwd_path,'./nlpir_tools/NLPIR-ICTCLAS/lib/win64/new/NLPIR.dll')
libSoFile=os.path.join(pwd_path,'./nlpir_tools/NLPIR-ICTCLAS/lib/linux64/libNLPIR.so')
NLPIR_ICTCLAS_path=os.path.join(pwd_path,'./nlpir_tools/NLPIR-ICTCLAS')
# dll =  CDLL(libSoFile)    # 支持linux
dll = CDLL(libFile) #支持windows


def loadFun(exportName, restype, argtypes):
    global dll
    f = getattr(dll,exportName)
    f.restype = restype
    f.argtypes = argtypes
    return f

class ENCODING:
    GBK_CODE        =   0               #默认支持GBK编码
    UTF8_CODE       =   GBK_CODE+1      #UTF8编码
    BIG5_CODE       =   GBK_CODE+2      #BIG5编码
    GBK_FANTI_CODE  =   GBK_CODE+3      #GBK编码，里面包含繁体字
 
 
Init = loadFun('NLPIR_Init', c_int, [c_char_p, c_int, c_char_p])
Tokenizer4IR = loadFun('NLPIR_Tokenizer4IR', c_char_p, [c_char_p, c_bool])
Freqstat=loadFun('NLPIR_WordFreqStat',c_char_p,[c_char_p])

if not Init(NLPIR_ICTCLAS_path.encode('UTF-8'),ENCODING.UTF8_CODE,b''):
    print("Initialization failed!")
    exit(-111111)
 
def tokenizer4IR(sentence):
    result = Tokenizer4IR(sentence.encode('UTF-8'), False)
    # print('result  ',result)
    return json.loads(result)

def Freq(sentence):
    result = Freqstat(sentence.encode('UTF-8'))
    result = str(result, encoding="utf-8")
    print(result)
    
if __name__ == "__main__":
    print('1111111')
    sent_list = ['他的薪奉很高',
            '少先队员因该主动给老人让坐',
            '宋庆龄于8月14日零晨1时抵达雅加达',
            '我们这些化夏子孙; 就难免必理不平衡',
            '文稿中仍会遗留许多误',
            '维护建筑市场场秩序']
    for sent in sent_list:
        print(tokenizer4IR(sent))
