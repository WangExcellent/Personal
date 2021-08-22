import random as rd
import sqlite3 as sql

bankstore = sql.connect('card.s3db')
cur = bankstore.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card(
    id integer,
    number TEXT,
    pin TEXT,
    balance INTEGER
    );""")


class bank():
    def __init__(self):
        cur.execute('select number, pin, balance from card')
        result = cur.fetchall()
        self.card = None
        self.PIN = None
        self.account = {}
        self.balance = {}
        if len(result) > 0:
            for i in range(len(result)):
                self.account[result[i][0]] = result[i][1]
                self.balance[result[i][0]] = result[i][2]


    def create(self):
        acreator = str(rd.randint(000000000, 999999999))
        self.card = '400000' + "0" * (9 - len(acreator)) + acreator
        self.card = self.card + user.Luhn_num(self.card)
        self.PIN = str(rd.randint(0000, 9999))
        self.PIN = "0" * (4 - len(self.PIN)) + self.PIN
        print("Your card has been created")
        print("Your card number:\n{}".format(self.card))
        print("Your card PIN:\n{}\n".format(self.PIN))
        self.account[self.card] = self.PIN
        self.balance[self.card] = 0
        cur.execute("INSERT INTO card VALUES (?,?,?,?)", (int(self.card), self.card, self.PIN, 0))
        bankstore.commit()

    def login(self):
        global flag
        self.card = input("Enter your card number: \n")
        self.PIN = input("Enter your PIN: \n")
        if self.card in self.account and self.PIN == self.account[self.card]:
            print("You have successfully logged in!\n")

            while True:
                print("""1. Balance\n2. Add income\n3. Do Transfer\n4. Close account\n5. Log out\n0. Exit""")
                n = int(input())
                if n == 1:
                    print("Balance: {}\n".format(self.balance[self.card]))
                elif n == 2:
                    self.balance[self.card] += int(input("Enter income:\n"))
                    cur.execute(
                        "update card set balance={} where id={}".format(self.balance[self.card], int(self.card)))
                    bankstore.commit()
                    print("Income was added!")
                elif n == 3:
                    user.transfer(input("Enter card number:\n"))
                elif n == 4:
                    cur.execute("delete from card where id='{}'".format(self.card))
                    print("The account has been closed!")
                    bankstore.commit()
                    break
                elif n == 5:
                    print("You have seccessfully logged out!\n")
                    break
                elif n == 0:
                    flag = False
                    print("Bye!")
                    break

        else:
            print("Wrong card number or PIN!")

    def transfer(self, target_account):
        if user.Luhn_num(target_account[0:15]) != target_account[15]:
            print("Probably you made a mistake in the card number. Please try again!")
        elif target_account not in self.account:
            print("Such a card does not exist.")
        elif target_account == self.card:
            print("You can't transfer money to the same account!")
        else:
            trans = int(input("Enter how much money you want to transfer:\n"))
            if trans > self.balance[self.card]:
                print("Not enough money!")
            else:
                self.balance[self.card] -= trans
                self.balance[target_account] += trans
                cur.execute("update card set balance={} where id={}".format(self.balance[self.card], int(self.card)))
                cur.execute(
                    "update card set balance={} where id={}".format(self.balance[target_account], int(target_account)))
                bankstore.commit()
                print("Success!")

    def Luhn_num(self, ori_num):
        ori_to_int = [int(a) for a in list(ori_num)]
        Luhn0 = [(ori_to_int[i] * 2 if i % 2 == 0 else ori_to_int[i]) for i in range(len(ori_to_int))]
        Luhn = [(num - 9 if num > 9 else num) for num in Luhn0]
        checksum = [str(a) for a in range(10) if (a + sum(Luhn)) % 10 == 0]
        return checksum[0]


user = bank()
flag = True
while flag == True:
    print("""1. Create an account\n2. Log into account\n0. Exit""")
    com = int(input())
    print()
    if com == 1:
        user.create()
        continue
    elif com == 2:
        user.login()
        continue
    elif com == 0:
        print("Bye!")
        break



cur.close()
bankstore.close()