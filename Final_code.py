import mysql.connector           #to create cursor object
import time                      #To just gave a sleep 
import uuid                      #for unique id in Park class
import datetime                  #to store the current time in park class table
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
s12="insert into revenue(U_id,Time,vehicle_number,cost,mallname,exit_time,month,date,year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
s13="SELECT MALLNAME FROM OWNER_DETAIL"
s14="select vehicle_number from park"
s15="select sum(cost) from revenue where mallname=%s group by mallname"
s16="select mallname from revenue"
s17="select vehicle_number from park"
s18="select sum(cost) from revenue where date(exit_time)=curdate() and mallname=%s"
s19="select sum(cost) from revenue where date(exit_time) > date_sub(curdate(), interval 7 day) and mallname=%s"
s20="select sum(cost) from revenue where date(exit_time) > date_sub(curdate(), interval 30 day) and mallname=%s"
s21="select sum(cost) from revenue where date(exit_time) > date_sub(curdate(), interval 90 day) and mallname=%s"
s22="select sum(cost) from revenue where date(exit_time) > date_sub(curdate(), interval 365 day) and mallname=%s"
s23="select sum(cost) from revenue where month=%s and mallname=%s"
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
        month_of_exit=exit_time.month
        date_of_exit=exit_time.day
        year_of_exit=exit_time.year
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
        b10=[id_uuid,time_of_stay1,number_vehicle,total_fair,name_of_mall,exit_time,month_of_exit,date_of_exit,year_of_exit]
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
        d={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
        mall_name_for_revenue=input('\nenter the name of mall\n')
        cur.execute(s16)
        list_of_mall_revenue=cur.fetchall()
        list_of_mall_revenue=list(list_of_mall_revenue)
        list_of_mall_revenue=[item for t in list_of_mall_revenue for item in t]
        if mall_name_for_revenue not in list_of_mall_revenue:
            print("\nYou Mall not present in revenue table||||\n")
            exit()
        ##  take a look here-----------------------*********
        print("PICK YOUR CHOISE")
        print("1.daily revenue","2.Weekly revenue","3.Montly Revenue","4.Quatarly revenue","5.yearly Revenue",sep="\n")
        l=int(input())
        b21=[mall_name_for_revenue]
        if l==1:
            cur.execute(s18,b21)
            daily_revenue=cur.fetchone()
            daily_revenue=sum(list(daily_revenue))
            print("Daily revenue")
            print(mall_name_for_revenue,":",daily_revenue)
        elif l==2:
            pass
            '''cur.execute(s19,b21)
            weekly_revenue=cur.fetchone()
            weekly_revenue=sum(list(weekly_revenue))
            print("Weekly revenue")
            print(mall_name_for_revenue,":",weekly_revenue)'''
        elif l==3:
            print("enter date range")
            print("from-->")
            start_range=input("dd/mm/yyyy")
            t1=start_range.find("/")
            t2=start_range.index("/",t1+1)
            #print(t1,t2)
            start_month=int(start_range[t1+1:t2])
            start_date=int(start_range[0:t1])
            print(start_date)
            #print(start_month)
            print("To--->")
            end_range=input("dd/mm/yyyy")
            t3=end_range.find("/")
            t4=end_range.index("/",t3+1)
            #print(t3,t4)
            end_month=int(end_range[t3+1:t4])
            end_date=int(end_range[0:t3])
            print(end_date)
            #print(end_range)
            for x in range(start_month,end_month+1):
                ba=[x,mall_name_for_revenue]
                cur.execute(s23,ba)
                month_revenue=cur.fetchone()
                if list(month_revenue)[0] is None:
                    print(d[x],":","0")
                else:
                    month_revenue=sum(list(month_revenue))
                    print(d[x],":",month_revenue)


            
            
            '''cur.execute(s20,b21)
            monthly_revenue=cur.fetchone()
            monthly_revenue=sum(list(monthly_revenue))
            print("Monthly revenue")
            print(mall_name_for_revenue,":",monthly_revenue)'''
        elif l==4:
            cur.execute(s21,b21)
            quatarly_revenue=cur.fetchone()
            quatarly_revenue=sum(list(quatarly_revenue))
            print("Quatarly revenue")
            print(mall_name_for_revenue,":",quatarly_revenue)
        elif l==5:
            cur.execute(s22,b21)
            yearly_revenue=cur.fetchone()
            yearly_revenue=sum(list(yearly_revenue))
            print("Yearly revenue")
            print(mall_name_for_revenue,":",yearly_revenue)
        else:
            print("CHOOSE CORRECTLY")
            exit()




        '''b21=[mall_name_for_revenue]
        cur.execute(s15,b21)
        revenue_of_mall=cur.fetchone()
        revenue_of_mall=sum(list(revenue_of_mall))
        print(mall_name_for_revenue,":",revenue_of_mall)'''


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
        # ------>write your code here<-------------------
        cur.execute(s17)
        list_of_vehicle_park=cur.fetchall()
        list_of_vehicle_park=list(list_of_vehicle_park)
        list_of_vehicle_park=[item for t in list_of_vehicle_park for item in t]
        if vechicle_number in list_of_vehicle_park:
            print("\nYOUR VEHICLE IS ALREADY PARKED!CHECK IT||||\n")
            exit()
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

