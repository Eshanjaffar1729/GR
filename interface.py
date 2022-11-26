#Many errors in this files was corrected by James_Hn
#Follow me no https://github.com/Eshanjaffar1729

import dbinit as d
import modules as m
import os, sys

while True:

    print('||==============Book My Show===================||')
    print('||      You can perform the following tasks    ||')
    print('|| Type 0 to reset Application                 ||')
    print('|| Type 1 to add a hall in your portal         ||')
    print('|| Type 2 to view all the halls in your portal ||')
    print('|| Type 3 to see the booking status of a hall  ||')
    print('|| Type 4 to book a ticket in a hall           ||')
    print('|| Type 6 to see booking of all the halls      ||')
    print('|| Type 7 to generate ticket for booking       ||')
    print('|| Type 8 to quit                              ||')
    print('||=============================================||')
    choice=m.inputNumber('Enter your choice:')
    if choice==0:
        d.dbcon()
    if choice == 1:
        hname=input('Enter your hall name:')
        fs = m.inputNumber('Enter the maximum front seats:')
        ms = m.inputNumber('Enter the maximum middle seats:')
        bs = m.inputNumber('Enter the maximum back seats:')
        m.addhall(hname,fs,ms,bs)
    if choice==2:
        import pandas as pd
        rec =m.hallstat()
        df = pd.DataFrame(rec)
        df.columns= ['Hall No', 'Hall Name', 'A-Type', 'B-Type', 'C-Type']
        print(df)
    if choice==4:
        import pandas as pd
        print('You have the following hall Numbers')
        print(m.hallnums())
        hno=m.inputNumber('Enter a valid hallno:')
        cname=input('Enter Customer name:')
        stype=input('Enter Seat Type as A,B,C:')
        noseat=m.inputNumber('Enter numbner of seats:')
        cost = m.inputNumber('Enter cost of each seat:')
        dis=0
        if noseat*cost>=2000:
            dis=100
        m.booking(hno,cname,noseat,cost,stype,dis)
    if choice==3:
        import pandas as pd
        print('You can get details of the following hall Numbers')
        print(m.hallnums())
        hno=m.inputNumber('Enter a valid hallno:')
        if hno in m.hallnums():
            rec = m.showhallbooking(hno)
            df=pd.DataFrame(rec)
            df.columns = ['Hall No','Ticket No','Hall Name','Seat Type','No of Seate','Rate','Discount']
            print(df)
        else:
            print('Invalid Hall Number')
    if choice==6:
        import pandas as pd
        rec = m.allbookings()
        df=pd.DataFrame(rec)
        df.columns=['Hall No','Ticket NO','Hall Name','Seat Type','No of Seats',\
        'Cost per seat','Discount','A-Type','B-Type','C-Type']
        print(df)
    if choice==7:
        tno = m.inputNumber('Enter the ticket number:')
        rec = m.getticketdet()
        if tno in rec:
            rec = m.printticket(tno)
            print("---------Ticket Details-----------")
            print("Ticket Number is   :%d" % (rec[0][0]))
            print("Hall Number is     :%d" % (rec[0][1]))
            print("Hall Name          :%s" % (rec[0][2]))
            print('Customer name is   :%s' % (rec[0][3]))
            print('Seat Type          :%s' % (rec[0][4]))
            print("Number of Seats    :%d" % (rec[0][5]))
            print("Cost per Seat      :%d" % (rec[0][6]))
            print("Discount           :%d" % (rec[0][7]))
            total = rec[0][5]*rec[0][6]-rec[0][7]
            print("Total Cost         :%d" % (total))
            #print(rec)
        else:
            print('Ticket Number not available')

    if choice==8:
        sys.exit(0)
    

    os.system('pause')
    os.system('cls')

#Many errors in this files was corrected by James_Hn
#Follow me no https://github.com/Eshanjaffar1729