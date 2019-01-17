from xml.etree import ElementTree

import requests
import re
from src.dy import db

def prettyXml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if element.text == None or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
        # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将elemnt转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


baseUrl = 'https://www.douyu.com/g_LOL'
baseUrl = 'https://www.douyu.com/252140'
# webbrowser.open('https://www.douyu.com/g_LOL')
res = requests.get(baseUrl)
text = res.text

print(text)
# print(res.text[20:len(text)])
# r'(.*) are (.*?) .*'   (<a class="play-list-link")(.*)</a>
searchObj = re.search(
    r'<a class="play-list-link"([\s\S]*?)data-sub_rt="0" href="/([\s\S]*?)" title=([\s\S]*?)<span class="dy-name ellipsis fl">([\s\S]*?)</span>([\s\S]*?)<span class="dy-num fr"  >([\s\S]*?)</span>([\s\S]*?)</a>',
    text, re.M | re.DOTALL)  # 在起始位置匹配
print(searchObj.group())
import time
time = round(time.time())
while searchObj and (searchObj.end() > 0):
    end = searchObj.end()

    uid = searchObj.group(2)
    name = searchObj.group(4)
    pNum = searchObj.group(6)
    pNum = pNum[0:pNum.__len__() - 1]
    # print("searchObj.group(2) : ", searchObj.group(2))
    # print("searchObj.group(4) : ", searchObj.group(4))
    # print("searchObj.group(6) : ", searchObj.group(6))
    #db.db_insert(uid,name,pNum,time)
    text = text[end:text.__len__()]
    searchObj = re.search(
        r'<a class="play-list-link"([\s\S]*?)data-sub_rt="0" href="/([\s\S]*?)" title=([\s\S]*?)<span class="dy-name ellipsis fl">([\s\S]*?)</span>([\s\S]*?)<span class="dy-num fr"  >([\s\S]*?)</span>([\s\S]*?)</a>',
        text, re.M | re.DOTALL)  # 在起始位置匹配
    pass

    # print("searchObj.group(1) : ", searchObj.group(1))
    # print("searchObj.group(2) : ", searchObj.group(2))
    # print("searchObj.group(3) : ", searchObj.group(3))
    # print("searchObj.group(4) : ", searchObj.group(4))

# tree = ElementTree.dump('<a><a/>')  # 解析test.xml这个文件，该文件内容如上文
# root = tree.getroot()  # 得到根元素，Element类
# root = ElementTree.fromstring(text)

# prettyXml(root, '\t', '\n')  # 执行美化方法
# ElementTree.dump(root)
