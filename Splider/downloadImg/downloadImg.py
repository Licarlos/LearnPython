import requests
import os
def downloadImg(url,path):
	
	try:
		headers={'User-Agent':'Mozilla/5.0'}
		res=requests.get(url,headers=headers)
		res.raise_for_status()
		res.encoding=res.apparent_encoding

		imgpath=url.split('/')[-1]
		# if (not os.path.exists(path)):
		# 	os.mkdir(path)
		# 	pass
		# imgpath=path+'/'+imgpath	
		# if (not os.path.exists(imgpath)): 
		# 	os.mknod(imgpath)             
		# 	pass
		with open(path+'/'+imgpath,'wb') as fs:
			print(path+'/'+imgpath,'wb');
			fs.write(res.content)
		fs.close()	
		print("抓取成功")
		pass
	except Exception as e:
		print("抓取失败")
	pass



imgUrl='https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/newmusic/img/default_8a5b42b2.png'
downloadImg(imgUrl,'d:');