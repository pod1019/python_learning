'''#二进制文件的处理流程和文本文件流程一致。首先还是要创建文件对象，不过，我们需要指
定二进制模式，从而创建出二进制文件对象
'''

with open ('Penguins.jpg','rb') as f: # 先读取二进制文件Penguins.jpg
    with open('Penguins.copy.jpg','wb') as w: # 再把上面读取的文件写入新的文件Penguins.copy.jpg中
        for line in f.readlines():
            w.write(line)

print('图片拷贝完成！...')