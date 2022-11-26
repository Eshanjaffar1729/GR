#Function to retuen the number of seats available in a hall
#Many errors in this files was corrected by James_Hn
#Follow me no https://github.com/Eshanjaffar1729
psd = input("Enter the password: ")
def getseats(hno):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT frontseats, midseats, backseats FROM hall_det WHERE hallno='%d'" % (hno)
        mycursor.execute(sql)
        rec = mycursor.fetchone()
        con.close()
    except myc.Error as err:
        print(err)
    finally:
        return rec

#Function to get all the hall numbers
def hallnums():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT hallno FROM hall_det ORDER BY hallno"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
        hlst =[]
        for x in rec:
            hlst.append(x[0])
    except myc.Error as err:
        print(err)
    finally:
        con.close()
        return hlst

#Function to get all ticket numbers
def getticketdet():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT tickectno FROM booking_det"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
        tlst =[]
        for x in rec:
            tlst.append(x[0])
    except myc.Error as err:
        print(err)
    finally:
        con.close()
        return tlst

#Function to update the seats based on bookings
def updateseats(hno,stype,amt):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        if stype=='A':
            sql = "UPDATE hall_det SET frontseats=frontseats-'%d' WHERE hallno='%d'" % (amt,hno)
        if stype=='B':
            sql = "UPDATE hall_det SET midseats=midseats-'%d' WHERE hallno='%d'" % (amt,hno)
        if stype=='C':
            sql = "UPDATE hall_det SET backseats=backseats-'%d' WHERE hallno='%d'" % (amt,hno)
        mycursor.execute(sql)
        con.commit()    
    except myc.Error as err:
        print(err)
    finally:
        print('Seats updated')
        con.close()
    
#Function to book the seats and also call update seats function     
def booking(hno, cname,noseat, cost,stype, disc=0):
    import mysql.connector as myc
    s1,s2,s3=getseats(hno)
    if (stype=='A' and noseat>s1) or (stype=='B' and noseat>s2) or (stype=='C' and noseat>s3):
        return 'No seats available'
    else:
        try:
            #changes where made here by James_HN
            con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
            mycursor=con.cursor()
            #https://github.com/Eshanjaffar1729
            sql1="SELECT MAX(tickectno) FROM booking_det"
            mycursor.execute(sql1)
            val = mycursor.fetchall()
            #https://github.com/Eshanjaffar1729
            if(val[0][0] !=None):
                tno = 1729+val[0][0]
            else:
                tno = 1729

            sql="INSERT INTO booking_det(tickectno,hallno,customer,no_of_seats,cost_of_seat,seattype, discount) \
            VALUES(%s,%s,%s,%s,%s,%s,%s)" 
            rows=[(tno,hno, cname,noseat, cost,stype, disc)]
            mycursor.executemany(sql,rows)
            con.commit()
            #update the seats after booking
            updateseats(hno,stype,noseat) 
            print("Your ticket Number is {}".format(tno))               
        except myc.Error as err:
            print(err)
        finally:
            print('Record Inserted')
            con.close()     


#Function to display booking details for a given hall
def showhallbooking(hno):
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.tickectno, b.hallno, h.hallname, b.seattype, b.no_of_seats, b.cost_of_seat, b.discount\
        FROM booking_det b, hall_det h WHERE b.hallno=h.hallno and b.hallno='%d'" % (hno)
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(showhallbooking(1001))

#Function to print the hall status
def hallstat():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT hallno, hallname,frontseats, midseats, backseats FROM hall_det" 
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(hallstat())  
#function to display all bookings
def allbookings():
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.tickectno, h.hallno, h.hallname, b.seattype, b.no_of_seats, b.cost_of_seat, b.discount,\
        h.frontseats, h.midseats, h.backseats FROM booking_det b, hall_det h WHERE b.hallno=h.hallno"
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(allbookings())

def addhall(hname, fs,ms,bs):
    try:
        #Correction where made here by James_HN
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')

        #Correction where made here by James_HN
        mycursor=con.cursor()
        sql1="SELECT MAX(hallno) FROM hall_det"
        mycursor.execute(sql1)
        val = mycursor.fetchall()
        Hallno=val[0][0]+1

        #Correction where made here by James_HN
        sql2="INSERT INTO hall_det(hallno,hallname, frontseats, midseats, backseats) VALUES({},'{}',{},{},{})".format(Hallno,hname,fs,ms,bs)
        mycursor.execute(sql2)
        con.commit()

    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        print('Hall added')
        con.close()
#addhall(1005,'VAISHNAVI-SAPPHIRE', 100,100,100) 

def printticket(tno):
    
    try:
        import mysql.connector as myc
        con = myc.connect(host='localhost',user='root',passwd=psd, database='cinemaproj')
        mycursor=con.cursor()
        sql = "SELECT b.tickectno, b.hallno, h.hallname, b.customer,b.seattype, b.no_of_seats, b.cost_of_seat, b.discount\
        FROM booking_det b, hall_det h WHERE b.hallno=h.hallno and b.tickectno='%d'" % (tno)
        mycursor.execute(sql)
        rec = mycursor.fetchall()
    except myc.Error as err:
        print(err)
        print("SQLSTATE", err.sqlstate)
    finally:
        con.close()
        return rec
#print(printticket(101))  

#Function to enforce integer input. Use this while accepting integers
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 


#Many errors in this files was corrected by James_Hn
#Follow me no https://github.com/Eshanjaffar1729