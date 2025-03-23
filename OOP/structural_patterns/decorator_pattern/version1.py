# 读取文件内容并输出
file_path = 'example.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
