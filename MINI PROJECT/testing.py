from select import select
import unittest
from json import JSONDecodeError
import operations
import json
from datetime import date

id1=operations.AutoGenerate_ModuleID()
id2=operations.AutoGenerate_ModuleID()
uid1=operations.AutoGenerate_UnitID()
uid2=operations.AutoGenerate_UnitID()

class Test_operations(unittest.TestCase):
    
    f=open('/home/projects/Project/modules.json','r+')
    f.seek(0)
    f.truncate()
    f.close()
    f1=open('/home/projects/Project/students.json','r+')
    f1.seek(0)
    f1.truncate()
    f1.close()
    f2=open('/home/projects/Project/units.json','r+')
    f2.seek(0)
    f2.truncate()
    f2.close()
    f3=open('/home/projects/Project/managers.json','r+')
    f3.seek(0)
    f3.truncate()

    def test_a(self):
        '''Testing Register Function'''
        Full_Name=[]
        Full_Name.append("Test Manager 1")
        Full_Name.append("Test Manager 2")
        Full_Name.append("Test Student 1")
        Full_Name.append("Test Student 2")
        Mobile_Number=[]
        Mobile_Number.append("1122334455")
        Mobile_Number.append("6677889900")
        Mobile_Number.append("9898989898")
        Mobile_Number.append("8787878787")
        Email=[]
        Email.append("testadmin1@gmail.com")
        Email.append("testadmin2@gmail.com")
        Email.append("teststudent1@gmail.com")
        Email.append("teststudent2@gmail.com")
        Password=[]
        Password.append("admin1")
        Password.append("admin2")
        Password.append("student1")
        Password.append("student2")
        type=[]
        type.append('manager')
        type.append('manager')
        type.append('student')
        type.append('student')
        f='/home/projects/Project/managers.json'
        f2='/home/projects/Project/students.json'
        for i in range(4):
            operations.Register(type[i],f,f2,Full_Name[i],Mobile_Number[i],Email[i],Password[i])
        Invalid_Full_Name=[]
        Invalid_Mobile_Number=[]
        Invalid_Email=[]
        Invalid_Password=[]
        Invalid_Type=[]
        '''-------'''
        Invalid_Full_Name.append("Manager with Invalid Number")
        Invalid_Mobile_Number.append("1234567")
        Invalid_Email.append("test@gmail.com")
        Invalid_Password.append("testpassword")
        Invalid_Type.append("manager")
        '''-------'''
        Invalid_Full_Name.append("Manager with Invalid Email")
        Invalid_Mobile_Number.append("0123456789")
        Invalid_Email.append("testgmail")
        Invalid_Password.append("testpassword")
        Invalid_Type.append("manager")
        '''-------'''
        Invalid_Full_Name.append("Student with Invalid Password")
        Invalid_Mobile_Number.append("0123456789")
        Invalid_Email.append("testgmail")
        Invalid_Password.append("")
        Invalid_Type.append("student")
        '''-------'''
        for i in range(3):
            operations.Register(Invalid_Type[i],f,f2,Invalid_Full_Name[i],Invalid_Mobile_Number[i],Invalid_Email[i],Invalid_Password[i])
        temp1=open(f,'r')
        temp2=open(f2,'r')
        generated_output=""
        try:
            content=json.load(temp1)
            content2=json.load(temp2)
            generated_output+=str(content)
            generated_output+=str(content2)
            temp1.close()
            temp2.close()
        except JSONDecodeError:
            self.assertEqual("expected_output","generated_output")
            temp1.close()
            temp2.close()
        mananger_expected_output=[{'Full Name': 'Test Manager 1', 'Mobile Number': '1122334455', 'Email': 'testadmin1@gmail.com', 'Password': 'admin1'}, {'Full Name': 'Test Manager 2', 'Mobile Number': '6677889900', 'Email': 'testadmin2@gmail.com', 'Password': 'admin2'}]
        student_expected_output=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        expected_output=str(mananger_expected_output)+str(student_expected_output)
        a=str(expected_output).lower()
        b=str(generated_output).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb) 

    def test_b(self):
        '''Testing Login functionality'''
        '''Populating Student Values'''
        temp=open('/home/projects/Project/students.json','r+')
        temp.seek(0)
        temp.truncate()
        l=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        json.dump(l,temp)
        temp.close()
        '''-----------------'''
        '''Populating Manager Values'''
        temp1=open('/home/projects/Project/managers.json','r+')
        temp1.seek(0)
        temp1.truncate()
        l1=[{'Full Name': 'Test Manager 1', 'Mobile Number': '1122334455', 'Email': 'testadmin1@gmail.com', 'Password': 'admin1'}, {'Full Name': 'Test Manager 2', 'Mobile Number': '6677889900', 'Email': 'testadmin2@gmail.com', 'Password': 'admin2'}]
        json.dump(l1,temp1)
        temp1.close()
        '''-----------------'''
        f='/home/projects/Project/managers.json'
        f1='/home/projects/Project/students.json'
        email="testadmin1@gmail.com"
        pswd="admin1"
        f1=operations.login("manager",f1,f,email,pswd)
        email1="Ar@gmail.com"
        pswd1="Helloar"
        f2=operations.login("students",f,f,email1,pswd1)
        ans=str(f1)+str(f2)
        expected_output="TrueFalse"
        a=str(expected_output).lower()
        a.replace(" ","")
        b=str(ans).lower()
        b.replace(" ","")
        self.assertEqual(a,b)

    def test_c(self):
        '''Creating Units'''
        f='/home/projects/Project/units.json'
        '''Populating with values'''
        t=open('/home/projects/Project/modules.json','r+')
        t.seek(0)
        t.truncate()
        units1=[]
        units1.append(uid1)
        units2=[]
        units2.append(uid1)
        units2.append(uid2)
        l=[{"Module ID": id1, "Module Name": "Data Science", "Module Start Date": "2022-01-25", "Module End Date": "2022-02-10", "Units": [uid1], "Created By": "Test Manager 1"}, {"Module ID": id2, "Module Name": "React", "Module Start Date": "2022-02-15", "Module End Date": "2022-03-17", "Units": [uid1,uid2], "Created By": "Test Manager 2"}]
        json.dump(l,t)
        t.close()
        '''----------------------'''
        Unit_ID=[]
        Unit_ID.append(uid1)
        Unit_ID.append(uid2)
        type_of_unit=[]
        type_of_unit.append("quiz")
        type_of_unit.append("live session") 
        title=[]
        title.append("DataScience101")
        title.append("React103")
        start_time=[]
        start_time.append("17:00:00")
        start_time.append("15:00:00")
        end_time=[]
        end_time.append("19:00:00")
        end_time.append("15:50:00")
        scheduled_date=[]
        scheduled_date.append("2022-01-28")
        scheduled_date.append("2022-01-01")
        for i in range(len(Unit_ID)):
            operations.Create_Unit(f,Unit_ID[i],type_of_unit[i],title[i],start_time[i],end_time[i],scheduled_date[i])
        expected_output=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        r=open('/home/projects/Project/units.json','r')
        try:
            data=json.load(r)
        except JSONDecodeError:
            data="wrong output"
        r.close()
        a=str(expected_output).lower()
        b=str(data).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)
    
    def test_d(self):
        '''Reading Unit details'''
        Unit_ID=uid1
        f='/home/projects/Project/units.json'
        '''----------------------'''
        t1=open('/home/projects/Project/units.json','r+')
        t1.seek(0)
        t1.truncate()
        l1=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        json.dump(l1,t1)
        t1.close()
        '''----------------------'''
        details=operations.Read_Unit_Details(f,Unit_ID)
        expected_output=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}]
        a=str(expected_output).lower()
        b=str(details).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)

    def test_e(self):
        '''Reading all Units created'''
        f='/home/projects/Project/units.json'
        '''----------------------'''
        t1=open('/home/projects/Project/units.json','r+')
        t1.seek(0)
        t1.truncate()
        l1=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        json.dump(l1,t1)
        t1.close()
        '''----------------------'''
        details=operations.Read_all_Units(f)
        expected_output=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        a=str(expected_output).lower()
        b=str(details).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)

    def test_f(self):
        '''Updating Unit'''
        f='/home/projects/Project/units.json'
        Unit_ID=uid1
        '''----------------------'''
        t1=open('/home/projects/Project/units.json','r+')
        t1.seek(0)
        t1.truncate()
        l1=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        json.dump(l1,t1)
        t1.close()
        '''----------------------'''
        new_start_time="14:30:00"
        operations.Update_Unit(f,Unit_ID,"Start Time",new_start_time)
        expected_output=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "14:30:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        r=open('/home/projects/Project/units.json','r')
        data=json.load(r)
        r.close()
        a=str(expected_output).lower()
        b=str(data).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)

    def test_g(self):
        '''Deleting Units'''
        f='/home/projects/Project/units.json'
        Unit_ID_tbd=uid2
        '''----------------------'''
        t1=open('/home/projects/Project/units.json','r+')
        t1.seek(0)
        t1.truncate()
        l1=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        json.dump(l1,t1)
        t1.close()
        '''----------------------'''
        operations.Delete_Unit(f,Unit_ID_tbd)
        expected_output=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}]
        r=open('/home/projects/Project/units.json','r')
        data=json.load(r)
        r.close()
        a=str(expected_output).lower()
        a.replace(" ","")
        b=str(data).lower()
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)
    

    def test_h(self):
        '''View Student Details | Reading Students'''
        Email="teststudent1@gmail.com"
        Full_Name="Test Student 1"
        '''Populating with values'''
        t=open('/home/projects/Project/students.json','r+')
        t.seek(0)
        t.truncate()
        l=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        json.dump(l,t)
        t.close()
        '''----------------------'''
        details=[]
        f='/home/projects/Project/students.json'
        details=operations.Read_Student(f,"9898989898")
        expected_output=[{"Full Name": "Test Student 1", "Mobile Number": "9898989898", "Email": "teststudent1@gmail.com", "Password": "student1", "Modules Enrolled": []}]
        a=str(expected_output).lower()
        b=str(details).lower()
        a.replace(" ","")
        b.replace(" ","")
        self.assertEqual(a,b)

    def test_i(self):
        '''Update Student'''
        f='/home/projects/Project/students.json'
        new_email="AdEy@gmail.com"
        '''Populating with values'''
        t=open('/home/projects/Project/students.json','r+')
        t.seek(0)
        t.truncate()
        l=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        json.dump(l,t)
        t.close()
        '''----------------------'''
        operations.Update_Student(f,"9898989898","Email",new_email)
        expected_output=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': new_email, 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        r=open('/home/projects/Project/students.json','r')
        data=json.load(r)
        r.close()
        a=str(expected_output).lower()
        a.replace(" ","")
        b=str(data).lower()
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)
    
    def test_j(self):
        '''Deleting Students'''
        f='/home/projects/Project/students.json'
        Mobile_no="9898989898"
        '''Populating with values'''
        t=open('/home/projects/Project/students.json','r+')
        t.seek(0)
        t.truncate()
        l=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        json.dump(l,t)
        t.close()
        '''----------------------'''
        operations.Delete_Student(f,Mobile_no)
        expected_output=[{'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        r=open('/home/projects/Project/students.json','r')
        data=json.load(r)
        r.close()
        a=str(expected_output).lower()
        b=str(data).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)

    def test_k(self):
        '''Enrolling Students'''
        f='/home/projects/Project/students.json'
        '''Populating Student Values'''
        t2=open('/home/projects/Project/students.json','r+')
        t2.seek(0)
        t2.truncate()
        l2=[{'Full Name': 'Test Student 1', 'Mobile Number': '9898989898', 'Email': 'teststudent1@gmail.com', 'Password': 'student1', "Modules Enrolled":[]}, {'Full Name': 'Test Student 2', 'Mobile Number': '8787878787', 'Email': 'teststudent2@gmail.com', 'Password': 'student2', "Modules Enrolled":[]}]
        json.dump(l2,t2)
        t2.close()
        '''-----------------'''
        '''Populating Unit Values'''
        t1=open('/home/projects/Project/units.json','r+')
        t1.seek(0)
        t1.truncate()
        l1=[{"Unit ID": uid1, "Type": "quiz", "Title": "DataScience101", "Scheduled Date": "2022-01-28", "Start Time": "17:00:00", "End Time": "19:00:00"}, {"Unit ID": uid2, "Type": "live session", "Title": "React103", "Scheduled Date": "2022-01-01", "Start Time": "15:00:00", "End Time": "15:50:00"}]
        json.dump(l1,t1)
        t1.close()
        '''----------------------'''
        '''Populating Module values'''
        t=open('/home/projects/Project/modules.json','r+')
        t.seek(0)
        t.truncate()
        units1=[]
        units1.append(uid1)
        units2=[]
        units2.append(uid1)
        units2.append(uid2)
        l=[{"Module ID": id1, "Module Name": "Data Science", "Module Start Date": "2022-01-25", "Module End Date": "2022-02-10", "Units": [uid1], "Created By": "Test Manager 1"}, {"Module ID": id2, "Module Name": "React", "Module Start Date": "2022-02-15", "Module End Date": "2022-03-17", "Units": [uid1,uid2], "Created By": "Test Manager 2"}]
        json.dump(l,t)
        t.close()
        '''----------------------'''
        operations.Enroll_in_module(f,"8787878787",id1)
        operations.Enroll_in_module(f,"8787878787",id2)
        c=[]
        c.append(id1)  
        c.append(id2)  
        expected_output=[{"Full Name": "Test Student 1", "Mobile Number": "9898989898", "Email": "teststudent1@gmail.com", "Password": "student1", "Modules Enrolled": []}, {"Full Name": "Test Student 2", "Mobile Number": "8787878787", "Email": "teststudent2@gmail.com", "Password": "student2", "Modules Enrolled": c}]
        r=open('/home/projects/Project/students.json','r')
        data=json.load(r)
        r.close()
        a=str(expected_output).lower()
        b=str(data).lower()
        a.replace(" ","")
        b.replace(" ","")
        fa=sorted(a)
        fb=sorted(b)
        self.assertEqual(fa,fb)
    

if __name__=='__main__':
    unittest.main()