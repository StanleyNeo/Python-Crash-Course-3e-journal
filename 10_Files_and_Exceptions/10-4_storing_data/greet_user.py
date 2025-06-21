# 10-4_greet_user 文件和异常 欢迎用户 20250621 Stanley Neo

from pathlib import Path
import json

# 从JSON文件读取用户名
文件路径 = Path('username.json')
文件内容 = 文件路径.read_text(encoding='utf-8')  # 添加编码参数
用户名 = json.loads(文件内容)

# 打印欢迎信息
print(f"欢迎回来, {用户名}!")

from pathlib import Path
import json


path = Path('username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
