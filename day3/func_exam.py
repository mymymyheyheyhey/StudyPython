# 함수 선언 및 사용

# 더하기 함수 선언
def add(a, b):
    res = a + b
    return res

# 함수 사용
print(add(54321, 1))

mid_val = add(3, 4)
print(mid_val * 3)

# 함수의 종류
def say_hello():
    return 'HELLO'

print(say_hello())

val = say_hello()
print(val.replace('O', ''))

# 결과 값이 없는 형태
def say_hello(name):
    print(f"HELLO, {name}")
    # return None 생략되어 있음/함수는 반드시 return을 갖는다.

say_hello('John')

# 둘 다 없는 경우
def say_goodbye():
    print('Bye')

say_goodbye()

# 매개변수 지정
def multi(a, b):
    return a * b

print(multi(3, 4))

# 매개 변수의 개수가 가변적일 때
def plus(*args):
    res = 0
    for i in args:
        res += i

    return res

print(plus(1))
print(plus(1, 2, 3))
print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 리턴 값이 2개 이상
def mul_and_div(x, y):
    mul = x * y
    div = x / y

    return (mul, div) # tuple

res1, res2 = mul_and_div(7, 8)
print(res1, res2)

def 사칙연산(x, y):
    return (x + y, x - y, x * y, x / y)

res1, res2, res3, res4 = 사칙연산(9, 5)

print(res1, res2, res3, res4)
print(type(사칙연산(1, 2)))


