# 10-1_reading_from_a_file 文件和异常 读取文件内容 20250620 Stanley Neo

from pathlib import Path

# 读取文件内容并打印
文件路径 = Path('pi_digits.txt')
文件内容 = 文件路径.read_text()
print(文件内容)

# 再次读取文件并按行处理
文件路径 = Path('pi_digits.txt')
文件内容 = 文件路径.read_text()

行列表 = 文件内容.splitlines()  # 移除空行和空白字符
for 行 in 行列表:
    print(行)

# from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()  # remove blank line strips, any whitespace characters
for line in lines:
    print(line)


