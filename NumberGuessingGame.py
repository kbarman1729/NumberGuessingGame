import random
l_bound = int(input("Enter lower bound: "))
u_bound = int(input("Enter upper bound: "))

number = random.randint(l_bound, u_bound)

print("      You have 5 chances to guess the number!")

def checking(number, u_bound, l_bound):
    one_fourth = int(u_bound/4)
    two_fourth = int(u_bound*(2/4))
    three_fourth = int(u_bound*(3/4))
    for i in range(1,6):
        guessed_num = int(input("Guess a number: "))
        if (guessed_num == number):
            print(f"Congratulation you did in {i} try!!")
            break
        if(guessed_num < number):
            if (abs(number - guessed_num) < one_fourth):
                print("Your guess is too near to the number!")
            elif (one_fourth <=abs(number - guessed_num) < two_fourth):
                print("Your guess is near to the number!")
            elif(abs(number - guessed_num) >= two_fourth ):
                print("Your guessed too small!")
        if(guessed_num > number):
            if (abs(number - guessed_num) < one_fourth):
                print("Your guess is too near to the number!")
            elif (one_fourth <=abs(number - guessed_num) < two_fourth):
                print("Your guess is near to the number!")
            elif(abs(number - guessed_num) >= two_fourth ):
                print("Your guessed too high!")
        if(i == 5):
            print("You lost the game!!")
    
checking(number, u_bound, l_bound)       
    
    
