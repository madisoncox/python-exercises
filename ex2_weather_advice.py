weather = raw_input("What is the weather? (cold, raining, etc.) ")

if weather == "Cold":
    print("Wear a sweater!")
elif weather == "Raining":
    print("Bring an umbrella!")
else:
    print("Dress normally :)")

weather = "Cold"
snowing = True

if weather == "Cold" and snowing == True:
    print("Wear a winter jacket")

weather = "Raining"
snowing = True

if weather == "Raining" or snowing == True:
    print("Bring a change of socks")

