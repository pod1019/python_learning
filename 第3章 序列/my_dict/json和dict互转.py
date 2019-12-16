'''
在Python语言中，json数据与dict字典以及对象之间的转化，是必不可少的操作。
在Python中自带json库。通过import json导入。
在json模块有2个方法，
loads()：将json数据转化成dict数据
dumps()：将dict数据转化成json数据
load()：读取json文件数据，转成dict数据
dump()：将dict数据转化成json数据后写入json文件
https://www.cnblogs.com/zhaohuanhuan/p/9230583.html
'''
# dict字典转json数据
import json
def dict_to_json():
    dict = {}
    dict['name'] = 'many'
    dict['age'] = 10
    dict['sex'] = 'male'
    print('字典dict是：{0}'.format(dict))
    j = json.dumps(dict)
    print('json数据是：{0}'.format(j))

# # 对象转json数据
# def obj_to_json():
#     stu = Student('007','007',28,'male','13000000000','123@qq.com')
#     print(type(stu))

# json数据转成dict字典
def json_to_dict():
    j  = ' {"id":"007","name":"007","age":28,"sex":"male","phone":"13000000000","email":"123@qq.com"} '
    dict = json.loads(j)
    print(j)
    print(dict)
# dict_to_json()
json_to_dict()