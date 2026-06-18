import random 
def play_game():
    print("\n Welcome to the Number Guessing Game!")
    print("I have selected a game between 1 and 100.")
    print("Try to guess it\n")
    secret_number=random.randint(1,100)
    attempt=0
    while True:
        try:
            guess=int(input("Enter your guess number (1-100):"))
            if guess < 1 or guess > 100:
                print("please enter the number between 1 and 100.\n")
                continue
            attempt+=1
            if guess<secret_number:
                print("Too low! Try again.\n")
            elif guess>secret_number:
                print("Too High! Try Again.\n")
            else:
                print("\n Congratulations!")
                print(f"You guessed the number{secret_number}correctly.")
                print(f"Total attempts:{attempt}")
                break
        except ValueError:
            print("Invalid Input ! Please enter a valid nunber.\n")
            
        while True:
            play_game()
            choice=input("\nDo you want to play again ? (yes/no)").lower()
            if choice!="yes":
                print("\n Thank you for playing!")
                print("Have  a great day !")
                break                 
                         