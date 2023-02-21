import os

# 所有txt文件所在的文件夹路径
folder_path = os.path.dirname(os.path.abspath(__file__))

# 存储所有txt文件中的数据
data = {}

# 遍历文件夹中的所有txt文件，读取数据并存储
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename)) as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i in data:
                    data[i].append(line.strip())
                else:
                    data[i] = [line.strip()]

# 将数据写入新的txt文件
with open('merged.txt', 'w') as f:
    # 写入标题行，使用对应列数据所在的文件名
    f.write('\t'.join([os.path.splitext(filename)[0] for filename in os.listdir(folder_path) if filename.endswith('.txt')]))
    f.write('\n')
    
    # 写入所有数据
    for i in range(len(data)):
        f.write('\t'.join(data[i]))
        f.write('\n')
