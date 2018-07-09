#coding=utf-8
#_author_='yuwei'
#Filename:00_CalHamletV1.py

def getText():
    txt = open("hamlet.txt","r").read()            #打开hamlet.txt文件
    txt = txt.lower()                      #避免大小写对词频统计产生干扰，所有词转为小写，仍然保持在txt变量中
    for ch in '!"#$%&()*+,-./:;<>?@[\\]^_{|}~':
        txt = txt.replace(ch,' ')                           #for in 遍历获取特殊符号，用空格替换特殊符号，仍然保持在txt变量中
    return txt

 #得到归一化结果，所有文本小写。

hamletTxt = getText()        #  对文件进行读取并且归一化
words = hamletTxt.split()     #所有单词是用空格分隔，所以可以使用split，将字符串分隔，以“列表”形式返回给变量，所以words是列表类型，每个元素就是空格分开的单词，
counts = {}                    #建立一个空字典。为了使每个单词与字数对应，所以用字典类型。
for word in words:              #逐一从words列表中取出每一个元素
    counts[word] = counts.get(word,0) + 1         #counts[word]即在counts字典中得到每一个word的值。#遍历words看元素是否在counts中，可以在字典中用.get方法可以键word的值。
    # 用某个单词word作为键索引字典，如果在里面，返回次数，后面+1说明单词后面又出现了一次。如果不在就加到字典中，并给当前赋值0。后面+1，即字典中新增了这个元素。

#词频排序
items = list(counts.items())              #dict.items()以列表返回可遍历的(键, 值) 元组数组   将字典类型转为列表类型便于操作.
items.sort(key=lambda x:x[1],reverse=True)     #指定列表中的元素排序来输出列表   #  .sort是列表中的方法，lambda即使用哪个多元元素列作为排序列，默认方法是从小到大，reverse=True 从大到小

#排序完，信息保存在item中，item[1]即为次数最多的元素

#打印前10及次数。

for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

