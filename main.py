import csv
enter_teacher=False
enter_student=False
def register_teacher():
    print("REGISTRATION")
    with open("teachers_login.csv",mode="a",newline='') as f:
        writer=csv.writer(f,delimiter=",")
        uname=input("Enter username:")
        password=input("Enter password:")
        password2=input("Enter password again:")
        if password==password2:
            writer.writerow([uname,password])
            print("Registration is succesful!")
            f.close()
        else:
            print("Please try again!")
            register_teacher()

def login_teacher():
    print("LOGIN")
    user=input("Enter username:")
    password=input("Please enter your password:")
    with open("teachers_login.csv",mode="r") as f:
        reader=csv.reader(f, delimiter=",")
        for row in reader:
            if row==[user,password]:
                print("You are logged in!")
                f.close()
                return True
        print("Please try again!")
        return login_teacher()

def register_student():
    print("REGISTRATION")
    with open("student_login.csv",mode="a",newline='') as f:
        writer=csv.writer(f,delimiter=",")
        uname=input("Enter username:")
        password=input("Enter password:")
        password2=input("Enter password again:")
        if password==password2:
            writer.writerow([uname,password])
            print("Registration is succesful!")
            f.close()
        else:
            print("Please try again!")
            register_student()

def login_student():
    print("LOGIN")
    user=input("Enter username:")
    password=input("Please enter your password:")
    with open("student_login.csv",mode="r") as f:
        reader=csv.reader(f, delimiter=",")
        for row in reader:
            if row==[user,password]:
                print("You are logged in!")
                f.close()
                return True
        print("Please try again!")
        return login_student()

def give_assignment():
    s=input("Give a name of assignment file:")
    s+=".txt"
    fh=open(s,'w')
    l=[]
    flag=True
    while flag==True:
        try:
            r=input("Copy your assignment here(press n to end):")
            if r=="n":
                flag=False
        except EOFError:
            break
        l.append(r+"\n")
        
    fh.writelines(l)
    fh.close()
    return teacher_menu()

def schedule_quiz():
    with open("scheduled_quizes.csv",mode="a",newline='') as q:
            writer=csv.writer(q,delimiter=",")
            date=input("Enter date of the quiz:")
            subject=input("Enter subject of the quiz:")
            topic=input("Enter topic of the quiz:")
            writer.writerow([date,subject,topic])
            print("Quiz Scheduled!")
            q.close()
            return teacher_menu()

def look_scheduled_quizes():
    with open("scheduled_quizes.csv",mode="r") as q:
        reader=csv.reader(q,delimiter=",")
        count=1
        for row in reader:
            print("""                 ------ QUIZ """,count,"""-----""")
            print("""                        Date:""",row[0])
            print("""                        Subject:""",row[1])
            print("""                        Topic:""",row[2])
            count+=1
        print("----That's it! All the best! :)-----")
        return teacher_menu()

def give_quiz():
    s=input("Give a name of questions file:")
    s+=".txt"
    fh=open(s,'w')
    l=[]
    flag=True
    while flag==True:
        try:
            r=input("Copy your questions here(press n to end):")
            if r=="n":
                flag=False
        except EOFError:
            break
        l.append(r+"\n")
    fh.writelines(l)
    fh.close()
    return student_menu()

def submit_assignment():
    s=input("Give a name of ans file:")
    s+=".txt"
    fh=open(s,'w')
    l=[]
    flag=True
    while flag==True:
        try:
            r=input("Copy your ans here(press n to end):")
            if r=="n":
                flag=False
        except EOFError:
            break
        l.append(r+"\n")
    fh.writelines(l)
    fh.close()
    return student_menu()

def attempt_quiz():
    s=input("Give a name of quiz ans file(Write options in capital & NA for not attempted):")
    s+=".txt"
    fh=open(s,'w')
    l=[]
    flag=True
    while flag==True:
        try:
            r=input("Copy your answers here(press n to end):")
            if r=="n":
                flag=False
        except EOFError:
            break
        l.append(r+"\n")
    fh.writelines(l)
    fh.close()
    return student_menu()

def quiz_ans():
    s=input("Give a name of quiz ans file(Write options in capital):")
    s+=".txt"
    fh=open(s,'w')
    l=[]
    flag=True
    while flag==True:
        try:
            r=input("Copy your assignment here(press n to end):")
            if r=="n":
                flag=False
        except EOFError:
            break
        l.append(r+"\n")
    fh.writelines(l)
    fh.close()
    return teacher_menu()

def check_quiz():
    s=input("Enter the name of quiz ans file:")
    r=input("Enter the name of ans file to be checked:")
    n=int(input("Enter the number of questions:"))
    s+=".txt"
    r+=".txt"
    fh=open(s,'r')
    gh=open(r,'r')
    correct_ans=fh.readlines()
    student_ans=gh.readlines()
    marks=0
    n=len(correct_ans)
    for i in range(n):
        if correct_ans[i]==student_ans[i]:
            marks+=1
    fh.close()
    gh.close()
    print("The student scored ",marks-1,"marks out of ",n-1)
    return teacher_menu()

def enter_marks():
    n=int(input("Enter students roll no. :"))
    s=input("Enter students name:")
    r=input("Enter subject and quiz no. :")
    m=int(input("Enter student's marks:"))
    with open("studentsmarks.csv",mode="a",newline='') as q:
        writer=csv.writer(q,delimiter=",")
        writer.writerow([n,s,r,m])
    return teacher_menu()

def see_marks():
    n=input("Enter students roll no. :")
    s=input("Enter students name:")
    r=input("Enter subject and quiz no. :")
    with open("studentsmarks.csv",mode="r") as q:
        reader=csv.reader(q,delimiter=",")
        for row in reader:
            if row[0:3]==[n,s,r]:
                print("your marks are:",row[3])
    return student_menu()


def teacher_menu():
    m=input("For menu Press y:")
    if m=="y":
        print("""           
                            1.Give Assignment
                            2.Schedule a Quiz
                            3.See scheduled quizes
                            4.Give Quiz
                            5.Enter ans for quiz
                            6.Check quiz
                            7.Enter students Marks""")
        t=int(input("Enter the number:"))
        teacher_task(t)

def student_menu():
    m=input("For menu press y:")
    if m=="y":
        print("""
                            1.Submit Assignment
                            2.See scheduled quizes
                            3.Check Marks
                            4.Attempt Quiz""")
        t=int(input("Enter the number:"))
        student_task(t)

def teacher_task(n):
    if n==1:
        give_assignment()
    if n==2:
        schedule_quiz()
    if n==3:
        look_scheduled_quizes()
    if n==4:
        give_quiz()
    if n==5:
        quiz_ans()
    if n==6:
        check_quiz()
    if n==7:
        enter_marks()

def student_task(n):
    if n==1:
        submit_assignment()
    if n==2:
        look_scheduled_quizes()
    if n==3:
        see_marks()
    if n==4:
        attempt_quiz()
    

role=input("Are you a Student(s) or Teacher(t):")
acc=input("Do you have and existing account? y or n:")
if role=='s' and acc=='y':
    enter_student=login_student()
if role=='s' and acc=='n':
    register_student()
    enter_student=login_student()
if role=='t' and acc=='y':
    enter_teacher=login_teacher()
if role=='t' and acc=='n':
    register_teacher()
    enter_teacher=login_teacher()

    
if enter_teacher:
    teacher_menu()
if enter_student:
    student_menu()


    







            


