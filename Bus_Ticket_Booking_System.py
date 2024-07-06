class Seat:
    def __init__(self,stype,price,place,id):
        self.__stype=stype
        self.__price=price
        self.__place=place
        self.id=id
    def getstype(self):
        return self.__stype
    def getprice(self):
        return self.__price
    def getplace(self):
        return self.__place
K1_seat=[ Seat("semi_sleeper",1500,"corner seat","SSC"),
       Seat("semi_sleeper",1000,"window seat","SSW"),
       Seat("sleeper",1200,"corner seat","SC"),
       Seat("sleeper",1250,"window seat","SW"),
       Seat("seater",1000,"corner seat","SEC"),
       Seat("seater",1050,"window seat","SEW")]
S1_seat=[ Seat("semi_sleeper",2500,"corner seat","SSC"),
       Seat("semi_sleeper",2000,"window seat","SSW"),
       Seat("sleeper",2200,"corner seat","SC"),
       Seat("sleeper",2250,"window seat","SW"),
       Seat("seater",2000,"corner seat","SEC"),
       Seat("seater",2050,"window seat","SEW")]

class Bus:
    def __init__(self,id,name):
        self.id=id
        self.__name=name
        self.__seat=[]
    def setter(self,stype,price,place,seat_id):
        self.__seat.append(Seat(stype,price,place,seat_id))
    def getname(self):
        return self.__name
    def getseat(self):
        return self.__seat
bus=[Bus("K1","Komban"),Bus("S1","SRM")]
l={"K1":K1_seat,"S1":S1_seat}
for i in bus:
    for j in l.keys():
        if i.id == j:
            for k in l[j]:
                i.setter(k.getstype(),k.getprice(),k.getplace(),k.id)

class Cart:
    def __init__(self,bus_id,seat_id,price):
        self.__bus_id=bus_id
        self.__seat_id=seat_id
        self.__price=price
    def getBus_id(self):
        return self.__bus_id
    def getSeat_id(self):
        return self.__seat_id
    def getPrice(self):
        return self.__price
cart=[]

class Booked:
    def __init__(self,bus_id,seat_id):
        self.bus_id=bus_id
        self.seat_id=seat_id
    @classmethod
    def calculation(self):
        total=0
        for i in cart:
            total=total+i.getPrice()-(i.getPrice()*Discount.discountrate(i.getBus_id(),i.getSeat_id()))
        return total
            
booked=[]
class Discount:
    def __init__(self,bus_id,seat_id,discount_rate):
        self.__bus_id=bus_id
        self.__seat_id=seat_id
        self.__discount_rate=discount_rate
    @classmethod
    def discountrate(self,bus_id,seat_id):
        for i in discount:
            if i.__bus_id == bus_id and i.__seat_id == seat_id:
                return i.__discount_rate
        
        return 0

discount=[Discount("K1","SSW",0.05),Discount("S1","SW",0.10),Discount("S1","SEC",0.15)]

def userChoiceIsToViewTheSeats():
    return ch==1
def userChoiceIsToBookTheSeats():
    return ch==2
def userChoiceIsToViewBookedSeats():
    return ch==3
def userChoiceIsToQuit():
    return ch==4
while True:
    print("*********WELCOME TO RED BUS**********")
    print("1.To view the seats\n2.To Book the seat\n3.To view the Booked Seats\n4.Exit")
    try:
        ch=int(input("Enter your choice:"))
        if userChoiceIsToViewTheSeats():
            print("******DISPLAYING THE SEATS********")
            for i in bus:
                for j in i.getseat():
                    print(f"BUS:{i.getname()} ||Bus_ID:{i.id} || SEAT_ID: {j.id} || SEAT_TYPE:{j.getstype()} || SEAT_PRICE: {j.getprice()} || SEAT_PLACE:{j.getplace()} ")
            print("-------------------------------------")
        elif userChoiceIsToBookTheSeats():
            for x in range(int(input("Enter How many Seats you want to book:"))):
                buss=input("Enter the bus_id:")
                seat=input("Enter the Seat id :")
                c=0
                for i in booked:
                    if buss==i.bus_id and seat==i.seat_id:
                        print("*******The Seat is already book**********")
                        c=c+1
                if c==0:
                    for i in range(len(bus)):
                        if  buss==bus[i].id:
                            c=0
                            for j in bus[i].getseat():
                                c=c+1
                                if seat==j.id:
                                    cart.append(Cart(bus[i].id,j.id,j.getprice()))
                                    print("*******BOOKING ADDED TO CART***********")
                                    break
                                elif c==len(bus[i].getseat()):
                                    print("**********Invalid Seat ID*********")
                            break
                        elif i==len(bus)-1:
                            print("**********Invalid BUS ID*********")
            if input("If you lile to conform Bookings(Y/N):") == "Y":
                for j in cart:
                    booked.append(Booked(j.getBus_id(),j.getSeat_id()))
                print("The Booked Seats are:")
                for i in cart:
                    print(f"Bus_ID:{i.getBus_id()} || Seat_ID:{i.getSeat_id()}")
                print(f"The total amount to pay:{Booked.calculation()}")
                print("**********BOOKING CONFORMED**************")
                cart=[]
            else:
                print("**********BOOKING CANCELLED**************")
                cart=[]
        elif userChoiceIsToViewBookedSeats():
            print("**********BOOKRD SEATS************")
            if len(booked)==0:
                print(" STILL  NO SEATS IS BOOKED ")
            else:
                for i in booked:
                    print(f"bus_id:{i.bus_id} || SEAT_ID:{i.seat_id}")
                print("*****************************")
        elif userChoiceIsToQuit():
            break
        else:
            print("Enter the valid option.")
    except ValueError:
        print("Enter option only in integer")
print("***************THANK YOU VISIT AGAIN***********")
