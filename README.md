<!--
 * @Descripttion: 
 * @Author: cjh (492795090@qq.com)
 * @Date: 2020-09-04 15:41:48
-->
# addressextract

## 中国城乡地区爬虫

爬取[中国城乡数据](http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html)，数据统计时间是2019年，有请求重试机制，执行[代码](./crawl_region/region_spider.py)即可获取所有省市五级地址，[数据](./crawl_region/data/address.json)以json格式存储
```
{
    "北京市": {
        "市辖区": {
            "东城区": {
                "东华门街道": [
                    "多福巷社区居委会",
                    "银闸社区居委会",
                    "东厂社区居委会",
                    "智德社区居委会",
                    "南池子社区居委会",
                    "黄图岗社区居委会",
                    "灯市口社区居委会",
                    "正义路社区居委会",
                    "甘雨社区居委会",
                    "台基厂社区居委会",
                    "韶九社区居委会",
                    "王府井社区居委会"
                ],
                "景山街道": [
                    "隆福寺社区居委会",
                    "吉祥社区居委会",
                    ······
                ]
            }
        }
    }
}
```

## 地址抽取
writing....

## 地址补全
writing....

## 地址纠错
writing....
