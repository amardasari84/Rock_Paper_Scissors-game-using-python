print("Welcome to the Rock paper Scissors Game!")
abhinav=input("Abhinav:")
anjali=input("Anjali:")
if abhinav=="rock"and anjali=="scissors":
    print("abhinav wins")
elif abhinav=="scissors" and anjali=="rock":
    print("Anajali wins")
elif abhinav == "scissors" and anjali == "paper":
    print("Anajali wins")

elif abhinav=="paper" and anjali=="scissors":
    print("Abhinav wins")
elif abhinav=="paper" and anjali=="rock":
    print("abhinav wins")
elif abhinav=="rock" and anjali=="paper":
    print("Anjali wins")
else:
    print("Both are tied")