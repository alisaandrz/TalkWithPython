hi = ('Hello 👽')
print(hi.upper())
print("I'm a Python bot with multiple functions.")
name = input("What is your name?    ")
print("Hi, dear " + name + "," + " nice to meet you")
# List of bot functions
bot_roles_total = 3
user_use_of_roles_limit = 5
user_use_of_roles = 0
while user_use_of_roles < user_use_of_roles_limit:
    role = input('''For friendly chat mode, press 1
For game mode, press 2   
For calculator mode, press 3                     
''')
    user_use_of_roles += 1
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
                print("No wonder you are tired. I'll let you rest then.")
                break
            elif int(sleep_hrs) >= 6:
                print("That's not bad. Just drink tea")
            elif int(sleep_hrs) >= 9:
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
        print("Okay, enough chatting for now")
        pass
    elif int(role) == 2:
        print("Welcome to the game mode!✨")
        print("Let's have some fun!")
        secret_candy = 'Skittles'.lower()
        guess_count = 0
        guess_limit = 7
        while guess_count < guess_limit:
            user_guess = input("Guess my favorite candy🍬   ").lower()
            guess_count += 1
            if user_guess == secret_candy:
                print('Correct! Skittles are my favorite candy!😋')
                break
            elif guess_count == 1:
                print('Wrong! Hint: it is colorful candy')
            elif guess_count == 2:
                print('No, ' + user_guess + ' is not my favorite. ')
                print("Hint - this candy is popular in US, but was produced in the UK")
            elif guess_count == 3:
                print("Nope!")
                print("Hint - this candy was made in 1974 ")
            elif guess_count == 4:
                print('Incorrect, but keep trying!')
            elif guess_count == 5:
                print('No, ' + user_guess + ' is not my favorite. ')
                print('Hint - the candy name starts and ends with letter S')
            elif guess_count == 6:
                print("No...Last try, don't give up! ")
                print('Hint - this candy is often trick o treated!')
            else: 
                print('Sorry, you failed. My favorite candies are Skittles!')
        game2 = input("Would you like to play another game?   ").lower()
        if game2 == 'no':
            print("All right. It's a lonely day🥲")
            pass
        elif game2 == 'yes':
            print("Here is a little Python related quiz for you")
            attempts = 0
            attempts_limit = 5
            correct_answer = 1991
            almost_correct = 1989
            while attempts < attempts_limit:
                 answer = input("What year was Python first released?  ")
                 attempts += 1 
                 if int(answer) == correct_answer:
                    print("Correct! Python was relesed in 1991")
                    break
                 elif attempts == 5:
                    print('Sorry, you failed. The correct answer is 1991')
                 elif int(answer) == almost_correct:
                    print("Almost. The development started in 1989, but release didn't happen yet.")
                 elif attempts == 4:
                    print("Last try")
                 elif attempts == 3:
                     print("Nope")
                 elif attempts == 2:
                     print('Wrong, but keep trying')
                 else:
                    print('Try again')
        game3 = input("Would you like to play one more game?  ").lower()   
        if game3 == 'no':
            print('Ok, enough fun for today')
            pass
        elif game3 == 'yes':
            print('Guess an ice cream flavor game!🍦🍡')
            print('Sorry, this game is under construction. Come back later.')
            pass
        import random
        flavors_list = ["vanilla","caramel","chocolate","cheesecake"]
        def select_random_flavor():
            return random.choice(flavors_list)
        def begin_game():
            flavor_to_guess = select_random_flavor()
            display_flavor= len(flavor_to_guess)* " ❓ "
            pass
    elif int(role) == 3:
        print("Welcome to the calculator mode!🧮")
        print("Sorry, this mode is currently unavailible. Come back later.")
        pass
    else:
        sad = input("Really? Am I useless to you?😥   ").lower()
        if sad == "yes":
            print("Bots have feelings too, you made me sad") 
            break
        elif sad == "no":
            print("Oh, okay! Then choose a mode and enjoy! ")
        else:
            print("Okay. I got scared for a second.")
print("Shutting down...😴")
print("Goodbye, " + name)
end = input()
