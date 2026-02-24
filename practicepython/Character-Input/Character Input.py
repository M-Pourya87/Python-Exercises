from datetime import date

def calculate_year(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age >= 100:
        return None
    return date.today().year + (100 - age)

def show_result(times, name, year):
    if year is None:
        print(f"Hi {name}, you are already 100 years old or more!")
    else:
        for _ in range(times):
            print(f"Hi {name}, you will turn 100 years old in the year {year}.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Number cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

name = input("Please enter your name: ")
age = get_positive_int("Please enter your age: ")
ask = get_positive_int("How many times do you want to see the result? ")

show_result(ask, name, calculate_year(age))
