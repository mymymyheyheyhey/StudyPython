# 리스트 연산
arr = list(range(5))
print(arr)

arr = list(range(1, 6))
print(arr)

arr = list(range(2, 101, 2))
print(arr)

print(arr[0] + arr[5])

# 2차원 배열 리스트
arr2 = [1, 2, ['hey', 'my', 'friend']]
print(arr2)
print(arr2[-1][1])
print(arr2[1])
print(arr2[2][1])
print(arr2[2][1][0])

arr3 = list(range(1, 4))
print(arr3)
print(arr3 * 3)

# 리스트 함수
del(arr3[1]) # 인덱스에 해당하는 값 제거
print(arr3)

arr3.remove(3) # 특정 값 제거
print(arr3)

# 리스트 삭제
arr4 = [1, 2, 3, 3]
arr4.remove(3)
print(arr4)

arr4 = [1, 2, 3, 3]
del(arr4[1])
print(arr4)

arr4 = [1, 2, 3, 3]
arr4.sort() # 튜플은 소트 불가능 리스트 가능
print(arr4)

arr4 = [1, 2, 3, 3]
arr4.reverse()
print(arr4)

arr4 = [1, 2, 3, 3]
arr4.insert(2, 10) # n번 인덱스 자리에 해당 값 삽입 나머지는 뒤로 밀림
print(arr4)

arr4 = [1, 2, 3, 3]
arr4[0] = 100
print(arr4)

tup1 = tuple(range(1, 6))
print(tup1)
print(tup1[3])

# 딕셔너리
dic1 = {1 : 'a'}
dic1[2] = 'b' # 숫자는 key 를 의미/숫자가 딕셔너리에 없으므로 새로 생성, 추가
dic1['name'] = 'John'
print(dic1)
del dic1['name'] # 키를 삭제하면 값도 함께 삭제된다.
print(dic1)

print(dic1.keys()) # 키만 출력
print(dic1.values()) # 값만 출력
print(dic1.items()) # 키와 값 모두 출력

# 리스트를 튜플로 변환
arr4 = [1, 2, 3, 3]
print(arr4)
tup2 = tuple(arr4)
print(tup2)

print(tup1)
arr5 = list(tup1) 
# 튜플은 수정 절대 불가하므로, 리스트로 변환하여 수정 후 다시 튜플로 변환함
print(arr5)
arr5.append(6)
print(arr5)
tup1 = tuple(arr5)
print(tup1)



