# 부산 버스 노선별 이용 건수
import csv

file_name = '부산버스정보.csv'
f = open(file_name, mode = 'r', encoding = 'utf-8')

reader = csv.reader(f, delimiter = ',')
next(reader) # 첫 줄 헤더 없앰

for line in reader:
    print(line)

f.close()


