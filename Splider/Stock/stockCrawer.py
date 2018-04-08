import requests
import traceback
import bs4
from bs4 import BeautifulSoup
import re

import json

# 下载Html
def downloadHtml(url,encoding='utf-8'):
    try:
        headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json'}
        res=requests.get(url,headers=headers,timeout=50)
        # print(res.apparent_encoding)
        res.raise_for_status()
        res.encoding=encoding
        return res.text
        pass
    except Exception as e:
        return ''
    pass


# 从东方财富网获取股票新列表
def getStockList(url):
    stockList=[]
    testUrl='{}&page=1'.format(url)
    rt=downloadHtml(testUrl)
    match=re.search(r'pages:[1-9]\d+',rt)
    pages=0
    if match:
        pages=int(match.group(0).split(':')[1])
        pass
    count=0;
    for page in range(pages):
        listUrl='{}&page={}'.format(url,page)
        data=downloadHtml(listUrl)
        match=re.search(r'\".+?\"',data)
        if match:
            stock_code=match.group(0).split(',')[1]
            stock_info_url='https://gupiao.baidu.com/stock/sh{}.html'.format(stock_code)
            rt=downloadHtml(stock_info_url)
            soup=BeautifulSoup(rt,'html.parser')
            # name
            name=soup.find(class_='bets-name').text.strip()
            dd1s=soup.find(class_='line1').find_all('dd')
            max=dd1s[2].string
            total=dd1s[10].string
            dd2s=soup.find(class_='line2').find_all('dd')
            min=dd2s[2].string
            per=dd2s[9].string
            stockList.append({'name':name,'total':total,'max':max,'min':min,'per':per})
            count=count+1
            print('\t{:.2f}%'.format(count*100/pages),end='')
            pass     
    return stockList

def save(path,sList):
    str=''
    for s in sList:
        temp='股票名称:{},总股本:{},每股净资产:{},最高:{},最低：{}'.format(s["name"],s["total"],s["per"],s["max"],s["min"])
        str='{}\n{}'.format(str,temp)
        print(str)
    pass
    with open(path,'w') as fs:
        fs.write(str)
    fs.close()


# 主函数
def main():
    stock_list_url='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C.2&sty=FCOIATA&sortType=C&sortRule=-1&pageSize=20&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c&jsName=quote_123&_g=0.5770085567014531'

    sList= getStockList(stock_list_url)
    save("f://stockinfos.txt",sList)
    pass

# 启动
main()