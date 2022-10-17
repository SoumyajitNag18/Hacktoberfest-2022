from random import randint


# all variables
user_run_counter = 0
ai_run_counter = 0



def number_generator(starting_int , stopint_int):
    return randint(starting_int , stopint_int)


# batting of both parties

def user_batting():
    print("you are batting")
    user_run_counter = 0
    wicket_flag = False
    while not wicket_flag:
        u_val = int(input("Enter a number between 1-6 : "))
        ai_val = number_generator(1,6)
        if(u_val != ai_val):
            user_run_counter = user_run_counter + u_val
            print(f"You scored {u_val} in this ball ..! baller choice was {ai_val}")
        else:
            print(f"it's a wicket  , ai's prediction was right {ai_val}")
            wicket_flag = True
    wicket_flag = False
    return user_run_counter



def ai_batting():
    print("you are fielding")
    ai_run_counter = 0
    wicket_flag = False
    while not wicket_flag:
        ai_val = number_generator(1,6)
        u_val = int(input("Enter a number between 1-6 : "))
        if(u_val != ai_val):
            ai_run_counter = ai_run_counter + ai_val
            print(f"ai scored {ai_val} in this ball ..! baller choice was {u_val}")
        else:
            print(f"it's a wicket  , user's prediction was right {ai_val}")
            wicket_flag = True
    wicket_flag = False
    return ai_run_counter






# tossing phase

if __name__ == "__main__":

    user_choice = int(input("chose 1 for head or 0 for tail : "))

    if(user_choice == number_generator(0,1)):
        print("You won the toss please chosse between bat and fielding. ")
        print("Type (b) for batting and (f) for fielding. ")

        user_choice = input("> ")

        if user_choice == 'b':
            
            user_run_counter = user_batting()
            print(f"You scored total {user_run_counter}")
            ai_run_counter = ai_batting()
            print(f"ai scored total {ai_run_counter}")
            if user_run_counter > ai_run_counter :
                print(f"you won by {user_run_counter - ai_run_counter} runs")
            else:
                print(f"you lost by {user_run_counter - ai_run_counter} runs")
            
        else:
            ai_run_counter = ai_batting()
            print(f"ai scored total {ai_run_counter}")
            user_run_counter = user_batting()
            print(f"You scored total {user_run_counter}")
            if user_run_counter > ai_run_counter :
                print(f"you won by {user_run_counter - ai_run_counter} runs")
            else:
                print(f"you lost by {user_run_counter - ai_run_counter} runs")


    else:
        print("You lost the toss , ")
        if(number_generator(0,1) == 0):
            print("ai chosse to bat first")
            ai_run_counter = ai_batting()
            print(f"ai scored total {ai_run_counter}")
            user_run_counter = user_batting()
            print(f"You scored total {user_run_counter}")
            if user_run_counter > ai_run_counter :
                print(f"you won by {user_run_counter - ai_run_counter} runs")
            else:
                print(f"you lost by {user_run_counter - ai_run_counter} runs")
        else:
            print("ai chosse to field first")
            user_run_counter = user_batting()
            print(f"You scored total {user_run_counter}")
            ai_run_counter = ai_batting()
            print(f"ai scored total {ai_run_counter}")
            if user_run_counter > ai_run_counter :
                print(f"you won by {user_run_counter - ai_run_counter} runs")
            else:
                print(f"you lost by {user_run_counter - ai_run_counter} runs")







    