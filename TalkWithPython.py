hi = ('Hello 👽')
print(hi.upper())
print("I'm Python")
name = input("What is your name?    ")
print("Hi, dear " + name)
print("Nice to meet you")
time = input('What time is it?   ')
if int(time) >= 9:
    print("It is time to go to sleep")
elif int(time) < 9:
    print(time + " is a perfect time to do something productive, " + name)
else:
    print(time + "Remember to spend your time wisely")
course = input("What class are you taking?    ")
print(course + " is a very important class")
print("Knowing " + course + " can be helpful in life")
mood = input("Are you feeling happy today?  ")
if mood == "yes":
    print("Glad to hear that 🤗")
elif mood == "no":
    print("Sorry to hear that 😔")
else:
    print("I hope you will feel greatful")
fav_season = input("What is your favorite time of the year?    ")
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
zzz = input("Are you tired?     ")
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
    weight_in_kg = input("How much do you weigh in kilograms?  ")
    weight_in_lb = float(weight_in_kg) / 0.45
    print(f"You weigh {weight_in_lb} in pounds.")
    scary = ("Sounds scary, right?")
    print(scary.upper())
end = input()
