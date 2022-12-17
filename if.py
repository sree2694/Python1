review = 0

if review == None:
    print("We have a review.")
else:
    print("No review")

if review != None:
    print("We have a review.")

review = 4.6

if review >= 4:
    if review > 4.5:
        if review == 5:
            print("Perfect")
        else:
            print("Excelent")
    else:
        print("Great")
elif review <= 4 and review > 3:
    print("Good")
else:
    print("Not so great")