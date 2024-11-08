"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Král
email: petr.kral36@seznam.cz
"""
import random
import time

def welcome_message():
    print("Vítejte ve hře Bulls & Cows!")
    print("Hádejte 4místné číslo, kde každá číslice je unikátní a první číslice není 0.")

def generate_secret_number():
    digits = list("123456789")  # první číslo nemůže být 0
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    remaining_digits = list("0123456789")
    for d in first_digit:
        remaining_digits.remove(d)
    return first_digit + "".join(random.sample(remaining_digits, 3))

def is_valid_guess(guess):
    if len(guess) != 4:
        print("Tip musí mít přesně 4 číslice.")
        return False
    if not guess.isdigit():
        print("Tip musí obsahovat pouze čísla.")
        return False
    if guess[0] == '0':
        print("Číslo nesmí začínat nulou.")
        return False
    if len(set(guess)) != 4:
        print("Číslice musí být unikátní.")
        return False
    return True

def evaluate_guess(secret, guess):
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for i in range(4) if guess[i] in secret and guess[i] != secret[i])
    return bulls, cows

def print_bulls_and_cows(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")

def play_game():
    secret_number = generate_secret_number()
    attempts = 0
    start_time = time.time()
    
    while True:
        guess = input("Zadejte svůj tip: ")
        if not is_valid_guess(guess):
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print_bulls_and_cows(bulls, cows)
        
        if bulls == 4:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Gratulujeme! Uhodli jste tajné číslo {secret_number} po {attempts} pokusech a za {elapsed_time:.2f} sekund.")
            return attempts, elapsed_time

def main():
    welcome_message()
    games_played = 0
    total_attempts = 0
    
    while True:
        attempts, elapsed_time = play_game()
        games_played += 1
        total_attempts += attempts
        
        print("\nChcete hrát znovu? (ano/ne)")
        again = input().lower()
        if again != "ano":
            break
    
    print(f"Odehráli jste {games_played} her s průměrem {total_attempts / games_played:.2f} pokusů na hru.")

if __name__ == "__main__":
    main()