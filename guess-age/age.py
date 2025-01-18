import random

print("Hello there, err...")
print("How uhh... how old are you?")

age = -1
guesses = list(range(1,31))
random.shuffle(guesses)

while True:
    if len(guesses) == 0:
        break;
    
    guess = guesses.pop(-1)
    
    test = input(f"are you {guess}? (y/n) ")

    if test == 'y':
        age = guess
        break;
    elif test == 'n':
        continue;
    else:
        guesses.append(guess)
        print("please just answer me y/n")

if age >= 18:
    print("thank god")
elif age >= 8:
    print("oh. I shouldn't be talking to you.")
elif age > 0:
    print("I don't believe you")
else:
    print("alright, I give up")
