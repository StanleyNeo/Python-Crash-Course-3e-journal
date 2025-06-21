# 10-1_pi_string 文件和异常 π字符串 20250620 Stanley Neo

from pathlib import Path

# 读取包含π百万位数的文件
文件路径 = Path('pi_million_digits.txt')
文件内容 = 文件路径.read_text()

# 处理文件内容
行列表 = 文件内容.splitlines()
π字符串 = ''
for 行 in 行列表:
    π字符串 += 行.lstrip()  # 移除每行左侧的空白字符

# 打印π的前50位和字符串长度
print(f"{π字符串[:52]}...")
print(f"字符串长度: {len(π字符串)}")

from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
