print('Hello, World!')

# 연산자
a = 11
b = 4
print(a + b)
print(a - b)
print(a / b)
print(a // b)
print(a % b)


# 문자열 연산 문자열끼리 + 로 연접 가능, 문자열 * 정수 == 문자열 정수 번 반복
stat1 = 'Hello'
stat2 = 'World'
print(stat1, stat2)
print(stat1 + stat2)
res = stat1 + stat2
print(res)
print(res * 3)
res = stat1, stat2
print(res)
print(type(res))

# 문자열 길이
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

# 문자열 자르기
day = '2022-01-17 14:39:25'
print(day[0:4], '년')
print(day[5:7], '월')
print(day[8:10], '일')

print(day[-8:-6], '시')
print(day[-5:-3], '분')
print(day[-2:], '초')

list_a = [1, 2, 3, 4, 5]
list_a[1] = 19
print(list_a)

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

# 문자열 포맷팅
첫번째 = '투'
두번째 = '유'
str1 = "I'm so happy {0} U.".format('to')
print(str1)

str2 = f"I'm so happy {첫번째} U, are {두번째}?"
print(str2)

# 숫자 천 단위 콤마 붙여 표기
money = 1000000000000
print(format(money, ',d'))

from datetime import datetime

now = datetime.now() # 현재 일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math

pi = math.pi
print(pi)
print('{0}'.format(pi))
print('{0:0.6f}'.format(pi))
print(f'{pi:0.6f}')

full_name = 'Hugo MG Sung'
age = 47
greeting = '''안녕하세요, 
저는 {0}입니다. 나이는 {1}살입니다.'''.format(full_name, age)
print(greeting)

greeting = f'''안녕하세요, 
저는 {full_name}입니다. 나이는 {age:0.3f}살입니다.'''
print(greeting)

part_name = full_name.split()
print(type(part_name))
print(part_name)

test = 'Hey, guys'
print(test.split())

# split 기준 설정
prac = 'TEST|2022|01|17|F45678'
split_codes = prac.split('|')
print(split_codes)

# 단어 교체
print(full_name.replace('Hugo MG', 'John'))

# strip 공백 완전 제거
aaa = '            Hello, World!     sd     '         
print(aaa)
print(aaa.lstrip())
print(aaa.rstrip())
print(aaa.strip()) # 좌우 공백 완전 제거

print(full_name.index('H'))
print(full_name.index('u'))
print(full_name.find('x')) # 결과 값 -1 : 찾는 글자가 없다는 뜻
print(full_name.find('MG'))

print('-'.join(full_name))
print(full_name.lower())
print(full_name.upper())
print(full_name.title())
print('&'.join(full_name))

