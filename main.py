import computer
import user
import winner

def play_game() :
    while True :
        uc = user.user_choice()
        cc = computer.computer_choice()
        if uc is None:
            continue
        winner.winner(uc, cc)
        
        round_choice = input("\nWanna play one more round ? (yes/no)").lower()
        if round_choice != "yes" :
            break
play_game()