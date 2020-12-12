import mysql.connector as sqlbruh

pas=input("ENTER PASSWORD OF SQL\n>>>")

conc=sqlbruh.connect(host='localhost',user='root',passwd=pas,database='Hospital_Management')

if conc.is_connected():
   print('SUCCESSFULLY CONNECTED\n')
else:
   print("NOT CONNECTED")

print("DATABASE :- Hospital_Management\nTABLES:- 1) p_details\n\t 2) d_details\n")   

cur=conc.cursor()

def p_reg():
     p_id=input("Enter Patient ID:")
     p_name=input("Enter Patient's Name:")
     p_age=str(input('Enter Age:'))
     p_sex=input("Enter Sex (M/F):")
     p_prob=input('Enter the Problem:')
     p_ph=str(input('Enter Contact number:'))
     insert="insert into p_details values({},'{}',{},'{}','{}',{})"
     cur.execute(insert.format(p_id,p_name,p_age,p_sex,p_prob,p_ph))
     conc.commit()
     print('\n-----------------------\nSUCCESSFULLY REGISTERED\n')
     
def p_shw():
     p=input("Enter the name:")
     cur.execute("select * from p_details")
     srh = cur.fetchall()
     c=0
     for i in srh:
        if i[1]==p:
           c=1
           p_srh="select*from p_details where p_name=('{}')"
           cur.execute(p_srh.format(p))
           p_det=cur.fetchall()
           print("\n{:^3}|{:^10}|{:^5}|{:^5}|{:^15}|{:^12}|".format("ID","NAME","AGE","SEX","PROBLEM"," CONTACT NO."))
           for j in p_det:
              print("{:<3}|{:<10}|{:<5}|{:<5}|{:<15}|{:<12}|".format(j[0],j[1],j[2],j[3],j[4],j[5]))
           print('\n')   
     if c==0:
           print("\n-----------------\nPATIENT NOT FOUND\n")    

def p_mod():
     p=input("Enter the name:")
     cur.execute("select * from p_details")
     srh = cur.fetchall()
     c=0
     for i in srh:
        if i[1]==p:
           c=1
           print("\nEnter Values To Be Modified:")
           p_id=input("Enter Patient ID:")
           p_age=str(input('Enter Age:'))
           p_prob=input('Enter the Problem:')
           p_ph=str(input('Enter Contact number:'))
           insert="update p_details set p_id={},p_age={},p_prob='{}',p_ph={} where p_name='{}'"
           cur.execute(insert.format(p_id,p_age,p_prob,p_ph,p))
           conc.commit()
           print('\n---------------------\nSUCCESSFULLY MODIFIED\n')
     if c==0:
           print("\n-----------------\nPATIENT NOT FOUND\n")

def p_rmv():
      p=input("Enter the name:")
      cur.execute("select * from p_details")
      srh = cur.fetchall()
      c=0
      for i in srh:
         if i[1]==p:
            c=1
            p_del="delete from p_details where p_name=('{}')"
            cur.execute(p_del.format(p))
            conc.commit()
            print("\n--------------------\nSUCCESSFULLY DELETED\n")
      if c==0:
          print("\n-----------------\nPATIENT NOT FOUND\n")    
def p_sha():
      p_det='select*from p_details '
      cur.execute(p_det)
      det= cur.fetchall()
      print("{:^3}|{:^10}|{:^5}|{:^5}|{:^15}|{:^12}|".format("ID","NAME","AGE","SEX","PROBLEM"," CONTACT NO."))
      for j in det :
            print("{:<3}|{:<10}|{:<5}|{:<5}|{:<15}|{:<12}|".format(j[0],j[1],j[2],j[3],j[4],j[5]))
      print('\n')    

def d_reg():
     d_name=input('Enter Doctor Name:')
     d_age=str(input('Enter Age:'))
     d_depa=input('Enter the Department:')
     d_wrk=input('Enter Working Hours:')
     d_ph=str(input('Enter Contact number:'))
     insert="insert into d_details values('{}',{},'{}','{}',{})"
     cur.execute(insert.format(d_name,d_age,d_depa,d_wrk,d_ph))
     conc.commit()
     print('\n-----------------------\nSUCCESSFULLY REGISTERED\n')    

def d_shw():
     d=input("Enter the name:")
     cur.execute("select * from d_details")
     srh = cur.fetchall()
     c=0
     for i in srh:
          if i[0]==d:
               c=1
               d_srh="select*from d_details where d_name=('{}')"
               cur.execute(d_srh.format(d))
               d_det=cur.fetchall()
               print("{:^10}|{:^5}|{:^15}|{:^13}|{:^12}|".format("NAME","AGE","DEPARTMENT","WORKING HOURS"," CONTACT NO."))
               for j in d_det:
                    print("{:<10}|{:<5}|{:<15}|{:<13}|{:<12}|".format(j[0],j[1],j[2],j[3],j[4]))
               print('\n')    
     if c==0:
          print("\n----------------\nDOCTOR NOT FOUND\n")    
def d_mod():
     d=input("Enter the name:")
     cur.execute("select * from d_details")
     srh = cur.fetchall()
     c=0
     for i in srh:
          if i[0]==d:
               c=1
               print("\nEnter Values To Be Modified:")
               d_age=str(input('Enter Age:'))
               d_depa=input('Enter the Department:')
               d_wrk=input('Enter Working Hours:')
               d_ph=str(input('Enter Contact number:'))
               insert="update d_details set d_age={},d_depa='{}',d_wrk='{}',d_ph={} where d_name='{}'"
               cur.execute(insert.format(d_age,d_depa,d_wrk,d_ph,d))
               conc.commit()
               print('\n---------------------\nSUCCESSFULLY MODIFIED\n')
     if c==0:
          print("\n----------------\nDOCTOR NOT FOUND\n")
def d_rmv():
     d=input("Enter the name:")
     cur.execute("select * from d_details")
     srh = cur.fetchall()
     c=0
     for i in srh:
          if i[0]==d:
               c=1
               d_del="delete from d_details where d_name=('{}')"
               cur.execute(d_del.format(d))
               conc.commit()
               print("\n--------------------\nSUCCESSFULLY DELETED\n")
     if c==0:
          print("\n----------------\nDOCTOR NOT FOUND\n")    
def d_sha():
     d_det="select*from d_details"
     cur.execute(d_det)
     det=cur.fetchall()
     print("{:^10}|{:^5}|{:^15}|{:^13}|{:^12}|".format("NAME","AGE","DEPARTMENT","WORKING HOURS"," CONTACT NO."))
     for j in det:
          print("{:<10}|{:<5}|{:<15}|{:<13}|{:<12}|".format(j[0],j[1],j[2],j[3],j[4]))
     print('\n')

print("------------------------------------------\n  WELCOME TO HOSPITAL MANAGEMENT SYSTEM\n------------------------------------------")
while True:
    print(" ---HOME PANEL--- ")
    print("\n1.Manage Patient")
    print("2.Manage Doctor")
    print("3.Exit Hospital Management System")
    ch=int(input("\n-------------\nENTER YOUR CHOICE\n-------------\n>>>"))
    if ch==1:
        while True:
           print("WELCOME TO PATIENT MANAGEMENT\n")
           print('1.Register a Patient')
           print('2.Show Patient Record')
           print('3.Modify a Patient Record')
           print('4.Remove a Patient Record')
           print("5.Show all patients Records")
           print("6.Go Back to Home Panel")
           ch_1=int(input("\n-------------\nENTER YOUR CHOICE\n-------------\n>>>"))

           if ch_1==1:
               p_reg()

           elif ch_1==2:
               p_shw()

           elif ch_1==3:
               p_mod()

           elif ch_1==4:
               p_rmv()

           elif ch_1==5:
               p_sha()
      
           elif ch_1==6:
                      print("\nGOING BACK TO HOME PANEL.....\n")
                      break            

    if ch==2:
        while True:
            print("WELCOME TO DOCTOR MANAGEMENT\n")
            print("1.Register a Doctor")
            print("2.Show Doctor Record")
            print('3.Modify a Doctor Record')
            print('4.Remove a Doctor Record')
            print("5.Show all doctors Records")
            print("6.Go Back to Home Panel")
            ch_2=int(input("\nENTER YOUR CHOICE\n>>>"))

            if ch_2==1:
                d_reg()

            elif ch_2==2:
                d_shw()

            elif ch_2==3:
                d_mod()

            elif ch_2==4:
                d_rmv()

            elif ch_2==5:
                d_sha()

            elif ch_2==6:
                      print("\nGOING BACK TO HOME PANEL.....\n")
                      break

        
    if ch==3:
        print("\nTHANK YOU FOR COMING")
        break
