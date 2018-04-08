import requests
import re
from bs4 import BeautifulSoup
import bs4

def downloadHtml(url):
    try:
        headers={'User-Agent':'Mozilla/5.0'}
        res=requests.get(url,headers=headers);
        res.raise_for_status()
        res.encoding=res.apparent_encoding
        return res.text
    except Exception as e:
        return ''
    pass
def getList(html):
    cList=[]
    try:
        soup=BeautifulSoup(html,'html.parser')
        items=soup.find_all(class_="item")
        for item in items:
            title=item.find('span',class_='title').string.strip()
            href=item.find('a')['href'].strip()
            img=item.find('span',class_='imgLink').find('img')['src'].strip()
            price=item.find('span',class_='pricedetail').find('strong').string.strip()
            shop=item.find('span',class_='shopNick').string.strip()
            c={'title':title,'href':href,'img':img,'price':price,'shop':shop}
            cList.append(c)
        return cList
    except Exception as e:
        return cList
    pass
def pagination(url):
    cList=[]
    try:
        for x in range(99):
            urlStr='{}&page={}'.format(url,x+1);
            print('正在抓取{}',urlStr)
            htmlStr=downloadHtml(urlStr)
            getList(htmlStr)
            for x in getList(htmlStr):
                cList.append(x)
                pass 
            pass
        pass
        return cList
    except Exception as e:
        return None
    pass
def main():
    keyword='男士裤子'
    url='http://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&clk1=ea787a1f04e09b58f3cdd4fc7bcca336&keyword='+keyword
    cList=pagination(url)
    print('共抓取商品数据{}条'.format(len(cList)))
    print('{:40}\t{:8}\t{:5}'.format('名称','价格','店铺'))
    for c in cList:
        print('{:40}\t{:8}\t{:5}\t'.format(c['title'],c['price'],c['shop']))
        pass
    pass
main()