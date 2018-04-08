import re
def reDemo():
    pattern=re.compile(r'world')
    match= pattern.search('helloworld',3,10)
    # match 
    print('string:{},re:{},po:{},endPo:{},start:{},end:{}'.format(match.string,match.re,match.pos,match.endpos,match.start(),match.end()))
    if match:
        print(match.group(0))
        pass
    pass

    # search
    match=re.search(r'world','helloworld')
    print(match.group(0))
    # split
    rt=re.split(r'\d{1}','aha3')
    print(rt)
    match_=re.match(r'\w','aha33')
    print(match_.group(0))
    # sub 替换
    rt_=re.sub(r'\d','_','aha3')
    print(rt_)
    #findall
    rt__=re.findall(r'\w','aha3')
    print(rt__)

    # p=r'[0-9]\d{5}'
    # m=re.search(p,'BIT 100086 BIT 100087')
    # if m:
    #     print(m.group(0))
    #     pass
    # 贪婪匹配
    # p=r'P[A-Z]+N'
    # m=re.search(p,'PNJJJNABCN')
    # if m:
    #     print(m.group(0))
    #     pass
    # 最小匹配
    p=r'P.*?N'
    m=re.search(p,'PNJJJNABCN')
    if m:
        print(m.group(0))
        pass
def main():
    reDemo()
    pass

main()