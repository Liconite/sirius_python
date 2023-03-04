import multiprocessing
import random
import time


def subscription_timer(subscription_time):
    time.sleep(subscription_time)
    print("Your subscription has expired.")
    exit()


def guess_the_number():
    print("Welcome to the guess the number game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess the secret number (between 1 and 100): "))
        attempts += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the secret number in {attempts} attempts.")
            break


if __name__ == '__main__':
    subscription_time = int(input("Enter subscription time (in seconds): "))

    subscription_process = multiprocessing.Process(target=subscription_timer, args=(subscription_time,))
    subscription_process.start()

    guess_the_number()

    subscription_process.join()
