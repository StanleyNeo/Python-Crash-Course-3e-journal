# 10-2_pi_write_message 文件和异常 写消息 20250621 Stanley Neo
from pathlib import Path  # 导入路径处理模块

# 准备要写入的文本内容
内容 = "我喜欢编程。\n"
内容 += "我喜欢开发新游戏。\n"
内容 += "我也喜欢处理数据。\n"
内容 += "我还喜欢Python编程。\n"

# 创建文件路径对象
文件路径 = Path('编程.txt')

# 将内容写入文件
文件路径.write_text(内容, encoding='utf-8')  # 使用UTF-8编码写入文件

from pathlib import Path  # import pathlib module

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
contents += "I also love Python coding.\n"

path = Path('programming.txt')
path.write_text(contents)   # write text to programming.txt file
