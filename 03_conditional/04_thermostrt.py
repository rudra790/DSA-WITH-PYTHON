device=input("enter device is active / inactive").lower()
temp=int(input("enter temprature"))
if device=="active":
    print("device is active")
    if temp>=35:
        print("high temprature!")
    else:
        print("temp normal")
else:
    print("device is active")