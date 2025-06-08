import json
import random

# function to load quotes
def load_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# function that will map lowercase inpput to the actual category names
def get_categories(quotes_data):
    return {key.lower(): key for key in quotes_data.keys()}


# function that gets a random quote from the category list
def get_random_quote(quotes_list):
    return random.choice(quotes_list)


# function that will print the quote
def print_quote(quote):
    print(f'\n"{quote["text"]}"\n- {quote["author"]}')

# function to get user name with validation
def get_user_info():
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name can't be empty. Please try again.")

# the main logic
user_name = get_user_info()
quotes_data = load_quotes("quotes.json")
category_dict = get_categories(quotes_data)

print(f'\nWelcome, {user_name}!')
print("Available categories:", ", ".join(category_dict.values()))

while True:
    user_input = input("\nChoose a category or type 'exit' to quit: ").strip().lower()

    if user_input == "exit":
        print(f"Goodbye {user_name}!")
        break

    if user_input in category_dict:
        selected_quote = get_random_quote(quotes_data[category_dict[user_input]])
        print_quote(selected_quote)
    else:
        print("Invalid category, please try another one.")

