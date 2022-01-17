# 자료형
print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))

# 숫자형
금액 = 12_345_666
print(금액) # '_'는 숫자에 사용하면 표시되지 않음(시각적 구분 위해 사용)

# 문자열
bruce_eckel = 'Life is short, You need Python'
print(bruce_eckel)

bruce_eckel = 'Life is short,\nYou need Python'
print(bruce_eckel)

bruce_eckel = '''Life is short,
You need Python'''
print(bruce_eckel)

# 불형 Boolean
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 1001)

bl_true = True
print(bl_true)
print(type(bl_true))
print(bl_true == True)
print(bl_true is True)

print(a is None) # True
print(val_sum is 1000) # True

# 의미가 있는 bool
print(bool(1)) # True
print(bool(0)) # False

# list
b = [1, 2, 3, 4, 5, 6, 7]
print(b)

bruce_eckel = 'Life is short, You need Python'
arr2 = [bruce_eckel.split()]
print(arr2)
print(type(arr2))

arr3 = [[1, 2, 3], [4, 5, 6]]
print(arr3)
print(type(arr3))

# 빈 리스트
arr4 = list()
print(arr4)
print(type(arr4))

# 튜플
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

# 딕셔너리
spiderman = { 'name' : '피터 파커'
            , 'age' : 18
            , 'weapon' : '웹슈터'}
print(spiderman)
print(type(spiderman))

# 집합
set1_int = set([1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4])
print(set1_int)
print(type(set1_int))


