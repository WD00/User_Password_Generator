import random

characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
characters2 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890)(*&^%$#!.,;][<>"

choice = input("Would you like your password to have special characters?\n1 = yes   2 = no\n")

if choice == '1':
    while 0 == 0:
        length = int(input("Type the length of your password:\n"))
        amount = int(input("Type the amount of passwords you would like to get:\n"))
        for x in range(0,amount):
            outcome = ""
            for x in range(0,length):
                outcome_ch = random.choice(characters2)
                outcome = outcome + outcome_ch
            print("Generated password: ",outcome)
        exit()

elif choice == '2':
    while 2 == 2:
        length = int(input("Type the length of your password:\n"))
        amount = int(input("Type the amount of passwords you would like to get:\n"))
        for x in range(0,amount):
            outcome = ""
            for x in range(0,length):
                outcome_ch = random.choice(characters)
                outcome = outcome + outcome_ch
            print("Generated password: ",outcome)
        exit()

else:
    print("Wrong. Try again.")

