# write your code here

import random as rd

def test1():
    i = 0
    r = 0
    while i < 5:
        a = rd.randint(2, 9)
        b = rd.randint(2, 9)
        c = rd.randint(0, 2)
        ope_dict = ['+', '-', '*']
        if ope_dict[c] == '+':
            ans = a + b
        elif ope_dict[c] == '-':
            ans = a - b
        elif ope_dict[c] == '*':
            ans = a * b
        print("{} {} {}".format(a, ope_dict[c], b))
        while True:
            x = input()
            if len(x) < 2:
                if x.isdigit():
                    if int(x) == ans:
                        print("Right!")
                        i += 1
                        r += 1
                        break
                    else:
                        print("Wrong!")
                        i += 1
                        break
                else:
                    print("Incorrect format.")
            else:
                if (x[0].isdigit() or x[0] == "-") and x[1:].isdigit():
                    if int(x) == ans:
                        print("Right!")
                        i += 1
                        r += 1
                        break
                    else:
                        print("Wrong!")
                        i += 1
                        break
                else:
                    print("Incorrect format.")
    p = input(f"Your mark is {r}/5. Would you like to save your result to the file? Enter yes or no.\n")
    if p in ['YES','y','yes','Yes']:
        name = input("What's your name?\n")
        file = open('results.txt','a',encoding='utf-8')
        file.write(f"{name}: {r}/5 in level 1 (simple operations with numbers 2-9).")
        file.close()
        print('The results are saved in "results.txt".')

def test2():
    i = 0
    r = 0
    while i < 5:
        a = rd.randint(11, 29)
        ans = a * a
        print(a)
        while True:
            x = input()
            if x.isdigit():
                if int(x) == ans:
                    print("Right!")
                    i += 1
                    r += 1
                    break
                else:
                    print("Wrong!")
                    i += 1
                    break
            else:
                print("Incorrect format.")
    p = input(f"Your mark is {r}/5. Would you like to save your result to the file? Enter yes or no.\n")
    if p in ['YES','y','yes','Yes']:
        name = input("What's your name?\n")
        file = open('results.txt','a',encoding='utf-8')
        file.write(f"{name}: {r}/5 in level 2 (simple operations with numbers 11-29).")
        file.close()
        print('The results are saved in "results.txt".')

com = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n""")

if com == '1':
    test1()
else:
    test2()

