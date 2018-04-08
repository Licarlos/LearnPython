import requests
from bs4 import BeautifulSoup


def downloadHtml(url):
	try:
		headers={'User-Agent':'Mozilla/5.0'}
		res=requests.get(url,headers=headers);
		res.raise_for_status()
		res.encoding=res.apparent_encoding
		return res.text
	except Exception as e:
    		return ''
def getUniVList(ulist,html):
	soup=BeautifulSoup(html,'html.parser')
	ret=soup.find('table',class_='tdbg_none').find_all('table')
	for tb in ret:
		tds=tb.find_all('td')
		for tdP in tds:
			for td in tdP('td'):
				title=td.find('a')['title']
				ulist.append(title)
	length=len(ulist)	

def main():
	url='http://www.unjs.com/'
	ulist=[]
	html=downloadHtml(url)
	getUniVList(ulist,html)
main()