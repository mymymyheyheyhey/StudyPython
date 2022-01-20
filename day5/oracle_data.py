# oracle_data
# 파이썬과 오라클을 연결
# cx_oracle 설치: pip install cx_oracle

# makedsn(호스트명/아이피주소, 포트넘버, 서비스 이름)
import cx_Oracle as cxo
dsn = cxo.makedsn('localhost', 1521, service_name = 'orcl')

# connect(user, password, dsn, encoding)
conn = cxo.connect(user = 'Scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor() # 마우스 커서와 같은 기능

try:
    for row in cur.execute('SELECT * FROM emp'):
        print(row)
    # cur.execute('SELECT COUNT(*) FROM emp') row 의 개수를 출력
    # result = cur.fetchone() 하나만 출력
    # print(result)

# for 를 사용한 위 구문과 아래는 같은 결과를 출력한다.
# cur.execute('SELECT * FROM emp')
# result = cur.fetchone()
# print(result)

except cxo.DatabaseError as e:
    print(f"쿼리문이 잘못되었습니다. {e}")

finally:
    cur.close()
    conn.close()


