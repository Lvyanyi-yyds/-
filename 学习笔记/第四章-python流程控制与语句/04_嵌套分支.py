age = int(input('请输入你的年龄：'))
has_report = input('您是否提交了体检报告？(是/否)')
level = int(input('请输入你的会员等级 (1/2/3)'))
print('*****情绪识别如下*****')
if 18 <= age <= 45:
    print('您的年龄符合比赛要求')
    if has_report == '是':
        print('您已提交体检报告')
        print('您可以参加比赛')
        if level ==1:
            print(f'尊敬的{level}会员，一份')
        elif level ==2:
            print(f'尊敬的{level}会员，两份')
        elif level ==3:
            print(f'尊敬的{level}会员，三份')
    elif has_report =='否':
        print('您未提交体检报告')
else:
    print('抱歉不符合')