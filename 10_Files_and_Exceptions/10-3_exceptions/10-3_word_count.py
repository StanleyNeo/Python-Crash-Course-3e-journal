# 10-3_word_count 文件和异常 字数统计 20250621 Stanley Neo

from pathlib import Path

def 统计字数(文件路径):
    """统计文件中大约的字数"""
    try:
        内容 = 文件路径.read_text(encoding='utf-8')
    except FileNotFoundError:
        # 文件不存在时静默处理
        pass
    else:
        # 计算文件中单词的大致数量
        单词列表 = 内容.split()
        单词数量 = len(单词列表)
        print(f"文件 {文件路径} 大约包含 {单词数量} 个单词。")

# 要统计的文件列表
文件列表 = [
    'alice.txt',
    'siddhartha.txt',
    'moby_dick.txt',
    'little_women.txt'
]

# 对每个文件进行字数统计
for 文件名 in 文件列表:
    文件路径 = Path(文件名)
    统计字数(文件路径)

from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
        'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)