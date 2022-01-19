# 내가 작성한 답안 (합격)
start, last = map(int, input().split())

lis = list(2 ** j 
for j in range(start, last + 1) if j != start + 1 and j != last - 1)

print(lis)


# 예시 답안
# start, last = map(int, input().split())

# lis = [2 ** j for j in range(start, last + 1)]
# del lis[1]
# del lis[-2]

# print(lis)
