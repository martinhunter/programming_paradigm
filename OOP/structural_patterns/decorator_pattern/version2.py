# 读取文件内容并输出，同时统计行数和字数
file_path = 'example.txt'
line_count = 0
word_count = 0
with open(file_path, 'r') as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        print(line, end='')
print(f'\nTotal lines: {line_count}')
print(f'Total words: {word_count}')
