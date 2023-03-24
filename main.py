from employee import employee
from analysis import analysis
from attandance import attandance
import datetime

a=analysis()
att=attandance()
ids=[]

def add_employee(ids):
    while True:
        id=int(input("Enter employee id :- "))
        if str(id) not in ids:
            break
        else:
            print(ids)
            print("Enter Id which is not already registered")
    name=input("Enter employee name :- ")
    join_date=datetime.datetime(int(input("Enter year of joining :- ")),
                           int(input("Enter month of joining :- ")),
                           int(input("Enter date of joining :- ")))
    employee_salary=int(input("Enter the salary of employee :- "))
    present_date=datetime.datetime.today()
    final=present_date-join_date
    if final.days>180:
        ids.append(id)
        set_project(id)
        project=True
    else:
        project=False
    date = str(join_date.date().day) +'/' + str(join_date.date().month) +'/'+ str(join_date.date().year)
    print(date)
    e=employee(name,id, date,employee_salary,project)

def set_project(id1):
    # ------------ a employee can have multiple projects----
    if id1 not in ids:
        print("Enter a id that exist")
        return
    
    f=open('projects.csv')
    lines=f.readlines()
    f.close()
    empid=id1
    pro=input("Project Name :- ")
    s_date=input("Enter Start date Of project [format=dd/mm/yy] :- ")
    d_date=input("Enter Deadline Of project [format=dd/mm/yy] :- ")
    e_date=input("Enter End date Of project [format=dd/mm/yy] :- ")
    val=input("Enter market value of project ")
    str=f"\n{empid},{pro},{s_date},{d_date},{e_date},{val}"
    lines.append(str)
    f=open('projects.csv','w')
    f.writelines(lines)
    f.close()

    



def printDetails(id=-1):
        f = open("Employee_details.csv",'r')
        lines=f.readlines()
        f.close()
        print("-"*110)
        print(f"{lines[0].split(',')[0]}\t{lines[0].split(',')[1]}\t{lines[0].split(',')[2]}\t{lines[0].split(',')[3]}\t{lines[0].split(',')[4]}".replace('\n','').expandtabs(19))
        print("-"*110)
        if(id!=-1):
            for i in lines[1:]:
                line=i.split(',')
                if int(line[0])==id:
                     print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}".expandtabs(19))
        else:
            for line in lines[1::]:
                line=line.split(',')
                print(f"{line[0]}\t{line[1]}\t{line[2]}\t{line[3]}\t{line[4]}".expandtabs(19))



while True:
    f=open('Employee_details.csv')
    lines=f.readlines()
    for line in lines[1:]:
        ids.append(line.split(',')[0])
    f.close()
    print(ids)
    print("1.Add New employee")
    print("2.Add Project")
    print("3.View All Employee Details")
    print("4.Get Particular Employee")
    print("5.Get incentive details")
    print("6.Get Last 30 Days Attandance Graph")
    print("7.Get Last 30 Days Attandance Count")
    print("8.Exit")
    choice=int(input("enter your choice :- "))
    if choice==1:
        add_employee(ids)
    elif choice==2:
        set_project(int(input("Enter the id")))
    elif choice==3:
        printDetails()
    elif choice==4:
        printDetails(int(input("Enter the id")))

    elif choice==5:
        margin=int(input("Enter the profit margin of company in %"))
        id=int(input("Enter the id of the employee"))
        print("Employee details with incentives limit")
        printDetails(id)
        a.incentives(id,margin)
    elif choice==6:
        id=int(input("Enter the id of the employee"))
        att.monthlyView(id)
    elif choice==7:
        id=int(input("Enter the id of the employee"))
        printDetails(id)
        count=att.monthlyView(id,True)
        print("Present Count:-"+str(count[0])+"\nAbsent Count:-"+str(count[1]))
    elif choice==8:
        break
    print()
    print("_"*110)
    print()
    print("_"*110)
    



