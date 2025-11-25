# 字符串加密程序
text = input('请输入：')
secret = ''
for t in text:
    unicode = ord(t)
    secret += chr(unicode + 1)
print(f'{secret}')
# 解密
secret = input('请输入解密：')
text = ''
for s in secret:
    text += chr(ord(s) - 1)
print(f'{text}')