import datetime
class analysis:
    def __init__(self):
        pass

    def calPerHeadProjectValue(self):
        '''
            Per head project Value is calculated 
            project_market_value/persons_Working_on_this_project

            returns:

            A Dictionary with Project name and its per head value 
        '''
        f=open("projects.csv",'r')
        lines= f.readlines()
        f.close()
        d={}
        # counting the number of employees working on projects
        for i in lines[1:]:
            i=i.split(",")
            if i[1] in d:
                # incrementing the count
                d[i[1]] += 1
            else:
                # initializing the count
                d[i[1]] = 1
        # print(d)
        valuePerHead={}
        for i in lines[1:]:
            i=i.split(",")
            valuePerHead[i[1]]=int(i[5])/d[i[1]]
        # print(valuePerHead)
        return valuePerHead


    def calEmployeeWorth(self,id,salary):
        '''
            employee Worth is calculated here

                        VALUE PER HEAD
            --------------------------------------------
            SALARY TAKEN DURING THE DURATION OF PROJECTS

        '''
        f=open("projects.csv",'r')
        lines= f.readlines()
        employeeWorth=0
        f.close()
        l=[]
        perDaySalary=salary/30
        expenseOnEmployee=0

        valuePerHead=self.calPerHeadProjectValue()
        sumPerHead=0

        for index,i in enumerate(lines[1:]):
            i=i.split(',')
            if int(i[0])==id:
                l.append(index+1)
        print(l)
        for i in l:
            i=lines[i].split(",")
            duration= datetime.datetime(int(i[4][-2:]),int(i[4][-5:-3]),int(i[4][:2]))-datetime.datetime(int(i[2][-2:]),int(i[2][-5:-3]),int(i[2][:2]))
            sumPerHead+=valuePerHead[i[1]]
            expenseOnEmployee+=perDaySalary*duration.days
        employeeWorth=sumPerHead/expenseOnEmployee
        return employeeWorth
    
    def employeeDetail(self,id):
        '''
            THIS FUCNTION RETURNS THE EMPLOYEE DETAILS
            RETURNS
                DETAILS OF EMPLOYEE 

        '''
        f=open('Employee_details.csv')
        lines=f.readlines()
        f.close()
        for i in lines[1:]:
            i=i.split(',')
            if int(i[0])==id:
                return i
                
    
    def incentives(self,id,margin):
        '''
            INCENTIVE WHICH CAN BE GIVEN TO THE EMPLOYEE IS CALCULATED

            PRINTS INCENTIVES
        '''
        a=self.employeeDetail(id)
        profit_givenout=float(a[4])-1
        incentive_multiplier=profit_givenout-(margin/100)

        if incentive_multiplier<=0:
            print("No incentives can be given to this employee")
        else:
            print(str(round(incentive_multiplier*int(a[3])))+" Rupees of incentives can be given")

