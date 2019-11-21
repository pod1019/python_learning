class CellPhone:
    def __init__(self,brand,price=0.0):
        self.brand = brand
        self.price = price

    def on(self):
        print('{} 手机开机...'.format(self.brand))

    def send_message(self,to,message):
        print(f'{self.brand} 给 {to} 发送短信：{message}')

c = CellPhone('iPhone 6S',5800.0)
c2 = CellPhone('小米 5',2900)



