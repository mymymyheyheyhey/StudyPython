# 파일 입출력

# 파일 출력
# f = open('newfile.txt', 'w')
# f.close() open 하면 close 가 나와야 한다.



# 특정 경로에 파일 생성
# f = open('C:\\Sources\Sample\\test.txt', 'w') # \를 문자로 사용하려면 2번 입력해야 한다.
# f.close()
# print('파일이 생성되었습니다.')



# newfile.txt 파일 입력 (읽어오기)
f = open('newfile.txt', 'r', encoding = 'utf-8')

while True:
    line = f.readline()
    
    if not line: 
        break

    print(line, end = '')

f.close()



