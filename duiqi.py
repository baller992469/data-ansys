# 打开文件
with open("merged.txt", "r") as f:
    # 逐行读取，从第二行开始
    lines = f.readlines()[1:]

# 将每行数据拆分为一个列表
data = [line.strip().split() for line in lines]

# 找到最短的行长度
min_length = max([len(row) for row in data])

# 删除多余的行，只保留最小行数之内的数据
data = [row for row in data if len(row) == min_length]

# 将结果写入新的txt文件
with open("new_filename.txt", "w") as f:
    for row in data:
        f.write(" ".join(row) + "\n")
