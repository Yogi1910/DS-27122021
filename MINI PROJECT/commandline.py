import json
import operations
from json import JSONDecodeError
from datetime import datetime,date

print("Welcome to Mini LMS")
i1=0
while(i1!=3):
    print("Press :")
    print("1: Register")
    print("2: Login")
    print("3: Exit")
    try:
        i1=int(input())
    except ValueError:
        print("Please enter valid choice")
        continue
    if i1==1:
        i2=0
        print("Press :")
        print("1: Register as Program Manager")
        print("2: Register as Student")
        try:
            i2=int(input())
        except ValueError:
            print("Please enter valid choice")
            continue
        if i2==1:
            print("Enter Full Name")
            f=input()
            print("Enter Mobile Number")
            m=input()
            print("Enter Email")
            e=input()
            print("Enter Password")
            p=input()
            fo=open('managers.json','r')
            if (len(f)*len(m)*len(e)*len(p))==0 or len(m)!=10 or len(p)<8:
                print("Please enter valid data")
                continue
            try:
                fc=str(json.load(fo))
                if m in fc:
                    print("Mobile Number already exists")
                    continue
            except JSONDecodeError:
                pass    
           
            o1=operations.Register('manager','managers.json','students.json',f,m,e,p)
            if o1==True:
                print("Registered Successfully as Manager")
            else:
                print("Registration unsuccessful")
                continue
        elif i2==2:
            print("Enter Full Name")
            f=input()
            print("Enter Mobile Number")
            m=input()
            print("Enter Email")
            e=input()
            print("Enter Password")
            p=input()
            fo=open('students.json','r')
            if (len(f)*len(m)*len(e)*len(p))==0 or len(m)!=10 or len(p)<8:
                print("Please enter valid data")
                continue
            try:
                fc=str(json.load(fo))
                if m in fc:
                    print("Mobile Number already exists")
                    continue
            except JSONDecodeError:
                pass            
            o1=operations.Register('student','managers.json','students.json',f,m,e,p)
            if o1==True:
                print("Registered Successfully as Student")
            else:
                print("Registration unsuccessful")
                continue
    elif i1==2:
            print("Press: ")
            print("1: Login as Program Manager")
            print("2: Login as Student")
            try:
                i3=int(input())
            except ValueError:
                print("Please enter valid choice")
                continue
            if i3==1:
                print("Enter Email:")
                e=input()
                print("Enter Password:")
                p=input()
                o2=operations.login('manager','students.json','managers.json',e,p)
                print(o2)
                if o2==True:
                    n=""
                    t=open('managers.json','r')
                    content=json.load(t)
                    t.close()
                    for i in range(len(content)):
                        if content[i]["Email"]==e and content[i]["Password"]==p:
                            n=content[i]["Full Name"]
                            break
                    print("Welcome "+str(n))
                    while True:
                        print("Press :")
                        print("1: Manage Modules")
                        print("2: Manage Students")
                        print("3: Manage Units")
                        print("0: Logout")
                        try:
                            i4=int(input())
                        except ValueError:
                            print("Please enter valid choice")
                            continue
                        if i4==1:
                            print("1: Create Module")
                            print("2: View all Modules")
                            print("3: View Module Details")
                            print("4: Update Module")
                            print("5: Delete Module")
                            try:
                                in12=int(input())
                            except ValueError:
                                print("Please enter valid choice")
                                continue
                            if in12==1:
                                id1=operations.AutoGenerate_ModuleID()
                                print("Module ID generated is "+str(id1))
                                print("Enter Module Name")
                                m_name=input()
                                print("Enter Start Date (YYYY-MM-DD)")
                                s_dt=input()
                                print("Enter End Date (YYYY-MM-DD)")
                                en_dt=input()
                                print("Enter Number of units")
                                try:
                                    n1=int(input())
                                except ValueError:
                                    print("Please enter valid data")
                                    continue
                                l=[]
                                fc=open('units.json','r')
                                cc=json.load(fc)
                                if len(cc)==0:
                                    print("No Units Available")
                                else:
                                    print("Units Available: ")
                                for i in range(len(cc)):
                                    print("Unit ID: "+str(cc[i]["Unit ID"]))
                                    print("Type: "+str(cc[i]["Type"]))
                                    print("Scheduled Date: "+str(cc[i]["Scheduled Date"]))
                                    print("Start Time: "+str(cc[i]["Start Time"]))
                                    print("End Time: "+str(cc[i]["End Time"]))
                                    print('\n')
                                for i in range(n1):
                                    print("Enter Unit ID")
                                    un_id=input()
                                    if un_id in str(cc):
                                        l.append(un_id)
                                    else:
                                        print("Please enter valid Unit ID")
                                        continue
                                if (len(m_name)*len(s_dt)*len(en_dt))==0 or str(s_dt)>str(en_dt):
                                    print("Plese enter valid data")
                                    continue
                                o3=operations.Create_Module('modules.json',id1,m_name,s_dt,en_dt,l,n)
                                if o3==True:
                                    print("Module Successfully created")
                                else:
                                    print("Please enter valid data")
                                    continue
                            elif in12==2:
                                u=[]
                                o=[]
                                c=[]
                                op5=operations.View_all_modules('modules.json',n,u,o,c)
                                if op5==False:
                                    print("No Modules Available")
                                    continue
                                else:
                                    a=False
                                    f=open('modules.json','r')
                                    try:
                                        cnt=json.load(f)
                                        for i in range(len(cnt)):
                                            if cnt[i]["Module ID"] in u and cnt[i]["Created By"]==n:
                                                print("Module ID: "+str(cnt[i]["Module ID"]))
                                                print("Module Name: "+str(cnt[i]["Module Name"]))
                                                print("Module Start Date: "+str(cnt[i]["Module Start Date"]))
                                                print("Module End Date: "+str(cnt[i]["Module End Date"]))
                                                print("Units: "+str(cnt[i]["Units"]))
                                                print("Module Status: Upcoming \n")
                                                a=True
                                            if cnt[i]["Module ID"] in o and cnt[i]["Created By"]==n:
                                                print("Module ID: "+str(cnt[i]["Module ID"]))
                                                print("Module Name: "+str(cnt[i]["Module Name"]))
                                                print("Module Start Date: "+str(cnt[i]["Module Start Date"]))
                                                print("Module End Date: "+str(cnt[i]["Module End Date"]))
                                                print("Units: "+str(cnt[i]["Units"]))
                                                print("Module Status: Ongoing \n")
                                                a=True
                                            elif cnt[i]["Module ID"] in c and cnt[i]["Created By"]==n:
                                                print("Module ID: "+str(cnt[i]["Module ID"]))
                                                print("Module Name: "+str(cnt[i]["Module Name"]))
                                                print("Module Start Date: "+str(cnt[i]["Module Start Date"]))
                                                print("Module End Date: "+str(cnt[i]["Module End Date"]))
                                                print("Units: "+str(cnt[i]["Units"]))
                                                print("Module Status: Completed \n")
                                        if a==False:
                                            print("No Modules available! \n")
                                    except JSONDecodeError:
                                        print("Modules not available")    
                            elif in12==3:
                                print("Enter Module ID: ")
                                mdl_id=input()
                                f9=open('modules.json','r')
                                try:
                                    c9=str(json.load(f9))
                                except JSONDecodeError:
                                    print("Modules not available")
                                    continue
                                l=operations.Read_Module('modules.json',mdl_id)
                                if len(l)==0:
                                    print("Invalid Module ID")
                                    continue
                                else:
                                    for i in range(len(l)):
                                        print("Module ID: "+str(l[i]["Module ID"]))
                                        print("Module Name: "+str(l[i]["Module Name"]))
                                        print("Module Start Date: "+str(l[i]["Module Start Date"]))
                                        print("Module End Date : "+str(l[i]["Module End Date"]))
                                        print("Units: "+str(l[i]["Units"]))
                                        date_today=str(date.today())
                                        if date_today<l[i]["Module Start Date"]:
                                            print("Module Status: Upcoming \n")
                                        elif date_today>=l[i]["Module Start Date"] and date_today<=l[i]["Module End Date"]:
                                            print("Module Status: Ongoing \n")
                                        else:
                                            print("Module Status: Completed \n")
                            elif in12==4:
                                print("Enter Module ID")
                                module_id=input()
                                print("Enter detail to be updated ( Module Name | Module Start Date | Module End Date )")
                                upd_dtl=input()
                                print("Enter new value")
                                n_dtl=input()
                                if (len(module_id)*len(upd_dtl)*len(n_dtl))==0:
                                    print("Please enter valid data")
                                    continue
                                o11=operations.Update_Module(n,'modules.json',module_id,upd_dtl,n_dtl)
                                if o11==True:
                                    print("Module Updated Successfully")
                                else:
                                    print("Cannot update module")
                            elif in12==5:
                                print("Enter Module ID to be deleted")
                                module_id=input()
                                if len(module_id)==0:
                                    print("Please enter valid ID")
                                    continue
                                o5=operations.Delete_Module(n,'modules.json',module_id)
                                if o5==True:
                                    print("Module Successfully Deleted")
                                else:
                                    print("Please enter valid ID")
                                    continue
                            else:
                                print("Please enter valid choice")
                                continue
                        elif i4==2:
                            print("Press: ")
                            print("1: View Student Details")
                            print("2: Update Student")
                            print("3: Delete Student")
                            print("4: Enroll a Student")
                            try:
                                in13=int(input())
                            except ValueError:
                                print("Please enter valid choice")
                                continue
                            if in13==1:
                                print("Enter Mobile Number of student")
                                Mo_num=input()
                                l=[]
                                l=operations.Read_Student('students.json',Mo_num)
                                if len(l)==0:
                                    print("Student does not exist")
                                else:
                                    for i in range(len(l)):
                                        print("\nFull Name: "+str(l[i]["Full Name"]))
                                        print("Mobile Number: "+str(l[i]["Mobile Number"]))
                                        print("Email: "+str(l[i]["Email"]))
                                        print("Modules Enrolled: "+str(l[i]["Modules Enrolled"]))
                                        print("")
                            elif in13==2:
                                print("Enter Mobile Number of Student")
                                M_num=input()
                                print("Enter Detail to be updated ( Full Name | Mobile Number | Email | Password )")
                                upd_dtl=input()
                                print("Enter new value")
                                n_dtl=input()
                                if (len(M_num)*len(upd_dtl)*len(n_dtl))==0 or len(M_num)!=10 or (upd_dtl=="Email" and '@' not in n_dtl) or (upd_dtl=="Email" and '.com' not in n_dtl) or (upd_dtl=="Mobile Number" and len(n_dtl)!=10) or (upd_dtl=="Password" and len(n_dtl)<8):
                                    print("Please enter valid data")
                                    continue
                                o12=operations.Update_Student('students.json',M_num,upd_dtl,n_dtl)
                                if o12==True:
                                    print("Student Updated Successfully")
                                else:
                                    print("Cannot update student")
                                    continue
                            elif in13==3:
                                print("Enter Mobile Number of Student")
                                M_num=input()
                                if len(M_num)<10:
                                    print("Please enter valid Mobile Number")
                                    continue
                                o13=operations.Delete_Student('students.json',M_num)
                                if o13==True:
                                    print("Student Deleted Successfully!")
                                else:
                                    print("Cannot delete student")
                            elif in13==4:
                                print("Enter Mobile Number of Student")
                                ph_num=input()
                                print("Enter Module ID")
                                md_id=input()
                                f11=open('students.json','r')
                                try:
                                    c11=json.load(f11)
                                except JSONDecodeError:
                                    print("Students not available")
                                    f11.close()
                                    continue
                                f11.close()
                                if ph_num not in str(c11):
                                    print("No such student exits!")
                                    continue
                                f21=open('modules.json','r')
                                try:
                                    c21=json.load(f21)
                                except JSONDecodeError:
                                    print("Modules not available")
                                    f21.close()
                                    continue
                                f21.close()
                                if md_id not in str(c21):
                                    print("No such module exits!")
                                    continue
                                if (len(md_id)*len(n))==0:
                                    print("Please enter valid Data")
                                    continue
                                else:
                                    op=operations.Enroll_in_module('students.json',ph_num,md_id)
                                    if op==True:
                                        print("Enrolled Successfully")
                                    else:
                                        print("Enrollment Unsucessful")
                            else:
                                print("Please enter valid choice")
                        elif i4==3:
                            print("Press: ")
                            print("1: Create Unit")
                            print("2: View all Units")
                            print("3: View Unit Details")
                            print("4: Update Unit")
                            print("5: Delete Unit")
                            try:
                                in14=int(input())
                            except ValueError:
                                print("Please enter valid choice")
                                continue
                            if in14==1:
                                uid=operations.AutoGenerate_UnitID()
                                print("Unit ID generated is "+str(uid))
                                print("Enter type of unit")
                                unit_type=input()
                                print("Enter name of unit")
                                unit_title=input()
                                print("Enter start time of unit (HH:MM:SS)")
                                unit_st_time=input()
                                print("Enter end time of unit (HH:MM:SS)")
                                unit_en_time=input()
                                print("Enter Scheduled date (YYYY-MM-DD)")
                                unit_date=input()
                                if (len(unit_type)*len(unit_title)*len(unit_st_time)*len(unit_en_time)*len(unit_date))==0 or len(unit_st_time)!=8 or len(unit_en_time)!=8 or str(unit_st_time)>str(unit_en_time):
                                    print("Please enter valid data")
                                else:
                                    operations.Create_Unit('units.json',uid,unit_type,unit_title,unit_st_time,unit_en_time,unit_date)
                                    print("Unit created successfully")
                            elif in14==2:
                                d=operations.Read_all_Units('units.json')
                                if len(d)==0:
                                    print("No units available")
                                    continue
                                else:
                                    for i in range(len(d)):
                                        print("Unit ID: "+str(d[i]["Unit ID"]))
                                        print("Unit Name: "+str(d[i]["Title"]))
                                        print("Unit Type: "+str(d[i]["Type"]))
                                        print('\n')
                            elif in14==3:
                                print("Enter Unit ID")
                                un_id=input()
                                d=operations.Read_Unit_Details('units.json',un_id)
                                if len(d)==0:
                                    print("Invalid Unit ID")
                                else:
                                    for i in range(len(d)):
                                        print("\nUnit ID: "+str(d[i]["Unit ID"]))
                                        print("Unit Name: "+str(d[i]["Title"]))
                                        print("Unit Type: "+str(d[i]["Type"]))
                                        print("Scheduled Date: "+str(d[i]["Scheduled Date"]))
                                        print("Unit Start Time: "+str(d[i]["Start Time"]))
                                        print("Unit End Time: "+str(d[i]["End Time"]))
                                        st=operations.Get_Unit_Status('units.json',un_id)
                                        print("Unit Status: "+str(st))
                                        print("")
                            elif in14==4:
                                print("Enter Unit ID")
                                un_id=input()
                                print("Enter Detail to be updated ( Type | Title | Scheduled Date | Start Time | End Time )")
                                dtl_upd=input()
                                print("Enter new value")
                                new_dtl=input()
                                if (len(un_id)*len(dtl_upd)*len(new_dtl))==0:
                                    print("Please enter valid data")
                                else:
                                    op9=operations.Update_Unit('units.json',un_id,dtl_upd,new_dtl)
                                    if op9==True:
                                        print("Unit updated successfully \n")
                                    else:
                                        print("Cannot update unit")
                            elif in14==5:
                                print("Enter Unit ID")
                                un_id=input()
                                if len(un_id)==0:
                                    print("Please enter valid data")
                                else:
                                    op=operations.Delete_Unit('units.json',un_id)
                                    if op==True:
                                        print("Unit deleted successfully")
                                    else:
                                        print("Cannot delete unit")
                            else:
                                print("Please enter valid Choice")
                        elif i4==0:
                            break
                        else:
                            print("Please enter valid Choice")
                else:
                    print("Invalid Credentials")
                    continue
            elif i3==2:
                print("Enter Email:")
                e=input()
                print("Enter Password:")
                p=input()
                o6=operations.login('student','students.json','managers.json',e,p)
                if o6==True:
                    t=open('students.json')
                    content=json.load(t)
                    n=""
                    mnum=""
                    for i in range(len(content)):
                        if content[i]["Password"]==p and content[i]["Email"]==e:
                            n=content[i]["Full Name"]
                            mnum=content[i]["Mobile Number"]
                            break
                    while True:
                        print("Press :")
                        print("1: View Today's Schedule")
                        print("2: Update Password")
                        print("3: View My Modules")
                        print("4: Logout")
                        try:
                            in2=int(input())
                        except ValueError:
                            print("Please enter valid choice")
                            continue
                        if in2==1:
                            f=open('students.json','r')
                            content=json.load(f)
                            f.close()
                            e=[]
                            for i in range(len(content)):
                                if content[i]["Full Name"]==n:
                                    e=content[i]["Modules Enrolled"]
                                    break
                            f1=open('modules.json','r')
                            content2=json.load(f1)
                            f1.close()
                            l=[]
                            t=[]
                            for i in range(len(e)):
                                for j in range(len(content2)):
                                    if e[i]==content2[j]["Module ID"]:
                                        t.append(content2[j]["Units"])
                            for i in range(len(t)):
                                tb=t[i]
                                for j in range(len(tb)):
                                    if tb[j] not in l:
                                        l.append(tb[j])
                            u=[]
                            o=[]
                            c=[]
                            operations.View_Todays_Schedule(l,'units.json',u,o,c)
                            if len(o)==0:
                                print("No units scheduled for today! \n")
                            else:
                                print("Today's Schedule: ")
                                for i in range(len(o)):
                                    print("Unit Name: "+str(o[i]["Title"]))
                                    print("Unit Type: "+str(o[i]["Type"]))
                                    print("Scheduled Date: "+str(o[i]["Scheduled Date"]))
                                    print("Unit Start Time: "+str(o[i]["Start Time"]))
                                    print("Unit End Time: "+str(o[i]["End Time"]))
                        elif in2==2:
                            print("New Password")
                            nw_p=input()
                            if len(nw_p)<8: 
                                print("Password should have at least 8 characters \n")
                                continue
                            op12=operations.Update_Student('students.json',mnum,"Password",nw_p)
                            if op12==True:
                                print("Password updated successfully")
                            else:
                                print("Cannot update Password")
                                continue
                        elif in2==3:
                            d=operations.Read_all_enrolled_modules('students.json',n)
                            if len(d)==0:
                                print("No Modules Enrolled \n")
                            else:
                                print(d)
                        elif in2==4:
                            break
                else:
                    print("Invalid credentials")
                    continue

