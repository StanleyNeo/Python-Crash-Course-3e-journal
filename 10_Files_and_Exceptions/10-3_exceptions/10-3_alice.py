# 10-3_alice 文件和异常 爱丽丝 20250621 Stanley Neo

from pathlib import Path

# 定义文件路径
文件路径 = Path('alice.txt')

try:
    # 尝试读取文件内容(使用UTF-8编码)
    文件内容 = 文件路径.read_text(encoding='utf-8')
except FileNotFoundError:
    # 文件不存在时的处理
    print(f"抱歉，文件 {文件路径} 不存在。")
else:
    # 计算文件中单词的大致数量
    单词列表 = 文件内容.split()
    单词数量 = len(单词列表)
    print(f"文件 {文件路径} 大约包含 {单词数量} 个单词。")

from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")