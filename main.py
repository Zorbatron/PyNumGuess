import random

def main():
    tries = 0
    initNum = random.randint(1, 100)
    print("Guess the number!")
    
    while True:
        while True:
            try:
                guessNum = int(input())
                break
            except ValueError:
                print("Please enter a number.")
    
        tries += 1

        if guessNum == initNum:
            print("You guessed correctly!")
            break
        elif guessNum > initNum:
            print("You were too high!")
        elif guessNum < initNum:
            print("You were too low!")

    print("It took you", tries, "guesses.")

if __name__ == "__main__":
    main()