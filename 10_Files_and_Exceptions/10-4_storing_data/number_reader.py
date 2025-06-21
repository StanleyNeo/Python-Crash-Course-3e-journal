# 10-4_number_reader 文件和异常 数据读取 20250621 Stanley Neo

from pathlib import Path
import json

# 定义JSON文件路径
文件路径 = Path('numbers2.json')

# 读取文件内容
文件内容 = 文件路径.read_text(encoding='utf-8')  # 添加编码参数确保正确处理中文

# 解析JSON数据
数字列表 = json.loads(文件内容)

# 打印解析后的数字列表
print(数字列表)

from pathlib import Path
import json

path = Path('numbers2.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
