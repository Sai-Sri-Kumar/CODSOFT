import random

def get_user_choice():
    while True:
        user_choice=input("\nEnter your choice :Rock or Paper or Scissors  ").lower()
        if(user_choice=="rock" or user_choice=="paper" or user_choice=="scissors") :
            return user_choice
        else:
            print("invalid choice choose between Rock,Paper,Scissors")

def get_comp_choice():
    return random.choice(['rock','paper','scissors'])

def winner(user_choice,comp_choice):
    if user_choice==comp_choice:
        return "tie"
    elif((user_choice=='paper' and comp_choice=='rock') or(user_choice=='scissors' and comp_choice=='paper') or (user_choice=='rock' and comp_choice=='scissors')):
        return "you win"
    else:
        return "computer wins"

def  display_results(user_choice,comp_choice,result):
    print("You chose : ",user_choice)
    print("Computer chose : ",comp_choice,"\n")
    print(result,"\n")

def main():
    your_score=0
    comp_score=0
    while True:
        user_choice=get_user_choice()
        comp_choice=get_comp_choice()
        result=winner(user_choice,comp_choice)
        display_results(user_choice,comp_choice,result)
        if(result=="you win"):
            your_score=your_score+1
        elif(result=="computer wins"):
            comp_score=comp_score+1
        print("your score : ",your_score," computer score : ",comp_score,"\n")
        ch=input("Do you want to play again? (yes/no)").lower()
        if(ch =="no"):
            if(your_score>comp_score):
                print("You Win!")
            elif(comp_score>your_score):
                print("Computer Wins!")
            else:
                print("It's a tie")
            print("Thank you for playing")
            break
if __name__=="__main__":
    main()
        
