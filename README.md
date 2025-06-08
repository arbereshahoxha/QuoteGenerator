# QuoteGenerator

## A random quote generator based on the category chosen

This beginner-level Python project prompts the user to enter a valid name and then allows them to select a category from a predefined list. Once a category is chosen, the program retrieves and displays a randomly selected quote from a collection stored in a JSON file.

This assignment consolidates foundational Python concepts learned in beginner-level courses, including user input validation, data handling with JSON, function modularity, and randomization.

### Requirements: 
- Python 3.6+
- No external libraries required (uses built-in modules: json, random)


### How to run : 
- Clone or download the repository.
- Make sure quotes.json is in the same directory as main.py.
- Run the script:python main.py


### Compliance with Project Requirements
1. Modular Functions:
    The code is organized into multiple distinct functions, each responsible for a single task. These include:
    load_quotes() for loading the quotes data from a JSON file,
    get_categories() for extracting available quote categories,
    get_user_info() for obtaining and validating user input,
    get_random_quote() for selecting a random quote from a category,
    print_quote() for formatting and displaying the selected quote.

2. Use of Data Structures:
    The project utilizes Python data structures effectively. The quotes data is stored as a dictionary, with each key representing a category and the value being a list of quote dictionaries. This structure facilitates easy lookup and manipulation.

3. User Input and Validation:
    User input is solicited for the user's name and the category choice. Input validation ensures that the user’s name is not empty and that the selected category exists within the dataset. The program continues to prompt the user until valid input is received or the user chooses to exit.

4. Logical Control Structures:
    The program employs control flow mechanisms such as loops and conditional statements (while, if/else) to manage program execution, handle user input validation, and provide appropriate responses or prompts based on the user’s actions.

5. Automatic Content Generation:
    Upon valid category selection, the program automatically retrieves and displays a randomly chosen quote from the selected category using Python’s built-in random.choice() function, ensuring dynamic content delivery.

