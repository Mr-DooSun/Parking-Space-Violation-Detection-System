import pymysql

class CarNumberDB :
    
    #host, user, password, db 이름 입력
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    #테이블에 모든 컬럼 출력
    def Show_table(self, table):
        connect = pymysql.connect(self.host, self.user,
                                  self.password, self.db, charset = "utf8")
        sql = "select * from " + table
        cursor = connect.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)

        connect.close()

    #테이블에 검색할 값이 있는지 검색
    def Search_table(self, table, carnumber) :
        connect = pymysql.connect(self.host, self.user,
                                  self.password, self.db, charset = "utf8")
        sql = "select * from " + table + " where 차량번호 = %s and 장애인차량여부 = 1"
        cursor = connect.cursor()
        cursor.execute(sql, carnumber)
        rows = cursor.fetchone()
        if(rows is None):
            return False
        else:
            return True

def main(number):
    car1 = CarNumberDB("localhost", "root", "1234", "car_db")
    car1.Show_table("car")
    
    if car1.Search_table("car",number):
        return "장애인 차량입니다."
    else:
        return "장애인 차량이 아닙니다."