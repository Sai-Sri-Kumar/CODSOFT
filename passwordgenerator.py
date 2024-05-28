import random
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','$','%','=',':','?','.','/','|','~','>','*','(',')','<']
lowAlphabets=['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capAlphabets=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def weakPass(length):
    password=''
    for i in range(length):
        char=random.choice(lowAlphabets)+random.choice(digits)
        password+=random.choice(char)
    return password

def medPass(length):
    password=''
    for i in range(length):
        char=random.choice(lowAlphabets)+random.choice(capAlphabets)+random.choice(digits)
        password+=random.choice(char)
    return password

def strongPass(length):
    password=''
    for i in range(length):
        char=random.choice(lowAlphabets)+random.choice(capAlphabets)+random.choice(digits)+random.choice(symbols)
        password+=random.choice(char)
    return password

def main():
    length=int(input("Enter length of the password : "))
    while True:
        print("\nChoose strength of your password")
        print("--------------------------------")
        print("1. Weak")
        print("2. Medium")
        print("3. Strong")
        ch=int(input("Enter your choice : "))
        if ch==1:
            password=weakPass(length)
            break
        elif ch==2:
            password=medPass(length)
            break
        elif ch==3:
            password=strongPass(length)
            break
        else:
            print("Invalid choice. Choose again")
    print("\nyour password is : ",password)

if __name__=='__main__':
    main()
