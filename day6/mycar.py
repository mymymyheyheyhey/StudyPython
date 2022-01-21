# class
from vehicle import car

if __name__ == '__main__':
    mycar = car('29허3385', 'Black')
    mycar.cnumber = '29허3385'
    mycar.colour = 'Black'
    mycar.fuel = 'gasoline'
    mycar.__company = 'Rolls Royce'
    mycar.year = 2020
    mycar.levels = 7

mycar.forward(3)
print(mycar)
print(f"이 차의 최대 기어는 {mycar.levels}단 입니다.")

mycar.setcompany('KIA')
mycar.companyname()
