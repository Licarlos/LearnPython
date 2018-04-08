import re
import requests
from bs4 import BeautifulSoup
import bs4

def downloadHtml(url):
	try:
		headers={'User-Agent':'Mozilla/5.0'}
		res=requests.get(url,headers)
		res.raise_for_status()
		res.encoding=res.apparent_encoding
		return res.text
		pass
	except Exception as e:
		return ''
		pass
	pass

def getList(html):
	collegeList=[]
	soup=BeautifulSoup(html,'html.parser')
	tb=soup.find(class_='tbl defTbl')
	for tr in tb.find_all('tr'):
		rank=tr.find(class_='t1').string
		a=tr.find(class_='t2').find('a')
		name=tr.find(class_='t2').string;
		if type(a) == bs4.element.Tag:
			name=a.string
			pass
		address=tr.find(class_='t3').string
		classify=tr.find(class_='t4').string
		hard=tr.find(class_='t5').string
		collegeList.append({'rank':rank,'name':name,'address':address,'classify':classify,'hard':hard});
	return collegeList

def printFormat(l):
	for x in l:
   		temp="{:^2} {} {} {} {}".format(x['rank'],x['name'],x['address'],x['classify'],x['hard'])
   		print(temp)
	pass
def main():
	url="http://www.gaokaopai.com/paihang-otype-4.html"
	html=downloadHtml(url)
	collegeList=getList(html)
	printFormat(collegeList)

main()