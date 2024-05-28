def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def mul(x,y):
    return(x*y)

def div(x,y):
    if(y==0):
        return("Error")
    return(x/y)

def main():
    while True:
        print("\nSelect Operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        while True:
            ch=int(input("Enter your choice : "))
            if ch in (1,2,3,4):
                num1=int(input("Enter 1st number : "))
                num2=int(input("Enter 2nd number : "))
                if ch==1:
                    print(num1,"+",num2,"=",add(num1,num2))
                elif ch==2:
                    print(num1,"-",num2,"=",sub(num1,num2))
                elif ch==3:
                    print(num1,"x",num2,"=",mul(num1,num2))
                elif ch==4:
                    if div(num1,num2)=="Error":
                        print("Zero Division Error. Cannot divide with 0")
                    else:
                        print(num1,"/",num2,"=",div(num1,num2))
                break
            else:
                print("Invalid choice. Choose again")
        choice=input("\nDo you want to use calculator again?(yes/no)").lower()
        if choice=="no":
            print("Closing...")
            break

if __name__=="__main__":
    main()
