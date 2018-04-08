import lxml
from lxml import etree
from lxml import html
class Lxmal_sample(object):
    """docstring for lxmal_sample"""
    def __init__(self):
        super(Lxmal_sample, self).__init__()
        self.path="F:\\Projects\\Learning\\src\\Zj.PythonDemo\\src\\lxmal\\test.html"
        self.html=open(self.path,'rb').read()
        print(self.html)
    def show(self):
        # print(dir(etree))
        tree=etree.HTML(self.html)
        # selector=tree.xpath('//li[@class="commit-row"]')
        # print(selector)
        pass
def main():
    Lxmal_sample().show()
    pass
if __name__ == '__main__':
    main()


