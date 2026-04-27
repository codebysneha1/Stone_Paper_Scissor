def user_choice() :
    print("\nSelect your Choice : ")
    print("1. Stone\n2. Paper\n3. Scissor")
    
    user_input = input('ENTER YOUR CHOICE : ')
    if not user_input.isdigit():
        print("ENTER VALID INPUT !!")
        return None
    
    user_input = int(user_input)
    if user_input == 1 :        return "Stone"
    elif user_input == 2 :      return "Paper"
    elif user_input == 3 :      return "Scissor"
    else :
        print("ENTER VALID INPUT !!")
        return None