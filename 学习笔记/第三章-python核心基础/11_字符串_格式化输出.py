name = '张三'
gender = '男'
weight = 65.2
age = 12
# 写法一加号拼接，只能是字符串
info1 = '我叫' + name + '我是' + gender + '生'
print(info1)
# 写法二：使用占位符 s = str f =float i = int
info2 = '我叫%s,我是%s生' % (name,gender)
print(info2)
# 写法三：使用f-string
info3 = f'我叫{name},我是{gender}生'
