''''''
# '''打印如下图案'''
#
# for i in range(0,5):
#     for j in range(0,5):
#         print(i,end=' ')
#     print()

'''99乘法表'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{0} * {1} = {2}'.format(j,i,(j*i)),end='\t')
    print()