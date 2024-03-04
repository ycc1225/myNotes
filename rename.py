import os
import re

# 定义匹配规则和替换规则
pattern = re.compile(r'!\[\d+\]\(./imgs/')
replacement = '![](./imgs/'

# 遍历当前文件夹
for root, dirs, files in os.walk('.'):
    for filename in files:
        # 只处理扩展名为 .md 的文件
        if filename.endswith('.md'):
            filepath = os.path.join(root, filename)
            # 打开文件并进行替换
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(pattern, replacement, content)
            # 将替换后的内容写回文件中
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)