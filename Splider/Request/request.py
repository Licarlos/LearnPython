import requests
# res.encoding=res.apparent_encoding


# if res.status_code!=200:
# 	return
def download_html(url):
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Content-Type':'Utf-8'}
		res=requests.get(url,headers=headers)
	    # res.raise_for_status()
		res.encoding=res.apparent_encoding
		# print(res.raise_for_status())
		print(res.text)
	except Exception as e:
		print("抓取异常")

download_html("https://www.jd.com/")
