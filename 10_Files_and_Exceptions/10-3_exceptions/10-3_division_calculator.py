# 10-3_division_calculator 文件和异常 异常处理 20250621 Stanley Neo
print("请给我两个数字，我将进行除法运算。")
print("输入'q'退出程序。")

while True:
    # 获取第一个数字输入
    第一个数字 = input("\n第一个数字: ")
    if 第一个数字 == 'q':
        break

    # 获取第二个数字输入
    第二个数字 = input("第二个数字: ")
    if 第二个数字 == 'q':
        break

    try:
        # 尝试执行除法运算
        结果 = int(第一个数字) / int(第二个数字)
    except ZeroDivisionError:
        # 处理除零错误
        print("除数不能为0！")
    except ValueError:
        # 处理非数字输入错误
        print("请输入有效的数字！")
    else:
        # 正常情况下的输出
        print(f"计算结果: {结果}")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)