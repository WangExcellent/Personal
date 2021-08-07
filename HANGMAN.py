import random as rd

print("H A N G M A N")

while True:
    
    com = input('Type "play" to play the game, "exit" to quit:')
    if com != "play" and com != "exit":
        continue
    elif com == "exit":
        break
    
    rd.seed()
    ans_list = ['python','java','kotlin','javascript']
    choice = rd.choice(ans_list)
    choice_list = list(choice)
    ans_now = "-" * len(choice)
    lives = 8
    ans_record = []

    while lives > 0 and "-" in ans_now:
        print()
        position = []
        letter = input("""{}
Input a letter: """.format(ans_now))
        if len(letter) != 1:
            print("You should input a single letter")
            ans_record.append(letter)
            continue
        elif not letter.islower():
            print("Please enter a lowercase English letter")
            ans_record.append(letter)
            continue
        elif letter in ans_record:
            print("You've already guessed this letter")
            continue
        ans_record.append(letter)
    
        if letter not in choice:
            print("That letter doesn't appear in the word")
            lives -= 1
        else:
            for j in range(len(choice)):
                if letter == choice[j]:
                    position.append(j)
            for j in range(len(position)):
                ans_now = ans_now[:position[j]] + letter + ans_now[position[j]+1:]


    print("You lost!" if lives == 0 else """
{}
You guessed the word!
You survived!""".format(choice) )







