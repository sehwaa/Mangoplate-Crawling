#DBConnect.py

import pymysql

def insertDB(dataDic):

    if '카테고리' in dataDic.keys():
        category = dataDic['카테고리']
    else:
        category = None
    
    if '이름' in dataDic.keys():
        R_name = dataDic['이름']
    else:
        R_name = None

    if '주소' in dataDic.keys():
        addr = dataDic['주소']
        x = addr.split(' ')
        R_gu = x[1]
        R_dong = x[2]
    else:
        addr = None
        R_gu = None
        R_dong = None

    if '전화번호' in dataDic.keys():
        tel = dataDic['전화번호']
    else:
        tel = None
    
    if '음식종류' in dataDic.keys():
        kind = dataDic['음식종류']
    else:
        kind = None
    
    if '평점' in dataDic.keys():
        rating = dataDic['평점']
    else:
        rating = None

    if '영업시간' in dataDic.keys():
        open_time = dataDic['영업시간']
    else:
        open_time = None

    if '휴일' in dataDic.keys():
        holiday = dataDic['휴일']
    else:
        holiday = None

    if '메뉴' in dataDic.keys():
        menu = dataDic['메뉴']
    else:
        menu = None

    try:
        conn = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='hotplace', charset='utf8')
        with conn.cursor() as cursor:
            sql = 'INSERT INTO s_restaurants (category, R_name, R_gu, R_dong, addr, tel, kind, rating, open_time, holiday, menu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (category, R_name, R_gu, R_dong, addr, tel, kind, rating, open_time, holiday, menu))
            conn.commit()
    finally:
        conn.close()
