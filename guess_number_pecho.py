import random
number = random. randint(1, 100)
attempts = 0
while True:
    guess = int(input())
    if guess == number:
        print("correct")
        print(attempts)
    elif guess < number:
        print("higher")
        attempts += 1
    elif guess > number:
        print("lower")
        attempts += 1