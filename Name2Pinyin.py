#coding:utf-8

from xpinyin import Pinyin

p = Pinyin()
filename = input('输入需要转换的文件名:')
savefile = open('save.txt','w')
parame = set()
with open(filename) as f:
	for i in f.readlines():
	    result = p.get_pinyin(i)
	    s = result.split('-')
	    result3 = s[0] + ''.join(s[1:])
	    print(result3.strip())
	    parame.add(result3.strip())

for i in parame:
	savefile.write(i + "\n")

print("#"*50)
print('文件转换成功，输出文件(结果已去重) --> save.txt')
savefile.close()
