

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter: ")
    letter = letter.upper()
    vowels = ["A", "E", "I", "O", "U"] 
    if letter.isalpha() != True:
        print("please enter a valid letter")
    elif letter in vowels:
        print("the letter " + letter + " is a vowel")
    else: 
        print("the letter " + letter + " is a constant")



# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input("Please enter your age: "))
    if age < 0:
        print("Enter a valid age idiot")
    elif age < 18:
        print('Too young to vote, loser!')
    else:
        print('You are old enough to vote, whoop-dee-fucking-doo')

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input("Input a dog's age: "))
    if dog_age <= 2:
        pup_age = dog_age * 10
        print(f"the dog's age in dog years is {pup_age}")
    else:
        total_age = 20 + (dog_age - 2) * 7
        print(f"in dog years the dog is {total_age} year's old, and he's a very good boy")


# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():

    temp_response = input("Is it cold outside? (yes/no): ").lower()

    rain_response = input("Is it raining outside? (yes/no): ").lower()

    if temp_response == "yes" and rain_response == "yes":
        print("Wear a waterproof coat.")
    elif temp_response == "yes" and rain_response == "no":
        print("Wear a warm coat.")
    elif temp_response == "no" and rain_response == "yes":
        print("Carry an umbrella.")
    elif temp_response == "no" and rain_response == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")


# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter 12-21, 1, 2, 3-19
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.


def determine_season():

    month = input("Please enter the month in it's abbreviated form (first 3 letters, i.e. January is jan):")
    day = input("Please enter the day of the month:")

    month = month.upper()
    day = int(day)

    if (month in ('JAN', 'FEB')):
        season = 'winter'
    elif (month == 'DEC' and day >= 21) or (month == 'MAR' and day <= 19):
        season = 'winter'
    elif (month in ('APR', 'MAY')):
        season = 'spring'
    elif (month == 'MAR' and day >= 20) or (month == 'JUN' and day <= 20):
        season = 'spring'
    elif (month in ('JUL', 'AUG')):
        season = 'summer'   
    elif (month == 'JUN' and day >= 21) or (month == 'SEP' and day <= 21):
        season = 'summer'
    elif (month in ('OCT', 'NOV')):
        season = 'fall'
    elif (month == 'SEP' and day >= 22) or (month == 'DEC' and day <= 20):
        season = 'fall'
    else:
        season = 'unknown season'
        
    print(f'{month} {day} is in {season}')

determine_season()

