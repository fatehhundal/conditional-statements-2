print("Welcome to the outfit picker!")

temperature = int(input("What is today's temperature (ºC)? "))

if temperature < 20:
    upper_clothing = "jacket"
    print("It is cold today.", end=" ")
    print("Wear a " + upper_clothing + ".")
else:
    upper_clothing = "t-shirt"
    print("It is warm today.", end=" ")
    print("Wear a " + upper_clothing + ".")

rain = input("Is it raining today? ")

if rain.lower() == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("What is the wind speed (km/h)? "))

if wind_speed > 30:
    windy = "yes"
    print("It is windy today.", end=" ")
    print("Wear a windbreaker over your", upper_clothing)
else:
    windy = "no"
    print("It is calm today.", end=" ")
    print("You don't need a windbreaker over your", upper_clothing)

puddles = input("Are there puddles on the ground? ")

if puddles.lower() == "yes":
    shoes = "boots"
    print("The ground is wet.", end=" ")
    print("Put on a pair of", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.", end=" ")
    print("Put on a pair of", shoes)

print("\nWeather check complete!")

print("\n======WEATHER OUTFIT PICKER======")
print("Temperature:", temperature)
print("Upper Clothing:", upper_clothing)
print("Raining:", rain)
print("Windy:", windy)
print("Shoes:", shoes)
print("=================================")