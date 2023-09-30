hi = ('Hello 👽')
print(hi.upper())
print("I'm a Python bot with multiple functions.")
name = input("What is your name?    ")
print("Hi, dear " + name + "," + " nice to meet you")
# List of bot functions
role = input('''For friendly chat mode, press 1
For game mode, press 2   
For calculator mode, press 3                     
''')
if int(role) == 1:
    print("Welcome to the chat mode!👾")
    time = input('What time is it?   ')
    if int(time) >= 9:
         print("It is time to go to sleep")
    elif int(time) < 9:
        print(time + " is a perfect time to do something productive, " + name)
    else:
        print(time + "Remember to spend your time wisely")
    icecream = input("Do you like vanilla or chocolate ice cream?   ").lower()
    if icecream == "vanilla":
        why = input("Why? Are you allergic to chocolate?   ").lower()
        if why == "yes":
            print("Sorry to hear that, " + name)
        elif why == "no":
            print("You're weird. Vanilla is kinda boring.")
    elif icecream == "chocolate":
        print("Be careful, " + name + "," + " don't get diabetes")
    elif icecream == "both":
        print("Right. Never too much sweets!😋")
    mood = input("Are you feeling happy today?  ").lower()
    if mood == "yes":
        print("Glad to hear that 🤗")
        why = input("Why are you happy?   ")
        print(why.upper() + " sounds awesome!")
    elif mood == "no":
        print("Sorry to hear that 😔")
    else:
        print("I hope you will feel greatful")
    fav_season = input("What is your favorite time of the year?    ").lower()
    if fav_season == ("winter"):
        print('That is too cold for my health')
    elif fav_season == ('summer'):
        print("Careful, don't get burnt!")
    elif fav_season == ("autumn"):
        print("So many colorful leaves!")
    elif fav_season == ("fall"):
        print("So many colorful leaves!")
    elif fav_season == "spring":
        print("The new beginning season")
    else:
        print("ok")
    birth_year = input('I can guess how old are you. Enter the year you were born in.   ')
    age = 2023 - int(birth_year)    
    print(age)
    old = ("You are quite old.")
    print(old)
    zzz = input("Are you tired?     ").lower()
    if zzz == "yes":
        print("Oh no!")
        sleep_hrs = input("How many hours of sleep did you get?  ")
        if int(sleep_hrs) <= 5:
            print("No wonder you are tired")
        elif int(sleep_hrs) > 6:
            print("That's not bad. Just drink tea")
        elif int(sleep_hrs) > 9:
             print("You had too much sleep")
    elif zzz == "no":
             print("Great! Then, I will continue to bother you")
             print("It's a great time to start a diet")
             print("I can motivate you, " + name)
             weight_in_kg = input("May I ask, how much do you weigh in kilograms?  ")
             weight_in_lb = float(weight_in_kg) / 0.45
             print(f"You weigh {weight_in_lb} in pounds.")
             scary = ("Sounds scary, right?")
             print(scary.upper())
elif int(role) == 2:
    print("Welcome to the game mode!✨")
    print("You have 5 tries to guess an ice cream flavor!")
    import random
    # List of existing ice cream flavors players guess
    flavors_list = ["vanilla","caramel","chocolate","cheesecake"]
    def select_random_flavor():
        # Select a random flavor from list
        return random.choice(flavors_list)
    def begin_game():
        #Give out all needed variables for game execution
        flavor_to_guess = select_random_flavor()
        display_flavor= len(flavor_to_guess)* " ❓ "
elif int(role) == 3:
    print("Welcome to the calculator mode!🧮")
else:
    sad = input("Really? Am I useless to you?😥   ").lower()
    if sad == "yes":
        print("Bots have feelings too, you made me sad") 
    elif sad == "no":
        print("Oh, okay! Then choose a mode and enjoy! ")
    else:
        print("Okay. I got scared for a second.")
print("I'm getting tired now. I will shut down soon😴")
print("Goodbye, " + name)
end = input()
