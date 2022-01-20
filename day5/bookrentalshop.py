# bookrentalshop.py
# divtbl, membertbl
import cx_Oracle as cxo

def myconn():
    dsn = cxo.makedsn('localhost', 1521, service_name = 'orcl')
    conn = cxo.connect(user = 'Scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

def S_All_divtbl(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM divtbl'
    for row in cur.execute(query):
        print(row)

def I_into_divtbl(conn, tup):
    cur = conn.cursor()
    query = '''INSERT INTO divtbl(division, names) 
               VALUES(:0, :1)'''
    cur.execute(query, tup)
    cur.close() # 커서로 쿼리 실행 후 커서를 닫아야 한다.
    conn.commit() # 커밋 데이터 변경 확정

def S_some_membertbl(conn):
    cur = conn.cursor()
    query = '''SELECT 
               names, levels, addr, mobile, email 
               FROM membertbl
               WHERE addr LIKE '서울%'
               AND UPPER(email) LIKE '%@NAVER.COM'
               ORDER BY idx DESC'''
    for row in cur.execute(query):
        print(row)
    cur.close()


def I_into_membertbl(conn, tup):
    cur = conn.cursor()
    # 인덱스 가져오기
    query = '''SELECT 
                ROWNUM, idx
                FROM (SELECT 
                idx FROM membertbl
                ORDER BY idx DESC) 
                WHERE ROWNUM = 1'''
    cur.execute(query)
    idx = cur.fetchone()[1]

    # 가져온 인덱스와 사용자가 입력한 정보를 종합하여 데이터베이스에 새로 추가
    intup = (idx + 1, tup[0], tup[1], tup[2], tup[3])
    query = '''INSERT INTO 
                membertbl(idx, names, levels, userid, password)
                VALUES (:1, :2, :3, :4, :5)'''
    cur.execute(query, intup)
    cur.close()
    conn.commit()


def update_memberinfo(conn, tup):
    cur = conn.cursor()
    query = '''UPDATE membertbl
               SET addr = :1
                 , mobile = :2
                 , email = :3
               WHERE idx = :4'''
    cur.execute(query, tup)
    cur.close()
    conn.commit()



def delete_division(conn, division):
    cur = conn.cursor()
    query = 'DELETE FROM divtbl WHERE division = :1'
    cur.execute(query, division)
    cur.close()
    conn.commit()




##########################################################################
if __name__ == '__main__':
    print('책 대여 프로그램 시작')
    # 데이터베이스 접속
    scott_con = myconn() 

    # divtbl 에서 데이터 조회
    print('책 장르 조회')
    S_All_divtbl(scott_con)

    # divtbl 에 새 데이터 입력
    division = input('색인 입력: ')
    names = input('장르 입력: ')
    tup = (division, names)
    I_into_divtbl(scott_con, tup)
    print('정보가 입력되었습니다')

    # membertbl 에서 데이터 조회
    S_some_membertbl(scott_con)

    # membertbl 에 새 데이터 입력
    # print('신규 회원 입력')
    # names = input('이름을 입력하세요: ')
    # levels = input('레벨을 입력하세요(A~D): ')
    # userid = input('아이디를 입력하세요(최대 20자): ')
    # password = input('패스워드를 입력하세요(최대 20자): ')
    # tup = names, levels, userid, password

    # I_into_membertbl(scott_con, tup)
    # print('등록이 완료되었습니다.')

    # membertbl 에 입력한 데이터 수정
    # idx = input('회원 번호를 입력하세요: ')
    # addr = input('새로 등록할 주소를 입력하세요: ')
    # mobile = input('-을 포함하여 새로 등록할 휴대 전화 번호를 입력하세요: ')
    # email = input('새로 등록할 이메일 주소를 입력하세요: ')
    # tup = addr, mobile, email, idx
    # update_memberinfo(scott_con, tup)
    # print('수정이 완료되었습니다.')
    
    # divtbl 에 임의 데이터 삭제
    print('책의 색인을 삭제합니다.')
    division = input('삭제할 책의 색인을 입력하세요: '), #data,: 하나의 데이터로 튜플 생성
    delete_division(scott_con, division)
    print('삭제가 완료되었습니다.')



    