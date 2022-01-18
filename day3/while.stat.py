# while 
from re import L


hit = 0
while hit < 100:
    hit += 1

    if hit > 10:
        break

    print(f"나무를 {hit}번 찍습니다.")
    

# for
for hit in range(1, 101):
    print(f"나무를 {hit}번 찍습니다")
