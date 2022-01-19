# 예외 처리

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    res = a / b
    return res

print('사칙연산 시작')

a, b = 4, 1
numbers = [3, 6, 9]

try:
    print(f"나눗셈 결과: {divide(a, b)}")
    res = int(numbers[1]) * 8
    num = int(input('수를 입력하세요'))

except ZeroDivisionError as e:
    print(f"나눗셈 예외 {e}")
except IndexError as e:
    print(f"인덱스 예외 {e}")
except ValueError as e:
    print(f"숫자를 입력하세요.")

finally:
    print(f"곱셈 결과: {multi(a, b)}")
    print(f"뺄셈 결과: {minus(a, b)}")
    print(f"덧셈 결과: {add(a, b)}")

print('사칙연산 종료')


# try:
#     예외 발생(가능) 코드
# except 발생 예외:
#     예외 발생 시 처리 코드
# finally:
#     예외 발생하여도 반드시 수행할 코드





