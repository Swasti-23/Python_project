import csv
def see_marks():
    n=input("Enter students roll no. :")
    s=input("Enter students name:")
    r=input("Enter subject and quiz no. :")
    with open("studentsmarks.csv",mode="r") as q:
        reader=csv.reader(q,delimiter=",")
        for row in reader:
            if row[0:3]==[n,s,r]:
                print("your marks are:",row[3])
see_marks()



        
