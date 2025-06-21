# 10-4_number_writing 文件和异常 数据写入 20250621 Stanley Neo
from pathlib import Path
import json

# 定义两组数字列表
数字列表1 = [2, 3, 5, 7, 11, 13]
数字列表2 = [2, 3, 5, 7, 11, 13, 15, 8, 0]

# 创建Path对象
文件路径1 = Path('numbers.json')
文件路径2 = Path('numbers2.json')

# 将列表转换为JSON格式字符串
json内容1 = json.dumps(数字列表1)
json内容2 = json.dumps(数字列表2)

# 将内容写入文件
文件路径1.write_text(json内容1, encoding='utf-8')
文件路径2.write_text(json内容2, encoding='utf-8')

print(f"已创建文件: {文件路径1} 和 {文件路径2}")

from pathlib import Path
import json


numbers = [2, 3, 5, 7, 11, 13]
numbers2 = [2, 3, 5, 7, 11, 13, 15, 8, 0]
path = Path('numbers.json')
path = Path('numbers2.json')
contents = json.dumps(numbers)
contents2 = json.dumps(numbers2)
path.write_text(contents)
path.write_text(contents2)
