class Employee:
    def __init__(self,name,department,title,salary):
        self.name = name
        self.department = department
        self.title = title
        self.salary = salary
    def testtt(self):
    def test2(self):
    def __repr__(self):
        print(f'<员工{self.name}>')

    def working(self):
        print(f'员工{self.name}在工作...')

class Developer(Employee):
    def __init__(self,name,department,title,salary,skills):
        Employee.__init__(self,name,department,title,salary)
        self.skills = skills

class Accountant(Employee):
    def __init__(self,name,department,title,salary,certification):
        Employee.__init__(self,name,department,title,salary)
        self.certification = certification

if __name__ == '__main__':
    d = Developer('Tom','技术部','高级工程师',13000,['Python','Flask'])
    print(d.name)
    d.working()

    a = Accountant('Mary','财务部','会计员',9000,'会计从业资格证')

    print(a.certification)
    a.working()