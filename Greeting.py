import datetime

# This is a class. Classes are blueprints for creating objects.
class Greeter:
    # This is defining an attribute, using arguments.
    #  Attributes are variables with values that belong to an object.
    # Pushing greeting argument's value into init method using self.
    # Self is a reference to the object itself.
    # Setting self.greeting variable/attribute to our greeting's argument to be used later.
    # Simply creathing methods to this class does NOT automativaclly call them.
    # We have to call them manually.
    def __init__(self, greeting):
        self.greeting = greeting
      

    # This is a method. Methods are functions that belong to an object.
    def print_greeting(self, current_time):
        # This is a function call with an argument.
        print(self.greeting, current_time)

name = input("What is your name? ")

# This is an object instantiation. It creates an instance of the class.
greeter_morning = Greeter(f"Good Morning, {name}!")
greeter_evening = Greeter(f"Good Evening, {name}!")
greeter_farewell = Greeter(f"Goodbye, {name}!")

# Determine the current time of day
current_time = datetime.datetime.now()
current_hour = current_time.hour

if 5 <= current_hour < 12:
    greeter_morning.print_greeting(f"it is {current_time.strftime('%D')}!")
elif 12 <= current_hour < 18:
    greeter_evening.print_greeting(f"it is {current_time.strftime('%D:%M:%Y:%H:%M:')}!")
else:
    greeter_farewell.print_greeting(f"it is {current_time.strftime('%M:%D:%Y:%H:%M:')}!")
