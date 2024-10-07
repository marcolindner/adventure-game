def solve_riddle(riddle):
    """Presents a riddle and checks the player's answer."""
    print("\n" + riddle['question'])
    answer = input("Your answer: ")
    if answer.strip().lower() == riddle['answer'].strip().lower():
        print("Correct! You can proceed.")
        return True
    else:
        print("Wrong! Try again.")
        return False

def end_game():
    """Says goodbye to the player and ends the game."""
    print("Thanks for playing! Goodbye.")
    exit()
