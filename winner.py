def winner(cc, uc) :
    if uc == cc :
        print("->You chose :", uc)
        print("->Computer chose :", cc)
        print("HENCE Draw")
    elif (uc == "Stone" and cc == "Scissor") or (uc == "Scissor" and cc == "Paper") or (uc == "Paper" and cc == "Stone") :
        print("->You chose :", uc)
        print("->Computer chose :", cc)
        print("You Win")
    else :
        print("->You chose :", uc)
        print("->Computer chose :", cc)
        print("You Lost")