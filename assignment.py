print("Welcome to the activity planner!")

hw_min = int(input("How many minutes will you spend on homework? "))

if hw_min > 60:
    print("That is a long homework session.")
    plan = "Start homework now"
else:
    print("That is a short homework session")
    plan = "Finish homework quickly"

ft = input("Will you have free time? ")

if ft.lower() == "yes":
    print("Reminder: pick a hobby for your free time!")

print("=====DAILY PLAN SUMMARY=====")
print("Homework minutes:", hw_min)
print("Plan:", plan)
print("Free time:", ft)