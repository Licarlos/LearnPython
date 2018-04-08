import urllib
import chardet

url='http://www.ruanmou.net/'
local="F://git/Zj.PythonDemo/src/a.html"
# html=urllib.urlopen(url)

# print html.info()
# print html.getcode()
# print html.read()

# print help(urllib) 
# print html.info().getparam("charset")

# urllib.urlretrieve(url ,local)

def automac_detect(a,b,c):

  print  "%.2f%%"%( 100*(a*b/c))

urllib.urlretrieve(url ,local,automac_detect)


content=urllib.urlopen(url).read()

charset=chardet.detect(content)
print charset["encoding"]

