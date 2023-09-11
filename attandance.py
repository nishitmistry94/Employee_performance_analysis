import datetime
import matplotlib.pyplot as plt
class attandance:
    def __init__(self) -> None:
        plt.figure(figsize=(15,6))
        pass
    def monthlyView(self,emp_id,getCountOnly=False):
        '''
            MONTHLY VIEW OF LAST 30 DAYS HRS WORKED IS DISPLAY IN GRAPH
        '''
        try:
            f = open('attandance_sheets//'+str(emp_id)+'.csv','r')
        except:
             print("the entered emp_id does not have an attandance sheet")
             print("Please retrieve the sheet from machine and put it in attandance_sheet folder")
             return
        lines = f.readlines()
        list = []
        absent_count=0
        present_count=0
        label =[]
        for line in lines[1:]:
                y = line.split(',')
                tite=y[1]
                if y[3]!="":
                    present_count+=1
                    t1 = datetime.datetime.strptime(y[4][:-1]+":00", "%H:%M:%S")
                    t2 = datetime.datetime.strptime(y[3]+":00", "%H:%M:%S")
                    duration = t2 - t1
                    list.append(abs(round(duration.total_seconds()/3600)))
                    label.append(y[2][:2]+"\n"+y[2][2:5])
                else:
                     absent_count+=1
                     list.append(0)
                     label.append(y[2][:2]+"\n"+y[2][2:5])  

        if getCountOnly:
             return present_count,absent_count
        
        plt.gcf().text(0.01, 0.5, "Absent Count:"+str(absent_count), fontsize=10,bbox=dict(facecolor='red', alpha=0.25))      
        plt.gcf().text(0.01, 0.55, "Present Count:"+str(present_count), fontsize=10,bbox=dict(facecolor='green', alpha=0.25))    
        plt.bar(label,list,width=0.3) 
        plt.title(tite.capitalize()+"'s Attandance")
        plt.show()       
        f.close()
        return present_count,absent_count