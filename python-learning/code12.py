def func1(n,m,p):
    if(n>m):
        if(n>p):
            print(f"The Greatest number is {n}")
    elif(m>p):
        print(f"The Greatest number is {m}")
    else:
        print(f"The Greatest number is {p}")

a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=int(input("Enter the 3rd number"))

func1(a,b,c)