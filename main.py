import random
import hangmanWords
import hangmanArt

print(hangmanArt.logo)
key = random.choice(hangmanWords.word_list)
print(f"The solution is {key}")
keyCount = len(key)
count=0
lives = 6
display = []
guessList = ""
isRunning = True

for i in range(keyCount):
    display += "_"

while isRunning != False:
    found = False
    guess = str(input("Guess a letter: ").lower())
    if guess in display:
        print(f"You already guessed {guess}, please try again.")
    for pos in range(keyCount):
        letter = key[pos]
        count+=1
        if guess == letter:
            display[pos] = guess
            found = True

    if found == False:
        print(f"You guessed {guess}, that's not in the word")
        lives -= 1
        if lives == 0:
            print("You lose.")
    print(f"{''.join(display)}")

    if "_" not in display or lives == 0:
        isRunning = False
        print("You Win!")
    if isRunning == True:
        print(hangmanArt.stages[lives])






