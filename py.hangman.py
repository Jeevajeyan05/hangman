Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... def choose_word():
...     word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm']
...     return random.choice(word_list)
... 
... def display_state(word, guessed_letters):
...     return ' '.join([letter if letter in guessed_letters else '_' for letter in word])
... 
... def hangman():
...     word = choose_word()
...     guessed_letters = set()
...     attempts_left = 6
... 
...     print("Welcome to Hangman!")
...     while attempts_left > 0:
...         print(f"\nWord: {display_state(word, guessed_letters)}")
...         guess = input("Guess a letter: ").lower()
... 
...         if len(guess) != 1 or not guess.isalpha():
...             print("⚠  Please enter a single alphabetic character.")
...             continue
...         if guess in guessed_letters:
...             print(f"🤔 You've already guessed '{guess}'.")
...             continue
... 
...         guessed_letters.add(guess)
...         if guess in word:
...             print("✅ Correct!")
...             if all(letter in guessed_letters for letter in word):
...                 print(f"\n🎉 You guessed it! The word was: {word}")
...                 return
...         else:
...             attempts_left -= 1
...             print(f"❌ Wrong! Attempts remaining: {attempts_left}")
... 
...     print(f"\n💀 You lost. The word was: {word}")
... 
... if _name_ == '_main_':
