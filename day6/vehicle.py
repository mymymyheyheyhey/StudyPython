# class

class car:
    year = 2020
    __company = 'Rolls Royce'
    cnumber = '29허3385'
    colour = 'Black'
    fuel = 'gasoline'
    
    def __init__(self, cnumber, colour):
        self.cnumber = cnumber
        self.colour = colour      

    def __str__(self) -> str:
        return f"이 차는 {self.year}년도에 생산되었습니다. {self.fuel}을 연료로 주행합니다."

# private
    def setcompany(self, company):
        self.__company = company

    def companyname(self):
        print(f"이 차량의 제조사는 {self.__company}입니다.")


    def forward(self, level):
        print(f"{self.colour}차가 {level}단으로 전진합니다.")

    def backward(self):
        print('후진')

    def rightward(self):
        print('우회전')

    def leftward(self):
        print('좌회전')

    def brake(self):
        print('정지')


