# 来自https://cloud.tencent.com/developer/article/1456912
# Python——三级菜单（字典＋文件读写）

current_layer_len = 4  #第一层省份编码长度是4位数
parent_layer = '10'   #父层编码初始值取编码前2位，也就是10.  输入下一级城市时，城市编码增加2位，父层编码就是切片城市编码［:－2］

with open('user22222222.txt', 'r',encoding='utf-8') as f:
    menu = f.read()
menu = eval(menu)

while True:
    current_layer = {key:value for key,value in menu.items() if len(key) == current_layer_len and key.startswith(parent_layer)}
    #取出相应位数编码的城市。
    print('The current layer of cities：')
    for i in current_layer:
        print(current_layer[i])
    choice = input('Please input the district(press b/q／d/c/a to back or quit or delete or change or append):').strip()
    if len(choice) == 0:continue
    if choice in current_layer.values():
        parent_layer = list(current_layer.keys())[list(current_layer.values()).index(choice)]
        # print(parent_layer) 字典无序，转换成列表，然后根据输入的城市的序号，获取当前城市的编码
        current_layer_len += 2
    elif choice == 'b':#返回上一层
        if current_layer_len-2:
            current_layer_len -= 2
            parent_layer = parent_layer[:-2]
    elif choice == 'd':#删除当前城市（如有下级一并删除）
        choice2=input('Please input the city you want to delete:'.strip())
        if choice2 in current_layer.values():
            for key in menu:
                if menu[key] == choice2:
                    sub_code=key
                    break
            sub_code2=[]
            for key in menu:
                if key.startswith(sub_code):
                    sub_code2.append(key) 
                    #如果要删的城市有子集，要全部删掉，比如要删1002天津，那就把1002开头的所有下级城市，一并删除，那也就是要汇集这些城市的序号。
            for code in sub_code2:
                del menu[code]
            continue
        else:
            print('invalid input!!!')
    elif choice == 'c':#修改当前城市名称
        choice2 = input('Please input the city you want to change:'.strip())
        if choice2 in current_layer.values():
            choice3 = input('Please input the result:'.strip())
            for key in menu:
                if menu[key] == choice2:
                    sub_code=key
                    break
            menu[sub_code]=choice3
            continue
        else:
            print('invalid input!!!')
    elif choice == 'a':#增加新城市
        choice2 = input('Please input the city you want to append current layer:'.strip())
        if choice2 in current_layer.values():
            print(f'{choice2} exists!!!')
        else:
            append_max_code = 0
            for sub_code in current_layer:
                if int(sub_code) > append_max_code:
                    append_max_code = int(sub_code) # 取当前层城市编码最大值
            append_max_code += 1
            #要增加一个新城市，同样，要编一个序号，取该级别下的最大序号，再加1，作为新城市的序号。
            menu[str(append_max_code)]=choice2
            continue
    elif choice == 'q':#退出并存盘数据。
        with open('district_database', 'w') as f:
            f.write(str(menu))# 按q退出时，再将最终结果写入文本中。
        break
    else:
        print('invalid input,try again please')


#初始化 将menu存入磁盘中
menu = {'北京':{
    '朝阳':{
        '国贸':{
            'CICC':{},
            'HP':{},
            '渣打银行':{},
            'CCTV':{}
        },
        '望京':{
            '陌陌':{},
            '奔驰':{},
            '360':{}
        },
        '三里屯':{
            '优衣库':{},
            'apple':{}
        }
    },
    '昌平':{
        '沙河':{
            '老男孩':{},
            '阿泰包子':{}
        },
        '天通苑':{
            '链家':{},
            '我爱我家':{}
        },
        '回龙观':{}
    },
    '海淀':{
        '五道口':{
            '谷歌':{},
            '网易':{},
            'Souhu':{},
            'Sogo':{},
            '快手':{}
        },
        '中关村':{
            'youku':{},
            'Iqiyi':{},
            '汽车之家':{},
            '新东方':{}
        }
    }
},
        '上海':{
            '浦东':{
                '陆家嘴':{
                    'CICC':{},
                    '高盛':{},
                    '摩根':{}
                },
                '外滩':{}
            },
            '闵行':{},
            '静安':{}
        },
        '山东':{
            '济南':{},
            '德州':{
                '乐陵':{
                    '丁务镇':{},
                    '城区':{}
                },
                '平原':{}
            },
            '青岛':{}
        }
}
a=str(menu)
with open('menu','w',encoding='utf8') as f:
    f.write(a)
#读取menu
with open('menu','r',encoding='utf8') as f:
    menu=eval(f.read().strip())
parent_layers=[]
current_layer = menu
while True:
    print('欢迎使用省市查询系统'.center(50,'*'))
    for key in current_layer:
        print('>>>',key)
    print('输入你要查询的地区省市或新增[add]、修改[revise]、删除[delete]、返回上一级[q]')
    choice = input('>>>').strip()
    #查询
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    #新增
    elif choice == 'add':
        user_add = input('请输入你要添加的省市区:').strip()
        if user_add in current_layer:
            print('此项已存在，请重新输入')
        else:
            current_layer[user_add]={}
            continue
    #修改
    elif choice =='revise':
        user_revise = input('请输入要修改的省市区:').strip()
        if user_revise in current_layer:
            user_revise_after = input('修改为:').strip()
            current_layer[user_revise_after]=current_layer[user_revise]
            del current_layer[user_revise]
            continue
    #删除
    elif choice =='delete':
        user_delete = input('请你输入要删除的省市区:').strip()
        if user_delete in current_layer:
            parent_layers.append(current_layer)
            del current_layer[user_delete]
            continue
        else:
            print('此项不存在，请重新输入:')
    #返回上一级或退出
    elif choice == 'q':
        if parent_layers:
            current_layer = parent_layers.pop()
        else:
            print('目前为最上级菜单，输入q后为退出系统！')
            print(type(current_layer))
            break
    else:
        print('输入非法，请重新输入选择！')
if type(current_layer) != list:
    with open('menu','w',encoding='utf8') as f:
        f.write(str(current_layer))