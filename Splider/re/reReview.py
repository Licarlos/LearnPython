import re
class reDemo(object):
    """docstring for reDemo"""
    def __init__(self):
        super(reDemo, self).__init__()
    def show(self):
        rt=re.findall(r'st.','ststr')
        print(rt)
        pass
def main():
    reDemo().show()
    pass
if __name__ == '__main__':
    main()
