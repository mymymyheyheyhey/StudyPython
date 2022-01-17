# 변수 - 파이썬 변수 제약 적음
a = '헬로'
print(a)

a = 3.14
print(a)

a = 10
print(a)

a = 99999999999999
print(a)

a = 1 / 10
print(a)

# How to assign variable
a = 3
b = 3.14
c = 'python'
d = (1, 2, 3) # 튜플
e = [1, 2, 3, 4] # 리스트
f = [7, '8', '$', a] # a에 3을 할당하였으므로 f 출력 시 a 자리에 3이 온다

# 변수명
val = 10
val2 = 20
# 4val = 40 # 숫자는 올 수 있지만 가장 첫 자리에는 올 수 없다
# val$ = 99 # 특수문자는 아예 넣을 수 없다.
# -val = 50 # 특수문자는 아예 넣을 수 없다.
# *val = 19 # 특수문자는 아예 넣을 수 없다.

val11 = 11
Val11 = 12 # 대소문자 구분한다 서로 다르다.

# 변수 타입
print(type(c))
print(type(d))
print(type(f))
print(type(0.1))

