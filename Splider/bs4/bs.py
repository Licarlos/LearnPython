import requests
from bs4  import BeautifulSoup 

def downloadHtml(url):
	try:
		headers={'User-Agent':'Mozilla/5.0'}
		res=requests.get(url,headers=headers)
		res.raise_for_status()
		res.encoding=res.apparent_encoding

		soup=BeautifulSoup(res.text,'html.parser')
		print(soup.find(id='cb_post_title_url'))
		pass
	except Exception as e:
		print("抓取失败")
	pass

	
url='http://www.cnblogs.com/wayneye/archive/2010/05/03/1726865.html'
downloadHtml(url)

