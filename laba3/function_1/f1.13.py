import random
def guess(s):
    r = random.randint(1,20)
    print(f"\nWell, {s}, I am thinking of a number between 1 and 20.")
    b = False
    i = 0
    while b == False:
        i += 1
        n = int(input("Take a gues\n"))
        if r==n:
            print(f"\n Good job, {s},You guessed my number in {i} guesses!")
            b = True
        elif r > n:
            print("\n Your guess is too low.")
        else:
            print("\n Your guess is too high.")

guess(input("Hello! What is your name? \n"))
