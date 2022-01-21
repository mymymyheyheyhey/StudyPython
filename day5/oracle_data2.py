# 커서에 접근하는 코드를 함수로 정의
import cx_Oracle as cxo

def myconn():
    
    dsn = cxo.makedsn('localhost', 1521, service_name = 'orcl') # datasourcename 오라클 접속 주소
    conn = cxo.connect(user = 'Scott', password = 'tiger', dsn = dsn, encoding = 'utf-8') 
    
    return conn

# 아이디와 패스워드 뿐 아니라 주소도 있어야 오라클 접속 가능
# dsn 과 conn 에 해당하는 정보
# 호스트이름 포트넘버 서비스이름 아이디 비밀번호 인코딩 정보 가 모두 있어야 오라클 접속 가능

def SAll(conn): # conn 객체를 인자에 할당하여 쿼리를 실행
    cur = conn.cursor() # 커서 생성
    query = 'SELECT * FROM emp' # emp 테이블의 모든 데이터를 불러옴
    for row in cur.execute(query):
        print(row)

def Senamejob(conn):
    cur = conn.cursor()
    query = 'SELECT ename, job FROM emp' # emp 테이블에서 ename, job 칼럼 조회
    
    # for row in cur.execute(query):
    #     print(row)
    
    cur.execute(query)
    while True:
        row = cur.fetchone() # 한 줄 씩 읽기 readline() 과 같은 기능
        print(row)
        if not row: break
        

def Sdeptname(conn, tup):
    cur = conn.cursor()
    query = f"SELECT * FROM dept WHERE deptno = :1 and loc = :2" 
    # 파이썬은 0부터 오라클은 1부터 :1 자리에 no 들어감
    # loc 은 글자라서 '' 안에 넣음
    # deptno 숫자라서 '' 넣지 않았음
    # :1 :2는 각각 튜플의 인덱스임
    cur.execute(query, tup) # 커서 객체로 쿼리를 실행
    # row = cur.fetchone()
    # print(row)
    for row in cur.execute(query):
        print(row)





if __name__ == '__main__': # 프로그램 시작 지점 (구문이며, 제어 구조가 아니다)
    print('프로그램 시작')
    # 함수 호출
    scott_conn = myconn() # dsn, connect() 실행 후 접속 객체 conn 리턴

    # print('SELECT * FROM emp;')
    # SAll(scott_conn)

    # print('SELECT ename, job FROM emp;')
    # Senamejob(scott_conn)

    no = input('검색할 부서 번호를 입력하세요')
    loc = input('검색할 지역을 입력하세요.').upper()
    tup = (no, loc)
    # print(f"부서번호: {no}, 지역: {loc}") # 사용자가 입력한 내용을 화면에 표시하여 안내함

    Sdeptname(scott_conn, tup) # 함수 실행

    print('프로그램 종료')

