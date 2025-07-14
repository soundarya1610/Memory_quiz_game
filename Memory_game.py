import random
import time

# 🪄 Word pools based on difficulty
easy_words = ['🙂', '😂', '😍', '😎', '😡']
medium_words = ['choreo', 'song', 'zygotam', 'margazhi', 'guava', 'stool', 'namma']
difficult_words = ['19', '5679', 'T23', 'congruency', 'above gilbert', 'zooplan', 
                   'pneumonoultramicroscopicsilicovolcanoconiosis', 'karyokyamamudaya', 'nontario']

# 🎉 Welcome message
print("🎮 Welcome to the Memory Quiz Game!")
level = input("Choose your level (easy / medium / difficult): ").lower()

# 🎯 Pick words based on level
if level == "easy":
    sequence = random.sample(easy_words, 3)
elif level == "medium":
    sequence = random.sample(medium_words, 5)
elif level == "difficult":
    sequence = random.sample(difficult_words, 7)
else:
    print("Invalid level selected. Please restart the game.")
    sequence = []

# 🧠 Show the sequence to memorize
if sequence:
    print("\n🧠 Memorize this:")
    print(sequence)
    time.sleep(5)  # Give 5 seconds to remember
    print("\n" * 50)  # Clear screen

    print("⌛ Time's up!")
    print("Now type what you remember, one by one.")
    user_answers = []

    for i in range(len(sequence)):
        ans = input(f"Enter item {i+1}: ")
        user_answers.append(ans.strip())

    # ✅ Score checking
    score = 0
    for item in user_answers:
        if item in sequence:
            score += 1

    print("\n✅ You got", score, "out of", len(sequence), "correct!")
    print("🎯 The correct sequence was:", sequence)
else:
    print("❌ Game could not start due to invalid input.")
