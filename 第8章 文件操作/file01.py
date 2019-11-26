#使用with管理文件写入操作
s = ["高一\n","高二\n","高三\n"]
with open (r"E:\mypy\第8章文件操作\bb.txt","w",encoding="utf-8") as f:
    f.writelines(s)


