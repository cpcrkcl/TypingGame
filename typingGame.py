import time 
import pandas as pd
import numpy as np

words = pd.read_csv('4000-most-common-english-words-csv.csv')

def display_menu():
    print("Choose number of words to type:")
    print("1. 10 words")
    print("2. 25 words")
    print("3. 50 words")
    print("4. 100 words")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            string_length = 10
            break
        elif choice == 2:
            string_length = 25
            break
        elif choice == 3:
            string_length = 50
            break
        elif choice == 4:
            string_length = 100
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")
typed_text = ""
for i in range(string_length):
    typed_text += np.random.choice(words.iloc[:, 0]) + " "

print(typed_text)
input("Press Enter when you're ready to start typing...")
start_time = time.time()
user_input = input("Type the text above: ")
end_time = time.time()

elapsed_time = end_time - start_time

word_count = len(user_input.split())
words_per_minute = (60/ elapsed_time) * word_count

correct_chars = sum(1 for a, b in zip(typed_text, user_input) if a == b)
total_chars = max(len(typed_text), len(user_input))
accuracy = (correct_chars / total_chars) * 100

print(f"Accuracy: {accuracy:.2f}%")

print(f"You typed at a speed of {words_per_minute} wpm")


