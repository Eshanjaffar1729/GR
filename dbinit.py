psd = int(input())
def dbcon():
    # Initial Script to create database schema
    import mysql.connector as myc

    try:
        con = myc.connect(host='localhost',user='root',passwd=psd)
        mycursor = con.cursor()
        mycursor.execute('DROP DATABASE IF EXISTS cinemaproj')
        mycursor.execute('CREATE DATABASE cinemaproj')
        mycursor.execute('USE cinemaproj')
        mycursor.execute('DROP TABLE IF EXISTS hall_det')
        sql = '''CREATE TABLE hall_det(
                    hallno INT(5) PRIMARY KEY,
                    hallname VARCHAR(20) NOT NULL,
                    frontseats INT(3) NOT NULL,
                    midseats INT(3) NOT NULL,
                    backseats INT(3) NOT NULL)'''
        mycursor.execute(sql)
        mycursor.execute('DROP TABLE IF EXISTS booking_det')
        sql = '''CREATE TABLE booking_det(
                    tickectno INT(5) PRIMARY KEY,
                    hallno INT(5) NOT NULL,
                    customer VARCHAR(15) NOT NULL,
                    no_of_seats INT(2) NOT NULL,
                    cost_of_seat INT(4) NOT NULL,
                    seattype CHAR(1) NOT NULL,
                    discount INT(3) NULL,
                    CONSTRAINT FOREIGN KEY(hallno) 
                    REFERENCES hall_det(hallno))'''
        mycursor.execute(sql)

        #Inserting Rows in to the Cinema hall table
        sql = """INSERT INTO hall_det(hallno, hallname, frontseats, midseats,backseats)
        VALUES(%s, %s, %s, %s, %s)"""
        rows = [(1001,'PVR-YPR',50,50,50),(1002,'INOX-MANTRI',50,50,50),\
        (1003,'PVR-GOP',50,50,50),(1004,'PHOENIX',60,50,50)]
        mycursor.executemany(sql, rows)
        con.commit()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        print('Database schema Creatred')
        con.close()
 
    
