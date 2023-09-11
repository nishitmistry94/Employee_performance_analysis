from analysis import analysis
class employee():
    def __init__(self,employee_name,employee_id,joining_date,employee_salary,project):
        self.employee_name=employee_name
        self.employee_id=employee_id
        self.joining_date=joining_date
        self.employee_salary=employee_salary
        an=analysis()
        if project:
            self.EPI=an.calEmployeeWorth(self.employee_id,self.employee_salary)
            self.EPI=round(self.EPI,2)
        else:
            self.EPI='N/A'
        self.write()

    def write(self):
        '''
            THIS FUNCTIONS WRITE THE DATA INTO FILE 
            EMPLOYEE_DETAILS.CSV
        '''
        f=open('Employee_details.csv')
        lines=f.readlines()
        f.close()
        str=f"\n{self.employee_id},{self.employee_name},{self.joining_date},{self.employee_salary},{self.EPI}"
        lines.append(str)
        f=open('Employee_details.csv','w')
        f.writelines(lines)
        f.close()
        
    def getIncentives(profit_margin):
        pass





