Weight = int(input("What is your weight? "))
which  = input("Type L for lbs or K for kg " )

if which.upper() == "L":
    new = Weight*.45
    print(f"Your weight in kg is {new}")
else:
    new = Weight/.45
    print(f"Your weight in pounds is {new}")