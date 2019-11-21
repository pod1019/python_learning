num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')
#求和
sum = float(num1) + float(num2)
print("数字{0} 和 数字{1}的和是：{2}".format(num1,num2,sum))
2
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data,indent=4)

print(json_str)