#encoding:utf-8
import os, re, codecs

# 定义正则表达式模式
pattern = re.compile(r'new "[^\u4e00-\u9fa5\n]*"')
g = open("未翻译的tl文本.txt", "w", encoding='utf-8')

# 遍历指定目录下的所有文件
for root, dirs, files in os.walk("../../Brothel_King-v0.3t-Chinese/tl/schinese"):
    for file in files:
        if file.endswith('.rpy'):
            file_path = os.path.join(root, file)
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
                # 遍历文件的每一行
                for line_num, line in enumerate(lines, start=1):
                    # 使用正则表达式匹配行
                    match = pattern.search(line)
                    if match:
                        # 输出匹配的行（包括行号）
                        g.write(f'{file}:{line_num}: {line.strip()}\n')
