import random
import datetime
import csv
ans='y'
Main=[['Name','GuestId','MobileNo','Email','RoomNo','CheckInDate','CheckOutDate','Membership','Bill']]
while ans=='y':
    Name=[]
    MobileNumber=[]
    Email=[]
    GuestId=[]
    RoomNo=[]
    CheckIn=[]
    CheckOut=[]
    Days=[]
    Membership=[]
    Bill=[]
    l1=random.sample(range(1,26), 25)
    l2=random.sample(range(26,51), 25)
    l3=random.sample(range(51,76), 25)
    l4=random.sample(range(76,101), 25)
    Applicant=[]
    a=input("Enter your name:")
    b=input("Enter your Phone No.")
    c=input("Enter your EmailId:")
    Name.append(a)
    MobileNumber.append(b)
    Email.append(c)
    d=input("Enter Check in Date in dd/mm/yyyy format:")
    e=input("Enter Check out Date in dd//mm/yyyy format:")
    CheckIn.append(d)
    CheckOut.append(e)
    L1=d.split('/')
    L2=e.split('/')
    InDate=datetime.date((int(L1[2])),(int(L1[1])),(int(L1[0])))
    OutDate=datetime.date((int(L2[2])),(int(L2[1])),(int(L2[0])))
    f=(OutDate-InDate).days
    Days.append(f)
    g=a[0:2]+b
    GuestId.append(g)
    print('''We have 4 types of Room:
1.Normal Non Ac, Price:-2000 Rs per day
2.Normal Ac, Price:-2500 Rs per day
3.Deluxe Ac, Price:-3500 Rs per day
4.King sized, Price:-5000 Rs per day''')
    print(''' Normal Non Ac includes
1.Two person Bedspace (Single room only) 
2.Telivison
3.Bathroom
4.One Almirah''')
    print(''' Normal Ac includes
1.Two person Bedspace (Single room only)
2.Telivison
3.Bathroom
4.One Almirah
5.Ac''')
    print(''' Deluxe Ac includes
1.Three person Bedspace (Single room only)
2.Telivison
3.Bathroom
4.One Almirah
5.Ac''')
    print(''' King sized includes
1.Four person Bedspace (Double rooms:-Two in one room and two in other room)
2.Telivison
3.Two Bathroom(One in both room)
4.Two Almirah(One in both room)
5.Two Ac(One in both room''')
    h=int(input("Enter your choice:"))
    if h==1:
        Membership.append('Silver')
        k=random.choice(l1)
        l1.remove(k)
        RoomNo.append(k)
        x=f*2000
        Bill.append(x)
        print('''Hurrah you have been assigned Silver Membership on the basis of your room choice
These are the previleges you will be getting:-
1.Free Breakfast Coupon for everyday of stay
2.Free Lunch Coupon for everyday of stay
3.Free Dinner Coupon for everyday of stay''')
    elif h==2:
        Membership.append('Silver')
        k=random.choice(l2)
        l2.remove(k)
        RoomNo.append(k)
        x=f*2500
        Bill.append(x)
        print('''Hurrah you have been assigned Silver Membership on the basis of your room choice
These are the previleges you will be getting:-
1.Free Breakfast Coupon for everyday of stay
2.Free Lunch Coupon for everyday of stay
3.Free Dinner Coupon for everyday of stay''')
    elif h==3:
        Membership.append('Gold')
        k=random.choice(l3)
        l3.remove(k)
        RoomNo.append(k)
        x=f*3500
        Bill.append(x)
        print('''Hurrah you have been assigned Gold Membership on the basis of your room choice
These are the previleges you will be getting:-
1.Free Breakfast Coupon for everyday of stay
2.Free Lunch Coupon for everyday of stay
3.Free Dinner Coupon for everyday of stay
4.Access to Swimming Pool
5.Access to Tennis Court''')
    elif h==4:
        Membership.append('Platinum')
        k=random.choice(l4)
        l4.remove(k)
        RoomNo.append(k)
        x=f*5000
        Bill.append(x)
        print('''Hurrah you have been assigned Platinum Membership on the basis of your room choice
These are the previleges you will be getting:-
1.Free Breakfast Coupon for everyday of stay
2.Free Lunch Coupon for everyday of stay
3.Free Dinner Coupon for everyday of stay
4.Access to Swimming Pool
5.Access to Tennis Court
6.Free massage Coupon(one time use)''')
    print('''Your details will be displayed in the format:-
            [Name,GuestId,MobileNo,Email,RoomNo,CheckInDate,CheckOutDate,Membership,Bill]''')
    Applicant=Applicant+Name+GuestId+MobileNumber+Email+RoomNo+CheckIn+CheckOut+Membership+Bill
    print(Applicant)
    Main.append(Applicant)
    ans=input("Do you want to add more data? y/n:")


    
with open('temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(Main)
