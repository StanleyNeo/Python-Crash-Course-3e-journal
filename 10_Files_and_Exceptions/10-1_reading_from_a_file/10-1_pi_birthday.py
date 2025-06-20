# 10-2_pi_birthday 文件和异常 生日出现在π 20250620 Stanley Neo

from pathlib import Path

# 读取包含π百万位数的文件
文件路径 = Path('pi_million_digits.txt')
文件内容 = 文件路径.read_text()

# 处理文件内容
行列表 = 文件内容.splitlines()
π字符串 = ''
for 行 in 行列表:
    π字符串 += 行.lstrip()  # 移除每行左侧的空白字符

# 检查生日是否在π的前百万位中
生日 = input("请输入您的生日，格式为月日年(如010199): ")
if 生日 in π字符串:
    print("您的生日出现在π的前百万位数字中！")
else:
    print("您的生日没有出现在π的前百万位数字中。")

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
