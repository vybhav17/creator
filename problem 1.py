x = int(input("enter a number"))

if x>0 :
    if x%2==0:
        print("positive and even")
    else:
        print("positive and odd")
elif x<0:
    if x%2==0:
        print("negative and even")
    else:
        print("negative and odd")
else:
    print("zero")
