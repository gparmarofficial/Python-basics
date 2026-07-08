medical = input("Medical cause?(Y/N):").upper()
if medical =="Y":
    print("allowed")
else:
    attendance = int(input("Enter attendance % :"))
    if attendance > 75:
        print("allowed")
    else:
        print("not allowed")
        

#activity2
units = float(input("Enter units consumed:"))
if units < 50:
    rate = 2.60
    tax = 25
elif units >50 and units <100:
    rate = 3.25
    tax = 35
elif units > 100 and units <200:
    rate = 5.26
    tax = 45
else:
    rate = 8.45
    tax = 75

total_bill = (units * rate) + tax

print ("Total bill:",total_bill)

#activity3
type_choise = input("Enter 1 for Bike or 2 for car:")
if type_choise == "1":
    bike_choise = input("Enter 1 for scooter 2 for sports bike:")
    if bike_choise =="1":
        print("you chose a scooter!")
    else:
        print("you can chose a sports bike")
elif  type_choise == "2":
    car_choise = input ("Enter 1 for Sedan and 2 for the SUV")
    if car_choise == "1":
        print("u can choose a sedan")
    else:
        print("u chose an SUV")
        
else:
    print("Invalid choise")