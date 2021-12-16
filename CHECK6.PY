import mysql.connector           #to create cursor object
import time                      #To just gave a sleep 
import uuid                      #for unique id in Park class
import datetime                    #to store the current time in park class table
mydb=mysql.connector.connect(host="localhost",user='root',password="admin",database="parking")
cur=mydb.cursor()
s1="INSERT INTO OWNER_DETAIL (MALLNAME,CAPACITYTWOWHEELER,CAPACITYFOURWHEELER) VALUES (%s,%s,%s)"
s2="INSERT INTO park (uuid,vehicle_number,vehicle_type,MALLNAME,entry_time) VALUES (%s,%s,%s,%s,%s)"
s5="update owner_detail set CAPACITYTWOWHEELER=%s where MALLNAME=%s"
s6="update owner_detail set CAPACITYFOURWHEELER=%s where MALLNAME=%s"
s7="select CAPACITYTWOWHEELER from owner_detail where mallname=%s"
s8="select CAPACITYFOURWHEELER from owner_detail where mallname=%s"
s9="update owner_detail set CAPACITYTWOWHEELER=%s where MALLNAME=%s"
s10="update owner_detail set CAPACITYFOURWHEELER=%s where MALLNAME=%s"
s11="delete from park where vehicle_number=%s"
s12="insert into revenue(U_id,Time,vehicle_number,cost,mallname) VALUES (%s,%s,%s,%s,%s)"
s13="SELECT MALLNAME FROM OWNER_DETAIL"
s14="select vehicle_number from park"
s15="select sum(cost) from revenue where mallname=%s group by mallname"
s16="select mallname from revenue"
class OWNER:
    def __init__(self,name) -> None:
        self.name=name
        self.space_two=int(input("enter the capacity of two wheelers"))
        self.space_four=int(input("enter the capacity of four wheelers"))
    def __str__(self) -> str:
        b1=[self.name,self.space_two,self.space_four]
        cur.execute(s1,b1)
        mydb.commit()
        print("\n")
        print("Thankyou |  your mall is successfully registered")
        return f"{self.name} mall has a capacity of {self.space_two} for two wheelers and {self.space_four} for four wheelers"
class PARK(OWNER):
    def __init__(self,mall_name,vehicle_type):
        self.mall_name=mall_name
        self.vehicle_type=vehicle_type
    @staticmethod
    def unpark():
        number_vehicle=input("enter vehicle number")
        cur.execute(s14)
        list_of_vehicle=cur.fetchall()
        list_of_vehicle=list(list_of_vehicle)
        list_of_vehicle=[item for t in list_of_vehicle for item in t]
        if number_vehicle not in list_of_vehicle:
            print("\nYOUR VEHICLE IS NOT PARKED HERE|||\n")
            exit()
        exit_time = datetime.datetime.now()
        s71="select vehicle_type,mallname,entry_time,uuid from park where vehicle_number=%s"
        b6=[number_vehicle]
        cur.execute(s71,b6)
        list_all=cur.fetchone()
        list_all=list(list_all)
        type_of_vehicle=list_all[0]
        name_of_mall=list_all[1]
        time_of_entry=list_all[2]
        time_of_stay1=(exit_time-time_of_entry)
        time_of_stay=(exit_time-time_of_entry).total_seconds()
        # fair is 1 rupee per minute
        total_fair=(time_of_stay//60)*1
        #print(time_of_stay)
        id_uuid=list_all[3]
        #print(id_uuid)
        b7=[name_of_mall]
        b9=[number_vehicle]
        b10=[id_uuid,time_of_stay1,number_vehicle,total_fair,name_of_mall]
        cur.execute(s12,b10)
        cur.execute(s11,b9)
        mydb.commit()
        #print(type_of_vehicle,name_of_mall,time_of_entry)
        if type_of_vehicle==2:
            cur.execute(s7,b7)
            past_capacity=cur.fetchone()
            #print(past_capacity)
            past_capacity=sum(list(past_capacity))
            b8=[past_capacity+1,name_of_mall]
            cur.execute(s9,b8)
            mydb.commit()
        elif type_of_vehicle==4:
            cur.execute(s8,b7)
            past_capacity=cur.fetchone()
            past_capacity=sum(list(past_capacity))
            b8=[past_capacity+1,name_of_mall]
            cur.execute(s10,b8)
            mydb.commit()
    @staticmethod
    def revenue_detail():
        mall_name_for_revenue=input('\nenter the name of mall\n')
        cur.execute(s16)
        list_of_mall_revenue=cur.fetchall()
        list_of_mall_revenue=list(list_of_mall_revenue)
        list_of_mall_revenue=[item for t in list_of_mall_revenue for item in t]
        if mall_name_for_revenue not in list_of_mall_revenue:
            print("\nYou Mall not present in revenue table||||\n")
            exit()
        b21=[mall_name_for_revenue]
        cur.execute(s15,b21)
        revenue_of_mall=cur.fetchone()
        revenue_of_mall=sum(list(revenue_of_mall))
        print(mall_name_for_revenue,":",revenue_of_mall)


print("\nChoose Your Self","Press 1 for OWNER","Press 2 for Park","Press 3 to unpark","Press 4 for Revenue details\n")
print("1.OWNER","2.Want to Park","3.Unpark","4.Revenue Details",sep="\n")
x=int(input())
cur.execute(s13)
list_of_mall=cur.fetchall()
list_of_mall=list(list_of_mall)
list_of_mall=[item for t in list_of_mall for item in t]
#print(list_of_mall)
if x==1:
    name=input("enter name of mall")
    if name in list_of_mall:
        print("\nYOUR MALL IS ALREADY REGISTERED|\n")
        exit()
    print(OWNER(name))
    print("\n")
elif x==2:
    mall_name=input("enter Mall name")
    if mall_name not in list_of_mall:
        print("\nTHIS MALL IS NOT REGISTERED IN OUR LIST !!!\n")
        exit()
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
                current_time = datetime.datetime.now()
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
                current_time = datetime.datetime.now()    
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
        print("\n")
        print("YOUR VEHICLE IS PARKED SUCCESSFULLY|")
        print("\n")
    else:
        print("SORRY!WE ARE OUT OF SPACE RIGHTNOW")
elif x==3:
    PARK.unpark()
    print("\nYOUR VEHICLE IS SUCCESSFULLY UNPARKED|||\n")
    print("\nTHANK YOU FOR THE VISIT|||\n")
elif x==4:
    PARK.revenue_detail()
else:
    print("ENTER CORRECTLY!")

