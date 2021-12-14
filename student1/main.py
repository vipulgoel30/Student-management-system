import fontstyle
import mysql.connector as c
db=c.connect(host="localhost",user="root",passwd="root",database="school")

  
def menu():
    print()
    print(fontstyle.apply("**************************************************".center(120),"yellow/ bold"))
    print(fontstyle.apply("**************************************************".center(120),"yellow/ bold"))
    print(fontstyle.apply('WELCOME TO SCHOOL MANAGEMENT SYSYTEM OF XYX SCHOOL'.center(120),"green bold"))
    print(fontstyle.apply("**************************************************".center(120),"yellow/ bold"))
    print(fontstyle.apply("**************************************************".center(120),"yellow/ bold"))
    print()
    print()
    print(fontstyle.apply("2.Show Tables","green bold"))
    print(fontstyle.apply("1.About","green bold"))
    print(fontstyle.apply("3.Create Table student_detail","green bold"))
    print(fontstyle.apply("4.Describe Table student_detail","green bold"))
    print(fontstyle.apply("5.Show All Records from Student_detail","green bold"))
    print(fontstyle.apply("6.Show Any no. of Records from top from Student_detail","green bold"))
    print(fontstyle.apply("7.Show Any no. of Records from bottom From Student_detail","green bold"))
    print(fontstyle.apply("8.Show 5 Records from Student_detail from top","green bold"))
    print(fontstyle.apply("9.Show 5 records from student_detail from bottom","green bold"))
    print(fontstyle.apply("10.Add Student Detail","green bold"))
    print(fontstyle.apply("11.Delete from Student detail","green bold"))
    print(fontstyle.apply("12.Update student mobile no. in student Detail Table","green bold"))
    print(fontstyle.apply("13. Create table marks","green bold"))
    print(fontstyle.apply("14.Add in marks table","green bold"))
    print(fontstyle.apply("15. Show Marks in marks table","green bold"))
    print(fontstyle.apply("16.Delete from marks","green bold"))
    print(fontstyle.apply("17.Update marks table","green bold"))
    print(fontstyle.apply("18. Search by Roll no.","green bold"))
    print(fontstyle.apply("19.Marks less than","green bold"))
    print(fontstyle.apply("20.Highest marks in each subject","green bold"))
    print(fontstyle.apply("21.Order by english marks","green bold"))
    print(fontstyle.apply("22. average marks of every subject","green bold"))
    print("******************************************************************")
menu()

# option 1
def about():
    print(fontstyle.apply("In this school mangement project there are two tables and 23 options","purple bold"))

#option 2
def show_tables():
    print(fontstyle.apply("Name of tables in current database school","purple bold"))
    mc=db.cursor()
    mc.execute("show tables")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))

#option 3
def create_student_detail():
    mc=db.cursor()
    mc.execute("create table if not exists student_detail(admno varchar(10) primary key ,name varchar(30),father_name varchar(30),mobile varchar(15) ,Addre_s varchar(40))")
    print(fontstyle.apply("Table Create","purple bold"))

#option 4
def desc_student_detail():
    print(fontstyle.apply("Show structure of student_detail","purple bold"))
    mc=db.cursor()
    mc.execute("DESC student_detail")
    for x in mc:
        print(fontstyle.apply(x,"green bold"))

#option 5
def show_recordsstudent_detail():
    print(fontstyle.apply("All records in student_detail","purple bold"))
    mc=db.cursor()
    mc.execute("SELECT * FROM student_detail")
    my=mc.fetchall()
    for x in my:
        print(fontstyle.apply(x,"green bold"))

#option 6
def anynofromtop():
    a=int(input(fontstyle.apply("Enter the no. of records from top ","cyan bold")))
    mc=db.cursor()
    mc.execute("select * from student_detail ")
    my=mc.fetchall()
    d=list()
    for i in my:
        d.append(i)
    for m in range(0,a):
        print(fontstyle.apply(d[m],"green bold"))

#option 7
def anynofrombottom():
    a=int(input(fontstyle.apply("Enter the no. if rows from bottom","cyan bold")))
    mc=db.cursor()
    mc.execute("select * from student_detail ")
    my=mc.fetchall()
    d=list()
    for i in my:
        d.append(i)
    for m in range(-1,-(a+1),-1):
        print(fontstyle.apply(d[m],"green bold"))

#option 8
def fivefromtop():
    print(fontstyle.apply("Top 5 records","purple bold"))
    mc=db.cursor()
    mc.execute("select * from student_detail")
    my=mc.fetchall()
    d=list()
    for i in my:
        d.append(i)
    for m in range(-1,-6,-1):
        print(fontstyle.apply(d[m],"green bold"))

#option 9
def fivefrombottom():
    print(fontstyle.apply("Five bootom records","purple bold"))
    mc=db.cursor()
    mc.execute("select* from student_detail")
    my=mc.fetchall()
    d=list()
    for i in my:
        d.append(i)
    for m in range(0,5):
        print(fontstyle.apply(d[m],"green bold"))

#option 10
def add_student_detail():
    admno1=input(fontstyle.apply("Enter the admission no.(upto 10 digits)","cyan bold"))
    name1=input(fontstyle.apply("Enter the name","cyan bold"))
    father1=input(fontstyle.apply("Enter the father name","cyan bold"))
    phone1=int(input(fontstyle.apply("Enter the phone no.","cyan bold")))
    address1=input(fontstyle.apply("Enter the address(upto 40 letters)","cyan bold"))
    mc=db.cursor()
    mc.execute("INSERT INTO student_detail(admno,name,father_name,mobile,Addre_s) VALUES(%s,%s,%s,%s,%s)",(admno1,name1,father1,phone1,address1))
    db.commit()

#option 11
def del_student_detail():
    adm=input(fontstyle.apply("Enter the admission no.","cyan bold"))
    mc=db.cursor()
    mc.execute("delete from student_detail where admno=%s",(adm,))
    print(fontstyle.apply("Record deleted","red bold"))
    db.commit()
    mc=db.cursor()
    mc.execute("select* from student_detail")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
#option 12
def update_student_detail():
    print(fontstyle.apply('Before any changes in table',"purple bold"))
    mc=db.cursor()
    mc.execute("SELECT * FROM student_detail")
    my=mc.fetchall()
    for x in my:
        print(fontstyle.apply(x,"green bold"))
        print()
    admn=input(fontstyle.apply("Enter the admission no.","cyan bold"))
    mobil=int(input(fontstyle.apply("Enter the mobile no.","cyan bold")))
    mc=db.cursor()
    mc.execute("update student_detail set mobile =%s where admno= %s",(mobil,admn,))
    print(fontstyle.apply("Record updated","red bold"))
    db.commit()
    mc=db.cursor()
    mc.execute("select* from student_detail")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
#option 13
def create_marks():
    mc=db.cursor()
    mc.execute("create table if not exists marks(admno varchar(10),roll int(5),name varchar(30),english float(5),hindi float(5),maths float(5),computer float(5))")
    print(fontstyle.apply('Table creatd',"purple bold"))
#option 14
def add_marks ():
    print(fontstyle.apply('Before any changes in table',"purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
    print(fontstyle.apply('Insert into marks new test marks',"purple bold"))
    admn=input(fontstyle.apply("enter the admission no.","cyan bold"))
    roll1=int(input(fontstyle.apply("enter the roll no.","cyan bold")))
    name1=input(fontstyle.apply("enter the name","cyan bold"))
    english1=float(input(fontstyle.apply("enter the english marks","cyan bold")))
    hindi1=float(input(fontstyle.apply("enter the hindi marks","cyan bold")))
    maths1=float(input(fontstyle.apply("enter the maths marks","cyan bold")))
    computer1=float(input(fontstyle.apply("enter the computer marks","cyan bold")))
    mc=db.cursor()
    mc.execute("insert into marks(admno,roll,name,english,hindi,maths,computer) VALUES(%s,%s,%s,%s,%s,%s,%s)",(admn,roll1,name1,english1,hindi1,maths1,computer1,))
    db.commit()
    print(fontstyle.apply("Done","purple bold"))
    print(fontstyle.apply("Changed table","purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
#option 15
def show_marks():
        print(fontstyle.apply("Show marks of all students","purple bold"))
        mc=db.cursor()
        mc.execute("select * from marks")
        for i in mc:
            print(fontstyle.apply(i,"green bold"))
#option 16
def delete_record():
    print(fontstyle.apply('Before any changes in table',"purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
        print()
        print()
    roll1=int(input(fontstyle.apply("enter the roll no.","cyan bold")))
    mc=db.cursor()
    mc.execute("delete from marks where roll=%s",(roll1,))
    db.commit()
    print(fontstyle.apply("Record deleted","purple bold"))
    print(fontstyle.apply("Table after deleting the record","purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))

#option 17
def update_marks():
    print(fontstyle.apply('Before any changes in table',"purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
        print()
        print()
    print(fontstyle.apply("1.english \n 2.hindi \n 3.maths \n 4.computer","purple bold"))
    choice=int(input(fontstyle.apply("enter the subject code from the above menu do yo want to update the marks","cyan bold")))
    roll1=int(input(fontstyle.apply("enter the roll no.","cyan bold")))
    if choice==1:
        english1=float(input(fontstyle.apply("enter the english marks","cyan bold")))
        mc=db.cursor()
        mc.execute("update marks set english =%s where roll=%s",(english1,roll1,))
        db.commit()
    elif choice==2:
        hindi1=float(input(fontstyle.apply("enter the hindi marks","cyan bold")))
        mc=db.cursor()
        mc.execute("update marks set english =%s where roll=%s",(hindi1,roll1,))
        db.commit()
    elif choice==3:
        maths1=float(input(fontstyle.apply("enter the maths marks","cyan bold")))
        mc=db.cursor()
        mc.execute("update marks set english =%s where roll=%s",(maths1,roll1,))
        db.commit()
    elif choice==4:
        computer1=float(input(fontstyle.apply("enter the computer marks","cyan bold")))
        mc=db.cursor()
        mc.execute("update marks set english =%s where roll=%s",(computer1,roll1,))
        db.commit()
    else:
        print(fontstyle.apply("enter the apppropriate choice","red bold"))
#option 18
def search_byrollno():
    print(fontstyle.apply('Search student record by entering roll no. ',"purple bold"))
    a=int(input(fontstyle.apply("Enter roll number : ","cyan bold")))
    mc=db.cursor()
    mc.execute("select * from marks where roll=%s",(a,))
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
#option 19
def marks_less_than():
    print(fontstyle.apply('To show details of those students who scored marks less than that in english',"purple bold"))
    m=float(input(fontstyle.apply("Enter marks to find less than that marks in English","cyan bold")))
    mc=db.cursor()
    mc.execute("select * from marks where english<%s",(m,))
    for i in mc:
        print(fontstyle.apply(i,"green bold"))

#option 20
def subject_max():
    mc=db.cursor()
    mc.execute("select max(english),max(hindi),max(computer),max(maths) from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))

#option 21
def orderby_subject():
    print(fontstyle.apply("Ascending order marks of english ","purple bold"))
    mc=db.cursor()
    mc.execute("select * from marks order by english ")
    print(fontstyle.apply(" Done ","purple bold"))
    for i in mc:
        print(fontstyle.apply(i,"green bold"))

#option 22
def avgmarks():
    print(fontstyle.apply("Avg marks in each subject","purple bold"))
    mc=db.cursor()
    mc.execute("select avg(maths),avg(computer),avg(english),avg(hindi) from marks")
    for i in mc:
        print(fontstyle.apply(i,"green bold"))
cm="Y"
while cm=="Y" or cm=="y":
    opt=int(input(fontstyle.apply("Enter your choice : ","cyan bold")))
    if opt==1:
        about()
    elif opt==2:
        show_tables()
    elif opt==3:
        create_student_detail()
    elif opt==4:
        desc_student_detail()
    elif opt==5:
        show_recordsstudent_detail()
    elif opt==6:
        anynofromtop()
    elif opt==7:
        anynofrombottom()
    elif opt==8:
        fivefromtop()
    elif opt==9:
        fivefrombottom()

    elif opt==10:
        add_student_detail()
    elif opt==11:
        del_student_detail()
    elif opt==12:
        update_student_detail()
    elif opt==13:
        create_marks()
    elif opt==14:
        add_marks()
    elif opt==15:
        show_marks()
    elif opt==16:
        delete_record()
    elif opt==17:
        update_marks()
    elif opt==18:
        search_byrollno()
    elif opt==19:
        marks_less_than()
    elif opt==20:
        subject_max()
    elif opt==21:
        orderby_subject()
    elif opt==22:
        avgmarks()
    else:
        print(fontstyle.apply('Invlaid option',"purple bold"))
    cm=input(fontstyle.apply("Do you want to continue or not: Y/N","cyan bold"))
