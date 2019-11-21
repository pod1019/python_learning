''''''
'''已知点的坐标(x,y)，判断其所在的象限'''


raw_x = input('请输入x坐标：')
raw_y = input('请输入y坐标：')
x = int(raw_x)
y = int(raw_y)

area = ''

if x>0 and y>0:
    area = '第一象限'
elif x<0 and y>0:
    area = '第二象限'
elif x<0 and y<0:
    area = '第三象限'
elif x>0 and y<0:
    area = '第四象限'

else:
    print('此点是原点！')

print(f"你输入的坐标是({x},{y}),此点在：{area}")