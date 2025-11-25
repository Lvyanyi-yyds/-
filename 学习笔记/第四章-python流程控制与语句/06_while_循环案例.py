print('您现在深处迷失，需要正确回答问题，才能逃出密室')
riddle ='你是谁'
answer = '我就是我，不一样的烟火'
guess = ''

while guess != answer:
    print(f'问题：{riddle}')
    guess = input('请输入答案：')
    if guess == answer:
        print('正确')
    else:
        print('错误')