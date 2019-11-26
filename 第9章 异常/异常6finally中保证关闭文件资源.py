# 读取文件，finally中保证文件资源
try:
    f = open("d:/a.txt","r")
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
finally:
    # f.close() # 由于文件不存在，所以f.close也报异常，所以也可以在finally中捕获异常，如下：
    try:
        f.close()
    except:
        print("文件未找到")

print("step4")