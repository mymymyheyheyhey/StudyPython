# 파일 쓰기
f = open('writefile.txt', 'w', encoding = 'utf-8')

f.write('저는 한국 사람입니다. \n') # 한 줄만 적음

texts = ['저는 한국 사람이죠\n', '이번에 2022년이 되었습니다.\n']

f.writelines(texts) # 리스트를 추가하여 적음

f.close()

f = open('writefile.txt', 'a', encoding = 'utf-8')

f.write('내용 추가할게요')

f.close()


