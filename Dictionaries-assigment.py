# WORD COUNTER PROGRAM
sentence = input("Enter a sentence: ")
words = sentence.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word counts:")
for word, count in word_counts.items():
    print(word, ":", count)



# GRADE CALCULATOR PROGRAM
grading_scale = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

subjects = ["Math", "Science", "English", "History"]
scores = {}

for subject in subjects:
    score = float(input("Enter your score for {}: ".format(subject)))
    scores[subject] = score

total_grade_points = 0
total_credits = len(subjects)

for subject, score in scores.items():
    grade = ""
    for grade_range, grade_point in grading_scale.items():
        if score >= grade_point:
            grade = grade_range
            break
    print("{}: {}".format(subject, grade))
    total_grade_points += grading_scale[grade]

overall_grade = total_grade_points / total_credits
print("Overall Grade: {:.2f}".format(overall_grade))




#SHOPPING LIST MANAGER

shopping_list = {}

def add_item(item):
    if item in shopping_list:
        print("Item is already in the shopping list.")
    else:
        shopping_list[item] = False
        print("Item added to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print("Item removed from the shopping list.")
    else:
        print("Item is not in the shopping list.")

def check_off_item(item):
    if item in shopping_list:
        shopping_list[item] = True
        print("Item checked off.")
    else:
        print("Item is not in the shopping list.")

def display_shopping_list():
    print("Shopping List:")
    for item, checked in shopping_list.items():
        if checked:
            print("[X] " + item)
        else:
            print("[ ] " + item)

while True:
    print("What would you like to do?")
    print("1. Add item to the shopping list")
    print("2. Remove item from the shopping list")
    print("3. Check off item on the shopping list")
    print("4. Display the shopping list")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "3":
        item = input("Enter the item to check off: ")
        check_off_item(item)
    elif choice == "4":
        display_shopping_list()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")





#MOVIE RATING TRACKER

movie_ratings = {}

def rate_movie(movie, rating):
    if movie in movie_ratings:
        movie_ratings[movie].append(rating)
    else:
        movie_ratings[movie] = [rating]

def get_average_rating(movie):
    if movie in movie_ratings:
        ratings = movie_ratings[movie]
        average_rating = sum(ratings) / len(ratings)
        return average_rating
    else:
        return None

while True:
    print("What would you like to do?")
    print("1. Rate a movie")
    print("2. Get the average rating of a movie")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        movie = input("Enter the movie title: ")
        rating = float(input("Enter your rating (1-5): "))
        rate_movie(movie, rating)
        print("Thank you for rating the movie!")
    elif choice == "2":
        movie = input("Enter the movie title: ")
        average_rating = get_average_rating(movie)
        if average_rating is not None:
            print("The average rating for", movie, "is", average_rating)
        else:
            print("The movie", movie, "has not been rated yet.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")



#TEMPERATURE CONVERTER
        

conversion_factors = {'C to F': lambda c: c * 9/5 + 32,
                      'F to C': lambda f: (f - 32) * 5/9}

def convert_temperature(temp, conversion):
    return conversion(temp)

while True:
    print("\nOptions:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_temperature(celsius, conversion_factors['C to F'])
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_temperature(fahrenheit, conversion_factors['F to C'])
        print("Temperature in Celsius:", celsius)
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")



#PHONEBOOK ORGANIZER
        

contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print(f"Contact '{name}' with phone number '{phone_number}' has been added.")

def search_contact(name):
    if name in contacts:
        phone_number = contacts[name]
        print(f"The phone number for '{name}' is '{phone_number}'.")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(name, phone_number):
    if name in contacts:
        contacts[name] = phone_number
        print(f"Contact '{name}' has been updated with the new phone number '{phone_number}'.")
    else:
        print(f"Contact '{name}' not found.")



#RESTURANT MENU PARSER
        

menu = {}

def read_menu(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            item, price, category = line.strip().split(',')
            menu[item] = {'price': float(price), 'category': category}

def browse_menu(category=None):
    print("Menu:")
    for item, details in menu.items():
        if category is None or details['category'] == category:
            print(f"{item}: ${details['price']} ({details['category']})")

file_path = input("Enter path to menu file: ")
read_menu(file_path)

while True:
    print("\nOptions:")
    print("1. Browse menu")
    print("2. Search for item")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        category = input("Enter category to browse (leave blank to browse all): ")
        browse_menu(category)
    elif choice == 2:
        item = input("Enter item to search for: ")
        if item in menu:
            print(f"{item}: ${menu[item]['price']} ({menu[item]['category']})")
        else:
            print("Item not found in the menu.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")


#PASSWORD GUESSER
        
import random
import string

password_constraints = {'length': 8, 'uppercase': True, 'lowercase': True, 'numbers': True, 'symbols': False}

def generate_password(constraints):
    characters = ''
    if constraints['uppercase']:
        characters += string.ascii_uppercase
    if constraints['lowercase']:
        characters += string.ascii_lowercase
    if constraints['numbers']:
        characters += string.digits
    if constraints['symbols']:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(constraints['length']))

print("Generated password:", generate_password(password_constraints))


#SONG ORGANIZER
songs = {}

def add_song(title, artist, genre):
    songs[title] = {'artist': artist, 'genre': genre}
    print(f"Song '{title}' added successfully.")

def sort_songs(criteria):
    sorted_songs = sorted(songs.items(), key=lambda x: x[1][criteria])
    for title, details in sorted_songs:
        print(f"{title}: Artist - {details['artist']}, Genre - {details['genre']}")

while True:
    print("\nOptions:")
    print("1. Add song")
    print("2. Sort songs")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        genre = input("Enter genre: ")
        add_song(title, artist, genre)
    elif choice == 2:
        print("\nSort by:")
        print("1. Title")
        print("2. Artist")
        print("3. Genre")
        criteria = int(input("Enter your choice: "))
        if criteria == 1:
            sort_songs('title')
        elif criteria == 2:
            sort_songs('artist')
        elif criteria == 3:
            sort_songs('genre')
        else:
            print("Invalid choice.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")


#TRAVEL BUDGET TRACKER
expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def display_expenses():
    print("Travel Expenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")

while True:
    print("\nOptions:")
    print("1. Add an expense")
    print("2. Display expenses")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        add_expense(category, amount)
        print("Expense added successfully.")
    elif choice == '2':
        display_expenses()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")