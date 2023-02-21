import math

with open('DA014#18.TXT', 'r') as infile, open('DA014#18out.txt', 'w') as outfile:
    # 跳过前200行
    dt=1.32031
    for _ in range(math.floor(dt*2560)):
        next(infile)
    # 逐行读取输入文件的剩余行
    for line in infile:
        # 获取当前行的第一个字)
        first_field = line.split()[0]
        # 将当前行写入输出文件
        outfile.write(line)