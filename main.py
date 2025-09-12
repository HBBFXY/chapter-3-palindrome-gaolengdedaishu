# 这里编写你的代码
# 获取用户输入
num = input("请输入一个5位数字：")
# 输入验证
if not num.isdigit():
    print("错误提示：输入必须是纯数字")
elif len(num) != 5:
    print("错误提示：输入必须是5位数字")
else:
    # 判断是否为回文数
    if num == num[::-1]:
        print("是回文数")
    else:
        print("不是回文数")
