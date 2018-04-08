import requests

def downloadHtml(url,params):
	try:
		headers={'User-Agent':'Mozilla/5.0'}
		res=requests.get(url,headers=headers,params=params)
		res.raise_for_status()
		res.encoding=res.apparent_encoding
		print(res.text[:1000])
		print(res.request.url)
		print(res.content)
		pass
	except Exception as e:
		print("抓取失败")
	pass


# downloadHtml("https://item.jd.com/5105026.html","");#京东

# downloadHtml("https://www.amazon.cn/dp/B01N772TPF/ref=cngwdyfloorv2_recs_0?pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=1QY7XH4KKWQ33YRNZHCM&pf_rd_r=1QY7XH4KKWQ33YRNZHCM&pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061","");#亚马逊

# downloadHtml("http://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=8DDC54D5FCA20702&rsv_spt=1&rsv_iqid=0xda09e3f1000449af&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_t=fb1fmokloziB6%2BWGPU6zzvBJ4gOq%2FTZPtMPXYh8QQOIosYeKb%2F2otCCsJRdASfBr8yVR&inputT=8418&rsv_sug4=8921&rsv_sid=1457_24866_21086_20697_24879_22157&_ss=1&clist=6d46e6a39fa01277&hsug=&f4s=1&csor=2&_cr1=33115",{'wd':'看看'})#百度

# downloadHtml("https://www.so.com/s?src=srp&fr=se7_toolbar&psid=246ed4f3ac995c8c2cfee17e90c2d5db",{'q':'看看'})#360搜索
downloadHtml("https://www.so.com/s?src=srp&fr=se7_toolbar&psid=246ed4f3ac995c8c2cfee17e90c2d5db&q="+'看看',"")#360搜索
