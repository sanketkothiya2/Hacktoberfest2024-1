import json
from datetime import datetime

# Function to load data from the file
def load_data():
    try:
        with open('habits.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save data to the file
def save_data(habits):
    with open('habits.json', 'w') as file:
        json.dump(habits, file, indent=4)

# Function to add a new habit
def add_habit(habits):
    habit_name = input("Enter the name of the new habit: ")
    habits[habit_name] = {
        'streak': 0,
        'last_done': None
    }
    print(f'Habit "{habit_name}" added.')

# Function to mark a habit as done
def mark_habit_done(habits):
    habit_name = input("Enter the name of the habit: ")
    if habit_name in habits:
        today = datetime.now().strftime('%Y-%m-%d')
        if habits[habit_name]['last_done'] == today:
            print(f'You have already completed "{habit_name}" today.')
        else:
            habits[habit_name]['streak'] += 1
            habits[habit_name]['last_done'] = today
            print(f'Great! "{habit_name}" marked as done for today.')
    else:
        print(f'Habit "{habit_name}" does not exist.')

# Function to display the habit status
def display_habits(habits):
    if not habits:
        print("No habits tracked yet.")
    else:
        print("\nHabit Tracker:")
        for habit, data in habits.items():
            print(f'{habit} - Streak: {data["streak"]} days')

# Main program
def main():
    habits = load_data()
    
    while True:
        print("\nHabit Tracker Menu")
        print("1. Add a new habit")
        print("2. Mark a habit as done")
        print("3. View habit status")
        print("4. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            mark_habit_done(habits)
        elif choice == '3':
            display_habits(habits)
        elif choice == '4':
            save_data(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
