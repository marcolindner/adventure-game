from game_utils import solve_riddle, end_game

def greeting():
    """Greets the player and explains the game rules."""
    print("Welcome to 'The Lost Treasure Hunt'!")
    print("Your goal is to find the lost treasure.")
    print("Navigate through the rooms and solve the riddles to proceed.\n")

def enter_room(room):
    """Describes the current room and available actions."""
    print(f"You enter {room['name']}.")
    print(room['description'])
    solved = False
    while not solved:
        solved = solve_riddle(room['riddle'])

def game():
    """Controls the flow of the game."""
    greeting()
    rooms = [
        {
            'name': 'the entrance hall',
            'description': 'A dark room with old paintings on the walls.',
            'riddle': {
                'question': 'I am not alive, but I grow. I have no lungs, but I need air. What am I?',
                'answer': 'fire'
            }
        },
        {
            'name': 'the library',
            'description': 'Shelves full of dusty books surround you.',
            'riddle': {
                'question': 'What words become shorter when you add letters to them?',
                'answer': 'short'
            }
        },
        {
            'name': 'the treasure chamber',
            'description': 'A shining treasure lies before you.',
            'riddle': {
                'question': 'What breaks when you speak it?',
                'answer': 'silence'
            }
        }
    ]

    current_room = 0
    while current_room < len(rooms):
        room = rooms[current_room]
        enter_room(room)
        if current_room < len(rooms) - 1:
            user_input = input("Do you want to go to the next room? (yes/no): ")
            if user_input.strip().lower() != 'yes':
                end_game()
        current_room += 1

    print("\nCongratulations! You have found the lost treasure!")
    end_game()

if __name__ == "__main__":
    game()
