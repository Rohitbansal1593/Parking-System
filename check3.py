import mysql.connector           #to create cursor object
import time                      #To just gave a sleep 
import uuid                      #for unique id in Park class
from datetime import datetime    #to store the current time in park class table
mydb=mysql.connector.connect(host="localhost",user='root',password="admin",database="parking")
cur=mydb.cursor()
s1="INSERT INTO OWNER_DETAIL (MALLNAME,CAPACITYTWOWHEELER,CAPACITYFOURWHEELER) VALUES (%s,%s,%s)"
s2="INSERT INTO park (uuid,vehicle_number,vehicle_type,MALLNAME,entry_time) VALUES (%s,%s,%s,%s,%s)"
s5="update owner_detail set CAPACITYTWOWHEELER=%s where MALLNAME=%s"
s6="update owner_detail set CAPACITYFOURWHEELER=%s where MALLNAME=%s"
class OWNER:
    def __init__(self,name) -> None:
        self.name=name
        self.space_two=int(input("enter the capacity of two wheelers"))
        self.space_four=int(input("enter the capacity of four wheelers"))
    def __str__(self) -> str:
        b1=[self.name,self.space_two,self.space_four]
        cur.execute(s1,b1)
        mydb.commit()
        return f"{self.name} mall has a capacity of {self.space_two} for two wheelers and {self.space_four} for four wheelers"
class PARK(OWNER):
    def __init__(self,mall_name,vehicle_type):
        self.mall_name=mall_name
        self.vehicle_type=vehicle_type
    @staticmethod

    #start from hereeeeeeeee------------>
    def unpark():
        number_vehicle=input("enter vehicle number")
        now = datetime.now()
        exit_time= now.strftime("%H:%M:%S") 
        s7="select entry_time from park where vehicle_number=%s"
        b6=[number_vehicle]
        cur.execute(s7,b6)
        time_of_entry=cur.fetchone()
        time_of_entry=list(time_of_entry)
        time_of_entry=time_of_entry[0]
        #print(time_of_entry)
        #print(exit_time)
        
        

        #self.check=1
        '''if vehicle_type==2:
            s3="select CAPACITYTWOWHEELER from OWNER_DETAIL where MALLNAME=mall_name"
            cur.execute(s3)
            self.result=cur.fetchall()
            if self.result<=0:
                print("Sorry! We are out of space")
                self.check=0
            else:
                self.id=str(uuid.uuid4()) 
                now = datetime.now()
                self.current_time = now.strftime("%H:%M:%S") 
        elif vehicle_type==4:
            s4="select CAPACITYFOURWHEELER from OWNER_DETAIL where MALLNAME=mall_name"
            cur.execute(s4)
            self.result=cur.fetchall()
            if self.result<=0:
                print("Sorry! We are out of space")
                self.check=0
            else:
                self.id=str(uuid.uuid4()) 
                now = datetime.now()
                self.current_time = now.strftime("%H:%M:%S")''' 
print("Choose Your Self","Press 1 for OWNER","Press 2 for Guest")
print("1.OWNER","2.Want to Park","3.Unpark",sep=" ")
x=int(input())
if x==1:
    name=input("enter name of mall")
    print(OWNER(name))
elif x==2:
    mall_name=input("enter Mall name")
    b3=[mall_name]
    print("Choose vehicle type")
    print("press 2 for Two Wheelers","press 4 for four wheelers")
    vehicle_type=int(input())
    print("checking for availability of space")
    time.sleep(2)
    check=1
    p=PARK(mall_name,vehicle_type)
    if vehicle_type==2:
            s3="select CAPACITYTWOWHEELER from OWNER_DETAIL where MALLNAME=%s"
            cur.execute(s3,b3)
            result=cur.fetchone()
            result=sum(list(result))
            if result<=0:
                check=0
                
            else:
                id=str(uuid.uuid4()) 
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S") 
                s3="select CAPACITYTWOWHEELER from OWNER_DETAIL where MALLNAME=%s"
                cur.execute(s3,b3)
                result=cur.fetchone()
                result=sum(list(result))
                b4=[result-1,mall_name]
                cur.execute(s5,b4)
                mydb.commit()
    elif vehicle_type==4:
            s4="select CAPACITYFOURWHEELER from OWNER_DETAIL where MALLNAME=%s"
            cur.execute(s4,b3)
            result=cur.fetchone()
            result=sum(list(result))
            if result<=0:
                check=0
                
            else:
                id=str(uuid.uuid4()) 
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                s4="select CAPACITYFOURWHEELER from OWNER_DETAIL where MALLNAME=%s"
                cur.execute(s4,b3)
                result=cur.fetchone()
                result=sum(list(result))
                b5=[result-1,mall_name]
                cur.execute(s6,b5)
                mydb.commit()
    if check==1:
        print("enter vehicle number")
        vechicle_number=input()
        b2=[id,vechicle_number,vehicle_type,mall_name,current_time]
        cur.execute(s2,b2)
        mydb.commit()
    else:
        print("sorry we are out of space")
elif x==3:
    PARK.unpark()
else:
    print("enter correctly")

