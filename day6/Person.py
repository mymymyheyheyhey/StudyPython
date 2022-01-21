# class

class Person:
    name = ''
    age = 0
    height = 0
    gender = ''
    feetsize = 250
    bloodtype = ''


# 생성자
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print('Person이 생성되었습니다.')

    def introduce(self):
        print(f"안녕, 내 이름은 {self.name} 라고 해.")

    def eat(self, food):
        print(f"{self.name}가 {food}을 먹는다.")

    def work(self, tool):
        print(f"{self.name}가 {tool}을 가지고 일한다.")



#===========================================================================

if __name__ == '__main__':
    ng = Person('Noel Gallagher', 54) # == __init__(self, name, age):
    ng.name = 'Noel Gallagher'
    ng.age = 54
    ng.bloodtype = 'O'
    ng.feetsize = 240
    ng.gender = 'male'
    ng.height = 174

    ng.eat('Potato chips')
    ng.work('Acoustic guitar')
    ng.introduce()

 
 
    # p = Person() # p라는 이름을 가진 객체 생성
    # print(type(p))
    # print(id(p)) # id 값

    # p2 = Person
    # print(type(p2))
    # print(id(p2))

