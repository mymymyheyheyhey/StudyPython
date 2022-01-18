# for

arr = list(range(1, 100))
print(arr)

for i in arr:
    print(f"{i:0.2f}")
    
# tuple for
arr2 = 'me', 'my', 'friend', 'Jane'
print(type(arr2))

for item in arr2:
    print(f"{item:>10}")


# 합계 for
numbers = list(range(1, 21, 2))
res = 0
for i in numbers:
    res += i

print(f"{numbers[0]} 부터 {numbers[-1]} 까지의 총 합은 {res} 입니다.")



numbers = list(range(1, 21))
for item in numbers:
    if item % 2 == 0:
        print(f"{item}은 짝수")


# break 13 이상
numbers = list(range(1, 21))
for item in numbers:
    if item > 12:
        break

    if item % 2 == 0:
        print(f"{item}은 짝수")

# continue
numbers = list(range(1, 21))
for item in numbers:
    if item == 15:
        continue

    if item % 2 == 1:
        print(f"{item}은 홀수")



# 구구단
for i in range(2, 10):
    if i == 8:
        continue
    print(f"{i}단 시작")

    for j in range(1, 10):
        print(f"{i} x {j} = {i * j:2d}", end = ' ')
    print() # 줄 바꿈



for i in range(4):
    for j in range(3):
        print('*', end = ' ')
    print() # == print('')


a = [1, 2, 3, 4]
result = [i * 3 for i in a]
print(result)

t = []
for i in a:
    t.append(i * 3)

print(t)

    


