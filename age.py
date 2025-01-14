import random

print("Hello there, err...")
print("How uhh... how old are you?")

age = -1
guess = 0
while True:
    guess = random.randint(1,30)
    test = input(f"are you {guess}? (y/n) ")

    if test == 'y':
        age = guess
        break;
    elif test == 'n':
        continue;
    else:
        print("please just answer me y/n")

if age >= 18:
    print("thank god")
else:
    print("oh. I shouldn't be talking to you.")
