def generate_profile(age):#статус
    if 0 <= age <= 12:
        return ("Child")
    elif 13 <= age <= 19:
        return ("Teenager")
    elif age >= 20:
        return ("Adult")

def age(year):#считает возраст
   return int(2025 - year)

user_name = input("Enter your full name: ")#имя
birth_year_str = input("Enter your birth year: ")#год
birth_year = int(birth_year_str)#перевод в инт
current_age = age(birth_year)
life_stage = generate_profile(current_age)

hobbies = []
while True:
   hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")
   if hobby_input.lower() == "stop":
        break
   else:
        hobbies.append(hobby_input)


user_profile ={
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies
}

print("---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")
if len(user_profile['hobbies']) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hob in user_profile['hobbies']:
        print(f"- {hob}")

