# hangman
import random
import art
import words

# print logo
print(art.logo)

# choose a random word
ran_word = random.choice(words.w_list)
size = len(ran_word)

# create a list
finding = []
for i in range(0, size):
    finding.append('-')

# check the guess letter is available ran_word
print(ran_word)

win = False
lives = 6

while lives > 0:
    # enter guessed letter
    guess = input('Enter a letter : ').lower()
    ctr = False

    # find if entered letter is already there
    if guess in finding:
        print('You already guessed this letter :)')
    for x in range(size):
        if ran_word[x] == guess:
            ctr = True
            finding[x] = guess

    # print guessed letters
    print(' '.join(finding))

    # decrease lives count
    if not ctr:
        lives -= 1
        print(art.stages[lives])

    # check win condition
    if '-' not in finding:
        win = True
        break

# print final result
if win:
    print('You Won')
else:
    print('Give up on your dreams and die')
